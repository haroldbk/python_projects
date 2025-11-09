import os
import json
import time
import http.server
import socketserver
import threading
import webbrowser
import urllib.parse
import requests

CLIENT_ID = '4c80ffa3-eec4-4105-938a-cdb09e7680dd'
CLIENT_SECRET = 'qQ38Q~KZU-nw3wQX9fKWBm8HAwy9l5AMVJlvrawM'
REDIRECT_URI = 'http://localhost:8000/callback'
AUTHORITY = 'https://login.microsoftonline.com/consumers'
SCOPES = ['Files.ReadWrite', 'offline_access']
PORT = 8000
TOKEN_FILE = 'token.json'
FOLDER_NAME = 'Dance_demos/shag'  # Name of the folder you want to access


auth_code = None  # Captured code

class AuthHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        global auth_code
        query = urllib.parse.urlparse(self.path).query
        params = urllib.parse.parse_qs(query)
        if 'code' in params:
            auth_code = params['code'][0]
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"<h2>You can close this tab and return to the script.</h2>")
        else:
            self.send_error(400, "Missing code in redirect")

def start_local_server():
    with socketserver.TCPServer(("", PORT), AuthHandler) as httpd:
        httpd.handle_request()

def open_browser_for_auth():
    params = {
        'client_id': CLIENT_ID,
        'response_type': 'code',
        'redirect_uri': REDIRECT_URI,
        'response_mode': 'query',
        'scope': ' '.join(SCOPES),
        'state': '12345',
    }
    auth_url = f"{AUTHORITY}/oauth2/v2.0/authorize?" + urllib.parse.urlencode(params)
    print("Opening browser for login...")
    webbrowser.open(auth_url)

def get_token_from_code(code):
    token_url = f"{AUTHORITY}/oauth2/v2.0/token"
    data = {
        'client_id': CLIENT_ID,
        'scope': ' '.join(SCOPES),
        'code': code,
        'redirect_uri': REDIRECT_URI,
        'grant_type': 'authorization_code',
        'client_secret': CLIENT_SECRET,
    }
    r = requests.post(token_url, data=data)
    if r.status_code == 200:
        token = r.json()
        token['expires_at'] = time.time() + int(token['expires_in']) - 60
        save_token(token)
        return token
    else:
        raise Exception(f"Failed to get token: {r.status_code} {r.text}")

def refresh_access_token(refresh_token):
    print("Refreshing token...")
    token_url = f"{AUTHORITY}/oauth2/v2.0/token"
    data = {
        'client_id': CLIENT_ID,
        'scope': ' '.join(SCOPES),
        'refresh_token': refresh_token,
        'redirect_uri': REDIRECT_URI,
        'grant_type': 'refresh_token',
        'client_secret': CLIENT_SECRET,
    }
    r = requests.post(token_url, data=data)
    if r.status_code == 200:
        token = r.json()
        token['expires_at'] = time.time() + int(token['expires_in']) - 60
        save_token(token)
        return token
    else:
        print("Refresh failed, clearing saved token.")
        os.remove(TOKEN_FILE)
        return None

def save_token(token_data):
    with open(TOKEN_FILE, 'w') as f:
        json.dump(token_data, f)

def load_token():
    if os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE, 'r') as f:
            return json.load(f)
    return None

def ensure_token():
    token = load_token()
    if token:
        if time.time() < token['expires_at']:
            return token
        else:
            # Try to refresh
            return refresh_access_token(token.get('refresh_token'))

    # No valid token, start full auth flow
    global auth_code
    server_thread = threading.Thread(target=start_local_server, daemon=True)
    server_thread.start()
    open_browser_for_auth()

    while auth_code is None:
        time.sleep(1)

    return get_token_from_code(auth_code)

def list_onedrive_files(access_token):
    # fname='blah'  used to genearate an error for debugging
    headers = {'Authorization': f'Bearer {access_token}'}
    #https://graph.microsoft.com/v1.0/me/drive/root:/Dance_demos:/children?select=name,id,webUrl
    r=requests.get( f"https://graph.microsoft.com/v1.0/me/drive/root:/{fname}:/children", headers=headers)
   # r = requests.get('https://graph.microsoft.com/v1.0/me/drive/root/children', headers=headers)
    file_list=[]
    if r.status_code == 200:
        #print("Files in OneDrive root:")
        
        for item in r.json().get('value', []):
           # print("-", item['id'], item['name'])
            file_list.append((item['id'],item['name']))
           # play = input("play this item y/n")
            #if play == 'y':
                 # play_video (item['id'],headers)
        return file_list
    else:
        print("Error accessing OneDrive:", r.status_code, r.text)
        error = "Error accessing OneDrive:", r.status_code, r.text
        file_list.append(('error', error))
        return file_list
def play_video(id,headers):
    file_id = id
    resp = requests.get(f'https://graph.microsoft.com/v1.0/me/drive/items/{file_id}',
                        headers = headers)
    url = resp.json()["@microsoft.graph.downloadUrl"]
    import vlc 
    player = vlc.MediaPlayer(url)
    player.play()     

def main(folder):
    global fname
    fname=f'Dance_demos/{folder}'
    token = ensure_token()
    if token:
        access_token = token['access_token']
        filelist=list_onedrive_files(access_token)
        return access_token, filelist
    
#token,list = main('mixed')
#for file in list:
#    print(file)

if __name__ == '__main__':
    main()


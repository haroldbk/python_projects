#Safaria Tutorial the Full Code
#https://developers.sefaria.org/reference/tutorial-dvar-torah-outliner#the-full-code
import requests


# Helper functions

def get_request_json_data(endpoint, ref=None, param=None):
    url = f"https://www.sefaria.org/{endpoint}"

    if ref:
        url += f"{ref}"

    if param:
        url += f"?{param}"

    response = requests.get(url)
    data = response.json()
    return data


def get_commentary_text(ref):
    data = get_request_json_data("api/v3/texts/", ref)

    # Checking to make sure we have a primary version for the commentary
    # (otherwise, the versions field would be empty).
    if "versions" in data and len(data['versions']) > 0:
        # Retrieve the general name of the commentary book (i.e. "Rashi on Genesis")
        title = data['title']

        # Retrieve the text of the commentary
        text = data['versions'][0]['text']

        # Return the title, and the text
        return title, text


if __name__ == '__main__':

    # Step One: Get the Parasha Data Using the Calendars API
    data = get_request_json_data("api/calendars")

    # Retrieve the list of calendar_items
    calendar_items = data['calendar_items']

    # Find the dictionary in calendar_items storing the metadata for Parashat Hashavua,
    # and save the ref, as well as the name of the week's Parasha.
    for item in calendar_items:
        if item['title']['en'] == 'Parashat Hashavua':
            parasha_ref = item['ref']
            parasha_name = item['displayValue']['en']

    ##################################################################

    # Step Two: Split the Ranged Ref to get the First Verse
    parasha_ref = parasha_ref.split("-")[0]

    ##################################################################

    # Step Three: Retrieve Text for the Verse
    data = get_request_json_data("api/v3/texts/", parasha_ref)
    he_vtitle = data['versions'][0]['versionTitle']
    he_pasuk = data['versions'][0]['text']

    # Change version to English - Retrieve the version title, and text for the English verse.
    get_request_json_data("api/v3/texts/", parasha_ref, "version=english")
    en_vtitle = data['versions'][0]['versionTitle']
    en_pasuk = data['versions'][0]['text']

    ##################################################################

    # Step Four: Get Commentaries
    data = get_request_json_data("api/related/", parasha_ref)

    # Set up our commentaries list
    commentaries = []

    # Iterate through the "links" in our data response, filtering for commentary links, and
    # appending the text reference to our commentaries list.
    for linked_text in data["links"]:
        if linked_text['type'] == 'commentary':
            commentaries.append(linked_text['ref'])

    com1_title, com1_text = get_commentary_text(commentaries[0])
    com2_title, com2_text = get_commentary_text(commentaries[1])
    com3_title, com3_text = get_commentary_text(commentaries[2])

    ##################################################################

    # Step Five: Print Parasha Outline

    print(f"My Outline for Parashat {parasha_name}")
    print(f"Hebrew: {he_pasuk} (edition: {he_vtitle})")
    print(f"English: {en_pasuk} (edition: {en_vtitle})")
    print("\nThree Commentaries:")
    print(f"A) {com1_title}: {com1_text}\n")
    print(f"B) {com2_title}: {com2_text}\n")
    print(f"C) {com3_title}: {com3_text}")

#sending post to Power Automate
import requests

payload={
  "requestor": "hbk",
  "city": "Dallas",
  "recordID": "20101017-5470-4f14-9947-6ed4d2f3c6"
}

r=requests.post("https://prod-154.westus.logic.azure.com:443/workflows/215f534c769b4a27bd4eb9a2292393ae/triggers/manual/paths/invoke?api-version=2016-06-01&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=oFsLr7BiWBvI9jp5Fo_b0lNin63REkqtYAtRfx4teIQ",json=payload)
print(r.text)

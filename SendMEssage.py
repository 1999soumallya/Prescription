import json
from getpass import getpass

reset_creds = False

if reset_creds:
    twilio_sid = getpass('What is Account SID')
    twilio_secret = getpass('What is Account Secret')
    data={
        "twilio_sid": twilio_sid,
        "twilio_secret": twilio_secret
    }
    json_data = json.dumps(data)
    with open('creds.json','+w') as f:
        f.write(json_data)
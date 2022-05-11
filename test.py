from trycourier import Courier

client = Courier(auth_token="")

response = client.send(
    event="",
    recipient="f949bf6b-ed11-4fb0-86a4-ee9c8235a33f",
    profile={
        "email": "saifnewblog@gmail.com",
    },
    data={
        "var": 'Player '
    },
    override={
        "override": {
            "channel": {
                "email": {
                    "attachments": [
                        {
                            "filename": "C:\\Users\\Rango\PycharmProjects\\valorant-stats-tracker\\report.pdf",
                            "contentType": "application/pdf",
                            "data": "Q29uZ3JhdHVsYXRpb25zLCB5b3UgY2FuIGJhc2U2NCBkZWNvZGUh"
                        }
                    ]
                }
            }
        }
    }
)
print(response['messageId'])

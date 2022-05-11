# Install Courier SDK: pip install trycourier
from trycourier import Courier

client = Courier(auth_token="")

resp = client.send_message(
  message={
    "to": {
      "email": "saifkwik@gmail.com",
    },
    "template": "TTS2W51F5MMNFZJQ9J6X5JV679WA",
    "data": {
    },

  }

)

print(resp['requestId'])
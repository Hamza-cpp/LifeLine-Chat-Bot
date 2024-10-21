# Copyright 2024 OKHADIR Hamza
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
from dotenv import load_dotenv
from twilio.rest import Client
from groq import Groq

load_dotenv()

# Your Account SID and Auth Token from console.twilio.com
twilio_account_sid = os.environ["TWILIO_ACCOUNT_SID"]
twilio_auth_token = os.environ["TWILIO_AUTH_TOKEN"]

# your Groq Api key from console.groq.com
groq_api_key = os.environ["GROQ_API_KEY"]

# twilio_client = Client(twilio_account_sid, twilio_auth_token)
# message = twilio_client.messages.create(
#     to="whatsapp:+212620661864",
#     from_="whatsapp:+14155238886",
#     body="Hello frhhhhhhhhhhhhhhhhhhhhhhom Python!",
# )

# print(message.sid)


groq_client = Groq(api_key=groq_api_key)
chat_completion = groq_client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Explain the importance of fast language models",
        }
    ],
    model="llama3-8b-8192",
)

print(chat_completion.choices[0].message.content)

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

load_dotenv()

# Your Account SID and Auth Token from console.twilio.com
account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="whatsapp:+212620661864",
    from_="whatsapp:+14155238886",
    body="Hello frhhhhhhhhhhhhhhhhhhhhhhom Python!",
)

print(message.sid)

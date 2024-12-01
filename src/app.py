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
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

load_dotenv()
app = Flask(__name__)

# Your Account SID and Auth Token from console.twilio.com
twilio_account_sid = os.environ["TWILIO_ACCOUNT_SID"]
twilio_auth_token = os.environ["TWILIO_AUTH_TOKEN"]
 
# def generate_answer(question):
#     chat_completion = groq_client.chat.completions.create(
#         messages=[
#             {
#                 "role": "user",
#                 "content": question,
#             }
#         ],
#         model="llama3-8b-8192",
#     )

#     answer = chat_completion.choices[0].message.content
#     return answer


@app.route("/")
def hello_world():
    
    return "✨ Hello, everyone the Life line Chat Bot is here ✨"


# Define a route to handle incoming requests
@app.route("/whatsapp", methods=["POST"])
def whatsapp():
    incoming_msg = request.values.get("Body", "").lower()
    print("WhatsApp Message: ", incoming_msg)

    # Generate the answer
    answer = generate_answer(incoming_msg)
    print("BOT Answer: ", answer)

    # Create a Twilio response
    resp = MessagingResponse()
    msg = resp.message()
    msg.body(answer)

    return str(resp)


# Run the Flask app
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=False, port=5000)

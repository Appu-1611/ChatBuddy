from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)
#-----------------------------------------------------------------------------------
"""
Install the Google AI Python SDK

$ pip install google-generativeai

See the getting started guide for more information:
https://ai.google.dev/gemini-api/docs/get-started/python
"""

import os

import google.generativeai as genai

os.environ['GOOGLE_API_KEY'] = "AIzaSyDyslmd7kuNkfYf_IGLJLs1E4rypobgN4c"

genai.configure(api_key = os.environ['GOOGLE_API_KEY'])

# genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# Create the model
# See https://ai.google.dev/api/python/google/generativeai/GenerativeModel
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
)

chat_session = model.start_chat(
  history=[
  ]
)

#-----------------------------------------------------------------------------------

# Replace with your actual API key and endpoint
#GOOGLE_GEMINI_API_KEY = 'AIzaSyDyslmd7kuNkfYf_IGLJLs1E4rypobgN4c'
#GOOGLE_GEMINI_ENDPOINT = 'https://generativelanguage.googleapis.com/v1/models/gemini-pro:generateContent'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json['message']
    print(user_input)

    """
    # Prepare the payload for the API request
    payload = {
        "prompt": user_input,
        "max_tokens": 150  # Adjust as needed
    }

    headers = {
        "Authorization": f"Bearer {GOOGLE_GEMINI_API_KEY}",
        "Content-Type": "application/json"
    }
    """
#---------------- My Code ---------------------------------------
    response = chat_session.send_message(user_input)
    print("Line 76" + response.text)
#--------------------------------------------------------------


    # Send the request to the Google Gemini API
    #response = requests.post(GOOGLE_GEMINI_ENDPOINT, json=payload, headers=headers)
    
    #if response.status_code == 200:
   # bot_response = response.json().get('choices', [{}])[0].get('text', '').strip()
    #else:
        #bot_response = "Sorry, I couldn't process your request."

    #return jsonify({'reply': bot_response})
    #return jsonify({'reply': response})
    return {'reply': response.text}
    #print(bot_response.text)

if __name__ == '__main__':
    app.run(debug=True)

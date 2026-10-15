import os
from flask import Flask, render_template, request
from google import genai

app = Flask(__name__)

# Initialize the Gemini AI Client
client = genai.Client()

@app.route('/')
def home():
    return render_template('index.html')

# 🛠️ THIS IS THE ROUTE THAT WAS MISSING INDEPENDENTLY:
@app.route('/ask-ai', methods=['POST'])
def ask_ai():
    user_message = request.form['message']
    
    try:
        # Requesting a response from the free flash model
        response = client.models.generate_content(
                 model='gemini-3.5-flash',
            contents=user_message,
        )
        bot_reply = response.text
    except Exception as e:
        bot_reply = f"Error: {str(e)}"
    
    return render_template('index.html', reply=bot_reply)

if __name__ == '__main__':
    app.run(debug=True)

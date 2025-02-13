import time
from flask import Flask, request
from googlesearch import search
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/", methods=["POST"])
def bot():
    user_msg = request.values.get('Body', '').lower()
    response = MessagingResponse()

    try:
        urls = []
        
        for url in search(user_msg, num=3): 
            urls.append(url)
            time.sleep(2)

        if not urls:
            response.message("No results found.")
        else:
            response.message(f"--- Results for '{user_msg}' ---")
            for res in urls:
                response.message(res) 

    except Exception as e:
        response.message(f"Error: {str(e)}") 

    return str(response)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)

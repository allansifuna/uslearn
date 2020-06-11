# Your code here
from flask import Flask, request
import os
app = Flask(__name__)

response = ""


@app.route('/', methods=['POST', 'GET'])
def ussd_callback():
    global response
    session_id = request.values.get("sessionId", None)
    service_code = request.values.get("serviceCode", None)
    phone_number = request.values.get("phoneNumber", None)
    text = request.values.get("text", "default")
    if text == '':
        response = "CON Welcome to shupavu. Select:- \n"
        response += "1. Exam questions \n"
        response += "2. Past Papers"
    elif text == '1':
        response = "CON Choose Exam Papers you want to view \n"
        response += "1. Targeter 003 \n"
        response += "2. Jesma 003"
    elif text == '1*1':
        response = "END Just a demo"
    elif text == '1*2':
        response = "END just a demo"
    elif text == '2':
        response = "END Just a Demo to confirm thet it all works"
    return response


if __name__ == '__main__':
    app.run(debug=True)

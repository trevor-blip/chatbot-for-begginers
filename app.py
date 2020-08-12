from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from corona import get_data


app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello, World!"


@app.route("/sms", methods=['POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Fetch the message
    msg_text = request.form.get('Body')
    phone_no = request.form.get('From')


    # Create reply
    data = get_data(msg_text)
    msg = MessagingResponse()
    resp=msg.message(data)

    return str(msg)


if __name__ == "__main__":
    app.run(debug=True)

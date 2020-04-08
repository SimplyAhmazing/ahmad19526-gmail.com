from flask import (
    flash,
    render_template,
    redirect,
    request,
    session,
    url_for,
)
from twilio.twiml.voice_response import VoiceResponse

from hotline import app
from hotline.view_helpers import twiml


@app.route('/')
@app.route('/ivr')
def home():
    return render_template('index.html')


@app.route('/ivr/welcome', methods=['POST'])
def welcome():
    response = VoiceResponse()
    with response.gather(
        num_digits=1, action=url_for('menu'), method="POST"
    ) as g:
        g.play('https://bangla-hotline.s3.amazonaws.com/prompt.mp3', loop=3)
    return twiml(response)


@app.route('/ivr/menu', methods=['POST'])
def menu():
    selected_option = request.form['Digits']
    print('Selected option', selected_option)

    response = VoiceResponse()
    response.say("Thank you for calling Bangla hotline")
    response.hangup()

    return twiml(response)

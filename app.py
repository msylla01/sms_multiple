from dotenv import load_dotenv
from flask import Flask, redirect, render_template, request, url_for
#import nexmo
import os
import sys
import vonage 

sys.getfilesystemencoding() 
#from .util import env_var, extract_error
 
# Load environment variables from a .env file:
load_dotenv('.env')
 
# Load in configuration from environment variables:
VONAGE_API_KEY = '37defc48'
VONAGE_API_SECRET = 'GINnNZt2r3gawGS3'
#NEXMO_NUMBER = 'abcdef12345678'


# Create a new Client object:

client = vonage.Client(key='37defc48', secret='GINnNZt2r3gawGS3')
sms = vonage.Sms(client)
#nexmo_client = vonage.Client(
#    key=NEXMO_API_KEY, secret=NEXMO_API_SECRET
#)
#sms = vonage.Sms(nexmo_client)
# Initialize Flask:
app = Flask(__name__)
app.config['SECRET_KEY'] = 'RANDOM-STRING_CHANGE-THIS-Ea359'


@app.route('/')
def index():
    """ A view that renders the Send SMS form. """
    return render_template('index.html')
    
    
@app.route('/send_sms', methods=['POST'])
def send_sms():
    """ A POST endpoint that sends an SMS. """

    # Extract the form values:
    to_number = request.form['to_number']
    message = request.form['message']
    name_compagny = request.form["name_compagny"]
    to_number = to_number.split(',')
    to_number = list(map(int, to_number))
    for phone in to_number:
        
    	# Send the SMS message:
    	result = sms.send_message( {

        	'from': name_compagny,
        	'to': phone,
        	'text': message,
    	})

    # Redirect the user back to the form:
    return redirect(url_for('index'))

from flask import Flask, request, jsonify, render_template
from faker import Faker
from twilio.jwt.access_token import AccessToken
from twilio.jwt.access_token.grants import SyncGrant


app = Flask(__name__)
fake = Faker()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/token')
def generate_token():
    #add your twilio credentials
    TWILIO_ACCOUNT_SID = AC9e56a803f9841599f7cd470628121799''
    TWILIO_SYNC_SERVICE_SID = 'c1a3f90b627540713168e05436cfe6d5'
    TWILIO_API_KEY = 'SK432e672835f0b4d1752f1930f09da75b'
    TWILIO_API_SECRET = '5c7yqrZA1qeikehKettsl9SjSE4BdW9C'

    username = request.args.get('username', fake.user_name())
    token = AccessToken(TWILIO_ACCOUNT_SID, TWILIO_API_KEY, TWILIO_API_SECRET, identity=username)
    sync_grant_access = SyncGrant(TWILIO_SYNC_SERVICE_SID)
    token.add_grant(sync_grant_access)
    return jsonify(identity=username, token=token.to_jwt().decode())



if __name__ == "__main__":
    app.run(port=5001)

# A function to download text and store it in text file
@app.route('/', methods = ['POST'])
def download_text():
    text_from_notepad = request.form['text']
    with open('workfile.txt','w') as f:
        f.write(text_from_notepad)

    path_to_store_txt = 'workfile.txt'
    return send_file(path_to_store_txt, as_attachment = True)

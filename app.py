from flask import Flask, render_template, redirect, session, current_app
import httplib2
import os
import json

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
from oauth2client.contrib.flask_util import UserOAuth2

try:
    import argparse
    flags = tools.argparser.parse_args(args=[])
except ImportError:
    flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/sheets.googleapis.com-python-quickstart.json

SCOPES = 'email profile'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'DecaQuestionTester'

app = Flask(__name__)
app.static_folder = 'static'



@app.route('/', methods=['GET', 'POST'])
def create_page():
    return render_template('home.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    print("HELLO")
    flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES, redirect_uri="http://127.0.0.1:5000/oauth2callback")
    flow.user_agent = APPLICATION_NAME
    auth_uri = flow.step1_get_authorize_url()
    print(auth_uri)
    return redirect(auth_uri, code=302)


@app.route('/oauth2callback', methods=['GET', 'POST'])
def callback():
    return redirect('/tests', code=302)


@app.route('/tests', methods=['GET'])
def tests():
    return render_template("tests.html")


@app.route('/<sheet>/<int:id>', methods=['GET'])
def hello_world(sheet, id):
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?'
                    'version=v4')
    service = discovery.build('sheets', 'v4', http=http,
                              discoveryServiceUrl=discoveryUrl)

    spreadsheetId = '1B84hzrKLUS1SXRH7HZzcgZ7sxXcOxNPh_Uy6cJyNx-Q'
    rangeName =  sheet + '!A2:G'
    result = service.spreadsheets().values().get(
        spreadsheetId=spreadsheetId, range=rangeName).execute()
    values = result.get('values', [])

    optionA = optionB = optionC = optionD = question = rightAnswer = ""

    if not values:
        print('No data found.')
    else:
        row = values[int(id)]
        print(row)
        # Print columns A and E, which correspond to indices 0 and 4.
        print('%s, %s, %s' % (row[1], row[2], row[4]))
        question = row[1]
        optionA = row[2]
        optionB = row[3]
        optionC = row[4]
        optionD = row[5]
        rightAnswer = row[6]

    return render_template('index.html', question = question, optionA = optionA, optionB = optionB,
                           optionC = optionC, optionD = optionD, rightAnswer = rightAnswer, newID = str(id+1) )


def get_credentials():
    home_dir = os.getcwd()
    credential_dir = home_dir
    print(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'sheets.googleapis.com-python-quickstart.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        print('Storing credentials to ' + credential_path)
    return credentials


if __name__ == '__main__':
    app.run()

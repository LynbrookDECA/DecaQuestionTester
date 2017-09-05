import os

# The secret key is used by Flask to encrypt session cookies.
# [START secret_key]
SECRET_KEY = '\x97V|\xb1Dn>\xafx\x94\x18{F%\x86\xe5\xc8s\x8a\xbfcE\x82\x1b'
# [END secret_key]

# There are three different ways to store the data in the application.
# You can choose 'datastore', 'cloudsql', or 'mongodb'. Be sure to
# configure the respective settings for the one you choose below.
# You do not have to configure the other data backends. If unsure, choose
# 'datastore' as it does not require any additional configuration.
DATA_BACKEND = 'datastore'

# Google Cloud Project ID. This can be found on the 'Overview' page at
# https://console.developers.google.com
PROJECT_ID = 'decaquestiontester'


GOOGLE_OAUTH2_CLIENT_ID = '555085055814-1f31dltl92tpfp3dkibogjf286n8isg9.apps.googleusercontent.com'
GOOGLE_OAUTH2_CLIENT_SECRET = '26fNzAbXRACzTyTSGfGv_WXK'

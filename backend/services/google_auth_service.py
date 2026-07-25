from google.oauth2 import id_token
from google.auth.transport import requests
import os


def verify_google_token(token):

    try:

        user_info = id_token.verify_oauth2_token(
            token,
            requests.Request(),
            os.getenv("GOOGLE_CLIENT_ID")
        )

        return user_info

    except Exception as e:

        print("Google Verify Error:", e)
        return None
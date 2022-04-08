import os

URL = "http://0.0.0.0:8000" if os.environ['APP_ENV'] == "local" else "https://eitango-test-api.herokuapp.com/"
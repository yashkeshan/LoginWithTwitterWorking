import pprint
from multiprocessing import Process
from urllib.parse import parse_qsl
from requests_oauthlib import OAuth1Session
import webbrowser
import web_server

# Below function runs and initiates twitter login page authentication and provides with oauth_token and oauth_verifier for authenticated user
def authentication_url(consumer_key, consumer_secret, oauth_callback):
    ck = consumer_key
    cs = consumer_secret
    requests_token_url = 'https://api.twitter.com/oauth/request_token' # Verification url to get verifier_token
    authenticate_url = 'https://api.twitter.com/oauth/authenticate' # Url for authenticating user with request_token
    twitter = OAuth1Session(ck, cs) # Passing api keys to Oauth1Session Authentication function

    response = twitter.post(requests_token_url, params={'oauth_callback':oauth_callback}) # Generates response url with tokens
    requests_token = dict(parse_qsl(response.content.decode("utf-8"))) # Stores elements from response url as dictionary
    print(requests_token)
    pprint.pprint(requests_token) # Print and display request token dictionary elements

    authentication_endpoint = '%s?oauth_token=%s'\
                              % (authenticate_url, requests_token['oauth_token'])

    print("\n Authentication endpoint URL is: \n ", authentication_endpoint) # Display final authentication url

    webbrowser.open(authentication_endpoint)
    print("\n Waiting to complete authentication process...... \n ") # Initiate authenticaiton url in web_browser

    proc = Process(target=web_server.run_server())
    proc.start()
    print("\n Web_server process was initiated........ \n ")


def main():
    api_key = "" # Private API Key
    api_secret_key = "" # API_SECRET_KEY
    callback_url = "http://127.0.0.1/return" # Whitelisted Local Callback_URL on Twitter Dev Portal
    authentication_url(api_key, api_secret_key, callback_url) # Run the Authentication function by passing necessary inputs


if __name__ == "__main__":
    main()

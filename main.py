import tweepy

all_keys = open("twitterKeys.txt", "r").read().splitlines()
api_key = all_keys[0]
api_key_secret = all_keys[1]
access_token = all_keys[2]
access_token_secret = all_keys[3]

authenticator = tweepy.OAuthHandler(api_key, api_key_secret)
authenticator.set_access_token(access_token, access_token_secret)

api = tweepy.API(authenticator, wait_on_rate_limit=True)


try:
    tweet = api.update_status('Your tweet content here')
    print("Tweet created successfully")
except tweepy.Forbidden as e:
    print("Forbidden error: Check your access level and permissions.")
    print(e)
except tweepy.TweepyException as e:
    print("An error occurred: ", e)






# query = 'python'
# num_tweets = 100

# tweets = tweepy.Cursor(api.search_tweets, q= query).items(num_tweets)

# username = 'iimuaeen'

# try:
#     user = api.get_user(screen_name=username)
#     print(f"Username: {user.screen_name}")
# except tweepy.errors.Forbidden as e:
#     print("Access Forbidden:", e)
# except tweepy.errors.TweepyException as e:  # A more general exception
#     print("Tweepy Exception:", e)


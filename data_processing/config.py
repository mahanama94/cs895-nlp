import os

# TODO: Move os environ to commandline args
START_DATE = os.environ.get("START", "2019-10-19")
END_DATE = os.environ.get("END", "2021-10-19")

DATA_DIRECTORY = os.environ.get("DATA_DIRECTORY", "../data/")
LOGGING_DIRECTORY = DATA_DIRECTORY + "logs/"

YAHOO_DATA_DIRECTORY = DATA_DIRECTORY + "yahoo/"
YAHOO_TICKER = os.environ.get("TICKER", "GME")

REDDIT_CLIENT_ID = "ec2mtK_u5AOmuJEKvu4raQ"
REDDIT_CLIENT_SECRET = "8TVgeCuv_gCuwSLnjJ9Ru2iMVgzCow"
REDDIT_USER_AGENT = "NLP"
REDDIT_DATA_DIRECTORY = DATA_DIRECTORY + "reddit/"

TWITTER_BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAG97VAEAAAAAxfbNzN%2BgTJO40r657osZkyXDxSg" \
                       "%3DSxpRIAt14wownlzsO5uL0kEXMvRVSekxTwGASj5OuCiGnfW9us "
TWITTER_TAG = os.environ.get("TWITTER_TAG", "$GME")
TWITTER_TWEET_COUNT = 100
TWITTER_DATA_DIRECTORY = DATA_DIRECTORY + "twitter/"

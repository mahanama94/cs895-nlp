import datetime
import logging
import csv

from tweepy import Client

from data_extractors.config import TWITTER_BEARER_TOKEN, LOGGING_DIRECTORY, TWITTER_TAG, TWITTER_DATA_DIRECTORY

start_date = datetime.datetime(2021, 10, 19)
end_date = datetime.datetime(2021, 10, 24)

if __name__ == '__main__':

    logging.basicConfig(filename=LOGGING_DIRECTORY + TWITTER_TAG + ".log", level=logging.INFO)

    client = Client(bearer_token=TWITTER_BEARER_TOKEN, wait_on_rate_limit=True)

    current_date = start_date
    time_delta = datetime.timedelta(days=1)

    while current_date < end_date:
        tweets = client.search_recent_tweets(query=TWITTER_TAG, start_time=current_date,
                                             expansions=["author_id"], tweet_fields=["created_at", "public_metrics"])

        csv_file = open(TWITTER_DATA_DIRECTORY + TWITTER_TAG + "-" + current_date.strftime("%Y-%m-%d") + ".csv",
                        "w", newline="\n")

        csv_writer = csv.DictWriter(csv_file, fieldnames=['id', 'author', 'text', 'created',
                                                          'retweets', 'replies', 'likes', 'quotes'])
        csv_writer.writeheader()

        for tweet in tweets.data:
            tweet_data = {
                "id": tweet.id,
                "author": tweet.author_id,
                "text": tweet.text,
                "created": tweet.created_at,
                "retweets": tweet.public_metrics.get("retweet_count", -1),
                "replies": tweet.public_metrics.get("reply_count", -1),
                "likes": tweet.public_metrics.get("like_count", -1),
                "quotes": tweet.public_metrics.get("quote_count", -1),
            }

            csv_writer.writerow(tweet_data)

        csv_file.close()
        logging.info("Completed for " + TWITTER_TAG + " on " + current_date.strftime("%Y-%m-%d"))

        current_date = current_date + time_delta

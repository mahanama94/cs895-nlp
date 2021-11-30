import datetime
import logging
import csv

import praw
from prawcore.exceptions import ServerError, TooLarge, RequestException
from data_processing.config import REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, REDDIT_USER_AGENT, REDDIT_DATA_DIRECTORY, LOGGING_DIRECTORY, \
    START_DATE, END_DATE

#
# Best/ Confidence ?= upvotes - downvotes
#
# Top ?= upvotes
#
# Hot ?= upvotes * time
#


start_date = datetime.datetime.strptime(START_DATE, "%Y-%m-%d")
end_date = datetime.datetime.strptime(END_DATE, "%Y-%m-%d")

if __name__ == '__main__':

    SUBREDDIT = "wallstreetbets"
    MAX_RETRIES = 5

    logging.basicConfig(filename=LOGGING_DIRECTORY + SUBREDDIT + ".log", level=logging.INFO)

    reddit_client = praw.Reddit(client_id=REDDIT_CLIENT_ID, client_secret=REDDIT_CLIENT_SECRET,
                                user_agent=REDDIT_USER_AGENT)

    current_date = start_date
    time_delta = datetime.timedelta(days=1)

    while current_date < end_date:
        # search_query = "daily discussion " + current_date.strftime("%B %d %Y")
        search_query = "Moves Tomorrow " + current_date.strftime("%B %d %Y")

        retries = 0

        while retries < MAX_RETRIES:
            try:
                submissions = reddit_client.subreddit(SUBREDDIT).search(search_query)
                submission = next(submissions)
                csv_file = open(REDDIT_DATA_DIRECTORY + submission.title + ".csv", "w", newline="\n")

                csv_writer = csv.DictWriter(csv_file, fieldnames=["created", "date", "subreddit", "id", "body",
                                                                  "parent_id", "score"])
                csv_writer.writeheader()

                comments = submission.comments.list()

                for comment in comments:
                    if isinstance(comment, praw.models.reddit.more.MoreComments):
                        try:
                            if isinstance(comment.comments(), praw.models.reddit.comment.CommentForest):
                                comments = comments + comment.comments().list()
                            else:
                                comments = comments + comment.comments()
                        except TooLarge:
                            logging.error("COMMENTS : Too Large " + search_query)
                    else:
                        csv_writer.writerow({
                            "created": comment.created_utc,
                            "date": current_date.strftime("%Y-%m-%d"),
                            "subreddit": SUBREDDIT,
                            "id": comment.id,
                            "body": comment.body,
                            "parent_id": comment.parent_id,
                            "score": comment.score
                        })

                csv_file.close()

                logging.info("Completed for " + search_query + " with " + submission.title)
                break
            except (ServerError, RequestException) as e:
                logging.warning("RETRY : " + str(retries) + " for " + search_query + str(e))
                retries = retries + 1
            except StopIteration:
                logging.error("SEARCH : No results for " + search_query)
                break

            except (FileNotFoundError, OSError) as e:
                logging.error("FILE: Unable to write to file for " + search_query + str(e))
                break

        if retries == MAX_RETRIES:
            logging.error("CONNECTION: Retry count exceeded")
        current_date = current_date + time_delta


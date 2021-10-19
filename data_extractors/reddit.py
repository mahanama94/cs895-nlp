import datetime
import logging
import csv

import praw
from config import REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, REDDIT_USER_AGENT, REDDIT_DATA_DIRECTORY, LOGGING_DIRECTORY

#
# Best/ Confidence ?= upvotes - downvotes
#
# Top ?= upvotes
#
# Hot ?= upvotes * time
#


start_date = datetime.date(2021, 10, 17)
end_date = datetime.date(2021, 10, 19)

if __name__ == '__main__':

    SUBREDDIT = "wallstreetbets"
    logging.basicConfig(filename=LOGGING_DIRECTORY + SUBREDDIT + ".log", level=logging.INFO)

    reddit_client = praw.Reddit(client_id=REDDIT_CLIENT_ID, client_secret=REDDIT_CLIENT_SECRET,
                                user_agent=REDDIT_USER_AGENT)

    current_date = start_date
    time_delta = datetime.timedelta(days=1)

    while current_date < end_date:
        search_query = "Daily Discussion Thread for " + current_date.strftime("%B %d, %Y")

        submissions = reddit_client.subreddit(SUBREDDIT).search(search_query)
        try:
            submission = next(submissions)
            csv_file = open(REDDIT_DATA_DIRECTORY + submission.title + ".csv", "w", newline="\n")

            csv_writer = csv.DictWriter(csv_file, fieldnames=["date", "subreddit", "id", "body", "parent_id", "score"])
            csv_writer.writeheader()

            comments = submission.comments.list()

            for comment in comments:
                if isinstance(comment, praw.models.reddit.more.MoreComments):
                    comments = comments + comment.comments()
                else:
                    csv_writer.writerow({
                        "date": current_date.strftime("%Y-%m-%d"),
                        "subreddit": SUBREDDIT,
                        "id": comment.id,
                        "body": comment.body,
                        "parent_id": comment.parent_id,
                        "score": comment.score
                    })

            csv_file.close()

            logging.info("Completed for " + search_query + " with " + submission.title)

        except StopIteration:
            logging.error("SEARCH : No results for " + search_query)

        current_date = current_date + time_delta


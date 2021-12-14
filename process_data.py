import argparse
import logging

from data_processing.processing.combine_files import run as run_combine_files
from data_processing.processing.token_count import run as run_token_count
from data_processing.processing.emoji_count import run as run_emoji_count
from data_processing.processing.unique_users import run as unique_user_run
from data_processing.processing.popularity import run as popularity_run

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    function_map = {
        "combine-files": run_combine_files,
        "token-count": run_token_count,
        "emoji-count": run_emoji_count,
        "unique-user-count": unique_user_run,
        "popularity": popularity_run
    }

    parser = argparse.ArgumentParser(description="Data processing for Reddit-Options dataset", add_help=False)

    parser.add_argument("--action", choices=function_map.keys(), default="token-count")

    args, unknown_args = parser.parse_known_args()

    function_map.get(args.action)(parser)

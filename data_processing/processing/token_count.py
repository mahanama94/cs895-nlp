import argparse
import logging

import pandas as pd


def run(parser):
    subparser = argparse.ArgumentParser(parents=[parser])

    subparser.add_argument("--combined-file", type=str, default="processed_data/reddit-combined.csv")
    subparser.add_argument("--token", type=str, default="GME")
    subparser.add_argument("--output-data-dir", type=str, default="processed_data/")

    args = subparser.parse_args()

    combined_file_name = args.combined_file
    token = args.token
    output_data_path = args.output_data_dir

    logging.info("Completed token occurrences for {}".format(token))

    df = pd.read_csv(combined_file_name)

    df["token_count"] = df["body"].astype("str").map(lambda body: body.count(token))

    token_occurrences = df.groupby("date").sum()

    token_occurrences.to_csv(output_data_path + "token-count-" + token + ".csv", columns=["token_count"])

    logging.info("Completed token occurrences for {}".format(token))


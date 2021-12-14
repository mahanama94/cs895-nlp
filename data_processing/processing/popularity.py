import argparse
import logging

import pandas as pd


def run(parser):
    subparser = argparse.ArgumentParser(parents=[parser])

    subparser.add_argument("--combined-file", type=str, default="processed_data/reddit-combined.csv")
    subparser.add_argument("--output-file", type=str, default="processed_data/popularity.csv")

    args = subparser.parse_args()

    combined_file_name = args.combined_file
    output_file = args.output_file

    df = pd.read_csv(combined_file_name)

    grouped_df = df.groupby("date").mean()

    grouped_df.to_csv(output_file)

    logging.info("Completed mean score")





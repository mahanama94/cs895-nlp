import argparse
import logging

import pandas as pd


def run(parser):
    subparser = argparse.ArgumentParser(parents=[parser])

    subparser.add_argument("--combined-file", type=str, default="processed_data/reddit-combined.csv")
    subparser.add_argument("--tokens", type=str, default="GME,gme,#GME,$GME,G M E,GMEE,GMEEE,GMEEEE,GMEEEEE,"
                                                         "GMEEEEEE,Game Stop,Gamestop,GameStop,GAMESTOP,Mr. Cohen,"
                                                         "Cohen,DADDY COHEN")
    subparser.add_argument("--output-file", type=str, default="processed_data/token-counts.csv")

    args = subparser.parse_args()

    combined_file_name = args.combined_file
    tokens = args.tokens.split(",")
    output_file = args.output_file

    df = pd.read_csv(combined_file_name)

    for token in tokens:
        logging.info("Completed token occurrences for {}".format(token))

        df[token] = df["body"].astype("str").map(lambda body: body.count(token))

        logging.info("Completed token occurrences for {}".format(token))

    token_occurrences = df.groupby("date").sum()

    token_occurrences.to_csv(output_file, columns=tokens)




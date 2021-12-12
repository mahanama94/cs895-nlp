import argparse

import emoji
import pandas as pd


def run(parser):
    subparser = argparse.ArgumentParser(parents=[parser])

    subparser.add_argument("--combined-file", type=str, default="processed_data/reddit-combined.csv")
    subparser.add_argument("--output-file", type=str, default="processed_data/emoji-counts.csv")

    args = subparser.parse_args()

    combined_file_name = args.combined_file
    output_file = args.output_file

    emojicons = ['🐂', '🧸', '🚀', '🌕', '🌚', '‍🌈🐻', '🐻', '💎🤲', '🙌', '💎',
                 '🧻🤲', '🍗', '🦍', '💪', '⚡', '🤡', '📈', '🥰', '😍', '💯']

    df = pd.read_csv(combined_file_name)
    for emojicon in emojicons:
        df[emoji.demojize(emojicon).replace(":", "")] = df["body"].astype("str").map(lambda body: body.count(emojicon))

    emoji_occurences = df.groupby("date").sum()

    emoji_occurences.to_csv(output_file, columns=list(map(lambda x: emoji.demojize(x).replace(":", ""), emojicons)))

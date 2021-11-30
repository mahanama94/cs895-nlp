import argparse
import os
import logging
import pandas as pd


def run(parser):
    subparser = argparse.ArgumentParser(parents=[parser])

    subparser.add_argument("--filtered-data-dir", type=str, default="processed_data/reddit-filtered/")
    subparser.add_argument("--output-data-dir", type=str, default="processed_data/")
    subparser.add_argument("--output-file", type=str, default="reddit-combined.csv")

    args = subparser.parse_args()

    filtered_data_path = args.filtered_data_dir
    output_data_path = args.output_data_dir
    output_file_name = args.output_file

    filenames = os.listdir(filtered_data_path)

    df = None

    total_files = len(filenames)
    i = 1
    for filename in filenames:

        logging.info("Starting " + str(i) + " of " + str(total_files) + " filename : " + filename)

        try:
            new_df = pd.read_csv(filtered_data_path + filename)
            if df is None:
                df = new_df

            else:
                df = pd.concat([df, new_df], axis=0)

            logging.info("Completed " + str(i) + " of " + str(total_files) + " filename : " + filename)

        except Exception as e:
            logging.error("Error: " + e.__str__() + str(i) + " of " + str(total_files) + " filename : " + filename)

        i = i + 1

    df.to_csv(output_data_path + output_file_name)

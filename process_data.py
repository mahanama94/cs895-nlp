import argparse
import logging

from data_processing.processing.combine_files import run as run_combine_files

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    function_map = {
        "combine-files": run_combine_files,
    }

    parser = argparse.ArgumentParser(description="Data processing for Reddit-Options dataset", add_help=False)

    parser.add_argument("--action", choices=function_map.keys(), default="combine-files")

    args, unknown_ards = parser.parse_known_args()

    function_map.get(args.action)(parser)

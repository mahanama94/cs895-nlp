import os

import pandas_datareader.data as web

from data_extractors.config import YAHOO_DATA_DIRECTORY

TICKER = os.environ.get("TICKER", "GME")
START = os.environ.get("START", "2010-01-01")
END = os.environ.get("END", "2021-01-01")

data_frame = web.DataReader(TICKER, data_source="yahoo", start=START, end=END)
data_frame.to_csv(YAHOO_DATA_DIRECTORY + TICKER + "-" + START + "-" + END + ".csv", index=False)
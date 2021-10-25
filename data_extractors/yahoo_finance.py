import pandas_datareader.data as web

from config import YAHOO_DATA_DIRECTORY, YAHOO_TICKER, START_DATE, END_DATE

if __name__ == '__main__':

    data_frame = web.DataReader(YAHOO_TICKER, data_source="yahoo", start=START_DATE, end=END_DATE)
    data_frame.to_csv(YAHOO_DATA_DIRECTORY + YAHOO_TICKER + "-" + START_DATE + "-" + START_DATE + ".csv", index=False)
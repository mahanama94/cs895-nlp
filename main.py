# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import pandas_datareader.data as web
import matplotlib.pyplot as plt

# Press the green button in the gutter to run the script.

# tickers = ["DJIA", "^GSPC", "MKTX", "NFLX", "NDAQ", "DPZ"]
tickers = ["GME", "AMC", "SNE", "NDAQ", "^GSPC", "IJR", "FTXD"]

df = web.DataReader(tickers, data_source="yahoo", start="2010-01-01", end="2020-09-01")

fig = plt.figure()
ax1 = fig.add_subplot(321)
ax2 = fig.add_subplot(322)
ax3 = fig.add_subplot(323)
ax4 = fig.add_subplot(324)
ax5 = fig.add_subplot(325)
ax6 = fig.add_subplot(326)

ax1.plot(df['Adj Close'][tickers[0]])
ax1.set_title(tickers[0])

ax2.plot(df['Adj Close'][tickers[1]])
ax2.set_title(tickers[1])
ax3.plot(df['Adj Close'][tickers[2]])
ax3.set_title(tickers[2])
ax4.plot(df['Adj Close'][tickers[3]])
ax4.set_title(tickers[3])
ax5.plot(df['Adj Close'][tickers[4]])
ax5.set_title(tickers[5])
ax6.plot(df['Adj Close'][tickers[5]])
ax6.set_title(tickers[5])

plt.tight_layout()


plt.show()

df.header()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

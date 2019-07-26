from tkinter import *
import matplotlib
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# import quandl
import alpha_vantage
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators

API_KEY = "50KIIW0O49WQBYAI"

# quandl.ApiConfig.api_key = "p9AaTZtsKtVc3sZqv6Bw"
# data = quandl.get('EOD/AAPL')
ts = TimeSeries(key=API_KEY, output_format='pandas')
av_data, meta_data = ts.get_intraday(symbol='AAPL', interval='1min', outputsize='full')

window = Tk()
window.title("AAPL Information")

fig = Figure(figsize=(5, 4), dpi=100)
a = fig.add_subplot(111)
fig.suptitle("AAPL Intraday")
av_data['4. close'].plot(ax=a)
canvas = FigureCanvasTkAgg(fig, master=window)
canvas.draw()
canvas.get_tk_widget().pack(side=LEFT, expand=1, fill=BOTH)

label = Label(window, text="AAPL")
label.pack()
l2 = Label(window, text="test")
l2.pack()

window.mainloop()
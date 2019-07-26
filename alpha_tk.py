from tkinter import *
import matplotlib
matplotlib.use('TkAgg')

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import alpha_vantage
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators

API_KEY = "50KIIW0O49WQBYAI"

window = Tk()
window.title("Stock Info")

fig = Figure(figsize=(5, 4), dpi=100)
a = fig.add_subplot(111)
canvas = FigureCanvasTkAgg(fig, master=window)
canvas.get_tk_widget().pack(side=LEFT, expand=1, fill=BOTH)

fig2 = Figure(figsize=(5, 4), dpi=100)
a2 = fig2.add_subplot(111)
canvas2 = FigureCanvasTkAgg(fig2, master=window)
canvas2.get_tk_widget().pack(side=LEFT, expand=1, fill=BOTH)

def load_stock(stock):
    a.clear()
    a2.clear()

    ts_data = None
    rsi_data = None

    ts = TimeSeries(key=API_KEY, output_format='pandas')
    ti = TechIndicators(key=API_KEY, output_format='pandas')
    
    while ts_data is None:
        try:
            ts_data, _ = ts.get_intraday(symbol=stock, interval='1min', outputsize='full')
        except KeyError:
            print("trying again...")
    
    while rsi_data is None:
        try:
            rsi_data, _ = ti.get_rsi(symbol=stock, interval='60min', time_period=60)
        except KeyError:
            print("trying again...")
    
    ts_data['4. close'].plot(ax=a)
    fig.suptitle(f"{stock} Intraday")
    rsi_data.plot(ax=a2)
    fig2.suptitle(f"{stock} RSI")

    canvas.draw()
    canvas2.draw()
    window.title(f"{stock} Info")

txt = Entry(window, width=10)
txt.insert(0, 'AAPL')

label = Label(window, text="Enter new stock here: ")

def clicked():
    txt.configure(text=f"Loading {txt.get()}...")
    load_stock(txt.get())
    txt.configure(text="Enter new stock here:")

btn = Button(window, text="GO", command=clicked)

btn.pack(side=BOTTOM)
txt.pack(side=BOTTOM)
label.pack(side=BOTTOM)

load_stock('AAPL')

window.mainloop()

# import plotly.plotly as py
import plotly.graph_objs as go
import plotly.figure_factory as ff
from plotly import __version__
from plotly.offline import plot

print(__version__)
import numpy as np
import pandas as pd
import scipy

from scipy import signal
# import os
# os.environ['HTTP_PROXY']="proxyhk.zte.com.cn"
# data = pd.read_csv(os.getcwd()+'\wind_speed_laurel_nebraska.csv')
# print('data length=%d' %(len(data)))
# df = data[0:10]

# table = ff.create_table(df)
# iplot(table)
# py.iplot(table, filename='wind-data-sample')
# trace1 = go.Scatter(
#     x=list(range(len(list(data['10 Min Std Dev'])))),
#     y=list(data['10 Min Std Dev']),
#     mode='lines',
#     name='Wind Data'
# )

# layout = go.Layout(
#     showlegend=True
# )

# trace_data = [trace1]
# fig = go.Figure(data=trace_data, layout=layout)
# plot(fig, filename='wind-raw-data-plot.html',show_link = False)
# py.iplot(fig, filename='wind-raw-data-plot')
import pymysql

try:
  con = pymysql.connect(host='localhost',user='root',password='mysql123',db='gp',charset='utf8')
except pymysql.err.OperationalError as e:
  print('Error is '+str(e))
  sys.exit()
#
df=pd.read_sql_query("SELECT date,close FROM hist_data WHERE code='000538'  AND date>'2014-06-03' AND date < '2016-07-13' ORDER By date",con)
# print(df)
trace1 = go.Scatter(
    x=list(df['date']),
    y=list(df['close']),
    mode='lines',
    name='Wind Data'
)

layout = go.Layout(
    showlegend=True
)

trace_data = [trace1]
fig = go.Figure(data=trace_data, layout=layout)
# plot(fig, filename='wind-raw-data-plot.html')

fc = 0.1
b = 0.08
N = int(np.ceil((4 / b)))
if not N % 2: N += 1
n = np.arange(N)
 
sinc_func = np.sinc(2 * fc * (n - (N - 1) / 2.))
window = 0.42 - 0.5 * np.cos(2 * np.pi * n / (N - 1)) + 0.08 * np.cos(4 * np.pi * n / (N - 1))
sinc_func = sinc_func * window
sinc_func = sinc_func / np.sum(sinc_func)

s = list(df['close'])
new_signal = np.convolve(s, sinc_func)

trace1 = go.Scatter(
    x=list(range(len(new_signal))),
    y=new_signal,
    mode='lines',
    name='Low-Pass Filter',
    marker=dict(
        color='#C54C82'
    )
)

layout = go.Layout(
    title='Low-Pass Filter',
    showlegend=True
)

trace_data = [trace1]
fig = go.Figure(data=trace_data, layout=layout)
# plot(fig, filename='fft-low-pass-filter.html')

fL = 0.1
fH = 0.3
b = 0.08
N = int(np.ceil((4 / b)))
if not N % 2: N += 1  # Make sure that N is odd.
n = np.arange(N)
 
# low-pass filter
hlpf = np.sinc(2 * fH * (n - (N - 1) / 2.))
hlpf *= np.blackman(N)
hlpf = hlpf / np.sum(hlpf)
 
# high-pass filter 
hhpf = np.sinc(2 * fL * (n - (N - 1) / 2.))
hhpf *= np.blackman(N)
hhpf = hhpf / np.sum(hhpf)
hhpf = -hhpf
hhpf[int((N - 1) / 2)] += 1
 
h = np.convolve(hlpf, hhpf)
s = list(df['close'])
new_signal = np.convolve(s, h)

trace1 = go.Scatter(
    x=list(range(len(new_signal))),
    y=new_signal,
    mode='lines',
    name='Band-Pass Filter',
    marker=dict(
        color='#BB47BE'
    )
)

layout = go.Layout(
    title='Band-Pass Filter',
    showlegend=True
)

trace_data = [trace1]
fig = go.Figure(data=trace_data, layout=layout)
plot(fig, filename='fft-band-pass-filter.html')
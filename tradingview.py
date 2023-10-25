import streamlit as st
from streamlit_lightweight_charts import renderLightweightCharts

st.set_page_config(layout="wide", page_title="USDKRW", page_icon=":taxi:")

import json
import numpy as np
import yfinance as yf
import pandas as pd
import pandas_ta as ta

from pprint import pprint

df = yf.Ticker('KRW=X').history(period='24mo', interval='1d')[['Open', 'High', 'Low', 'Close', 'Volume']]

# print(df)

df = df.reset_index()
df.columns = ['time','open','high','low','close','volume']
df['time'] = df['time'].dt.strftime('%Y-%m-%d')  

data = json.loads(
    df.filter(['time','close'], axis=1)
      .rename(columns={"close": "value"})
      .to_json(orient = "records"))

# pprint(data)

priceVolumeChartOptions = {
    "height": 400,
    "rightPriceScale": {
        "scaleMargins": {
            "top": 0.2,
            "bottom": 0.25,
        },
        "borderVisible": False,
    },
    "overlayPriceScales": {
        "scaleMargins": {
            "top": 0.7,
            "bottom": 0,
        }
    },
    "layout": {
        "background": {
            "type": 'solid',
            "color": '#131722'
        },
        "textColor": '#d1d4dc',
    },
    "grid": {
        "vertLines": {
            "color": 'rgba(42, 46, 57, 0)',
        },
        "horzLines": {
            "color": 'rgba(42, 46, 57, 0.6)',
        }
    },
    "timeScale": {
        "borderColor": "rgba(197, 203, 206, 0.8)",
        "barSpacing": 10,
        "minBarSpacing": 8,
        "timeVisible": True,
        "secondsVisible": False,
    },
}

priceVolumeSeries = [
    {
        "type": 'Area',
        "data":  data,
        "options": {
            "topColor": 'rgba(38,198,218, 0.56)',
            "bottomColor": 'rgba(38,198,218, 0.04)',
            "lineColor": 'rgba(38,198,218, 1)',
            "lineWidth": 2,
        }
    },
]

st.subheader("USD/KRW")

renderLightweightCharts([
    {
        "chart": priceVolumeChartOptions,
        "series": priceVolumeSeries
    }
], 'priceAndVolume')
import streamlit as st
from streamlit_lightweight_charts import renderLightweightCharts

st.set_page_config(layout="wide", page_title="USDKRW", page_icon=":taxi:")

st.markdown("""
<style>
    #MainMenu, header, footer {visibility: hidden;}

    /* This code gets the first element on the sidebar,
    and overrides its default styling */
    section[data-testid="stSidebar"] div:first-child {
        top: 0;
        height: 100vh;
    }
</style>
""",unsafe_allow_html=True)

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
    "height": 300,
    "rightPriceScale": {
        "scaleMargins": {
            "top": 0.1,
            "bottom": 0.1,
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

st.markdown('## 달러/원 환율, 대내외 금리 조정과 유가 하락에도 대외 불안에 환율 혼조\n전일 달러/원 환율은 미 국채 금리의 하락과 국제유가 조정 등으로 달러화가 약세를 보임에 따라 역외에서 달러 매도가 지속되고, 국내 증시 반등 등 위험회피심리도 완화됨에 따라 10.6원 급락한 1,343.1원으로 마감함. NDF 역외환율은 10월 PMI 업황 지수에서 미국 경제가 양호하여 달러가 강세를 보였으나 미국채 금리 혼조와 뉴욕 증시 상승, 국제유가 하락 등에 전일보다 0.75원 상승한 1,341.7원에 호가됨 금일 달러/원 환율은 양호한 미국 경제와 미 달러화 강세, 역외 NDF 환율 상승 등으로 1,340원대 초중반에서 등락할 전망. 미국 국채 금리는 혼조세를 보이고, 뉴욕증시는 반등했지만 금리 상승에 대한 부담과 미국 연준의 긴축 지속 우려도 잔존함. 다행히 이- 팔 전쟁에도 유가는 하락하여 국내 수입, 물가 등에 대한 부담은 완화. 국내외 증시가 조정을 보이고, 대외 불안 요인이 남아있어 시장 경계심리는 지속될 전망\n ## 글로벌 동향, 양호한 미국 경제에 비해 부진한 유로 경제, 달러 강세 심화\n전일 미 달러화는 유로화 및 일본 엔화, 영국 파운드화에 대해 모두 강세, 주요 6개 통화로 구성된 달러화 지수는 0.64% 상승한 106.27pt를 기록함. 전일 발표된 S&P 글로벌 미국 제조업 PMI 지수가 50.0을 기록하여 예상치 49.5를 상회했고, 서비스업 PMI 지수 역시 50.9로 예상치 49.9를 상회함. 미국 제조업과 서비스업 업황이 기준치를 다시 상회함에 따라 양호한 미국 경제를 시사함. 반면 유로 PMI 제조업 지수는 43.0으로 예상치 43.7를 하회, 서비스업 역시 47.8로 기준치 50을 하회함. 미국 경제는 전월보다 개선된 반면 유로 경제는 전월보다 둔화, 미국과 유로의 경제 상황 차이에 달러가 유로 대비 강세를 기록함. 미국채 금리는 소폭 상승, 강보합세를 보였으며, 국제유가는 공급 차질 우려 완화로 하락, 배럴당 83달러대로 낮아짐\n\n## 마켓 이슈, 26일 미국 3분기 성장률은 상당히 개선, 4분기에는 둔화 전망\n 26일 발표될 미국 3분기 경제성장률 잠정치는 전분기에 비해 상당히 개선될 것으로 예상됨. 애틀란타 연준에서 매주 추정하여 발표하는 GDPNow는 3분기 성장률이 전기비연율로 5.4%에 달할 것으로 예측함. 지난 7월 이후 미국의 고용과 소비 등의 경제지표가 양호하게 발표됨에 따라 3분기 경제는 전분기에 기록한 2.1%에 비해 두 배 이상의 성장세를 보일 것으로 전망함. 블룸버그 컨센서스에서도 3분기 성장률이 4.5%에 이를 것으로 예상. 이를 감안하면 적어도 3분기 성장은 4%를 상회, 지난 1분기와 2분기에 기록한 2.1%에 비해 두 배 이상의 성장이 가능할 전망. 3분기 성장은 개인소비지출과 민간투자, 순수출 등이 모두 성장을 견인할 것으로 예상됨. 다만 4분기에는 고금리의 실물경제 부담, 주택경기 부진에 따른 건설투자 위축, 그리고 기저효과 등으로 둔화될 전망, 다만 4분기 경제가 얼마나 조정을 보일지가 관건임')

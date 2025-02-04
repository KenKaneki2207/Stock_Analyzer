import streamlit as st
from streamlit_lightweight_charts import renderLightweightCharts
import pandas as pd

charts = ['Candle', 'Line']

def candle_stick(data):
    chartOptions = {
        "layout": {
            "textColor": 'white',
            "background": {
                "type": 'solid',
                "color": 'black'
            }
        },
        "timeScale": {  
            "timeVisible": True,  
            "secondsVisible": False,
            "minBarSpacing": 6,
        },
        "grid": {
            "vertLines": {
                "visible": False  # Disable vertical grid lines
            },
            "horzLines": {
                "visible": False  # Disable horizontal grid lines
            }
        },
        'height': 580,
    }

    seriesCandlestickChart = [
        {
            "type": 'Candlestick',
            "data": data,
            "options": {
                "upColor": '#26a69a',
                "downColor": '#ef5350',
                "borderVisible": False,
                "wickUpColor": '#26a69a',
                "wickDownColor": '#ef5350'
            }
        }
    ]

    renderLightweightCharts([
        {
            "chart": chartOptions,
            "series": seriesCandlestickChart
        }
    ], 'candlestick')

def line_chart(data):
    chartOptions = {
        "layout": {
            "textColor": 'white',
            "background": {
                "type": 'solid',
                "color": 'black'
            }
        },
        "timeScale": {  
            "timeVisible": True,  
            "secondsVisible": False,
            "minBarSpacing": 4,
        },
        "grid": {
            "vertLines": {
                "visible": False  # Disable vertical grid lines
            },
            "horzLines": {
                "visible": False  # Disable horizontal grid lines
            }
        },
        'height': 580,
        'width' : 880,
    }

    seriesLineChart = [
        {
            "type": 'Line',
            "data": data,
            "options": {
                "color": '#26a69a',
                "lineWidth": 2,
                "crossHairMarkerVisible": True,
                "crossHairMarkerRadius": 4,
                "priceLineVisible": True
            }
        }
    ]

    renderLightweightCharts([
        {
            "chart": chartOptions,
            "series": seriesLineChart
        }
    ], 'line_chart')


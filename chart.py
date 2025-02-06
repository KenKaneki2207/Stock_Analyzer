from streamlit_lightweight_charts import renderLightweightCharts

charts = ['Candle', 'Line']

def candle_stick(data, key, date):
    chartOptions = {
        "layout": {
            "textColor": 'white',
            "background": {
                "type": 'solid',
                "color": 'black'
            }
        },
        "timeScale": {  
            "timeVisible": date,  
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
        "height": 550,
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
    ], key)

def line_chart(data, key, date):
    chartOptions = {
        "layout": {
            "textColor": 'white',
            "background": {
                "type": 'solid',
                "color": 'black'
            }
        },
        "timeScale": {  
            "timeVisible": date,  
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
        'height' : 550,
    }

    seriesLineChart = [
        {
            "type": 'Line',
            "data": data,
            "options": {
                "color": '#ffd869',
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
    ], key)

def display_chart(chat, data, key, date):
    if chat == "Candle":
        candle_stick(data, key, date)
    else:
        line_chart(data, key, date)

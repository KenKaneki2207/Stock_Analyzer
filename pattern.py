import warnings

# Suppress all warnings
warnings.filterwarnings("ignore")

# returns the color of the candle
def color(candle):
    open, close = candle[0] , candle[3]
    if open > close:
        return 'r'
    else:
        return 'g'

# returns the length of body and shadow
def anatomy(candle):
    open, high, low, close = candle[0], candle[1], candle[2], candle[3]

    body = round(abs(close - open), 2)
    upper_shadow = round(min((high - close), (high - open)), 2)
    lower_shadow = round(min((close - low), (open - low)), 2)
    full = round(high - low, 2)
    return body, upper_shadow, lower_shadow, full

# hammer pattern
def hammer(candle):
    body, upper_shadow, lower_shadow, full = anatomy(candle)
    if lower_shadow > 1.5*body and upper_shadow/full < 0.1:
        return True
    else:
        return False 

# inverted hammer
def inverted_hammer(candle):
    body, upper_shadow, lower_shadow, full = anatomy(candle)
    if upper_shadow > 1.5*body and lower_shadow/full < 0.1:
        return True
    else:
        return False

# marubozu candle
def marubozu(candle):
    body, upper_shadow, lower_shadow, full = anatomy(candle)
    if lower_shadow/full < 0.1 and upper_shadow/full < 0.1:
        return True
    else:
        return False

# bullush_englufing 
def bullish_engulfing(candle1, candle2):
    body1, upper_shadow1, lower_shadow1, full1 = anatomy(candle1)
    body2, upper_shadow2, lower_shadow2, full2 = anatomy(candle2)
    if color(candle1) == "r" and color(candle2) == "g":
        if body1 < body2:
            if candle1['Close'] >= candle2['Open'] and candle1['Open'] <= candle2['Close']:
                return True 
    return False

# piercing line
def piercing_line(candle1, candle2):
    body1, upper_shadow1, lower_shadow1, full1 = anatomy(candle1)
    body2, upper_shadow2, lower_shadow2, full2 = anatomy(candle2)
    if color(candle1) == "r" and color(candle2) == "g":
        candle_1_50per = body1*0.5 + candle1['Close']
        if candle1['Close'] > candle2['Open'] and candle2['Close'] > (candle_1_50per):
            return True
    return False

def pattern_recoginzer(candle1, candle2):
    if hammer(candle1):
        return "Hammer"
    elif marubozu(candle1):
        return "Marubozu"
    elif bullish_engulfing(candle1, candle2):
        return "Bullish Engulfing"
    elif piercing_line(candle1, candle2):
        return "Pirecing Line"
    else:
        return None

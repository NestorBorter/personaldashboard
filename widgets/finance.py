import yfinance

def get_etf(ticker):
    myetf = yfinance.Ticker(ticker)
    data = myetf.fast_info

    financeDict = dict(data)

    # calculating daily percentage
    financeDict["dailypercentage"] = round((financeDict["lastPrice"] / financeDict["previousClose"]) * 100 - 100, 2)

    return financeDict

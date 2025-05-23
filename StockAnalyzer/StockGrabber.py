from turtledemo.penrose import start
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np
from contourpy.util.data import simple
from googleapiclient.discovery import build
from google.oauth2 import service_account
import requests
from dotenv import load_dotenv
import os
load_dotenv()
Spreadsheet_key = os.getenv('SpreadSheet_Key')


# Define the range and the new values you want to write
SERVICE_ACCOUNT_FILE = 'service_accountTest.json' # your JSON
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SPREADSHEET_ID = Spreadsheet_key  # your sheet ID

# Authenticate
creds = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)
service = build('sheets', 'v4', credentials=creds)

def simpleData(ticker, startDate, endDate):
    simpleValues = {}
    tickerData = yf.Ticker(ticker)
    simpleValues["Previous_Close_Price"] = tickerData.fast_info.previous_close
    simpleValues["Open_Price"] = tickerData.fast_info.open
    if startDate == endDate:
        simpleValues["High_Price"] = tickerData.fast_info.day_high
    else:
        history = tickerData.history(start=startDate, end=endDate)
        highest = history["High"].max()
        simpleValues["High_Price"] = float(highest)
    simpleValues["Ten_Day_Volume"] = tickerData.fast_info.ten_day_average_volume
    return simpleValues

def SMA(ticker, startDate, endDate, window):
    tickerData = yf.Ticker(ticker)
    data = tickerData.history(start=str(startDate), end=str(endDate))
    close_prices = data["Close"]

    sma_series = close_prices.rolling(window=window).mean()



    close_prices.plot(label="Close Price")
    sma_series.plot(label=f"{window}-Day SMA")
    plt.legend()
    plt.show()

    return sma_series.head(15)

def EMA(ticker, startDate, endDate, window):
    tickerData = yf.Ticker(ticker)
    data = tickerData.history(start=str(startDate), end=str(endDate))
    close_prices = data["Close"]

    ema_series = close_prices.ewm(span=window, adjust=False).mean()

     # show first 15 EMA values
    '''
    # Optional: plot Close price and EMA
    close_prices.plot(label="Close Price")
    ema_series.plot(label=f"{window}-Day EMA")
    plt.legend()
    plt.show()
    '''
    return ema_series.head(15)

def plot_SMA_and_EMA(ticker, startDate, endDate, window):
    tickerData = yf.Ticker(ticker)
    data = tickerData.history(start=str(startDate), end=str(endDate))
    close_prices = data["Close"]

    sma_series = close_prices.rolling(window=window).mean()
    ema_series = close_prices.ewm(span=window, adjust=False).mean()

    print(f"First 15 SMA values:\n{sma_series.head(15)}\n")
    print(f"First 15 EMA values:\n{ema_series.head(15)}\n")

    close_prices.plot(label="Close Price")
    sma_series.plot(label=f"{window}-Day SMA")
    ema_series.plot(label=f"{window}-Day EMA")

    plt.legend()
    plt.title(f"{ticker} Close Price, SMA & EMA ({window} days)")
    plt.show()

def Graphing_RSI(ticker, start_date, end_date, window=14):
    ticker_data = yf.Ticker(ticker)
    data = ticker_data.history(start=start_date, end=end_date)

    close = data["Close"]

    # Calculate price changes
    delta = close.diff()

    # Separate gains and losses
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)

    # Calculate average gain/loss
    avg_gain = gain.rolling(window=window).mean()
    avg_loss = loss.rolling(window=window).mean()

    rs = avg_gain / avg_loss.replace(0, 1e-10)
    rsi = 100 - (100 / (1 + rs))
    rsi.name = f"RSI-{window}"

    # Drop NaN values/Cleaning Data
    rsi = rsi.dropna()
    rsi.index = rsi.index.date

    # Plot
    '''
    rsi.plot(label=f"{window}-Day RSI")
    plt.axhline(70, color='red', linestyle='--', label='Overbought (70)')
    plt.axhline(30, color='green', linestyle='--', label='Oversold (30)')
    plt.title(f"{ticker} RSI")
    plt.legend()
    plt.show()
    '''
    #Index is the date, and the header is the bottom
    return [[float(val)] for val in rsi.values]

def RSI(ticker, start_date, end_date, window=14):
    ticker_data = yf.Ticker(ticker)
    data = ticker_data.history(start=start_date, end=end_date)

    close = data["Close"]

    # Calculate price changes
    delta = close.diff()

    # Separate gains and losses
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)

    # Calculate average gain/loss
    avg_gain = gain.rolling(window=window).mean()
    avg_loss = loss.rolling(window=window).mean()

    rs = avg_gain / avg_loss.replace(0, 1e-10)
    rsi = 100 - (100 / (1 + rs))
    rsi.name = f"RSI-{window}"

    # Drop NaN values/Cleaning Data
    rsi = rsi.dropna()
    rsi.index = rsi.index.date

    
    '''
    rsi.plot(label=f"{window}-Day RSI")
    plt.axhline(70, color='red', linestyle='--', label='Overbought (70)')
    plt.axhline(30, color='green', linestyle='--', label='Oversold (30)')
    plt.title(f"{ticker} RSI")
    plt.legend()
    plt.show()
    '''
    #Index is the date, and the header is the bottom
    return rsi.to_string(index=False, header=False)


def MACD(ticker, startDate, endDate, fast=12, slow=26, signal=9):
    tickerData = yf.Ticker(ticker)
    data = tickerData.history(start=str(startDate), end=str(endDate))
    close_prices = data["Close"]

    # Calculate EMAs
    ema_fast = close_prices.ewm(span=fast, adjust=False).mean()
    ema_slow = close_prices.ewm(span=slow, adjust=False).mean()

    # MACD line
    macd_line = ema_fast - ema_slow

    # Signal line
    signal_line = macd_line.ewm(span=signal, adjust=False).mean()

    # MACD Histogram
    macd_histogram = macd_line - signal_line

    #cleaning
    macd_line.index = macd_line.index.date
    signal_line.index = signal_line.index.date
    '''
    # Plot
    plt.figure(figsize=(10, 5))
    plt.plot(macd_line, label="MACD Line", color="blue")
    plt.plot(signal_line, label="Signal Line", color="orange")
    plt.bar(macd_histogram.index, macd_histogram, label="Histogram", color="gray", alpha=0.3)
    plt.title(f"{ticker} MACD Indicator")
    plt.legend()
    plt.show()
    '''
    #Index is the date, and the header is the bottom

    return {
        "MACD": macd_line.to_string(index=True, header=False),
        "Signal": signal_line.to_string(index=True, header=False),
        "Histogram": macd_histogram
    }

def BollingerBands(ticker, startDate, endDate, window=20):
    tickerData = yf.Ticker(ticker)
    data = tickerData.history(start=str(startDate), end=str(endDate))
    close_prices = data["Close"]

    # Calculate the middle band (SMA)
    sma = close_prices.rolling(window=window).mean()

    # Standard deviation
    std = close_prices.rolling(window=window).std()

    # Upper and Lower Bands
    upper_band = sma + (2 * std)
    lower_band = sma - (2 * std)
    '''
    # Plot everything
    plt.figure(figsize=(10, 5))
    plt.plot(close_prices, label="Close Price", color="blue")
    plt.plot(sma, label=f"{window}-Day SMA (Middle Band)", color="orange")
    plt.plot(upper_band, label="Upper Band", color="green", linestyle="--")
    plt.plot(lower_band, label="Lower Band", color="red", linestyle="--")
    plt.fill_between(close_prices.index, lower_band, upper_band, color="gray", alpha=0.1)
    plt.title(f"{ticker} Bollinger Bands")
    plt.legend()
    plt.show()
    '''

    return {
        "SMA": sma,
        "Upper Band": upper_band,
        "Lower Band": lower_band
    }

def VWAP(ticker, Startdate, endDate, interval="1m"):
    tickerData = yf.Ticker(ticker)
    data = tickerData.history(start=Startdate, end=endDate, interval=interval)

   
    if data.empty:
        print("No intraday data available. Choose a recent date within the past 30 days.")
        return

    # Calculate Typical Price
    typical_price = (data["High"] + data["Low"] + data["Close"]) / 3

    # VWAP: Cumulative (Price * Volume) / Cumulative Volume
    vwap = (typical_price * data["Volume"]).cumsum() / data["Volume"].cumsum()

    # Plotting
    plt.figure(figsize=(12, 6))
    plt.plot(data.index, data["Close"], label="Close Price", alpha=0.6)
    plt.plot(data.index, vwap, label="VWAP", color="purple", linewidth=2)
    plt.title(f"{ticker} VWAP on {Startdate}")
    plt.xlabel("Time")
    plt.ylabel("Price")
    plt.legend()
    plt.grid(True)
    plt.show()

    #only works during trading hours
    return vwap.to_string(index = True, header = False)

def stochastic_oscillator(ticker, startDate, endDate, period=5, smooth_k=3):
    tickerData = yf.Ticker(ticker)
    data = tickerData.history(start=str(startDate), end=str(endDate))

    high = data['High']
    low = data['Low']
    close = data['Close']

    # Calculate %K
    lowest_low = low.rolling(window=period).min()
    highest_high = high.rolling(window=period).max()
    percent_k = 100 * ((close - lowest_low) / (highest_high - lowest_low))

    # Calculate %D as SMA of %K
    percent_d = percent_k.rolling(window=smooth_k).mean()

    # Plotting
    plt.figure(figsize=(12, 6))
    plt.plot(data.index, percent_k, label='%K (Fast Stochastic)', color='blue')
    plt.plot(data.index, percent_d, label='%D (Slow Stochastic)', color='orange')
    plt.axhline(80, color='red', linestyle='--', label='Overbought (80)')
    plt.axhline(20, color='green', linestyle='--', label='Oversold (20)')
    plt.title(f'Stochastic Oscillator for {ticker}')
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.legend()
    plt.grid(True)
    plt.show()


    return percent_k, percent_d

def calculate_OBV(ticker, startDate, endDate):
    tickerData = yf.Ticker(ticker)
    data = tickerData.history(start=str(startDate), end=str(endDate))

    close = data['Close']
    volume = data['Volume']

    obv = [0]  

    for i in range(1, len(close)):
        if close[i] > close[i-1]:
            obv.append(obv[-1] + volume[i])
        elif close[i] < close[i-1]:
            obv.append(obv[-1] - volume[i])
        else:
            obv.append(obv[-1])

    data['OBV'] = obv
    '''
    # Plot Close Price and OBV with twin y-axes
    fig, ax1 = plt.subplots(figsize=(12,6))

    ax1.plot(data.index, close, color='black', label='Close Price')
    ax1.set_ylabel('Price ($)', color='black')
    ax1.tick_params(axis='y', labelcolor='black')

    ax2 = ax1.twinx()
    ax2.plot(data.index, data['OBV'], color='purple', label='OBV')
    ax2.set_ylabel('On-Balance Volume', color='purple')
    ax2.tick_params(axis='y', labelcolor='purple')

    # Combine legends
    lines_1, labels_1 = ax1.get_legend_handles_labels()
    lines_2, labels_2 = ax2.get_legend_handles_labels()
    ax1.legend(lines_1 + lines_2, labels_1 + labels_2, loc='upper left')

    plt.title(f'On-Balance Volume (OBV) and Close Price for {ticker}')
    plt.show()
    '''

    return data['OBV']

def paste_numbers_to_column(service, spreadsheet_id, sheet_name, values, start_column='A'):
    """
    Paste list of lists into a Google Sheet column (e.g., A1, A2, A3...)

    Args:
        service: Authorized Sheets API service instance.
        spreadsheet_id: ID of the target spreadsheet.
        sheet_name: Name of the target sheet/tab.
        values: List of lists of numbers (e.g., [[42.6], [37.1], ...])
        start_column: Column to start writing into (default 'A').
    """
    end_row = len(values)
    range_to_update = f"{sheet_name}!{start_column}1:{start_column}{end_row}"

    body = {
        "values": values
    }

    result = service.spreadsheets().values().update(
        spreadsheetId=spreadsheet_id,
        range=range_to_update,
        valueInputOption='RAW', 
        body=body
    ).execute()

    print(f"{result.get('updatedCells')} cells updated.")





range_to_update = 'Sheet1!A1:E6'
print("What stock are you looking to research about?")
stockTicker = input()
result = MACD(stockTicker, "2025-03-19", "2025-05-23")
macd_line = result["MACD"]
signal_line = result["Signal"]
stockSimpleData = simpleData(stockTicker, "2025-03-19", "2025-05-19")
rsi_values = Graphing_RSI(stockTicker, "2025-03-19", "2025-05-23")
paste_numbers_to_column(service, SPREADSHEET_ID, "Sheet2", rsi_values)
values = [
    ['Stock', stockTicker , "03/19/2025", "05/23/2025"],
    ['RSI', str(RSI(stockTicker, "2025-03-19", "2025-05-23"))],
    ['Simple Data',"Previous close", "Open Price", "High Price", "Ten day volume"],
    ["", round(stockSimpleData["Previous_Close_Price"],2), round(stockSimpleData["Open_Price"],2),round(stockSimpleData["High_Price"],2),round(stockSimpleData["Ten_Day_Volume"],2)],
    ["MACD info", "MACD", "", "Signal Line"],
    ["", str(macd_line),"", str(signal_line)]

]

body = {
    'values': values
}


result = service.spreadsheets().values().update(

    spreadsheetId=SPREADSHEET_ID,
    range=range_to_update,
    valueInputOption='RAW',
    body=body
).execute()

bold_request = {
    "requests": [
        {
            "repeatCell": {
                "range": {
                    "sheetId": 0,        
                    "startRowIndex": 0,
                    "endRowIndex": 5,
                    "startColumnIndex": 0,
                    "endColumnIndex": 1
                },
                "cell": {
                    "userEnteredFormat": {
                        "textFormat": {
                            "bold": True
                        }
                    }
                },
                "fields": "userEnteredFormat.textFormat.bold"
            }
        }
    ]
}

response = service.spreadsheets().batchUpdate(
    spreadsheetId=SPREADSHEET_ID,
    body=bold_request
).execute()

print(f"{result.get('updatedCells')} cells updated.")

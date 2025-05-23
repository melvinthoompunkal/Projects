# Stock Technical Analysis & Google Sheets Integration

This Python project fetches, analyzes, visualizes, and uploads stock market technical indicators data using Yahoo Finance API and the Google Sheets API. It supports various technical indicators like SMA, EMA, RSI, MACD, Bollinger Bands, VWAP, Stochastic Oscillator, and OBV.


# Features

* Fetches stock price and volume data using yfinance.
* Calculates technical indicators including:

  * Simple Moving Average (SMA)
  * Exponential Moving Average (EMA)
  * Relative Strength Index (RSI)
  * Moving Average Convergence Divergence (MACD)
  * Bollinger Bands
  * Volume Weighted Average Price (VWAP)
  * Stochastic Oscillator
  * On-Balance Volume (OBV)
* Plots and visualizes stock prices and indicators with matplotlib.
* Authenticates and writes analysis results to a Google Sheet using the Google Sheets API and OAuth2 Service Account.
* Supports user input for stock ticker symbol and date ranges.
* Uses pandas for data manipulation and numpy for numerical calculations.



# Skills & Technologies Used

* Python programming for financial data analysis.
* Working knowledge of yfinance for stock data retrieval.
* Implementation of common technical analysis indicators:

  * Moving averages (SMA, EMA)
  * Momentum indicators (RSI, Stochastic Oscillator)
  * Trend indicators (MACD, Bollinger Bands)
  * Volume indicators (VWAP, OBV)
* Data visualization with matplotlib.
* Interaction with Google Sheets API for real-time data update in spreadsheets.
* Authentication and authorization using Google OAuth2 service accounts.
* Manipulating and cleaning time series data using pandas.
* Using NumPy for numerical operations.
* Reading input and printing results to the console for user interaction.
* Understanding of Google Sheets API batch update requests for formatting.



# Usage

1. Place your Google service account JSON key file (`service_accountTest.json`) in the project directory.
2. Set your target Google Spreadsheet ID in the `SPREADSHEET_ID` variable.
3. Run the script:

   ```bash
   python StockGrabber.py
   ```
4. When prompted, input the stock ticker symbol (e.g., `AAPL`).
5. The script will:

   * Fetch the stock data,
   * Calculate selected technical indicators,
   * Plot charts (optional, uncomment plot sections in the code),
   * Write indicator values and summaries into your specified Google Sheet,
   * Format headers as bold in the sheet.



## Notes

* Ensure you have enabled the Google Sheets API and created a service account with appropriate access.
* The current date range is hardcoded, but you can modify it as needed.
* Plotting is optional and commented out in some functions to avoid blocking script execution.
* Data precision is rounded when uploading to Google Sheets for better readability.
* This code is suitable as a base for expanding into more complex stock analysis and reporting tools.

---

# Installation

Install the required Python packages:

```bash
pip install pandas yfinance matplotlib google-api-python-client google-auth numpy contourpy requests
```

---

## License

This project is open-source and free to use under the MIT License.

import yfinance as yf
import streamlit as st
import datetime as dt



st.title("Stock Monitor")

# Sidebar for stock selection
st.sidebar.header("Select Stock")
stock_symbol = st.sidebar.text_input("Enter Stock Symbol (e.g., AAPL, TSLA, MSFT)", value="AAPL")

# Fetch stock data
if stock_symbol:
    try:
        stock = yf.Ticker(stock_symbol)
        stock_info = stock.info

        # Display stock details
        st.header(f"Stock Details for {stock_symbol}")
        st.write(f"**Company Name:** {stock_info.get('longName', 'N/A')}")
        st.write(f"**Sector:** {stock_info.get('sector', 'N/A')}")
        st.write(f"**Industry:** {stock_info.get('industry', 'N/A')}")
        st.write(f"**Market Cap:** {stock_info.get('marketCap', 'N/A')}")
        st.write(f"**Current Price:** {stock_info.get('currentPrice', 'N/A')}")
        st.write(f"**52 Week High:** {stock_info.get('fiftyTwoWeekHigh', 'N/A')}")
        st.write(f"**52 Week Low:** {stock_info.get('fiftyTwoWeekLow', 'N/A')}")

        # Historical data
        st.header("Historical Data")
        period = st.sidebar.selectbox("Select Period", ["1d", "5d", "1mo", "3mo", "6mo", "1y", "2y", "5y", "10y", "max"])
        hist_data = stock.history(period=period)
        st.line_chart(hist_data['Close'])

    except Exception as e:
        st.error(f"Error fetching data for {stock_symbol}: {e}")
else:
    st.warning("Please enter a stock symbol to monitor.")
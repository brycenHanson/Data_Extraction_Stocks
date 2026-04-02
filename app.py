import streamlit as st 
import yfinance as yf 
import pandas as pd 
import matplotlib.pyplot as plt

st.aset_page_config(page_tite = "Stock Data Extraction App" , layout = "wide")

st.title("Stock Data Extraction App")

st.write("Extract stock market prices from Yahoo Finance using ticker")

st.sidebar.header("User Input")

ticker = st.sidebar.text_input("Enter Stock Ticker" , "AAPL")

start_date = st.sidebar.date_input("Start Date" , pd.to_datetime("2022-01-01")

end_date = st.sidebar.date_input("End Date" , pd.to_datetime("today"))

 #download data button
if st.sidebar.button("Get Data"):

  #create ticker object
stock = yf.Ticker(ticker)

#download historical price data 
df = stock.history(start = start_date , end = end_date)
#check the data
if df.empty: 
  st.error("No data found. Please check the ticker symbol or data range")
 #show sucsess messege
else: 
  st.success(f"Data successfully extracted for {ticker}")
  #Display company Information 
  st.subheader("Company Information")
  info = stock.info 

  company_name = info.get("longName" , "N/A")
  sector = info.get("sector" , "N/A")
  industry = info.get("industry" , "N/A")
  market_cap = info.get("marketCap" , "N/A")
  website = info.get("website" , "N/A")

  st.write(f"**Company Name:** {company_name}")
  st.write(f"**Sector:** {sector}")
  st.write(f"**Industry:** {industry}")
  st.write(f"**Market Cap:** {market}")

  #display stock data
  st.subheader("Historical Stock Data")
  st.dataframe(df)

  #plot Closing Price 
  st.subheader("Closing Price Chart")
  fig, ax = plt.subplots()
  ax.plot(df.index , df["Close"])
  ax.set_xlabel("Date")
  ax.set_ylabel("Closing Price")
  ax.set_title(f"{ticker} Closing Price")
  st.pyplot(filter
            
  #Convert dataframe to CSV for download 
  csv = df.to_csv().encode("utf-8")

  #Download button for csv
  st.download_button(
      label = "Download Data as CSV",
      data = csv,
      file_name = f"{ticker}_stock_data.csv" , 
      mime = "text/csv")                                

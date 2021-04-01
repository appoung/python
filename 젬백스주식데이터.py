import yfinance as yf
data = yf.download(['082270.kq','kq'],start = "2021-04-01")
print(data)
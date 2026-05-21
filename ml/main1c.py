import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from datetime import datetime

data = pd.read_csv('data.csv')
data.head()

data = data.rename(columns={'Open': 'Open', 'High': 'High', 'Low': 'Low', 'Close': 'Close'})
data.head()
data['Date'] = pd.to_datetime(data['Date'])

data = data.sort_values('Date')

plt.plot(data['Date'], data['Open'], label='Open', color='blue', linewidth=2)
plt.plot(data['Date'], data['Close'], label='Close', color='red')
plt.xlabel('Date')
plt.ylabel('Price')
plt.title('Stock Price Over Time')
plt.legend()
plt.grid()
plt.savefig('stock_price1.png')

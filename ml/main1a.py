import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from datetime import datetime

d = pd.read_csv('data.csv')
d.head()

d = d.rename(columns={'Open': 'Open', 'High': 'High', 'Low': 'Low', 'Close': 'Close'})
d.head()

d['Date'] = pd.to_datetime(d['Date'])
d = d.sort_values('Date')

plt.scatter(d['Open'], d['Close'])
plt.savefig('scattera.png')

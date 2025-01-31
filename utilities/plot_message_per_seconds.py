import matplotlib.pyplot as plt
import pandas as pd

# Load data from CSV file
data = pd.read_csv('utilities//message_per_seconds.csv')

# Subtract the first Timestamp from all Timestamps
data['Timestamp'] = data['Timestamp'] - data['Timestamp'].min()

# Plot messages per second
plt.figure(figsize=(10, 6))
plt.plot(data['Timestamp'], data['Messages per second'])
plt.xlabel('Time (seconds)')
plt.ylabel('Messages')
plt.xlim([0, data['Timestamp'].max()])
plt.title('Messages per Second')
plt.show()

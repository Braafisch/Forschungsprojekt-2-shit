import os
import pandas as pd
import matplotlib.pyplot as plt

latency_value = "new_system"
size_value = "pfusch"
data_load = pd.read_csv('src\\results\\process_load_diffrents.csv')

if not os.path.exists(f'plots\\{size_value}MB'):
    os.makedirs(f'plots\\{size_value}MB')
if not os.path.exists(f'plots\\{size_value}MB\\{latency_value}Hz'):
    os.mkdir(f'plots\\{size_value}MB\\{latency_value}Hz')

start = 0
end = 300
begin_time = data_load['Timestamp'].min()
data_load['Timestamp'] = data_load['Timestamp'] - begin_time
data_load = data_load[(data_load['Timestamp'] >= start) & (data_load['Timestamp'] <= end)]
data_load['Timestamp'] = data_load['Timestamp'] - start

if end > data_load['Timestamp'].max():
    end = round(data_load['Timestamp'].max())

# Plot and save CPU Load
plt.figure(figsize=(10, 5))
plt.plot(data_load['Timestamp'], data_load['CPU Load'], label='CPU Load', color='green')
plt.xlabel('Time')
plt.ylabel('CPU Load (%)')
plt.ylim(0, 100)
plt.xlim(0, end)
plt.legend()
plt.title('CPU Load Over Time')
# Add vertical red stripes every 10 seconds
for i in range(0, int(end-start), 10):
    plt.axvline(x=i, color='red', alpha=0.2, linestyle='--')
plt.savefig(f'plots\\{size_value}MB\\{latency_value}Hz\\cpu_load.svg', format='svg')
plt.savefig(f'plots\\{size_value}MB\\{latency_value}Hz\\cpu_load.png', format='png')
plt.close()

# Plot and save Memory Usage
plt.figure(figsize=(10, 5))
plt.plot(data_load['Timestamp'], data_load['Used Memory'], label='Memory Usage', color='orange')
plt.xlabel('Time')
plt.ylabel('Memory Usage (MB)')
plt.ylim(0, 300)
plt.xlim(0, end)
plt.legend()
plt.title('Memory Usage Over Time')

# Add vertical red stripes every 10 seconds
for i in range(0, int(end-start), 10):
    plt.axvline(x=i, color='red', alpha=0.2, linestyle='--')

plt.savefig(f'plots\\{size_value}MB\\{latency_value}Hz\\memory_usage.svg', format='svg')
plt.savefig(f'plots\\{size_value}MB\\{latency_value}Hz\\memory_usage.png', format='png')
plt.close()
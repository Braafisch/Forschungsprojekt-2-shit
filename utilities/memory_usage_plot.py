import os
import pandas as pd
import matplotlib.pyplot as plt

latency_value = 92
size_value = 4
# Load the data
data_load = pd.read_csv('src\\results\\24_11_04_2024-10-17-16-32-11_1MB_100Hz_system_load.csv')
# data_latency = pd.read_csv('src\\results\\radar_latency_50MB_200Hz.csv')
# data_throughput = pd.read_csv(f'src\\results\\throughput_log_50MB_200Hz.csv')
# data_load = pd.read_csv(f'src\\results\\system_load_{size_value}MB_{latency_value}HZ.csv')
# data_latency = pd.read_csv(f'src\\results\\radar_latency_{size_value}MB_{latency_value}HZ.csv')
# data_throughput = pd.read_csv(f'src\\results\\throughput_log_{size_value}MB_{latency_value}HZ.csv')

if not os.path.exists(f'plots\\{size_value}MB'):
    os.makedirs(f'plots\\{size_value}MB')
if not os.path.exists(f'plots\\{size_value}MB\\{latency_value}Hz'):
    os.mkdir(f'plots\\{size_value}MB\\{latency_value}Hz')

# only use 30 seconds of data_load for better visualization of the plot
# and in the time between 10 and 40 seconds
# the data_load in timestamp looks like this: 1719578740.2194355
# get the max of the min timestamp of both data_load and data_latency
start = 20
end = 320
# begin_time = max(data_load['Timestamp'].min(), data_latency['Publish Time'].min(), data_throughput['Timestamp'].min())
# begin_time = max(data_load['Timestamp'].min(), data_latency['Publish Time'].min())
begin_time = data_load['Timestamp'].min()
data_load['Timestamp'] = data_load['Timestamp'] - begin_time
data_load = data_load[(data_load['Timestamp'] >= start) & (data_load['Timestamp'] <= end)]
data_load['Timestamp'] = data_load['Timestamp'] - start
# set beginning of time to 0
# data_latency['Publish Time'] = data_latency['Publish Time'] - begin_time
# data_latency = data_latency[(data_latency['Publish Time'] >= start) & (data_latency['Publish Time'] <= end)]
# data_latency['Publish Time'] = data_latency['Publish Time'] - start

# # set beginning of time to 0
# data_throughput['Timestamp'] = data_throughput['Timestamp'] - begin_time
# data_throughput = data_throughput[(data_throughput['Timestamp'] >= start) & (data_throughput['Timestamp'] <= end)]
# data_throughput['Timestamp'] = data_throughput['Timestamp'] - start
# data_throughput['Throughput (msgs/sec)'] = data_throughput['Throughput (msgs/sec)'] - latency_value

# plot the data

# Plot and save CPU Load
plt.figure(figsize=(10, 5))
plt.plot(data_load['Timestamp'], data_load['CPU Load'], label='CPU Load', color='green')
plt.xlabel('Time')
plt.ylabel('CPU Load (%)')
plt.ylim(0, 100)
plt.xlim(0, end- start)
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
plt.plot(data_load['Timestamp'], data_load['Percent Used'], label='Memory Usage', color='orange')
plt.xlabel('Time')
plt.ylabel('Memory Usage (%)')
plt.ylim(0, 100)
plt.xlim(0, end- start)
plt.legend()
plt.title('Memory Usage Over Time')

# Add vertical red stripes every 10 seconds
for i in range(0, int(end-start), 10):
    plt.axvline(x=i, color='red', alpha=0.2, linestyle='--')

plt.savefig(f'plots\\{size_value}MB\\{latency_value}Hz\\memory_usage.svg', format='svg')
plt.savefig(f'plots\\{size_value}MB\\{latency_value}Hz\\memory_usage.png', format='png')
plt.close()

# Plot and save Latency
# plt.figure(figsize=(10, 5))
# plt.plot(data_latency['Publish Time'], data_latency['Latency'], label='Latency', color='red')
# plt.xlabel('Time')
# plt.ylabel('Latency (s)')
# # Calculate the maximum latency and set y-axis limit with extra space
# latency_max = data_latency['Latency'].max()
# plt.ylim(0, latency_max * 1.1)
# plt.xlim(start, end- start)
# plt.legend()
# plt.title('Latency Over Time')
# plt.savefig(f'plots\\{size_value}MB\\{latency_value}Hz\\latency.svg', format='svg')
# plt.savefig(f'plots\\{size_value}MB\\{latency_value}Hz\\latency.png', format='png')
# plt.close()

# # Plot and save Throughput as a bar chart without gaps
# plt.figure(figsize=(10, 5))
# plt.bar(data_throughput['Timestamp'], data_throughput['Throughput (msgs/sec)'], label='Throughput', color='blue')
# plt.xlabel('Time')
# plt.ylabel('Throughput (msgs/sec)')
# # plt.ylim(0, 200) # Uncomment and adjust if you want to set specific y-axis limits
# plt.xlim(start, end- start)
# plt.ylim(data_throughput['Throughput (msgs/sec)'].min()-1,data_throughput['Throughput (msgs/sec)'].max()+1)
# plt.legend()
# plt.title('Throughput Over Time')
# plt.savefig(f'plots\\{size_value}MB\\{latency_value}Hz\\throughput.svg', format='svg')
# plt.savefig(f'plots\\{size_value}MB\\{latency_value}Hz\\throughput.png', format='png')
# plt.close()

# plt.tight_layout()
# plt.show()

# save mean, max and min values in .txt file

# Calculate the mean values
cpu_load_mean = data_load['CPU Load'].mean()
memory_usage_mean = data_load['Percent Used'].mean()
memory_usage_real_mean = data_load['Used Memory'].mean()
# latency_mean = data_latency['Latency'].mean()
# throughput_mean = data_throughput['Throughput (msgs/sec)'].mean()

# Calculate the max values
cpu_load_max = data_load['CPU Load'].max()
memory_usage_max = data_load['Percent Used'].max()
memory_usage_real_max = data_load['Used Memory'].max()
# latency_max = data_latency['Latency'].max()
# throughput_max = data_throughput['Throughput (msgs/sec)'].max()

# Calculate the min values
cpu_load_min = data_load['CPU Load'].min()
memory_usage_min = data_load['Percent Used'].min()
memory_usage_real_min = data_load['Used Memory'].min()
# latency_min = data_latency['Latency'].min()
# throughput_min = data_throughput['Throughput (msgs/sec)'].min()

# Save the values in a .txt file
with open(f'plots\\{size_value}MB\\{latency_value}Hz\\system_metrics.txt', 'w') as f:
    f.write("System Metrics:\n")
    f.write(f"Memory-Usage: Durchschnitt = {round(memory_usage_mean, 2)} % ({round(memory_usage_mean/100*7.7, 2)} GiB), Maximum = {round(memory_usage_max, 2)} % ({round(memory_usage_max/100*7.7, 2)} GiB), Minimum = {round(memory_usage_min, 2)} % ({round(memory_usage_min/100*7.7, 2)} GiB)\n")
    f.write(f"CPU-Load: Durchschnitt = {round(cpu_load_mean, 2)} %, Maximum = {round(cpu_load_max, 2)} %, Minimum = {round(cpu_load_min, 2)} %\n")
    # f.write(f"Latenz: Durchschnitt = {round(latency_mean*1000, 2)} ms , Maximum = {round(latency_max*1000, 2)} ms, Minimum = {round(latency_min*1000, 2)} ms\n")
    # f.write(f"Durchsatz: Durchschnitt = {round(throughput_mean, 2)}, Maximum = {round(throughput_max, 2)}, Minimum = {round(throughput_min, 2)}\n")
    # f.write(f"Memory-Usage: Durchschnitt = {memory_usage_mean} % ({memory_usage_mean/100*7.7} GiB), Maximum = {memory_usage_max} % ({memory_usage_max/100*7.7} GiB), Minimum = {memory_usage_min} % ({memory_usage_min/100*7.7} GiB)\n")
    # f.write(f"CPU-Load: Durchschnitt = {cpu_load_mean} %, Maximum = {cpu_load_max} %, Minimum = {cpu_load_min} %\n")
    # f.write(f"Latenz: Durchschnitt = {latency_mean*1000} ms , Maximum = {latency_max*1000} ms, Minimum = {latency_min*1000} ms\n")
    # f.write(f"Durchsatz: Durchschnitt = {throughput_mean}, Maximum = {throughput_max}, Minimum = {throughput_min}\n")    
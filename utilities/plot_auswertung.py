import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


categories = ['1MB/10Hz', '1MB/100Hz', '4MB/10Hz']
mean_values = [575.01, 612.12, 591.02]
max_values = [595.28, 704.6, 612.8] 
min_values = [541.7, 550.55, 579.66] 

x = np.arange(len(categories))
width = 0.35

fig, ax = plt.subplots(figsize=(10, 6))
rects1 = ax.bar(x - width/2, max_values, width, label='Maximum', color='skyblue')
rects2 = ax.bar(x + width/2, min_values, width, label='Minimum', color='lightcoral')
rects3 = ax.bar(x, mean_values, width, label='Mean', color='yellow', alpha=0.7)

ax.set_ylabel('Memory Usage (MB)')
ax.set_title('Maximum and Minimum Values')
ax.set_xticks(x)
ax.set_xticklabels(categories)
ax.legend()

# Add value labels on top of each bar
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate(f'{height}Msg/s',
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),
                    textcoords="offset points",
                    ha='center', va='bottom')
        
autolabel(rects1)
autolabel(rects2)
autolabel(rects3)

plt.ylim(0, 1000)  # Set y-axis limits from 0 to 100%
plt.show()

colors = ['red', 'blue', 'green', 'orange', 'purple', 'brown', 'pink', 'gray', 'olive', 'cyan']

file1 = "4MB_10Hz"
file2 = "1MB_100Hz"
file3 = "1MB_10Hz"
process_load_data_1mb_10hz = pd.read_csv(f'src\\results\\new_messagurements\\{file3}\\process_load_diffrents.csv')
process_load_data_1mb_100hz = pd.read_csv(f'src\\results\\new_messagurements\\{file2}\\process_load_diffrents.csv')
process_load_data_4mb_10hz = pd.read_csv(f'src\\results\\new_messagurements\\{file1}\\process_load_diffrents.csv')
msg_per_seconds_radar_data_1mb_10hz = pd.read_csv(f'src\\results\\new_messagurements\\{file3}\\message_per_seconds.csv')
msg_per_seconds_radar_data_1mb_100hz = pd.read_csv(f'src\\results\\new_messagurements\\{file2}\\message_per_seconds.csv')
msg_per_seconds_radar_data_4mb_10hz = pd.read_csv(f'src\\results\\new_messagurements\\{file1}\\message_per_seconds.csv')

start_time_1mb_10hz = 1737224091.4501011
start_tine_1mb_100hz = 1737209744.357547
start_time_4mb_10hz = 1737218942.326054

end_time_1mb_10hz = 1737224091.4501011 + 600
end_time_1mb_100hz = 1737209744.357547 + 600
end_time_4mb_10hz = 1737218942.326054 + 600

process_load_data_1mb_10hz = process_load_data_1mb_10hz[(process_load_data_1mb_10hz['Timestamp'] >= start_time_1mb_10hz) & (process_load_data_1mb_10hz['Timestamp'] <= end_time_1mb_10hz)]
process_load_data_1mb_100hz = process_load_data_1mb_100hz[(process_load_data_1mb_100hz['Timestamp'] >= start_tine_1mb_100hz) & (process_load_data_1mb_100hz['Timestamp'] <= end_time_1mb_100hz)]
process_load_data_4mb_10hz = process_load_data_4mb_10hz[(process_load_data_4mb_10hz['Timestamp'] >= start_time_4mb_10hz) & (process_load_data_4mb_10hz['Timestamp'] <= end_time_4mb_10hz)]

msg_per_seconds_radar_data_1mb_10hz = msg_per_seconds_radar_data_1mb_10hz[(msg_per_seconds_radar_data_1mb_10hz['Timestamp'] >= start_time_1mb_10hz) & (msg_per_seconds_radar_data_1mb_10hz['Timestamp'] <= end_time_1mb_10hz)]
msg_per_seconds_radar_data_1mb_100hz = msg_per_seconds_radar_data_1mb_100hz[(msg_per_seconds_radar_data_1mb_100hz['Timestamp'] >= start_tine_1mb_100hz) & (msg_per_seconds_radar_data_1mb_100hz['Timestamp'] <= end_time_1mb_100hz)]
msg_per_seconds_radar_data_4mb_10hz = msg_per_seconds_radar_data_4mb_10hz[(msg_per_seconds_radar_data_4mb_10hz['Timestamp'] >= start_time_4mb_10hz) & (msg_per_seconds_radar_data_4mb_10hz['Timestamp'] <= end_time_4mb_10hz)]

fig, ax1 = plt.subplots(figsize=(12, 6))
ax1.plot(process_load_data_1mb_10hz['Timestamp'] - start_time_1mb_10hz, process_load_data_1mb_10hz['Total CPU Load'], label='1MB/10Hz', color=colors[0])
ax1.plot(process_load_data_1mb_100hz['Timestamp'] - start_tine_1mb_100hz, process_load_data_1mb_100hz['Total CPU Load'], label='1MB/100Hz', color=colors[1])
ax1.plot(process_load_data_4mb_10hz['Timestamp'] - start_time_4mb_10hz, process_load_data_4mb_10hz['Total CPU Load'], label='4MB/10Hz', color=colors[2])
ax1.set_xlabel('Time (s)')
ax1.set_ylabel('CPU Load (%)')
ax1.set_title('CPU Load Over Time')
ax1.legend()
ax1.set_ylim(0, 200)
ax1.set_xlim(0, 600)
plt.show()

fig, ax1 = plt.subplots(figsize=(12, 6))
ax1.plot(process_load_data_1mb_10hz['Timestamp'] - start_time_1mb_10hz, process_load_data_1mb_10hz['Total Used Memory'], label='1MB/10Hz', color=colors[0])
ax1.plot(process_load_data_1mb_100hz['Timestamp'] - start_tine_1mb_100hz, process_load_data_1mb_100hz['Total Used Memory'], label='1MB/100Hz', color=colors[1])
ax1.plot(process_load_data_4mb_10hz['Timestamp'] - start_time_4mb_10hz, process_load_data_4mb_10hz['Total Used Memory'], label='4MB/10Hz', color=colors[2])
ax1.set_xlabel('Time (s)')
ax1.set_ylabel('Memory Load (MB)')
ax1.set_title('Memory Load Over Time')
ax1.legend()
ax1.set_ylim(0, 1000)
ax1.set_xlim(0, 600)
plt.show()

fig, ax1 = plt.subplots(figsize=(12, 6))
ax1.plot(msg_per_seconds_radar_data_1mb_10hz['Timestamp'] - start_time_1mb_10hz, msg_per_seconds_radar_data_1mb_10hz['Messages per second'], label='1MB/10Hz', color=colors[0],drawstyle='steps-pre')
ax1.plot(msg_per_seconds_radar_data_1mb_100hz['Timestamp'] - start_tine_1mb_100hz, msg_per_seconds_radar_data_1mb_100hz['Messages per second'], label='1MB/100Hz', color=colors[1],drawstyle='steps-pre')
ax1.plot(msg_per_seconds_radar_data_4mb_10hz['Timestamp'] - start_time_4mb_10hz, msg_per_seconds_radar_data_4mb_10hz['Messages per second'], label='4MB/10Hz', color=colors[2],drawstyle='steps-pre')
ax1.set_xlabel('Time (s)')
ax1.set_ylabel('Messages per second (Msg/s)')
ax1.set_title('Memory Load Over Time')
ax1.legend()
ax1.set_ylim(0, 100)
ax1.set_xlim(0, 600)
plt.show()

msg_per_seconds_radar_data_1mb_10hz = msg_per_seconds_radar_data_1mb_10hz[msg_per_seconds_radar_data_1mb_10hz['Messages per second'] > 0]
msg_per_seconds_radar_data_1mb_100hz = msg_per_seconds_radar_data_1mb_100hz[msg_per_seconds_radar_data_1mb_100hz['Messages per second'] > 0]
msg_per_seconds_radar_data_4mb_10hz = msg_per_seconds_radar_data_4mb_10hz[msg_per_seconds_radar_data_4mb_10hz['Messages per second'] > 0]

len_msg_per_seconds_radar_data_1mb_10hz = len(msg_per_seconds_radar_data_1mb_10hz)
len_msg_per_seconds_radar_data_1mb_100hz = len(msg_per_seconds_radar_data_1mb_100hz)
len_msg_per_seconds_radar_data_4mb_10hz = len(msg_per_seconds_radar_data_4mb_10hz)

total_messages_1mb_10hz = msg_per_seconds_radar_data_1mb_10hz['Messages per second'].sum()
total_messages_1mb_100hz = msg_per_seconds_radar_data_1mb_100hz['Messages per second'].sum()
total_messages_4mb_10hz = msg_per_seconds_radar_data_4mb_10hz['Messages per second'].sum()

mean_messages_per_second_1mb_10hz = total_messages_1mb_10hz / len_msg_per_seconds_radar_data_1mb_10hz
mean_messages_per_second_1mb_100hz = total_messages_1mb_100hz / len_msg_per_seconds_radar_data_1mb_100hz
mean_messages_per_second_4mb_10hz = total_messages_4mb_10hz / len_msg_per_seconds_radar_data_4mb_10hz

mean_values = [round(mean_messages_per_second_1mb_10hz, 2), round(mean_messages_per_second_1mb_100hz, 2), round(mean_messages_per_second_4mb_10hz, 2)]
max_values = [round(msg_per_seconds_radar_data_1mb_10hz['Messages per second'].max(), 2), round(msg_per_seconds_radar_data_1mb_100hz['Messages per second'].max(), 2), round(msg_per_seconds_radar_data_4mb_10hz['Messages per second'].max(), 2)]
min_values = [round(msg_per_seconds_radar_data_1mb_10hz['Messages per second'].min(), 2), round(msg_per_seconds_radar_data_1mb_100hz['Messages per second'].min(), 2), round(msg_per_seconds_radar_data_4mb_10hz['Messages per second'].min(), 2)]

fig, ax = plt.subplots(figsize=(12, 6))
rects1 = ax.bar(x - width/2, max_values, width, label='Maximum', color='skyblue')
rects2 = ax.bar(x + width/2, min_values, width, label='Minimum', color='lightcoral')
rects3 = ax.bar(x, mean_values, width, label='Mean', color='yellow', alpha=0.7)

ax.set_ylabel('Messages per second (Msg/s)')
ax.set_title('Maximum and Minimum Values')
ax.set_xticks(x)
ax.set_xticklabels(categories)
ax.legend()

autolabel(rects1)
autolabel(rects2)
autolabel(rects3)

plt.ylim(0, 100)  # Set y-axis limits from 0 to 100%
plt.show()
import os
import pandas as pd
import matplotlib.pyplot as plt

specific_file = "1MB_100Hz"
# result_plot_path = f"plots\\new_results\\{specific_file}"
colors = ['red', 'blue', 'green', 'orange', 'purple', 'brown', 'pink', 'gray', 'olive', 'cyan']

# if not os.path.exists(result_plot_path):
#     os.makedirs(result_plot_path)

process_load_data = pd.read_csv(f'src\\results\\new_messagurements\\{specific_file}\\process_load_diffrents.csv')
message_per_seconds_data = pd.read_csv(f'src\\results\\new_messagurements\\{specific_file}\\message_per_seconds.csv')
msg_counter_data = pd.read_csv(f'src\\results\\new_messagurements\\{specific_file}\\msg_counter.csv')
other_topics_data = pd.read_csv(f'src\\results\\new_messagurements\\{specific_file}\\other_topics.csv')

# get highest start time of all dataframes
start_time = max(process_load_data['Timestamp'].min(), message_per_seconds_data['Timestamp'].min(), msg_counter_data['Timestamp'].min(), other_topics_data['Timestamp'].min())
end_time = min(process_load_data['Timestamp'].max(), message_per_seconds_data['Timestamp'].max(), msg_counter_data['Timestamp'].max(), other_topics_data['Timestamp'].max())
print(start_time)
# start_time = max(process_load_data['Timestamp'].min(), message_per_seconds_data['Timestamp'].min())
# end_time = min(process_load_data['Timestamp'].max(), message_per_seconds_data['Timestamp'].max())
# filter dataframes to only include data between start_time and end_time
process_load_data = process_load_data[(process_load_data['Timestamp'] >= start_time) & (process_load_data['Timestamp'] <= end_time)]
message_per_seconds_data = message_per_seconds_data[(message_per_seconds_data['Timestamp'] >= start_time) & (message_per_seconds_data['Timestamp'] <= end_time)]
msg_counter_data = msg_counter_data[(msg_counter_data['Timestamp'] >= start_time) & (msg_counter_data['Timestamp'] <= end_time)]
other_topics_data = other_topics_data[(other_topics_data['Timestamp'] >= start_time) & (other_topics_data['Timestamp'] <= end_time)]
# set beginning of time to 0
process_load_data['Timestamp'] = process_load_data['Timestamp'] - start_time
message_per_seconds_data['Timestamp'] = message_per_seconds_data['Timestamp'] - start_time
msg_counter_data['Timestamp'] = msg_counter_data['Timestamp'] - start_time
other_topics_data['Timestamp'] = other_topics_data['Timestamp'] - start_time

x_max = 600
cpu_y_max = 250

# plot total cpu load and total memory load in one plot
fig,ax1 = plt.subplots(figsize=(12, 6))
plt.subplots_adjust(right=0.85, left=0.15)
# fig.tight_layout() 
ax2 = ax1.twinx()
ax3 = ax1.twinx()
ax4 = ax1.twinx()

# offset label
ax3.yaxis.set_ticks_position('left')
ax3.yaxis.set_label_position('left')
ax3.spines.left.set_position(('axes', -0.1))
ax4.spines.right.set_position(('axes', 1.1))
# Plot CPU Load
ax1.plot(process_load_data['Timestamp'], process_load_data['Total CPU Load'], label='CPU Load', color=colors[2])
# ax1.plot(process_load_data['Timestamp'], process_load_data['Radar CPU'], label='Radar CPU Load', color=colors[3])
# ax1.plot(process_load_data['Timestamp'], process_load_data['Ameise CPU'], label='Ameise CPU Load', color=colors[5])
# ax1.plot(process_load_data['Timestamp'], process_load_data['Core CPU'], label='Core CPU Load', color=colors[6])
ax2.plot(process_load_data['Timestamp'], process_load_data['Total Used Memory'], label='Memory Load', color=colors[1])
ax3.plot(msg_counter_data['Timestamp'], msg_counter_data['Messages'], label='Message Counter', color=colors[0],drawstyle='steps-pre')
ax4.plot(message_per_seconds_data['Timestamp'], message_per_seconds_data['Messages per second'], label='Messages per second', color=colors[4])
# Plot Memory Load
ax1.set_xlim(0, x_max)
ax1.set_ylim(0,cpu_y_max)
ax2.set_ylim(500,2500)
ax3.set_ylim(0,2500)
ax4.set_ylim(0,125)
# Labeling
ax1.set_xlabel('Time')
ax1.set_ylabel('CPU Load (%)', color=colors[2])
ax2.set_ylabel('Memory Load (MB)', color=colors[1])
ax3.set_ylabel('Message Counter', color=colors[0])
ax4.set_ylabel('Messages per second', color=colors[4])
ax1.set_title('CPU and Memory Load Over Time')
ax1.tick_params(axis='y', colors=colors[2])
ax2.tick_params(axis='y', colors=colors[1])
ax3.tick_params(axis='y', colors=colors[0])
ax4.tick_params(axis='y', colors=colors[4])
plt.show()
print(f"Berlin was geht ab!")

sec_fig, sec_ax1 = plt.subplots(figsize=(12, 6))
sec_ax1.plot(process_load_data['Timestamp'], process_load_data['Total CPU Load'], label='Total', color=colors[2])
sec_ax1.plot(process_load_data['Timestamp'], process_load_data['Radar CPU'], label='Radar', color=colors[3])
sec_ax1.plot(process_load_data['Timestamp'], process_load_data['Ameise CPU'], label='Ameise', color=colors[5])
sec_ax1.plot(process_load_data['Timestamp'], process_load_data['Core CPU'], label='Core', color=colors[6])
sec_ax1.set_xlim(0, x_max)
sec_ax1.set_ylim(0,cpu_y_max)
sec_ax1.set_xlabel('Time')
sec_ax1.set_ylabel('CPU Load (%)')
sec_ax1.set_title('CPU Load Over Time')
sec_ax1.legend()
plt.show()

third_fig, third_ax1 = plt.subplots(figsize=(12, 6))
third_ax2 = third_ax1.twinx()
third_ax1.plot(process_load_data['Timestamp'], process_load_data['Core CPU'], label='Core CPU', color=colors[0])
third_ax2.plot(other_topics_data['Timestamp'], other_topics_data['Messages'], label='Ameise Msg per second', color=colors[1])

# third_ax2.plot(message_per_seconds_data['Timestamp'], message_per_seconds_data['Messages per second'], label='Radar Msg per second', color=colors[2])
third_ax1.set_xlim(0, x_max)
third_ax1.set_ylim(0,cpu_y_max-50)
third_ax2.set_ylim(0,5000)
third_ax1.set_xlabel('Time')
third_ax1.set_ylabel('CPU Load (%)', color=colors[0])
third_ax2.set_ylabel('Messages per second', color=colors[1])
third_ax1.tick_params(axis='y', colors=colors[0])
third_ax2.tick_params(axis='y', colors=colors[1])
third_ax1.set_title('Core CPU Load and Msg/s Over Time')
plt.show()

# Plot all Memory Load
fourth_fig, fourth_ax1 = plt.subplots(figsize=(12, 6))
# fourth_ax2 = fourth_ax1.twinx()
fourth_ax1.plot(process_load_data['Timestamp'], process_load_data['Total Used Memory'], label='Total', color=colors[1])
fourth_ax1.plot(process_load_data['Timestamp'], process_load_data['Radar Memory'], label='Radar', color=colors[3])
fourth_ax1.plot(process_load_data['Timestamp'], process_load_data['Ameise Memory'], label='Ameise', color=colors[5])
fourth_ax1.plot(process_load_data['Timestamp'], process_load_data['Core Memory'], label='Core', color=colors[6])
fourth_ax1.set_xlim(0, x_max)
fourth_ax1.set_ylim(0,2500)
# fourth_ax2.set_ylim(30,33)
fourth_ax1.set_xlabel('Time')
fourth_ax1.set_ylabel('Memory Load (MB)')
fourth_ax1.set_title('Memory Load Over Time')
# fourth_ax1.legend()
plt.show()

# Plot Radar CPU Load Memory Load Message Counter Message per second over Time
fifth_fig, fifth_ax1 = plt.subplots(figsize=(12, 6))
plt.subplots_adjust(right=0.85, left=0.15)
fifth_ax2 = fifth_ax1.twinx()
fifth_ax3 = fifth_ax1.twinx()
fifth_ax4 = fifth_ax1.twinx()

fifth_ax3.yaxis.set_ticks_position('left')
fifth_ax3.yaxis.set_label_position('left')
fifth_ax3.spines.left.set_position(('axes', -0.1))
fifth_ax4.spines.right.set_position(('axes', 1.1))

fifth_ax1.plot(process_load_data['Timestamp'], process_load_data['Radar CPU'], label='CPU Load', color=colors[3])
fifth_ax2.plot(process_load_data['Timestamp'], process_load_data['Radar Memory'], label='Memory Load', color=colors[8])
fifth_ax3.plot(msg_counter_data['Timestamp'], msg_counter_data['Messages'], label='Message Counter', color=colors[0],drawstyle='steps-pre')
fifth_ax4.plot(message_per_seconds_data['Timestamp'], message_per_seconds_data['Messages per second'], label='Messages per second', color=colors[4])
fifth_ax1.set_xlim(0, x_max)
fifth_ax1.set_ylim(0,30)
fifth_ax2.set_ylim(31,31.5)
fifth_ax3.set_ylim(0,2500)
fifth_ax4.set_ylim(0,20)
fifth_ax1.set_xlabel('Time')
fifth_ax1.set_ylabel('CPU Load (%)', color=colors[3])
fifth_ax2.set_ylabel('Memory Load (MB)', color=colors[8])
fifth_ax3.set_ylabel('Message Counter', color=colors[0])
fifth_ax4.set_ylabel('Messages per second', color=colors[4])
fifth_ax1.set_title('Radar Messurements Over Time')
fifth_ax1.tick_params(axis='y', colors=colors[3])
fifth_ax2.tick_params(axis='y', colors=colors[8])
fifth_ax3.tick_params(axis='y', colors=colors[0])
fifth_ax4.tick_params(axis='y', colors=colors[4])
plt.show()

#calculate the mean, the max and the min of the data
def print_statistics(data):
    print("Mean:", round(data.mean(),2))
    print("Max:", round(data.max(),2))
    print("Min:", round(data.min(),2))
    # print("Standard Deviation:", data.std())
    # print("Variance:", data.var())
    # print("Skewness:", data.skew())
    # print("Kurtosis:", data.kurtosis())
    # print("Median:", data.median())
    # print("Range:", data.max() - data.min())
    # print("Interquartile Range:", data.quantile(0.75) - data.quantile(0.25))
    
# print stat for the CPU Load
print("CPU Load Total:")
print_statistics(process_load_data['Total CPU Load'])
print("CPU Load Core:")
print_statistics(process_load_data['Core CPU'])
print("CPU Load Ameise:")
print_statistics(process_load_data['Ameise CPU'])
print("CPU Load Radar:")
print_statistics(process_load_data['Radar CPU'])
# print stat for the Memory Load
print("Memory Load Total:")
print_statistics(process_load_data['Total Used Memory'])
print("Memory Load Core:")
print_statistics(process_load_data['Core Memory'])
print("Memory Load Ameise:")
print_statistics(process_load_data['Ameise Memory'])
print("Memory Load Radar:")
print_statistics(process_load_data['Radar Memory'])
# print Message per second
print("Message per second Radar:")
print_statistics(message_per_seconds_data['Messages per second'])
# print Message others per second
print("Message per second Ameise:")
print_statistics(other_topics_data['Messages'])
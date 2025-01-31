import os
import pandas as pd
import matplotlib.pyplot as plt

csv_file = "src\\scripts\\ameise_bag_stats_sec.csv"
colors = ['red', 'blue', 'green', 'orange', 'purple', 'brown', 'pink', 'gray', 'olive', 'cyan']
data = pd.read_csv(csv_file)

fig,ax1 = plt.subplots(figsize=(12, 6))
# Width of each bar
bar_width = 0.2

# Position of bars on x-axis
r1 = data["Second"] - bar_width/2
r2 = [x - bar_width for x in r1]
r3 = [x + bar_width for x in r1]
r4 = [x + bar_width for x in r3]

# Creating bars
ax1.bar(r1, data["Kamera"], width=bar_width, label='Kamera Msg', color=colors[0])
ax1.bar(r2, data["Lidar"], width=bar_width, label='Lidar Msg', color=colors[1])
ax1.bar(r3, data["Odometry"], width=bar_width, label='Odometry Msg', color=colors[2])
ax1.bar(r4, data["Sonstige"], width=bar_width, label='Sonstige Msg', color=colors[3])

# Add legend
ax1.legend()
ax1.set_xticks(range(11))
# Add labels
plt.xlabel('Seconds')
plt.ylabel('Message Count')
plt.show()

fig,ax1 = plt.subplots(figsize=(12, 6))
# Width of each bar
bar_width = 0.2

# Position of bars on x-axis
r1 = data["Second"] - bar_width/2
r2 = [x - bar_width for x in r1]
r3 = [x + bar_width for x in r1]
r4 = [x + bar_width for x in r3]

# Creating bars
ax1.bar(r1, data["Kamera Data Size"], width=bar_width, label='Kamera Size', color=colors[0])
ax1.bar(r2, data["Lidar Data Size"], width=bar_width, label='Lidar Size', color=colors[1])
ax1.bar(r3, data["Odometry Data Size"], width=bar_width, label='Odometry Size', color=colors[2])
ax1.bar(r4, data["Sonstige Data Size"], width=bar_width, label='Sonstige Size', color=colors[3])

# Add legend
ax1.legend()
ax1.set_xticks(range(11))

# Add labels
plt.xlabel('Seconds')
plt.ylabel('Message Size')
plt.show()

csv_file_msec = "src\\scripts\\ameise_bag_stats_msec.csv"
data = pd.read_csv(csv_file_msec)

fig,ax1 = plt.subplots(figsize=(12, 6))
ax1.plot(data["Second"], data["Kamera"], label='Kamera Msg', color=colors[0])
ax1.plot(data["Second"], data["Lidar"], label='Lidar Msg', color=colors[1])
ax1.plot(data["Second"], data["Odometry"], label='Odometry Msg', color=colors[2])
ax1.plot(data["Second"], data["Sonstige"], label='Sonstige Msg', color=colors[3])

# limits
ax1.set_xlim(1000, 2000)
ax1.set_ylim(0, 150)
# Add legend
ax1.legend()
# Add labels
plt.xlabel('Milliseconds')
plt.ylabel('Message Count')
plt.show()

fig,ax1 = plt.subplots(figsize=(12, 6))
# ax1.plot(data["Second"], data["Kamera Data Size"], label='Kamera Size', color=colors[0])
# ax1.plot(data["Second"], data["Lidar Data Size"], label='Lidar Size', color=colors[1])
# ax1.plot(data["Second"], data["Odometry Data Size"], label='Odometry Size', color=colors[2])
# ax1.plot(data["Second"], data["Sonstige Data Size"], label='Sonstige Size', color=colors[3])
ax1.vlines(data["Second"], 0, data["Kamera"], colors=colors[0], alpha=0.3)
ax1.vlines(data["Second"], 0, data["Lidar"], colors=colors[1], alpha=0.3)
ax1.vlines(data["Second"], 0, data["Odometry"], colors=colors[2], alpha=0.3)
ax1.vlines(data["Second"], 0, data["Sonstige"], colors=colors[3], alpha=0.3)
ax1.plot(data["Second"], data["Kamera"], 'o', label='Kamera Msg', color=colors[0], markersize=3)
ax1.plot(data["Second"], data["Lidar"], 'o', label='Lidar Msg', color=colors[1], markersize=3)
ax1.plot(data["Second"], data["Odometry"], 'o', label='Odometry Msg', color=colors[2], markersize=3)
ax1.plot(data["Second"], data["Sonstige"], 'o', label='Sonstige Msg', color=colors[3], markersize=3)
# limits
ax1.set_xlim(1000, 2000)
ax1.set_ylim(0, 160)
# Add legend
ax1.legend()
# Add labels
plt.xlabel('Milliseconds')
plt.ylabel('Message Size')
plt.show()

max_msg_count_camera = data["Kamera"].max()
print(f"Max Kamera Msg Count: {max_msg_count_camera}")
max_msg_size_camera = data["Kamera Data Size"].max()
print(f"Max Kamera Msg Size: {max_msg_size_camera}")
max_msg_count_lidar = data["Lidar"].max()
print(f"Max Lidar Msg Count: {max_msg_count_lidar}")
max_msg_size_lidar = data["Lidar Data Size"].max()
print(f"Max Lidar Msg Size: {max_msg_size_lidar}")
max_msg_count_odometry = data["Odometry"].max()
print(f"Max Odometry Msg Count:{max_msg_count_odometry}")
max_msg_size_odometry = data["Odometry Data Size"].max()
print(f"Max Odometry Msg Size: {max_msg_size_odometry}")
max_msg_count_sonstige = data["Sonstige"].max()
print(f"Max Sonstige Msg Count: {max_msg_count_sonstige}")
max_msg_size_sonstige = data["Sonstige Data Size"].max()
print(f"Max Sonstige Msg Size: {max_msg_size_sonstige}")
# max overall msg count
max_msg_count = max(max_msg_count_camera, max_msg_count_lidar, max_msg_count_odometry, max_msg_count_sonstige)
print(f"Max Msg Count: {max_msg_count}")
# max overall msg size
max_msg_size = max(max_msg_size_camera, max_msg_size_lidar, max_msg_size_odometry, max_msg_size_sonstige)
print(f"Max Msg Size: {max_msg_size}")
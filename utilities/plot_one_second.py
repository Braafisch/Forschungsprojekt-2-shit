import os
import pandas as pd
import matplotlib.pyplot as plt
def ResizeDatum(data):
    pre_topic = None
    pre_datum = None
    pre_time = None
    for datum in data.itertuples():
        current_topic = datum.Topic
        current_size = datum.DataSize
        current_time = datum.Time
        if pre_topic is None:
            pass
        else:
            if pre_topic == current_topic and pre_time == current_time:
                data.loc[datum.Index, "DataSize"] = pre_datum + current_size
        pre_topic = current_topic
        pre_datum = data.loc[datum.Index, "DataSize"]
        pre_time = current_time

def ToMB(data):
    return round(data/(1024**2))

csv_file_input = "src\\scripts\\ameise_bag_into_csv.csv"
colors = ['red', 'blue', 'green', 'orange', 'purple', 'brown', 'pink', 'gray', 'olive', 'cyan']
data = pd.read_csv(csv_file_input)

# only plot 1 to 2 seconds
data = data[(data["Time"] >= 1000) & (data["Time"] <= 2000)]
data["Time"] = data["Time"] - 1000

# filter Topic to Odometry, Kanera, Lidar, Sonstige
odo_data = data[data["Topic"] == "Odometry"]
ResizeDatum(odo_data)
kamera_data = data[data["Topic"] == "Kamera"]
ResizeDatum(kamera_data)
lidar_data = data[data["Topic"] == "Lidar"]
ResizeDatum(lidar_data)
sonstige_data = data[data["Topic"] == "Sonstige"]
ResizeDatum(sonstige_data)
odo_data["DataSize"] = ToMB(odo_data["DataSize"])
kamera_data["DataSize"] = ToMB(kamera_data["DataSize"])
lidar_data["DataSize"] = ToMB(lidar_data["DataSize"])
sonstige_data["DataSize"] = ToMB(sonstige_data["DataSize"])

fig,ax1 = plt.subplots(figsize=(12, 6))
ax1.vlines(odo_data["Time"], 0, odo_data["DataSize"], label='Odometry Msg', color=colors[0])
ax1.vlines(kamera_data["Time"], 0, kamera_data["DataSize"], label='Kamera Msg', color=colors[1])
ax1.vlines(lidar_data["Time"], 0, lidar_data["DataSize"], label='Lidar Msg', color=colors[2])
ax1.vlines(sonstige_data["Time"], 0, sonstige_data["DataSize"], label='Sonstige Msg', color=colors[3])
ax1.plot(odo_data["Time"], odo_data["DataSize"], 'o', color=colors[0], markersize=3)
ax1.plot(kamera_data["Time"], kamera_data["DataSize"], 'o', color=colors[1], markersize=3)
ax1.plot(lidar_data["Time"], lidar_data["DataSize"], 'o', color=colors[2], markersize=3)
ax1.plot(sonstige_data["Time"], sonstige_data["DataSize"], 'o', color=colors[3], markersize=3)
# limits
ax1.set_xlim(0, 1000)
ax1.set_ylim(0, 8)
ax1.legend()

plt.xlabel('Milliseconds')
plt.ylabel('Message Size in MB')
plt.show()
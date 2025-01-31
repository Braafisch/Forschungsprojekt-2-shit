
import matplotlib.pyplot as plt
import numpy as np

# Sample data
categories = ['AMEISE', '1MB/10Hz', '1MB/100Hz', '4MB/1Hz']
# mean_values = [35.98,29.45,28.78,31.15]
# max_values = [43.2, 40.7, 39.3, 40.4]  # Example maximum percentages
# min_values = [18.7, 19.9, 20.0, 19.4]  # Example minimum percentages
mean_values = [42.89, 40.32, 41.29, 43.46]
max_values = [58.0, 59.0, 59.0, 59.5]  # Example maximum percentages
min_values = [1.2, 8.2, 9.3, 9.9]  # Example minimum percentages

x = np.arange(len(categories))
width = 0.35

fig, ax = plt.subplots(figsize=(10, 6))
rects1 = ax.bar(x - width/2, max_values, width, label='Maximum', color='skyblue')
rects2 = ax.bar(x + width/2, min_values, width, label='Minimum', color='lightcoral')
rects3 = ax.bar(x, mean_values, width, label='Mean', color='yellow', alpha=0.7)


# Customize the plot
ax.set_ylabel('Percentage (%)')
ax.set_title('Maximum and Minimum Values')
ax.set_xticks(x)
ax.set_xticklabels(categories)
ax.legend()

# Add value labels on top of each bar
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate(f'{height}%',
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),
                    textcoords="offset points",
                    ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)
autolabel(rects3)

plt.ylim(0, 100)  # Set y-axis limits from 0 to 100%
plt.show()

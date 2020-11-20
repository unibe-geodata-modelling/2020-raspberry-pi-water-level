import csv
import matplotlib
import statistics
import pandas as pd
from matplotlib import pyplot as plt

filename = "distance_ranger.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    dist_list = []
    time_list = []
    for row in reader:
      if row[0] == "":
        continue
      a_dist = float(row[0])
      a_time = row[1]
      dist_list.append(a_dist)
      time_list.append(a_time)

df = pd.DataFrame()
df['Time'] = time_list
df['Distance'] = dist_list
df['Moving Average Distance'] = df ['Distance'].rolling(window=5, min_periods=2, center=True).mean()
#window legt fest wie viele Werte zusammengefasst werden
#minperiods legt fest wie viele Werte mindestens vorhanden sein müssen nicht NA um im mov.average einen Wert und nicht NA anzuzeigen
#centre gleich True gibt an dass wir den wert plus 2 vorhin und 2 nachher für den moving average berücksichtigen wollen und nicht 4 vorher

print(df)

graph = df.plot.line(x='Time', y=['Moving Average Distance', 'Distance'])
graph.set_xlabel('Time')
graph.set_ylabel('Distance [cm]')
plt.show()





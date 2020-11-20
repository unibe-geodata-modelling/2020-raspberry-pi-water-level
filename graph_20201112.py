import csv
import matplotlib
import statistics
import pandas as pd
from matplotlib import pyplot as plt

filename_grove= "distance_ranger.csv"
with open(filename_grove) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    dist_list_grove = []
    time_list_grove = []
    for row in reader:
      if row[0] == "":
        continue
      a_dist = float(row[0])
      a_time = row[1]
      dist_list_grove.append(a_dist)
      time_list_grove.append(a_time)
      
filename_tf = "distance_tfmini.csv"
with open(filename_tf) as g:
    reader = csv.reader(g)
    header_row = next(reader)
    dist_list_tf = []
    time_list_tf = []
    for row in reader:
      if row[0] == "":
        continue
      b_dist = int(row[0])
      b_time = row[1]
      dist_list_tf.append(b_dist)
      time_list_tf.append(b_time)
    #print(dist_list)
    #print(time_list)

df = pd.DataFrame()
df['Time'] = time_list_grove
df['Distance Grove'] = dist_list_grove
df['Distance TF'] = dist_list_tf
df['Moving Average Distance Grove'] = df ['Distance Grove'].rolling(window=5, min_periods=2, center=True).mean()
df['Moving Average Distance TF'] = df ['Distance TF'].rolling(window=5, min_periods=2, center=True).mean()
#window legt fest wie viele Werte zusammengefasst werden
#minperiods legt fest wie viele Werte mindestens vorhanden sein müssen nicht NA um im mov.average einen Wert und nicht NA anzuzeigen
#centre gleich True gibt an dass wir den wert plus 2 vorhin und 2 nachher für den moving average berücksichtigen wollen und nicht 4 vorher

print(df)

graph = df.plot.line(x='Time', y=['Moving Average Distance', 'Distance'])
graph.set_xlabel('Time')
graph.set_ylabel('Distance [cm]')
plt.show()





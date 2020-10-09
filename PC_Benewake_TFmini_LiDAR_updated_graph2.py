import csv
from matplotlib import pyplot as plt

filename = "distance_tfmini.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    dist_list = []
    time_list = []
    for row in reader:
      if row[0] == "":
        continue
      a_dist = int(row[0])
      a_time = row[1]
      dist_list.append(a_dist)
      time_list.append(a_time)
    #print(dist_list)
    #print(time_list)

#Plot Data
    fig = plt.figure(dpi = 128, figsize = (10,6))
    plt.plot(time_list, dist_list, "o", c = 'red')
    #Format Plot
    plt.title("Plot TFmini", fontsize = 24)
    plt.xlabel('Time',fontsize = 16)
    plt.ylabel("Distance [cm]", fontsize = 16)
    plt.tick_params(axis = 'both', which = 'major' , labelsize = 5)
    plt.show()

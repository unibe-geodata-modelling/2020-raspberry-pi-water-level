import csv
from matplotlib import pyplot as plt

filename = "distance_tfmini.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    dist_list = []
    for row in reader:
      if row[0] == "":
        continue
      a_dist = int(row[0])
      dist_list.append(a_dist)
    #print(dist_list)

#Plot Data
    fig = plt.figure(dpi = 128, figsize = (10,6))
    plt.plot(dist_list, c = 'red') #Line 1
    #Format Plot
    plt.title("Plot TFmini", fontsize = 24)
    plt.xlabel('',fontsize = 16)
    plt.ylabel("Distance [cm]", fontsize = 16)
    plt.tick_params(axis = 'both', which = 'major' , labelsize = 16)
    plt.show()

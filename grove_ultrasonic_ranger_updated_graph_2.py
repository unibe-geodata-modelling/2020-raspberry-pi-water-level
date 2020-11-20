import csv
import matplotlib
import statistics
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
a = 0
b = 9

while (True):
	dist_list_10 = dist_list[a:b]
	mean_dist_10 = statistics.mean(dist_list_10)
	print (mean_dist_10)
	a = a+1
	b = b+1
      
a=0
b=9
mylist = [1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9]
mylist_10 = mylist[a:b]
mylist_10
mean10 = statistics.mean(mylist_10)
print(mean10)


#Plot Data
    #fig = plt.figure(dpi = 128, figsize = (10,6))
    #plt.plot(time_list, dist_list, "o", c = 'red')
    #Format Plot
    #plt.title("Plot Grove Ranger", fontsize = 24)
    #plt.xlabel('Time',fontsize = 16)
    #plt.ylabel("Distance [cm]", fontsize = 16)
    #plt.tick_params(axis = 'both', which = 'major' , labelsize = 5)
    #plt.show()


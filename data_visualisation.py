import os
import csv
import glob
import matplotlib
import pandas as pd
from matplotlib import pyplot as plt

#save work directory to variable and get list of all .csv files in work directory
workdir = os.getcwd()
print(workdir)
extension = "csv"
csvlist = glob.glob('*.{}'.format(extension))
print(csvlist)

#loop for each .csv file in list
for i in csvlist:
    #create pathname for .png image from .csv  path
    filename = i
    file_root = (os.path.splitext(filename)[0])
    print(file_root)
    imgpath = os.path.join(workdir,file_root + ".png")
    print (imgpath)
    
    #read data from csv to individual lists
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)
        dist_list_a = []
        dist_list_b = []
        time_list = []
        #specify list range for contextual number of observations
        obs_list = list(range(1,61))
        for row in reader:
            if row[0] == "":
                continue
            a_dist = float(row[0])
            b_dist = float(row[1])
            a_time = row[2]
            dist_list_a.append(a_dist)
            dist_list_b.append(b_dist)
            time_list.append(a_time)

    #shorten lists to desired number of observations (60)
    del dist_list_a[60:]
    del dist_list_b[60:]
    del time_list[60:]

    #create dataframe from lists for graph
    df = pd.DataFrame()
    df['Observation_Number'] = obs_list
    df['Time'] = time_list
    df['Distance_TFmini'] = dist_list_a
    df['Distance_Grove'] = dist_list_b
    
    #calculate moving average and add to dataframe
    df['Moving_Average_Distance_TFmini'] = df ['Distance_TFmini'].rolling(window=5, min_periods=2, center=True).mean()
    df['Moving_Average_Distance_Grove'] = df ['Distance_Grove'].rolling(window=5, min_periods=2, center=True).mean()

    #plot graph (alternative: plot 'Time' as opposed to 'Observation Number')
    graph = df.plot.line(x='Observation_Number', y=['Distance_TFmini', 'Moving_Average_Distance_TFmini', 'Distance_Grove', 'Moving_Average_Distance_Grove'])
    graph.set_xlabel('Observation Number')
    graph.set_ylabel('Distance [cm]')
    
    #save graph as .png file using path created earlier
    plt.savefig(imgpath,dpi = 400)

import matplotlib.pyplot as plt
import numpy as np # for sine function
import csv

t = [] # column 0
data1 = [] # column 1
data2 = [] # column 2

with open('sigA.csv') as f:
    # open the csv file
    reader = csv.reader(f)
    for row in reader:
        # read the rows 1 one by one
        t.append(float(row[0])) # leftmost column
        data1.append(float(row[1])) # second column
        #data2.append(float(row[2])) # third column

sample_rate = len(t)/t[-1]
print("Sample rate: " + str(sample_rate))

#plotting
plt.plot(t,data1)
plt.xlabel('Time (s)')
plt.ylabel('Signal')
plt.title('Frequency Signal vs Time')
plt.show()
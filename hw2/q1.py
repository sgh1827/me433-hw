import csv

#t = [] # column 0
data1 = [] # column 1
data2 = [] # column 2

with open('sigA.csv') as f:
    # open the csv file
    reader = csv.reader(f)
    for row in reader:
        # read the rows 1 one by one
        #t.append(float(row[0])) # leftmost column
        data1.append(float(row[0])) # second column
        data2.append(float(row[1])) # third column
        
for i in range(len(data1)):
    # print the data to verify it was read
    print(str(data1[i]) + ", " + str(data2[i]))
        
with open('sigB.csv') as f:
    # open the csv file
    reader = csv.reader(f)
    for row in reader:
        # read the rows 1 one by one
        #t.append(float(row[0])) # leftmost column
        data1.append(float(row[0])) # second column
        data2.append(float(row[1])) # third column
        
for i in range(len(data1)):
    # print the data to verify it was read
    print(str(data1[i]) + ", " + str(data2[i]))        

with open('sigC.csv') as f:
    # open the csv file
    reader = csv.reader(f)
    for row in reader:
        # read the rows 1 one by one
        #t.append(float(row[0])) # leftmost column
        data1.append(float(row[0])) # second column
        data2.append(float(row[1])) # third column  
        
for i in range(len(data1)):
    # print the data to verify it was read
    print(str(data1[i]) + ", " + str(data2[i]))        
        
with open('sigD.csv') as f:
    # open the csv file
    reader = csv.reader(f)
    for row in reader:
        # read the rows 1 one by one
        #t.append(float(row[0])) # leftmost column
        data1.append(float(row[0])) # second column
        data2.append(float(row[1])) # third column

for i in range(len(data1)):
    # print the data to verify it was read
    print(str(data1[i]) + ", " + str(data2[i]))

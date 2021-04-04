import matplotlib.pyplot as plt
import numpy as np
import csv

dt = 1.0/10000.0 # 10kHz
t = np.arange(0.0, 1.0, dt) # 10s
# a constant plus 100Hz and 1000Hz
#t = np.asarray(t)
s = 4.0 * np.sin(2 * np.pi * 100 * t) + 0.25 * np.sin(2 * np.pi * 1000 * t) + 25

Fs = 10000 # sample rate
Ts = 1.0/Fs; # sampling interval
ts = np.arange(0,t[-1],Ts) # time vector

t1 = [] # column 0
data1 = [] # column 1
t2 = [] # column 0
data2 = [] # column 1
t3 = [] # column 0
data3 = [] # column 1
t4 = [] # column 0
data4 = [] # column 1

with open('sigA.csv') as f:
    # open the csv file
    reader = csv.reader(f)
    for row in reader:
        # read the rows 1 one by one
        t1.append(float(row[0])) # leftmost column
        data1.append(float(row[1])) # second column
        #data2.append(float(row[2])) # third column

y1 = data1 # the data to make the fft from
n1 = len(y1) # length of the signal
k1 = np.arange(n1)
T1 = n1/Fs
frq1 = k1/T1 # two sides frequency range
frq1 = frq1[range(int(n1/2))] # one side frequency range
Y1 = np.fft.fft(y1)/n1 # fft computing and normalization
Y1 = Y1[range(int(n1/2))] 

fig, (ax1, ax2) = plt.subplots(2, 1)
ax1.plot(t1,y1,'b')
ax1.set_xlabel('Time')
ax1.set_ylabel('Amplitude')
ax2.loglog(frq1,abs(Y1),'b') # plotting the fft
ax2.set_xlabel('Freq (Hz)')
ax2.set_ylabel('|Y(freq)|')
plt.show()

with open('sigB.csv') as g:
    # open the csv file
    reader = csv.reader(g)
    for row in reader:
        # read the rows 1 one by one
        t2.append(float(row[0])) # leftmost column
        data2.append(float(row[1])) # second column
        #data2.append(float(row[2])) # third column
        
y2 = data2 # the data to make the fft from
n2 = len(y2) # length of the signal
k2 = np.arange(n2)
T2 = n2/Fs
frq2 = k2/T2 # two sides frequency range
frq2 = frq2[range(int(n2/2))] # one side frequency range
Y2 = np.fft.fft(y2)/n2 # fft computing and normalization
Y2 = Y2[range(int(n2/2))] 

fig, (ax1, ax2) = plt.subplots(2, 1)
ax1.plot(t2,y2,'b')
ax1.set_xlabel('Time')
ax1.set_ylabel('Amplitude')
ax2.loglog(frq2,abs(Y2),'b') # plotting the fft
ax2.set_xlabel('Freq (Hz)')
ax2.set_ylabel('|Y(freq)|')
plt.show()

with open('sigC.csv') as h:
    # open the csv file
    reader = csv.reader(h)
    for row in reader:
        # read the rows 1 one by one
        t3.append(float(row[0])) # leftmost column
        data3.append(float(row[1])) # second column
        #data2.append(float(row[2])) # third column

y3 = data3 # the data to make the fft from
n3 = len(y3) # length of the signal
k3 = np.arange(n3)
T3 = n3/Fs
frq3 = k3/T3 # two sides frequency range
frq3 = frq3[range(int(n3/2))] # one side frequency range
Y3 = np.fft.fft(y3)/n3 # fft computing and normalization
Y3 = Y3[range(int(n3/2))] 

fig, (ax1, ax2) = plt.subplots(2, 1)
ax1.plot(t3,y3,'b')
ax1.set_xlabel('Time')
ax1.set_ylabel('Amplitude')
ax2.loglog(frq3,abs(Y3),'b') # plotting the fft
ax2.set_xlabel('Freq (Hz)')
ax2.set_ylabel('|Y(freq)|')
plt.show()


with open('sigD.csv') as m:
    # open the csv file
    reader = csv.reader(m)
    for row in reader:
        # read the rows 1 one by one
        t4.append(float(row[0])) # leftmost column
        data4.append(float(row[1])) # second column
        #data2.append(float(row[2])) # third column

y4 = data4 # the data to make the fft from
n4 = len(y4) # length of the signal
k4 = np.arange(n4)
T4 = n4/Fs
frq4 = k4/T4 # two sides frequency range
frq4 = frq4[range(int(n4/2))] # one side frequency range
Y4 = np.fft.fft(y4)/n4 # fft computing and normalization
Y4 = Y4[range(int(n4/2))] 

fig, (ax1, ax2) = plt.subplots(2, 1)
ax1.plot(t4,y4,'b')
ax1.set_xlabel('Time')
ax1.set_ylabel('Amplitude')
ax2.loglog(frq4,abs(Y4),'b') # plotting the fft
ax2.set_xlabel('Freq (Hz)')
ax2.set_ylabel('|Y(freq)|')
plt.show()


        

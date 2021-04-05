import matplotlib.pyplot as plt
import numpy as np
import csv

A1=0.995
A2=0.999
A3=0.99
A4=0.996

B1=0.005
B2=0.001
B3=0.01
B4=0.004

#def filteration(old,new,start, x):
 #   sum=0
  #  for i in range(x):
   #     sum = sum + old[(start)+i]
        
    #new.append(sum/x)


    
def fft_plot(t, nt, s, ns,A,B):
    
    #dt = 1.0/10000.0 # 10kHz
    t = np.asarray(t)
    nt = np.asarray(nt)
    Fs = 10000 # sample rate
    Ts = 1.0/Fs; # sampling interval
    ts = np.arange(0,t[-1],Ts) # time vector
    y = s # the data to make the fft from
    n = len(y) # length of the signal
    k = np.arange(n)
    T = n/Fs
    frq = k/T # two sides frequency range
    frq = frq[range(int(n/2))] # one side frequency range
    Y = np.fft.fft(y)/n # fft computing and normalization
    Y = Y[range(int(n/2))]
    
    nts = np.arange(0,nt[-1],Ts) # time vector
    ny = ns # the data to make the fft from
    nn = len(ny) # length of the signal
    nk = np.arange(nn)
    nT = nn/Fs
    nfrq = nk/nT # two sides frequency range
    nfrq = nfrq[range(int(nn/2))] # one side frequency range
    nY = np.fft.fft(ny)/nn # fft computing and normalization
    nY = nY[range(int(nn/2))]

    fig, (ax1, ax2) = plt.subplots(2, 1)
    ax1.set_title('A = ' + str(A) + ', ' + 'B = ' + str(B))
    #ax1.plot(t,y,'b')
    #ax1.set_xlabel('Time')
    #ax1.set_ylabel('Amplitude')
    ax1.plot(t, s, 'black')
    ax1.plot(nt, ns, 'red') #filtered
    ax1.set_xlabel('Time [s]')
    ax1.set_ylabel('Signal')
    ax2.loglog(frq,abs(Y),'black') # plotting the fft
    ax2.loglog(nfrq,abs(nY),'red') # plotting the filtered fft
    ax2.set_xlabel('Freq (Hz)')
    ax2.set_ylabel('|Y(freq)|')
    #plt.show()

t1 = [] # column 0
data1 = [] # column 1
t2 = [] # column 0
data2 = [] # column 1
t3 = [] # column 0
data3 = [] # column 1
t4 = [] # column 0
data4 = [] # column 1
nt1 = []
nt2 = []
nt3 = []
nt4 = []
ndata1 = []
ndata2 = []
ndata3 = []
ndata4 = []


with open('sigA.csv') as f:
    # open the csv file
    reader = csv.reader(f)
    for row in reader:
        # read the rows 1 one by one
        t1.append(float(row[0])) # leftmost column
        data1.append(float(row[1])) # second column
        #data2.append(float(row[2])) # third column
#fft_plot(t1,data1)

dt1 = len(t1)/t1[-1]
new = data1[0]
for ii in range(1,len(data1)):
    new = A1*new + B1*data1[ii]
    ndata1.append(new)
print("Sample rate 1: " + str(dt1))
nt1 = t1[1:]
fft_plot(t1, nt1, data1, ndata1,A1,B1)
#fft(nt1, ndata1, dt1)



with open('sigB.csv') as g:
    # open the csv file
    reader = csv.reader(g)
    for row in reader:
        # read the rows 1 one by one
        t2.append(float(row[0])) # leftmost column
        data2.append(float(row[1])) # second column
        #data2.append(float(row[2])) # third column
#fft_plot(t2,data2) 
dt2 = len(t2)/t2[-1]
new2 = data2[0]
for ii in range(1, len(data2)):
    new2 = A2*new2 + B2*data2[ii]
    ndata2.append(new2)
print("Sample rate 1: " + str(dt2))
nt2 = t2[1:]
fft_plot(t2, nt2, data2, ndata2,A2,B2)      


with open('sigC.csv') as h:
    # open the csv file
    reader = csv.reader(h)
    for row in reader:
        # read the rows 1 one by one
        t3.append(float(row[0])) # leftmost column
        data3.append(float(row[1])) # second column
        #data2.append(float(row[2])) # third column
#fft_plot(t3,data3)
dt3 = len(t3)/t3[-1]
new = data3[0]
for ii in range(1, len(data3)):
    new = A3*new + B3*data3[ii]
    ndata3.append(new)
print("Sample rate 3: " + str(dt3))
nt3 = t3[1:]
fft_plot(t3, nt3, data3, ndata3,A3,B3)



with open('sigD.csv') as m:
    # open the csv file
    reader = csv.reader(m)
    for row in reader:
        # read the rows 1 one by one
        t4.append(float(row[0])) # leftmost column
        data4.append(float(row[1])) # second column
        #data2.append(float(row[2])) # third column
#fft_plot(t4,data4)

dt4 = len(t4)/t4[-1]
ndata4 = []
new = data4[0]
for ii in range(1, len(data4)):
    new = A4*new + B4*data4[ii]
    ndata4.append(new)
print("Sample rate 4: " + str(dt4))
nt4 = t4[1:]
fft_plot(t4, nt4, data4, ndata4,A4,B4)

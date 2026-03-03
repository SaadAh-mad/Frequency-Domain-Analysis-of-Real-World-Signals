import numpy as np, matplotlib.pyplot as plt, scipy
t_min = -1
t_max = 1
num_t = 1000
t = np.linspace(t_min,t_max,num_t)
f = 2
xt = np.cos(2*np.pi*f*t)

#Lets plot the signal
plt.plot(t,xt)
plt.xlabel("t")
plt.ylabel("Amplitude")
plt.title("Plot of cos(2* pi * f * t) ")

#Define sampling period/sampling frequency
Fs = 5 #double of frequency to avoid aliasing 
Ts = 1/Fs
#To create the pulse train for sampling, use linspace or arange 
pulse_train = np.arange(t_min,t_max,Ts)
#Plot the pulse train
plt.stem(pulse_train,np.ones(len(pulse_train)))

#Use Stem plot for showing the quantization
xt_sampled = np.cos(2*np.pi*f*pulse_train)
plt.stem(pulse_train, xt_sampled)
#Plot the original signal on top so we can see the samples  
plt.plot(t,xt,'r')

#Signal Recovery
x_rs , t_rs = scipy.signal.resample(xt_sampled, 1000, pulse_train) 
plt.plot(t_rs, x_rs)
plt.plot(t,xt,)


import numpy as np, matplotlib.pyplot as plt

#define x(t) as a pulse function
num_t = 100 
xt = np.zeros(num_t)
xt[:10] = 1
plt.plot(xt)
plt.title("Plot of x(t)")
plt.xlabel("sample index")
plt.ylabel("Value of x(t)")

fxt = np.fft.fft(xt)
#First plot is the real part
plt.subplot(1,2,1)
plt.plot(np.fft.fftshift(np.real(fxt)))
plt.title("Plot of real part of FT of x(t)")
plt.ylabel("Magnitude")
plt.xlabel("Frequency Index")

#Second plot is the imaginary part
plt.subplot(1,2,2)
plt.plot(np.fft.fftshift(np.imag(fxt)))
plt.title("Plot of imaginary part of FT of x(t)")
plt.ylabel("Magnitude")
plt.xlabel("Frequency Index")

#Plot in polar form
#First plot is the real part
plt.subplot(1,2,1)
plt.plot(np.fft.fftshift(np.abs(fxt)))
plt.title("Magnitude of FT of x(t)")
plt.ylabel("Magnitude")
plt.xlabel("Frequency Index")

#Second plot is the imaginary part
plt.subplot(1,2,2)
plt.plot(np.fft.fftshift(np.angle(fxt)))
plt.title("Angle of the FT of x(t)")
plt.ylabel("Magnitude")
plt.xlabel("Frequency Index")


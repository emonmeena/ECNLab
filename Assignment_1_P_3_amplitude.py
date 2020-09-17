
# Masthead - 
# Owner - Mayank Meena 
# Enroll no. 19114055, O-3
# Code Editor - VSCode 2020
# Terminal - WSL Ubuntu 2020

# Contact -
# Website - https://mayankmeena.netlify.app/
# Email - mayank_m@cs.iitr.ac.in

# Social -
# GitHub - https://github.com/maayami
# YouTube - https://www.youtube.com/channel/UCwcdyxP6uk5zso-L4lY4Y8g?view_as=subscriber
# Twitter - https://twitter.com/Meina_Mk

#importing required libraries
import numpy as np
import matplotlib.pyplot as plt
# defining required pointspace
x = np.linspace(0, 2*np.pi, 100)
fig, axx = plt.subplots(nrows=1, ncols=4, squeeze=False, figsize = (20, 5))
axx[0, 0].plot(x, np.sqrt(13)*np.exp(0.5*x))
axx[0, 0].set_title('Amplitude for part 1')
axx[0, 1].plot(x, 2*x + np.arctan(1.5))
axx[0, 1].set_title('Phase for part 1')

for axs in axx.flat[:2]:
    axs.set(xlabel='t')
# showing plot
plt.show()
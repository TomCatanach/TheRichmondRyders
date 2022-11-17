import numpy as np
import matplotlib.pyplot as plt

def animate(i):
    ln1.set_data(x, np.absolute(psi_m1[100*i])**2)
    time_text.set_text('Animation'.format(100*i*dt*1e4))
   
fig, ax = plt.subplots(1,1, figsize=(7,5))


#ax.grid()
ln1, = plt.plot([], [], 'r-', lw=2, markersize=8, label='wavefunc')
time_text = ax.text(0.70, 15, '', fontsize=15,
           bbox=dict(facecolor='white', edgecolor='black'))
ax.set_ylim(-5,25)
ax.set_xlim(0.2)
ax.set_ylabel('$|\psi(x)|^2$', fontsize=30)
ax.set_xlabel('$x/L$', fontsize=30)
ax.legend(loc='upper left')
ax.set_title('Animation')
ani = animation.FuncAnimation(fig, animate, frames=1000, interval= 50)
ani.save('using ffmpeg', fps=50,dpi=100)
plt.show()
# Random Plots 

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)

List_1 = np.random.randint(0, 101, size = 40)
List_2 = np.random.randint(0, 101, size = 40)
List_3 = np.random.randint(0, 101, size = 40)

fig = plt.figure()
axis = fig.subplots(2, 1) #2 is the rows and 1 is the columns 

axis[0].plot(range(len(List_1)), List_1, color = 'orange', linewidth = 10)
axis[0].plot(range(len(List_2)), List_2, color = 'red', linestyle = '--')
axis[0].set_title('Top Subplot')
axis[0].set_xlabel('Position')

axis[1].plot(range(len(List_3)), List_3, color = 'magenta', marker = 'D')
axis[1].set_title('Bottom Subplot')
axis[1].set_xlabel('Position')

plt.tight_layout()
plt.savefig('Random_Plots_Plot')
plt.show()
# Monte Carlo Pi

import numpy as np
import matplotlib.pyplot as plt

def Pi_Estimation(N):
    
    Random_points = np.random.rand(N, 2)
    
    distances = np.linalg.norm(Random_points, axis=1)
    
    points_inside_circle = np.sum(distances <= 1)
    
    pi_estimate = 4 * points_inside_circle / N
    
    return pi_estimate

N_values = [int(1e3), int(1e4), int(1e5), int(1e6)]

for N in N_values:
    
    pi_estimate = Pi_Estimation(N)

    print(f"N = {N}: Estimated value of Pi = {pi_estimate}")

N = int(1e4)

points = np.random.rand(N, 2)

distances = np.linalg.norm(points, axis=1)

points_inside = points[distances <= 1]

points_outside = points[distances > 1]

plt.figure(figsize=(6, 6))
plt.plot(points_inside[:, 0], points_inside[:, 1], 'y.', label='Inside Quarter Circle')
plt.plot(points_outside[:, 0], points_outside[:, 1], 'b.', label='Outside Quarter Circle')
plt.gca().set_aspect('equal', adjustable='box')
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.title('Monte Carlo Estimation of Pi')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.text(0.1, 0.9, f'Estimated Pi: {Pi_Estimation(N)}', fontsize=12, weight = 'bold')
plt.legend()
plt.savefig('Monte_Carlo_Pi_Plot')
plt.show()
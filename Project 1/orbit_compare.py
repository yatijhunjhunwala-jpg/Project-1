import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def gravitational_motion(state, t):
    """
    Planet around a star (2-body, star fixed at origin).
    state = [x, y, vx, vy]
    """
    x, y, vx, vy = state

    # Distance from star (r)
    r = np.sqrt(x**2 + y**2)
    # commented out r2 calc since r is enough
    # r2 = x**2 + y**2 

    # Acceleration components
    # Using GM = 1 unit for simplicity here
    ax = -1.0 * x / (r**3)
    ay = -1.0 * y / (r**3)

    return [vx, vy, ax, ay]

# Initial conditions
state_circular = [1.0, 0.0, 0.0, 1.0]
# Circular orbit: velocity = 1 gives stable circle at r=1

state_elliptical = [1.0, 0.0, 0.0, 0.7]
# Elliptical: lower velocity (0.7) makes it fall inward

# Time grid
t = np.linspace(0, 20, 1000)
# integrating for 20 time units 

# Run the integrator
solution_circ = odeint(gravitational_motion, state_circular, t)
solution_ellip = odeint(gravitational_motion, state_elliptical, t)

plt.figure(figsize=(10, 5)) #Plot

# Plot 1: Circular orbit
plt.subplot(1, 2, 1)
plt.plot(solution_circ[:, 0], solution_circ[:, 1], color="lightskyblue", linewidth=2, label="Orbit")
plt.plot(0, 0, marker="*", color="#F2C94C", markersize=14, label="Star") 
plt.title("Circular Orbit")
plt.xlabel("X (AU)")
plt.ylabel("Y (AU)")
plt.axis("equal") # keep aspect ratio square
plt.grid(True, alpha=0.25)
plt.legend()

# Plot 2: Elliptical orbit
plt.subplot(1, 2, 2)
plt.plot(solution_ellip[:, 0], solution_ellip[:, 1], color="mediumorchid", linewidth=2, label="Orbit")
plt.plot(0, 0, marker="*", color="#F2C94C", markersize=14, label="Star") 
plt.title("Elliptical Orbit")
plt.xlabel("X (AU)")
plt.axis("equal")
plt.grid(True, alpha=0.25)
plt.legend()

plt.tight_layout()
plt.savefig("orbit_comparison.png", dpi=160)
print("Saved orbit_comparison.png")
plt.show()
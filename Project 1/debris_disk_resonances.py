import numpy as np
import matplotlib.pyplot as plt

N_PARTICLES = 2000
PLANET_POS = 2.0 # Planet at 2 AU

# Disk parameters
DISK_INNER = 1.0
DISK_OUTER = 3.0

print(f"Generating debris disk with {N_PARTICLES} particles...")

# 1) Generate Random ring of particles
r = np.random.uniform(DISK_INNER, DISK_OUTER, N_PARTICLES)
theta = np.random.uniform(0, 2*np.pi, N_PARTICLES)
# Uniform distribution in radius and angle

# Convert polar to cartesian
x = r * np.cos(theta)
y = r * np.sin(theta)

# 2) Calculate Resonance locations 
resonances = {
    "2:1": PLANET_POS * (1/2)**(2/3),
    "3:2": PLANET_POS * (2/3)**(2/3),
    "4:3": PLANET_POS * (3/4)**(2/3),
}
# Using Kepler's 3rd Law scaling: r_res = r_planet * (T_planet / T_particle)^(2/3)

print("Calculated Resonance Locations:")
for name, radius in resonances.items():
    print(f"  {name} Resonance at {radius:.2f} AU")

# Distance array for histogram
r_particles = np.sqrt(x**2 + y**2)

# 3) Plotting results
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

# Left plot: Top-down view of the system
ax1.scatter(x, y, s=4, c="#8e8e8e", alpha=0.45, label="Debris Dust")
ax1.plot(0, 0, marker="*", color="#F2C94C", markersize=16, label="Star")
ax1.plot(PLANET_POS, 0, "o", color="lightskyblue", markersize=10, label="Perturber Planet")
# Alpha makes overlapping points clearer

# Add resonance circles to visualize where gaps should be
for name, radius in resonances.items():
    circle = plt.Circle((0, 0), radius, fill=False, color="mediumorchid", linestyle="--", alpha=0.55)
    ax1.add_artist(circle)

ax1.set_title("Debris Disk System Top-Down")
ax1.set_xlabel("X (AU)")
ax1.set_ylabel("Y (AU)")
ax1.axis("equal") # Crucial for circular look
ax1.grid(alpha=0.2)
ax1.legend(loc="upper right")

# Right plot: Radial distribution (Histogram)
ax2.hist(r_particles, bins=50, color="#9a9a9a", alpha=0.8, edgecolor="white")
# This shows the density of particles at different radii

# Vertical lines for resonances
ax2.axvline(resonances["2:1"], color="mediumorchid", linestyle="--", linewidth=2, label="2:1 Resonance")
ax2.axvline(resonances["3:2"], color="lightskyblue", linestyle="--", linewidth=2, label="3:2 Resonance")
ax2.axvline(resonances["4:3"], color="#6FCF97", linestyle="--", linewidth=2, label="4:3 Resonance")

ax2.set_title("Radial Distribution of Dust")
ax2.set_xlabel("Distance from Star (AU)")
ax2.set_ylabel("Number of Particles")
ax2.grid(alpha=0.25)
ax2.legend()

plt.tight_layout()
plt.savefig("debris_disk_structure.png", dpi=160)
print("Saved debris_disk_structure.png")
plt.show()
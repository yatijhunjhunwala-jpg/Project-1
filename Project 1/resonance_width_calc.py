import numpy as np
import matplotlib.pyplot as plt
import math # might need this for sqrt? 

#modelling the physics 
# Width of resonance depends on Planet Mass (mu)
# Formula: Width ~ (Mass_Ratio)^0.5 
def resonance_width(mass_ratio, a_planet=2.0):
    scaling_factor = 1.5 # tested 1.5 vs 2.0 coefficient
    
    # simplified scaling law for 2:1 resonance gap width
    # Using 2.0 as approximate pre-factor based on literature
    w = 2.0 * a_planet * np.sqrt(mass_ratio)
    return w

# Generating the data 
# We want to see how the gap size changes as the planet gets bigger
# Going from Earth-mass (approx 1e-6) up to Jupiter-mass (1e-3)
mass_ratios = np.linspace(0.000001, 0.001, 100)
widths = resonance_width(mass_ratios)

# Plotting
plt.figure(figsize=(9, 6))

# Plot the theoretical scaling law
plt.plot(mass_ratios, widths, color='cornflowerblue', linewidth=2, label='Theory Curve')

plt.title("Theoretical Width of Resonance Gaps")
plt.xlabel("Planet Mass Ratio (M_planet / M_star)")
plt.ylabel("Gap Width (AU)")
plt.grid(True, alpha=0.4)

# Add specific points for Earth and Jupiter to give a sense of scale
earth_ratio = 3.003e-6
plt.plot(earth_ratio, resonance_width(earth_ratio), 'o', color='mediumorchid', label='Earth')

jup_ratio = 0.954e-3
plt.plot(jup_ratio, resonance_width(jup_ratio), 'o', color='teal', label='Jupiter')

plt.legend()
plt.tight_layout()

plt.savefig("resonance_theory.png")
print("Theory plot saved.")
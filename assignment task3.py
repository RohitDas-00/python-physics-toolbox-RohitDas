# =============================================================================
# SIMPLE PARTICLE ENERGY CALCULATOR
# =============================================================================

# Constant
EV_TO_J = 1.6e-19   # 1 eV = 1.6 × 10^-19 J

class Particle:
    def __init__(self, name, mass_kg, velocity_m_s, charge_c=0):
        self.name = name
        self.mass_kg = float(mass_kg)
        self.velocity_m_s = float(velocity_m_s)
        self.charge_c = float(charge_c)

    # Kinetic Energy (Joules)
    def kinetic_energy(self):
        return 0.5 * self.mass_kg * self.velocity_m_s**2

    # Kinetic Energy (eV)
    def kinetic_energy_ev(self):
        return self.kinetic_energy() / EV_TO_J

    # Potential Energy (Joules)
    def potential_energy(self, V):
        return self.charge_c * V

    # Potential Energy (eV)
    def potential_energy_ev(self, V):
        return self.potential_energy(V) / EV_TO_J


# Realistic particle data
electron = Particle("Electron", 9.11e-31, 2e6, -1.6e-19)
proton   = Particle("Proton", 1.67e-27, 1e5,  1.6e-19)
alpha    = Particle("Alpha", 6.64e-27, 5e4,  3.2e-19)

particles = [electron, proton, alpha]

# Applied potential (for bonus)
V_applied = 1000  # Volts

# Output
print(f"{'Particle':<12}{'KE (eV)':>15}{'PE (eV)':>15}")
print("-" * 42)

for p in particles:
    print(f"{p.name:<12}{p.kinetic_energy_ev():>15.2e}{p.potential_energy_ev(V_applied):>15.2e}")
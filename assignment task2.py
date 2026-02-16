# =============================================================================
# #MATERIAL PROPERTIES LOOKUP
# =============================================================================
import matplotlib.pyplot as plt
#creating dictionary which will include material density,conductivity and young modulus
materials = {
    "Aluminum": {"density_g_cm3": "2.7", "conductivity": 3.5e7, "youngs_modulus_GPa": 70},
    "Copper": {"density_g_cm3": "8.96", "conductivity": 5.96e7, "youngs_modulus_GPa": 110},
    "Silicon": {"density_g_cm3": "2.33", "conductivity": 1e-3, "youngs_modulus_GPa": 130},
    "Graphene": {"density_g_cm3": "2.2", "conductivity": 1e8, "youngs_modulus_GPa": 1000}
}

# taking input with error handling
try:
    name = input("Enter new material name: ").strip()
    density = input("Enter its density (g/cm^3): ").strip()
    conductivity = float(input("Enter its conductivity: "))
    youngs = float(input("Enter its Young's modulus (GPa): "))

except ValueError:
    print("\nError: Conductivity and Young's modulus must be numbers.")

# Add material
materials[name] = {                 #adding new key-value pair
        "density_g_cm3": density,
        "conductivity": conductivity,
        "youngs_modulus_GPa": youngs}

# -------- Finding Highest Conductivity --------
max_material = max(materials, key=lambda x: materials[x]["conductivity"])
max_cond = materials[max_material]["conductivity"]

# -------- Get Density List as Floats (list comprehension + cleaning) --------
density_list = [float(materials[m]["density_g_cm3"].strip()) for m in materials]

# -------- Clean Output of Dictionary -----------------------------------------
print("\nUpdated Materials Dictionary:")
for mat, props in materials.items():
    print(f"\n{mat}")
    print(f"  Density (g/cm^3): {props['density_g_cm3']}")
    print(f"  Conductivity: {props['conductivity']}")
    print(f"  Young's Modulus (GPa): {props['youngs_modulus_GPa']}")

# -------- Display Results --------
print("\nMaterial with Highest Conductivity:", max_material, "=", max_cond)
print("List of Densities (float):", density_list)

# -------- Short Comment ------------------------------------------------------
print("-"*40)
print("Dictionaries helps as:")
print("Dictionaries organize experimental data by linking each material")
print("to its physical properties, enabling efficient storage, lookup,")
print("comparison, and structured data management.")

# ---- Conductivity Plot by matplot -------------------------------------------
plt.figure()
plt.bar(materials.keys(),
        [materials[m]["conductivity"] for m in materials])
plt.title("Material Conductivity Comparison")
plt.xlabel("Material")
plt.ylabel("Conductivity")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ---- Density Plot -----------------------------------------------------------
plt.figure()
plt.bar(materials.keys(), density_list)
plt.title("Material Density Comparison")
plt.xlabel("Material")
plt.ylabel("Density (g/cm^3)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
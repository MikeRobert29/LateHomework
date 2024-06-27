richter_str = input("Enter the Richter scale measurement (1.0 - 10.0): ")

richter = float(richter_str)

energy_joules = 10 ** (1.5 * richter)

tons_of_TNT = energy_joules / (4.184 * 10 ** 9)

nutritious_lunches = energy_joules / 2930200

print(f"Energy released in Joules: {energy_joules:.2e} J")

print(f"Equivalent in tons of exploded TNT: {tons_of_TNT:.2e} tons")

print(f"Number of nutritious lunches: {nutritious_lunches:.2e}")
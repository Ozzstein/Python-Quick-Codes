import pint
u = pint.UnitRegistry()

area = 1.37 * 10**6 * u.km**2
solar_insolation = 5.8 * u.kWh / u.metre**2 / u.day
energy_available = solar_insolation * area

energy_demand = 200 * u.TWh / u.year

distance = 3500 * u.km
efficiency = 0.2 * 0.9 * (1 - 0.1)**(distance / (1000 * u.km))

ratio = (energy_demand / energy_available * efficiency).to_base_units()
assert ratio.unitless
print(f"{ratio.magnitude:.6%} of the country's deserts")
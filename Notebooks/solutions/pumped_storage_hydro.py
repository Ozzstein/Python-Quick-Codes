import pint
u = pint.UnitRegistry()

u.define('swimming_pool = 50 * 25 * 3 * m**3')

mass_of_water_per_litre = 1.0 * u.kg / u.litre
mass = mass_of_water_per_litre * u.swimming_pool

stored_energy = mass * u.gravity * (1 * u.meter)
print(stored_energy.to(u.kWh))
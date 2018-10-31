"""
How many square metres of solar panels on your roof would you need to power your electric car?

Assumptions:
- you drive 30 km per day
- average electric car energy use: 20 kilowatt hours (kWh) / 100 km. (For reference: Tesla can do 15 kWh / 100km)
- average solar insolation: 4.24 kWh / square metre / day (Melbourne average)
- average number of sunshine hours (Melbourne): 2200 per year
- solar panel efficiency: 17%
"""
import pint
u = pint.UnitRegistry()

distance = 30 * u.km / u.day
energy_over_distance = 20 * u.kWh / (100 * u.km)
solar_insolation = 4.24 * u.kWh / u.metre**2 / u.day
panel_efficiency = 0.17

car_energy_per_day = energy_over_distance * distance
solar_energy_per_day = solar_insolation * panel_efficiency
solar_area = car_energy_per_day / solar_energy_per_day

print(round(solar_area.to_base_units(), 1))

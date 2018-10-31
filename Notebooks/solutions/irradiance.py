irradiance = {'Perth': 19 * u.MJ / u.metre**2 / u.day,
              'Brisbane': 4.8 * u.kWh / u.metre**2 / u.day,
              'Los Angeles': 1560 * u.Btu / u.foot**2 / u.day}

for (key, val) in irradiance.items():
    print('{:12s}: {}'.format(key, round(val.to('W / m**2'), 1)))
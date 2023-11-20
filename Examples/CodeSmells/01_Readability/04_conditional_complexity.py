import datetime

measured_voltage = 0.005
measured_current = 0.01
max_resistance = 10
min_temperature = 30
measured_temperature = 25
max_temperature = 50
temperature_override = False
t_start = 0
max_duration = 50

# Code smell
if measured_voltage / measured_current < max_resistance \
        and (min_temperature < measured_temperature < max_temperature
             or temperature_override) \
        and (datetime.now() - t_start).total_seconds() < 2.45:
    print('Result is valid')


# Better
def resistance_within_limits():
    measured_resistance = measured_voltage / measured_current
    return measured_resistance < max_resistance
def temperature_within_limits():
    within_limits = min_temperature < measured_temperature < max_temperature
    return within_limits or temperature_override
def duration_within_limits():
    measurement_duration = (datetime.now() - t_start).total_seconds()
    return measurement_duration < max_duration
if resistance_within_limits() and temperature_within_limits() and duration_within_limits():
    print('Result is valid')


if __name__ == '__main__':
    pass

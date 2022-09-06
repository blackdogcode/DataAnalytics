import matplotlib.pyplot as plt
import csv

move_avg_len = 5

global_years, global_temps = [], []
global_temps_csv = None
with open("global_temperature.csv", mode='r') as global_temperature_file:
    global_temps_csv = csv.reader(global_temperature_file)
    out = next(global_temps_csv, None)  # disregard headers
    for line in global_temps_csv:
        year, temp = map(float, line)
        global_years.append(year)
        global_temps.append(temp)

global_move_avg_temps = []
for year in range(move_avg_len, len(global_temps) + 1):
    avg_temp = sum(global_temps[year - move_avg_len:year]) / move_avg_len
    global_move_avg_temps.append(avg_temp)


local_years, local_temps = [], []
local_temps_csv = None
with open("seoul_temperature.csv", mode='r') as local_temperature_file:
    local_temps_csv = csv.reader(local_temperature_file)
    out = next(local_temps_csv, None)  # disregard headers
    for line in local_temps_csv:
        year, temp = map(float, line)
        local_years.append(year)
        local_temps.append(temp)

local_move_avg_temps = []
for year in range(move_avg_len, len(local_temps) + 1):
    avg_temp = sum(local_temps[year - move_avg_len:year]) / move_avg_len
    local_move_avg_temps.append(avg_temp)

start_year = max(global_years[0], local_years[0])
global_start_year_idx = global_years.index(start_year)
local_start_year_idx = local_years.index(start_year)
print(global_start_year_idx, local_start_year_idx)

plt.plot(global_years[move_avg_len - 1:], global_move_avg_temps, local_years[move_avg_len - 1:], local_move_avg_temps)
plt.show()

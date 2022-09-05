import matplotlib.pyplot as plt
import csv

move_avg_len = 13

years, temps = [], []
global_temperature = None
with open("global_temperature.csv", mode='r') as global_temperature_file:
    global_temperature = csv.reader(global_temperature_file)
    out = next(global_temperature, None)  # disregard headers
    for line in global_temperature:
        year, temp = map(float, line)
        years.append(year)
        temps.append(temp)
    init_pt, last_pt = 0, move_avg_len
    move_avg_temp = []
    for year in range(move_avg_len, len(temps) + 1):
        avg_temp = sum(temps[year - move_avg_len:year]) / move_avg_len
        move_avg_temp.append(avg_temp)

    plt.plot(move_avg_temp)
    plt.show()

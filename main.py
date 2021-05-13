import matplotlib.pyplot as plt
import csv

x = []
y = []

with open('Bad Drivers by State.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(str(row[0]))
        y.append(int(row[4]))

plt.plot(x,y)

plt.xlabel('States')
plt.ylabel('Number of Drivers involved in Fatal Accident')
plt.title('Number of Drivers involved in Fatal Accident by State')
plt.show()
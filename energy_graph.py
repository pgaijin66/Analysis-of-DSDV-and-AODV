import matplotlib.pyplot as plt; plt.rcdefaults()
import matplotlib.pyplot as plt
import numpy as np

data = open('energy_graph.txt','r')
initialEnergy = []
finalEnergy = []
energyConsumed = []
for item in data:
	demo = item.split(' ')
	initialEnergy.append(int(demo[0]))
	finalEnergy.append(int(demo[1]))
	energyConsumed.append(int(demo[2][0:-1]))

print(initialEnergy)
print(finalEnergy)
print(energyConsumed)

n_groups = 2
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.25
opacity = 0.8

rects1 = plt.bar(index, tuple(initialEnergy), bar_width, alpha=opacity, color='g',label='Initial Energy')
rects2 = plt.bar(index+bar_width, tuple(finalEnergy), bar_width, alpha=opacity,color='b',label='Final Energy')
rects3 = plt.bar(index+bar_width+bar_width, tuple(energyConsumed),bar_width, alpha=opacity,color='r',label='Energy Consumed')

plt.xlabel('Protocol')
plt.ylabel('Energy Amount')
plt.xticks(index+bar_width, ('DSDV','AODV'))
plt.legend()
plt.tight_layout()
plt.show()


data.close()

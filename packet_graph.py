import matplotlib.pyplot as plt; plt.rcdefaults()
import matplotlib.pyplot as plt
import numpy as np

data = open('packet_graph.txt','r')
send_count = []
received_count = []
dropped_count = []
for item in data:
	demo = item.split(' ')
	send_count.append(int(demo[0]))
	received_count.append(int(demo[1]))
	dropped_count.append(int(demo[2][0:-1]))

print(send_count)
print(received_count)
print(dropped_count)

n_groups = 2
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.25
opacity = 0.8

rects1 = plt.bar(index, tuple(send_count), bar_width, alpha=opacity, color='g',label='Packet Sent')
rects2 = plt.bar(index+bar_width, tuple(received_count), bar_width, alpha=opacity,color='b',label='Packet Received')
rects3 = plt.bar(index+bar_width+bar_width, tuple(dropped_count),bar_width, alpha=opacity,color='r',label='Packet Dropped')

plt.xlabel('Protocols')
plt.ylabel('Number of packet')
plt.xticks(index+bar_width, ('DSDV','AODV'))
plt.legend()
plt.tight_layout()
plt.show()


data.close()

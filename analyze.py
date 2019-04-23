from pprint import pprint as pp
import sys

file_name=sys.argv[1]
data_trace = open(file_name,'r')
graph_data = open('packet_graph.txt','a+')
energy_data = open('energy_graph.txt','a+')
send_count = 0
received_count = 0
list_trace = []
line_count = 0
dropped_count = 0

for line in data_trace:
	list_trace.append(line)
	line_count += 1
	
for i in range(line_count):
	if((list_trace[i].split(' '))[0] == 's'):
		send_count += 1
	elif((list_trace[i].split(' '))[0] == 'r'):
		received_count += 1
	elif((list_trace[i].split(' '))[0] == 'D'):
		dropped_count += 1
	else:
		pass
	 
pp('Number of packets sent: {}'.format(send_count))
pp('Number of packet received: {}'.format(received_count))
pp('Number of packet dropped: {}'.format(dropped_count))
pp('Simulation time: {} ms'.format((list_trace[-1].split(' '))[1]))
initialEnergy=float((list_trace[1].split(' '))[14])
FinalEnergy=float((list_trace[-1].split(' '))[14])
energyConsumed=initialEnergy - FinalEnergy

pp('Initial Energy: {} '.format(initialEnergy))
pp('Energy Consumed: {}'.format(energyConsumed))
pp('Final Energy: {}'.format(FinalEnergy))

graph_data.write('%d %d %d\n' % (send_count,received_count,dropped_count))
energy_data.write('%d %d %d\n' % (initialEnergy,FinalEnergy,energyConsumed))

data_trace.close()
graph_data.close()
energy_data.close()

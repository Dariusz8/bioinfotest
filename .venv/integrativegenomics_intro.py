#chap 4 - bioinformatics a practical approach with python
#Dariusz Czeczuk
#Start date: 1-5-2025
#Last mod: 1-5-2025
#TODO missing

import network as nx
import scipy.integrate
import numpy as np
import matplotlib.pyplot as plt

#define function that models the differential equations of the metabolic network
dydt = np.zeros_like(y)
    reactant,product,rate = reaction
    dydt[reactant] -= rate['k']*y[reactant]
    dydt[product] += rate['k']*y[reactant]
    return dydt

#initialize metabolic network
metabolic_net = nx.DiGraph()
metabollic_net.add_edge('glucose','ethanol',k=0.1)
metabollic_net.add_edge('glucose','pyruvate',k=0.05)
#additional reactions...

#initialize concentrations of metabolites
initial_concentrations = np.array([10,0,0])
#example initial conditions

#time points to simulate
time_points = np.linspace(0,100,num=1000)

#simulate metabolic network over time
solution = scipy.integrate.solve_ivp(t_eval=time_points)

#plot results

plt.plot(time_points,solution.y.T)
plt.xlabel('Time')
plt.ylabel('Concentration')
plt.legend(['Glucose','Ethanol','Pyruvate'])
plt.show()


# import networkx as nx
# import scipy.integrate
# import numpy as np
# import matplotlib.pyplot as plt
#
# # Define function that models the differential equations of the metabolic network
# def metabolic_model(t, y, network):
#     dydt = np.zeros_like(y)
#     for edge in network.edges(data=True):
#         reactant = edge[0]
#         product = edge[1]
#         rate = edge[2]['k']
#         dydt[network.nodes[reactant]['index']] -= rate * y[network.nodes[reactant]['index']]
#         dydt[network.nodes[product]['index']] += rate * y[network.nodes[reactant]['index']]
#     return dydt
#
# # Initialize metabolic network
# metabolic_net = nx.DiGraph()
#
# # Add metabolites as nodes and store indices
# metabolic_net.add_node('glucose', index=0)
# metabolic_net.add_node('ethanol', index=1)
# metabolic_net.add_node('pyruvate', index=2)
#
# # Add reactions as edges with rate constants
# metabolic_net.add_edge('glucose', 'ethanol', k=0.1)
# metabolic_net.add_edge('glucose', 'pyruvate', k=0.05)
#
# # Initialize concentrations of metabolites
# initial_concentrations = np.array([10, 0, 0])  # Example: [glucose, ethanol, pyruvate]
#
# # Time points to simulate
# time_points = np.linspace(0, 100, num=1000)
#
# # Simulate metabolic network over time
# solution = scipy.integrate.solve_ivp(
#     fun=lambda t, y: metabolic_model(t, y, metabolic_net),
#     t_span=(time_points[0], time_points[-1]),
#     y0=initial_concentrations,
#     t_eval=time_points
# )
#
# # Plot results
# plt.plot(time_points, solution.y.T)
# plt.xlabel('Time')
# plt.ylabel('Concentration')
# plt.legend(['Glucose', 'Ethanol', 'Pyruvate'])
# plt.title('Metabolic Network Simulation')
# plt.show()

import matplotlib.pyplot as plt 

cardiac_cycle = [62, 60, 62, 64, 68, 77, 80, 76, 71, 66, 61, 61, 62]

# The * 10 copies the list 10 times 
expected_cycles = cardiac_cycle[1:-2] * 10 

print(expected_cycles)

plt.plot(expected_cycles)
plt.show()
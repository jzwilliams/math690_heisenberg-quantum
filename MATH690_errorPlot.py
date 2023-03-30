import numpy as np
import matplotlib.pyplot as plt 

# Plot error
err = lambda nvals : [1 - 0.98**n for n in nvals]
n = [i for i in range(101)]
half = [0.5 for i in n]
plt.plot(n,err(n),'-r',n,half,'--k')
plt.xlabel("Number of CNOT gates")
plt.ylabel("Probability of error")
plt.legend(["Error probability","50% error chance"])
plt.title("P(at least one error), independent CNOT errors only")
plt.savefig("Error.pdf",bbox_inches="tight")
plt.show()
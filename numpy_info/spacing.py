import numpy as np
x = np.linspace(10, 20, 5)
print(x)


# set base of log space to 2
a = np.logspace(1, 10, num=10, base=2)
print(a)

a = np.arange(10)
s = slice(0, 10, 2)
print(a[s])

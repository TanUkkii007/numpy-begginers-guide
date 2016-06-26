import numpy as np

c = np.loadtxt('data.csv', delimiter=',', usecols=(6,), unpack=True)

estimates = np.zeros((len(c), 3))

for i in range(len(c)):
    a = c.copy()
    a[i] = np.nan
    estimates[i, ] = [np.nanmean(a), np.nanvar(a), np.nanstd(a)]
    print("estimates", estimates[i])

print("Estimates variance", estimates.var(axis=0))
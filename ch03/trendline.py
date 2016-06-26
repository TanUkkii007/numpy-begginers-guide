import numpy as np
import matplotlib.pyplot as plt

def fit_line(t,y):
    '''Fits t to a line y = at + b'''
    A = np.vstack([t, np.ones_like(t)]).T
    return np.linalg.lstsq(A, y)[0]

# Determine pivots
h,l,c = np.loadtxt('data.csv', delimiter=',', usecols=(4,5,6), unpack=True)

pivots = (h+l+c)/3

# Fit trend lines
t = np.arange(len(c))
sa, sb = fit_line(t, pivots - (h-l))
ra, rb = fit_line(t, pivots + (h-l))

support = sa*t + sb
resistance = ra*t + rb

condition = (c > support) & (c < resistance)
print("condition", condition)

between_bands = np.where(condition)
print("between_bands", between_bands)

print("support[between_bands]", support[between_bands])
print("c[between_bands]", c[between_bands])
print("resistance[between_bands]", resistance[between_bands])

n_between_bands = len(np.ravel(between_bands))
print("Number points between bands", between_bands)
print("Ratio between bands", float(n_between_bands)/len(c))

print("Tomorrows support", sa * (t[-1] + 1) + sb)
print("Tomorrows resistance", ra * (t[-1] + 1) + rb)

a1 = c[c > support]
a2 = c[c < resistance]
print("Number of points between bands 2nd approach" ,len(np.intersect1d(a1, a2)))

plt.plot(t, c, label='Data')
plt.plot(t, support, '--', lw=2.0, label='Support')
plt.plot(t, resistance, '-.', lw=3.0, label='Resistance')
plt.title('Trend Lines')
plt.xlabel('Days')
plt.ylabel('Price ($)')
plt.grid()
plt.legend()
plt.show()


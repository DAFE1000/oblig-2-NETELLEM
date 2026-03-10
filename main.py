import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import brentq

# definer funksjonen og den deriverte
def f(x):
    return np.exp(-x/4) * np.arctan(x)

def df(x):
    return return np.arctan(x) - 4 / (x**2 + 1)

# regner toppPunkt
x_max = brentq(df, 1, 3)
y_max = f(x_max)
print(f"Toppunkt: x* = {x_max:.4f}, f(x*) = {y_max:.4f}")

#Ploter den
x = np.linspace(-10, 12, 1000)
plt.plot(x, f(x))
plt.plot(x_max, y_max, 'ro', label=f'Toppunkt ({x_max:.4f}, {y_max:.4f})')
plt.legend()
plt.grid(True)
plt.title(r'$f(x) = (4-x)\arctan(x) + \frac{1}{2}\ln(x^2+1)$')
plt.show()

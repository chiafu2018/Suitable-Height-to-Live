import numpy as np 
import matplotlib.pyplot as plt
from scipy.optimize import leastsq

X_male = np.array([161.5, 164.5, 167.5, 170.5, 173.5, 176.5, 179.5, 182.5, 185.5, 188.5, 191.5, 194.5])
Y_male = [5.3, 10.7, 9.3, 8, 13.3, 24, 9.3, 12, 4, 0, 1.3, 2.7]

X_female = np.array([146.5, 149.5, 152.5, 155.5, 158.5, 161.5, 164.5, 167.5, 170.5, 173.5, 176.5, 179.5, 182.5])
Y_female = [1.1, 1.1, 2.8, 5.7, 17, 17.6, 17, 9.7, 9.1, 8, 4.5, 3.4, 2.8]

def func(params, x):
    a, b, c = params
    return a*x*x+b*x+c

def error(params, x, y):
    return func(params, x) - y

def solvePara(X, Y):
    p0 = [10, 10, 10] # Initial Value
    Para = leastsq(error, p0, args=(X,Y))
    return Para

def draw_curve(Para, X, Y):
    a, b, c = Para[0]
    print("y="+str(round(a,2))+"x*x"+str(round(b,2))+"x"+str(round(c,2)))
    print(f"Preferable Height:{round(-b/(2*a), 2)}cm")

    plt.figure(figsize=(8,6))
    plt.scatter(X, Y, color='green', label = 'sample data', linewidths=1)
    x = np.linspace(min(X), max(X), int(max(X)-min(X)))
    y = a*x*x+b*x+c
    plt.plot(x, y, color='red', label = 'preferable height curve', linewidth=2)
    plt.title("PLOT")
    plt.legend()
    plt.show()

Para = solvePara(X_male, Y_male)
print("Preferable Male Height Curve:")
draw_curve(Para, X_male, Y_male)

Para = solvePara(X_female, Y_female)
print("Preferable Female Height Curve:")
draw_curve(Para, X_female, Y_female)


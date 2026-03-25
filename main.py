import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

# -------------------------------
# CONSTANTS
# -------------------------------
gamma = 1.4
R = 287

T0 = 300        # K
P0 = 3e5        # Pa

# Sutherland constants
mu0 = 1.716e-5
T_ref = 273
S = 110.4

# -------------------------------
# GEOMETRY
# -------------------------------
x = np.linspace(0, 0.075, 200)
A = 1 + 2*(x - 0.0375)**2
A_star = np.min(A)

# -------------------------------
# AREA-MACH FUNCTION
# -------------------------------
def area_mach(M, A_ratio):
    return (1/M)*((2/(gamma+1)*(1+(gamma-1)/2*M**2))**((gamma+1)/(2*(gamma-1)))) - A_ratio

# -------------------------------
# MACH SOLUTION
# -------------------------------
M = np.zeros_like(x)

for i in range(len(x)):
    A_ratio = A[i]/A_star
    
    if x[i] < 0.0375:
        M[i] = fsolve(area_mach, 0.3, args=(A_ratio))[0]
    else:
        M[i] = fsolve(area_mach, 2.0, args=(A_ratio))[0]

# -------------------------------
# SHOCK
# -------------------------------
shock_index = int(0.6 * len(x))

M1 = M[shock_index]

M2 = np.sqrt((1 + ((gamma-1)/2)*M1**2) / (gamma*M1**2 - (gamma-1)/2))

for i in range(shock_index, len(x)):
    M[i] = M2 * (1 - 0.5*(i-shock_index)/(len(x)-shock_index))

# -------------------------------
# FLOW PROPERTIES
# -------------------------------
T = T0 / (1 + (gamma-1)/2 * M**2)
P = P0 * (T/T0)**(gamma/(gamma-1))
rho = P / (R * T)

a = np.sqrt(gamma * R * T)
V = M * a

# -------------------------------
# SUTHERLAND VISCOSITY
# -------------------------------
mu = mu0 * (T/T_ref)**1.5 * (T_ref + S)/(T + S)

# -------------------------------
# PLOTS
# -------------------------------
plt.figure(figsize=(15,10))

# Pressure
plt.subplot(2,2,1)
plt.plot(x*1000, P/1000)
plt.axvline(x[shock_index]*1000, linestyle='--')
plt.title("Pressure Distribution (kPa)")
plt.xlabel("Length (mm)")

# Velocity
plt.subplot(2,2,2)
plt.plot(x*1000, V)
plt.axvline(x[shock_index]*1000, linestyle='--')
plt.title("Velocity Distribution (m/s)")
plt.xlabel("Length (mm)")

# Temperature
plt.subplot(2,2,3)
plt.plot(x*1000, T)
plt.title("Temperature Distribution (K)")
plt.xlabel("Length (mm)")

# Viscosity
plt.subplot(2,2,4)
plt.plot(x*1000, mu)
plt.title("Viscosity (Sutherland Model)")
plt.xlabel("Length (mm)")

plt.tight_layout()
plt.show()
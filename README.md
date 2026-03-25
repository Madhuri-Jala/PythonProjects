# PythonProjects
Python Projects | DESIGN OPTIMIZATION | CFD AUTOMATION | POST-PROCESSING | CAD + SIMULATION INTEGRATION
# ✈️ Numerical Modeling of Compressible Flow with Shock Formation in a Converging-Diverging Nozzle

---

## 📌 Project Overview

This project presents a **high-fidelity quasi-1D compressible flow solver** for a converging-diverging (CD) nozzle using Python.

The model captures:
- Subsonic → Sonic → Supersonic transition
- Normal shock formation
- Thermodynamic and transport property variations

---

## 🎯 Objectives

- Solve compressible flow through a CD nozzle  
- Implement **Area–Mach relation using nonlinear solver**  
- Model **shock wave behavior**  
- Analyze pressure, velocity, temperature, and viscosity  

---

## 📐 Geometry

The nozzle geometry used in the simulation:

<img src="geometry.png" width="500"/>

---

## 📊 Results

### 🔹 Pressure, Velocity, Temperature & Viscosity Distribution

<img src="results/main_results.png" width="700"/>


---

## 🔍 Key Observations

- Flow accelerates to **Mach 1 at the throat**  
- Supersonic flow develops in the diverging section  
- A **normal shock** causes:
  - Sudden pressure increase  
  - Sudden velocity drop  
- Post-shock flow becomes subsonic  
- Pressure increases in the diverging section after shock  

---

## 🧠 Governing Physics

- Isentropic flow relations  
- Area–Mach relation  
- Normal shock equations  
- Sutherland viscosity model  

---

## ⚙️ Methodology

1. Defined nozzle geometry using area variation  
2. Solved Mach number using `fsolve`  
3. Applied subsonic and supersonic solutions  
4. Introduced shock in diverging section  
5. Computed flow properties  
6. Visualized results  

---

## 💻 Code Implementation

```python
# main.py (core logic)

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
# Solve Mach using fsolve
# Apply shock relations
# Compute flow properties

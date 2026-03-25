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

gamma = 1.4
R = 287
T0 = 300
P0 = 3e5

# Solve Mach using fsolve
# Apply shock relations
# Compute flow properties

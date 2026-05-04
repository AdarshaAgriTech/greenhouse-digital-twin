## Greenhouse Digital Twin & Control System

## Overview:
This project simulates an automated greenhouse system using Python.

It models real-world greenhouse operations including:
- Climate control (temperature, humidity, light)
- Nutrient management (EC and pH)
- Water tank management (level and pump control)
- Integrated system interactions

## Features
- Real-time environmental simulation
- Closed-loop control system
- Hysteresis-based pump control (30%–70% logic)
- Thermal screen automation
- Fan-pad cooling and fogger control
- Nutrient dosing (EC & pH regulation)
- System interaction (climate ↔ water ↔ nutrients)


##  System Architecture

The system consists of 4 modules:

- `environment.py` → Climate simulation & control  
- `nutrient.py` → EC & pH management  
- `tank.py` → Water level & pump control  
- `controller.py` → Central system controller  


## Control Logic

The system follows a closed-loop control approach:

- Temperature > 30°C → Cooling system activated  
- RH < 60% → Fogger activated  
- Lux > threshold → Thermal screen closes  
- EC < 1.5 → Nutrient dosing  
- pH out of range → Correction applied  
- Tank < 30% → Pump ON  
- Tank > 70% → Pump OFF  


##  Example Output:
Temp: 28.3 °C | RH: 64.8% | Lux: 52000
EC: 1.75 dS/m | pH: 6.10
Water Level: 65% | Pump: False

## Concepts Demonstrated:
-Digital Twin Modeling
-Control Systems Engineering
-Hysteresis Logic
-System Interaction Modeling
-IoT-based Automation Simulation

## Future Improvements
-IoT hardware integration (ESP32)
-Cloud data logging
-Web dashboard visualization
-AI-based predictive control


##  Author
Dr. Adarsha Gopalakrishna Bhat
Ph.D. Soil and Water Conservation Engineering
ICAR-IARI, New Delhi

## How to Run
Clone the repository and run:

```bash
python controller.py

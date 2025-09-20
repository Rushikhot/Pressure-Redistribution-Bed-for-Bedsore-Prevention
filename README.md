# Smart Bed for Pressure Ulcer Prevention

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Status: Development](https://img.shields.io/badge/Status-Development-orange.svg)]()

IoT-enabled smart bed system that prevents pressure ulcers through automated monitoring and intervention.

## Problem
- 57-60% of hospitalized patients develop pressure ulcers
- Manual repositioning every 2 hours is labor-intensive
- Current solutions are expensive or require constant monitoring

## Solution
Smart bed with automated pressure redistribution using:
- **Real-time monitoring**: 6 BME280 sensors track pressure, temperature, humidity
- **Micro-vibrations**: 25-50Hz vibrations improve blood circulation
- **Auto-repositioning**: Servo motors provide gentle lateral movements
- **No manual intervention**: Algorithm-driven responses to risk thresholds

## Hardware
- ESP32 microcontroller
- 6x BME280 sensors
- 6x Vibration motors (ERM)
- 2x SG90 servo motors
- 7.4V LiPo battery
- SD card for data logging

## Getting Started
1. Clone repository: 
   ```bash
   git clone https://github.com/Rushikhot/Pressure-Redistribution-Bed-for-Bedsore-Prevention.git
   ```
2. Install Arduino IDE and ESP32 support
3. Wire components per circuit diagram
4. Upload firmware to ESP32
5. Mount sensors on bed surface

## Project Structure
- **Code**: Main control program in `src/` folder
- **Components**: Complete parts list in `Docs/Components`
- **Circuit Design**: KiCAD files in `Hardware/circuit-design/`
- **3D Casing**: Fusion360 models in `Hardware/casing/`
- **Documentation**: Project docs in `Docs/` folder


## Team
**Group Avishkar** - IIT Guwahati
- Sharvani Pokala
- K S Ranjith  
- Sai Hari Hara Sudheshna Chunduru
- Rushikesh Balaji Khot

**Mentors**: Dr. Erwin Fuhrer, Dr. Subrata Pramanik, Dr. Kanagaraj

## License
MIT License - see [LICENSE](LICENSE) file

---
⚠️ **Disclaimer**: Research prototype for educational purposes. Clinical validation required before medical use.

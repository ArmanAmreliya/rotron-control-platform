
# rotron-control-platform

Rotron is a Python-based industrial control system for robotic arms, combining real-time simulation, motion control, and hardware execution. It provides a modular platform for developing, simulating, and controlling robotic systems with both a GUI and hardware interface.

## Features
- Real-time robot arm simulation using PyBullet
- Motion control and trajectory planning
- GUI for manual and automated control (PySide6)
- Hardware communication with ESP32 microcontroller
- Easily configurable robot parameters

## Project Structure

```
main.py                  # Main entry point
requirements.txt         # Python dependencies
test_pybullet.py         # PyBullet simulation test
config/
	robot_config.json      # Robot configuration
control/
	controller.py          # Motion control logic
gui/
	main_window.py         # GUI application
hardware/
	esp32.py               # ESP32 communication
simulation/
	simulator.py           # Simulation logic
utils/                   # Utility functions (if any)
```

## Requirements
- Python 3.8+
- pybullet
- numpy
- PySide6
- pyserial

Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

To run the main application:

```bash
python main.py
```

To test the PyBullet simulation:

```bash
python test_pybullet.py
```

## License
MIT

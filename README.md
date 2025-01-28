# Computer Vision Hand Counter on Raspberry Pi

This repository contains the code and resources for a **Computer Vision Hand Counter** that uses Mediapipe on a Raspberry Pi. The system communicates with an Arduino to control LEDs based on the number of fingers detected, offering an intuitive, gesture-based control mechanism.

## Features
- **Hand Tracking with Mediapipe**: Detects and counts fingers in real time.
- **Raspberry Pi Integration**: Runs the Mediapipe-based hand counter on a Raspberry Pi.
- **Arduino Communication**: Sends finger count data to an Arduino over serial communication.
- **LED Control**: Each finger count activates a corresponding LED connected to the Arduino.

## Components
1. **Raspberry Pi**: Runs the hand counter program.
2. **Arduino**: Controls the LEDs based on the Raspberry Pi's input.
3. **LEDs**: Represent finger count visually.
4. **Mediapipe Library**: Provides hand tracking and finger count functionality.

## Software Requirements
- Raspberry Pi OS (latest version recommended)
- Python 3.x
- Mediapipe library
- PySerial for serial communication

## Installation Instructions
1. **Set up the Raspberry Pi**:
   - Install required libraries:
     ```bash
     sudo apt-get update
     sudo apt-get install python3-pip
     pip3 install mediapipe pyserial
     ```

2. **Upload the Arduino Code**:
   - Write the Arduino sketch to control LEDs based on the received serial data.
   - Upload the code using the Arduino IDE.

3. **Run the Hand Counter Program on Raspberry Pi**:
   - Clone this repository:
     ```bash
     git clone <repository_url>
     cd Computer-Vision-Hand-Counter
     python3 hand_counter.py
     ```

## How It Works
1. The **Raspberry Pi** detects the number of raised fingers using Mediapipe.
2. The finger count is sent to the **Arduino** via serial communication.
3. The **Arduino** activates the corresponding number of LEDs based on the received count.

## Applications
- Gesture-based home automation.
- Educational projects for computer vision and embedded systems.
- Intuitive control interfaces for IoT devices.

Feel free to contribute, suggest improvements, or use this project as a learning tool for computer vision and embedded systems integration!

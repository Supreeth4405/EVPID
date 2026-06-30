# EVPID (Equilibrium Via PID)

EVPID is an Arduino-based ball-and-beam control system that uses a PID controller to balance a ball at a desired position. The project includes a custom Python telemetry dashboard for real-time visualization, PID tuning, and experiment logging.


## 📸 Model

![EVPID Model](EVPID_Images/Front_Left.jpg)


## 🚀 Features

* Closed-loop PID control
* Real-time telemetry dashboard
* Live P, I, D, and PID output graphs
* Adjustable Kp, Ki, Kd, and setpoint values without requiring firmware reuploads
* CSV logging for experiments
* Trial summary generation with controller parameters and statistics


## 🛠 Hardware Used

* Arduino Uno
* HC-SR04 Ultrasonic Sensor
* Servo Motor
* Ball-and-Beam Assembly


## 📚 Software & Libraries Used

### Arduino

* PlatformIO
* Custom PID Implementation **(Files Included)**

### Python

* PySerial: https://pyserial.readthedocs.io/
* DearPyGui: https://github.com/hoffstadt/DearPyGui


## 🏗️ Build Instructions

* Clone the repository and open `EVPID_Hardware` in PlatformIO.
* Upload `Main.cpp` to the Arduino.
* Install the required Python libraries.
* If the Arduino is connected to **COM5**, simply run the provided executable.
* For any other COM port, update the port in `Main.py` and run the application manually.


## 🔌 Circuit Diagram

The complete circuit diagram is available inside `EVPID_Images`.

Refer to the diagram before assembling the hardware.


## 📂 Code

All Arduino code is available inside `EVPID_Hardware`.

All Python telemetry code is available inside `EVPID_Telemetry`.

Refer to the circuit diagram, upload the firmware, run the telemetry application, and start experimenting with different PID parameters.


## 📖 Code Modules

### Hardware

* **PID.h / PID.cpp** – PID calculations
* **Sensor.h / Sensor.cpp** – Ultrasonic distance measurement
* **Main.cpp** – Main application code

### Telemetry

* **Main.py** – Main application
* **DAQ.py** – Serial data acquisition
* **Dashboard.py** – Functions for plotting graphs and creating windows
* **CSV_Logger.py** – CSV logging, trial summaries, and experiment management
* **Customisations.py** – GUI styling and visual elements


## ⚙️ Final PID Parameters

* Kp = 8
* Ki = 0.625
* Kd = 0.45
* Setpoint = 15 cm


## 🖥️ Telemetry Dashboard

The custom Python telemetry application provides:

### Live Monitoring

* Distance graph
* Error graph
* Servo angle graph
* Individual P, I, and D term graphs
* Combined PID output graph

### Controls

* Adjustable Kp, Ki, and Kd values
* Adjustable setpoint
* Enable/Disable PID control
* Enable/Disable servo control
* Start/Stop logging
* Serial connection management


## 📄 Logging

Each trial automatically generates a CSV file containing:

### Controller Parameters

* Kp
* Ki
* Kd
* Setpoint

### Trial Summary Statistics

* Trial duration
* Maximum servo angle
* Minimum servo angle
* Final error
* Maximum distance
* Minimum distance
* Average error
* Maximum deviation from the setpoint

### Raw Trial Data

* Time
* Distance
* Error
* Servo angle
* P term
* I term
* D term
* PID output


## 📊 Validation Trials

* **Trial 1** – Ball starts from the left extreme
* **Trial 2** – Ball starts from the right extreme
* **Trial 3** – Disturbance rejection test

Corresponding videos, telemetry screenshots, and log files are available inside `EVPID_Trials` and `EVPID_Log`.


## 📸 Demo

Photos, telemetry screenshots, videos, and circuit diagrams are available in their respective folders.


## 🔮 Future Improvements

* Design a custom PCB
* Improve the mechanical construction
* Implement wireless telemetry
* Experiment with advanced control algorithms


## 👤 Author

Developed by Supreeth (June 2026).
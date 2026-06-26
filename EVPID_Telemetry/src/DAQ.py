import serial

class DAQ:

    def __init__(self, port, baudrate):
        self.data = serial.Serial(port, baudrate)

        self.dist = 0
        self.error = 0
        self.angle = 0
        self.time = 0

        self.P = 0
        self.I = 0
        self.D = 0
        self.PID = 0

        self.Kp = 0
        self.Ki = 0
        self.Kd = 0
        self.SetPoint = 0

        self.dists = []
        self.errors = []
        self.angles = []
        self.times = []

        self.P_Values = []
        self.I_Values = []
        self.D_Values = []
        self.PID_Values = []

    def Clean_Lists(self):
        self.dists.clear()
        self.errors.clear()
        self.angles.clear()
        self.times.clear()

        self.P_Values.clear()
        self.I_Values.clear()
        self.D_Values.clear()
        self.PID_Values.clear()
    
    def get_values(self):
        values = self.data.readline().decode("UTF-8").strip().split(",")

        if len(values) != 12:
            return
    
        self.dist = float(values[0])
        self.error = float(values[1])
        self.angle = float(values[2])
        self.time = float(values[3])

        self.P = float(values[4])
        self.I = float(values[5])
        self.D = float(values[6])
        self.PID = float(values[7])

        self.Kp = float(values[8])
        self.Ki = float(values[9])
        self.Kd = float(values[10])
        self.SetPoint = float(values[11])

        self.dists.append(self.dist)
        self.errors.append(self.error)
        self.angles.append(self.angle)
        self.times.append(self.time)

        self.P_Values.append(self.P)
        self.I_Values.append(self.I)
        self.D_Values.append(self.D)
        self.PID_Values.append(self.PID)

        self.dists = self.dists[-100:]
        self.errors = self.errors[-100:]
        self.angles = self.angles[-100:]
        self.times = self.times[-100:]
        
        self.P_Values = self.P_Values[-100:]
        self.I_Values = self.I_Values[-100:]
        self.D_Values = self.D_Values[-100:]
        self.PID_Values = self.PID_Values[-100:]
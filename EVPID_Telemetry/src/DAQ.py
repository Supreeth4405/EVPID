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

        self.Is_Logging = False

        self.log_dists = []
        self.log_errors = []
        self.log_angles = []
        self.log_times = []

        self.log_P_Values = []
        self.log_I_Values = []
        self.log_D_Values = []
        self.log_PID_Values = []
    
    def get_values(self):
        values = self.data.readline().decode("UTF-8").strip().split(",")
    
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

        if self.Is_Logging == True:
            self.log_dists.append(self.dist)
            self.log_errors.append(self.error)
            self.log_angles.append(self.angle)
            self.log_times.append(self.time)

            self.log_P_Values.append(self.P)
            self.log_I_Values.append(self.I)
            self.log_D_Values.append(self.D)
            self.log_PID_Values.append(self.PID)

        self.dists = self.dists[-100:]
        self.errors = self.errors[-100:]
        self.angles = self.angles[-100:]
        self.times = self.times[-100:]
        
        self.P_Values = self.P_Values[-100:]
        self.I_Values = self.I_Values[-100:]
        self.D_Values = self.D_Values[-100:]
        self.PID_Values = self.PID_Values[-100:]

    def Start_Logging(self):
        self.Is_Logging = True

        self.log_dists.clear()
        self.log_errors.clear()
        self.log_angles.clear()
        self.log_times.clear()

        self.log_P_Values.clear()
        self.log_I_Values.clear()
        self.log_D_Values.clear()
        self.log_PID_Values.clear()

    def Stop_Logging(self):
        self.Is_Logging = False
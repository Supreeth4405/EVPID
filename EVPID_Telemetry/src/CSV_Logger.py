import csv
from  datetime import datetime

class Log_CSV:
    def __init__(self):
        self.Is_Logging = False

        self.log_dists = []
        self.log_errors = []
        self.log_angles = []
        self.log_times = []

        self.log_P_Values = []
        self.log_I_Values = []
        self.log_D_Values = []
        self.log_PID_Values = []

    def Start_Logging(self, data):
        self.Is_Logging = True
        self.Start_Time = data.time

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

    def Logging(self, data):
        if self.Is_Logging == True:

            Relative_Time = data.time - self.Start_Time

            self.log_dists.append(data.dist)
            self.log_errors.append(data.error)
            self.log_angles.append(data.angle)
            self.log_times.append(Relative_Time)

            self.log_P_Values.append(data.P)
            self.log_I_Values.append(data.I)
            self.log_D_Values.append(data.D)
            self.log_PID_Values.append(data.PID)

    def Calculate_Summary(self, data):
        self.Trial_Duration = self.log_times[-1]
        self.Max_Servo_Angle = max(self.log_angles)
        self.Min_Servo_Angle = min(self.log_angles)
        self.Final_Error = self.log_errors[-1]
        self.Max_Distance = max(self.log_dists)
        self.Min_Distance = min(self.log_dists)
        self.Average_Error = sum(abs(error) for error in self.log_errors)/len(self.log_errors)

        below = abs(data.SetPoint - self.Min_Distance)
        above = abs(self.Max_Distance - data.SetPoint)

        self.Max_Deviation = max(below, above)


    def Save_CSV(self, data):
        Current_Time = datetime.now()
        file_name = ("EVPID_Log/EVPID_" + Current_Time.strftime("%d-%m-%y_%H-%M-%S") + ".csv")
        self.Calculate_Summary(data)

        with open(file_name, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["kp", "ki", "kd", "SetPoint"])
            writer.writerow([data.Kp, data.Ki, data.Kd, data.SetPoint])
            writer.writerow([])
            writer.writerow(["Trial Duration", "Max Servo Angle", "Min Servo Angle", "Final Error", "Max Distance", "Min Distance", "Average Error", "Max Deviation"])
            writer.writerow([self.Trial_Duration, self.Max_Servo_Angle, self.Min_Servo_Angle, self.Final_Error, self.Max_Distance, self.Min_Distance, self.Average_Error, self.Max_Deviation])
            writer.writerow([])
            writer.writerow(["Time", "Distance", "Error", "Servo Angle", "P Term", "I Term", "D Term", "PID Output"])
            for i in range(len(self.log_times)):
                writer.writerow([self.log_times[i], self.log_dists[i], self.log_errors[i], self.log_angles[i], self.log_P_Values[i], self.log_I_Values[i], self.log_D_Values[i], self.log_PID_Values[i]])

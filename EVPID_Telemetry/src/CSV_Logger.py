from datetime import datetime
import csv

def Save_CSV(data):
    Current_Time = datetime.now()
    file_name = ("..\EVPID_Log\EVPID_" + Current_Time.strftime("%d-%m-%y_%H-%M-%S") + ".csv"
)

    with open(file_name, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["kp", "ki", "kd", "SetPoint"])
        writer.writerow([data.Kp, data.Ki, data.Kd, data.SetPoint])
        writer.writerow([])
        writer.writerow(["Time", "Distance", "Error", "Servo Angle", "P Term", "I Term", "D Term", "PID Output"])
        for i in range(len(data.log_times)):
            writer.writerow([data.log_times[i], data.log_dists[i], data.log_errors[i], data.log_angles[i], data.log_P_Values[i], data.log_I_Values[i], data.log_D_Values[i], data.log_PID_Values[i]])
import dearpygui.dearpygui as telemetry
from DAQ import DAQ
import Dashboard
import CSV_Logger

def Toggle_Logging(sender, app_data):
    if data.Is_Logging:
        data.Stop_Logging()
        CSV_Logger.Save_CSV(data)
        telemetry.set_item_label("LogButton", "Start Logging")
    else:
        data.Start_Logging()
        telemetry.set_item_label("LogButton", "Stop Logging")

data = DAQ("COM5", 9600)

telemetry.create_context()

with telemetry.window(label="EVPID_Telemetry", no_title_bar=True):

    with telemetry.group(horizontal=True):

        Dashboard.Plot_Graph(443, 248.6, "DISTANCE", data.times, data.dists, "DTime", "D", "Distance")
        Dashboard.Plot_Graph(443, 248.6, "PROPOTIONAL", data.times, data.P_Values, "PTime", "P", "Pro")
        Dashboard.Plot_Graph(443, 248.6, "PID", data.times, data.PID_Values, "PIDTime", "PID", "pid")
    
    with telemetry.group(horizontal=True):

        Dashboard.Plot_Graph(443, 248.6, "ERROR", data.times, data.errors, "ETime", "E", "Error")
        Dashboard.Plot_Graph(443, 248.6, "INTEGRAL", data.times, data.I_Values, "ITime", "I", "Int")
        
        with telemetry.child_window(width=443, height=248.6):

            with telemetry.group(horizontal=True):

                Dashboard.Create_Child_window(137, 114.3, "Distance", 10, "DistanceV", "0.00cm")
                Dashboard.Create_Child_window(137, 114.3, "Error", 10, "ErrorV", "0.00cm")
                Dashboard.Create_Child_window(137, 114.3, "Servo_Angle", 10, "AngleV", "65.0")

            with telemetry.group(horizontal=True):

                Dashboard.Create_Child_window(101.5, 114.3, "P_Term", 10, "PV", "0.00")
                Dashboard.Create_Child_window(101.5, 114.3, "I_Term", 10, "IV", "0.00")
                Dashboard.Create_Child_window(101.5, 114.3, "D_Term", 10, "DV", "0.00")
                Dashboard.Create_Child_window(101.5, 114.3, "PID_Term", 10, "PIDV", "0.00")
    
    with telemetry.group(horizontal=True):

        Dashboard.Plot_Graph(443, 248.6, "ANGLE", data.times, data.angles, "STime", "S", "Servo")
        Dashboard.Plot_Graph(443, 248.6, "DERIVATIVE", data.times, data.D_Values, "dtTime", "dt", "Der")

        with telemetry.child_window(width=443, height=248.6):

            with telemetry.group(horizontal=True):

                Dashboard.Create_Child_window(101.5, 114.3, "Kp", 10, "Kp", "8.00")
                Dashboard.Create_Child_window(101.5, 114.3, "Ki", 10, "Ki", "0.63")
                Dashboard.Create_Child_window(101.5, 114.3, "Kd", 10, "Kd", "0.45")
                Dashboard.Create_Child_window(101.5, 114.3, "SetPoint", 10, "SetPoint", "15.0")

            with telemetry.group(horizontal=True):
                telemetry.add_button(label="Start Logging", tag="LogButton", callback=Toggle_Logging)

telemetry.create_viewport(title="EVPID", width=1500, height=1320)
telemetry.setup_dearpygui()
telemetry.show_viewport()
telemetry.toggle_viewport_fullscreen()

while telemetry.is_dearpygui_running():

    data.get_values()

    Dashboard.Show_Limit_Graph("DTime", "D", "Distance", data.times, data.dists, 30, 0)
    Dashboard.Show_Limit_Graph("ETime", "E", "Error", data.times, data.errors, 15, -15)
    Dashboard.Show_Limit_Graph("STime", "S", "Servo", data.times, data.angles, 130, 0)

    Dashboard.Show_Graph("PTime", "P", "Pro", data.times, data.P_Values)
    Dashboard.Show_Graph("ITime", "I", "Int", data.times, data.I_Values)
    Dashboard.Show_Graph("dtTime", "dt", "Der", data.times, data.D_Values)
    Dashboard.Show_Graph("PIDTime", "PID", "pid", data.times, data.PID_Values)

    telemetry.set_value("DistanceV", str(data.dist) + "cm")
    telemetry.set_value("ErrorV", str(data.error) + "cm")
    telemetry.set_value("AngleV", str(data.angle))

    telemetry.set_value("PV", str(data.P))
    telemetry.set_value("IV", str(data.I))
    telemetry.set_value("DV", str(data.D))
    telemetry.set_value("PIDV", str(data.PID))

    telemetry.set_value("Kp", str(data.Kp))
    telemetry.set_value("Ki", str(data.Ki))
    telemetry.set_value("Kd", str(data.Kd))
    telemetry.set_value("SetPoint", str(data.SetPoint))

    telemetry.render_dearpygui_frame()

telemetry.destroy_context()

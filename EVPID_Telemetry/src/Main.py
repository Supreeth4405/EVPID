import dearpygui.dearpygui as telemetry
from DAQ import DAQ
import Dashboard
import CSV_Logger

Servo_Active = True
PID_Active = False

def Toggle_Logging(sender, app_data):
    if logger.Is_Logging:
        logger.Stop_Logging()
        logger.Save_CSV(data)
        telemetry.set_item_label("LogButton", "Start Logging")
        telemetry.set_value("_Log", "Not Logging")
    else:
        logger.Start_Logging(data)
        telemetry.set_item_label("LogButton", "Stop Logging")
        telemetry.set_value("_Log", "Logging")

def Apply_Kp():
    kp = telemetry.get_value("KpInput")
    data.data.write(("Kp:" + str(kp) + "\n").encode())

def Apply_Ki():
    ki = telemetry.get_value("KiInput")
    data.data.write(("Ki:" + str(ki) + "\n").encode())

def Apply_Kd():
    kd = telemetry.get_value("KdInput")
    data.data.write(("Kd:" + str(kd) + "\n").encode())

def Apply_SP():
    SP = telemetry.get_value("SPInput")
    data.data.write(("SP:" + str(SP) + "\n").encode())

def Toggle_PID():
    global PID_Active
    if PID_Active:
        data.data.write(("PID_OFF\n").encode())
        telemetry.set_value("_PID", "OFFLINE")
        PID_Active = False
    else:
        data.data.write(("PID_ON\n").encode())
        telemetry.set_value("_PID", "ACTIVE")
        PID_Active = True

def Toggle_Servo():
    global Servo_Active
    if Servo_Active:
        data.data.write(("SERVO_OFF\n").encode())
        telemetry.set_value("_Servo", "OFFLINE")
        Servo_Active = False
    else:
        data.data.write(("SERVO_ON\n").encode())
        telemetry.set_value("_Servo", "ACTIVE")
        Servo_Active = True

def Connect_COM():
    global data

    if data is None:
        try:
            data = DAQ("COM5", 9600)
            data.Clean_Lists()

            telemetry.set_value("_Connect", "Connected")
            telemetry.set_item_label("ConnectButton", "Disconnect")
        except:
            telemetry.set_value("_Connect", "Failed")
    else:
        data.data.close()
        data = None
        telemetry.set_value("_Connect", "Disconnected")
        telemetry.set_item_label("ConnectButton", "Connect")

data = None
logger = CSV_Logger.Log_CSV()

telemetry.create_context()

with telemetry.window(label="EVPID_Telemetry", no_title_bar=True):

    with telemetry.group(horizontal=True):

        Dashboard.Plot_Graph(443, 248.6, "DISTANCE", [], [], "DTime", "D", "Distance")
        Dashboard.Plot_Graph(443, 248.6, "PROPOTIONAL", [], [], "PTime", "P", "Pro")
        Dashboard.Plot_Graph(443, 248.6, "PID", [], [], "PIDTime", "PID", "pid")
    
    with telemetry.group(horizontal=True):

        Dashboard.Plot_Graph(443, 248.6, "ERROR", [], [], "ETime", "E", "Error")
        Dashboard.Plot_Graph(443, 248.6, "INTEGRAL", [], [], "ITime", "I", "Int")
        
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

        Dashboard.Plot_Graph(443, 248.6, "ANGLE", [], [], "STime", "S", "Servo")
        Dashboard.Plot_Graph(443, 248.6, "DERIVATIVE", [], [], "dtTime", "dt", "Der")

        with telemetry.child_window(width=443, height=248.6):

            with telemetry.group(horizontal=True):

                Dashboard.Create_Child_Window_Small(101.5, 44, "Kp", "Kp")
                Dashboard.Create_Child_Window_Small(101.5, 44, "Ki", "Ki")
                Dashboard.Create_Child_Window_Small(101.5, 44, "Kd", "Kd")
                Dashboard.Create_Child_Window_Small(101.5, 44, "SetPoint", "SetPoint")

            with telemetry.group(horizontal=True):
                telemetry.add_input_float(width=101.5, default_value=8.0, tag="KpInput")
                telemetry.add_input_float(width=101.5, default_value=0.625, tag="KiInput")
                telemetry.add_input_float(width=101.5, default_value=0.45, tag="KdInput")
                telemetry.add_input_float(width=101.5, default_value=15.0, tag="SPInput")

            with telemetry.group(horizontal=True):
                telemetry.add_button(width=101.5, height=44, label="Apply Kp", tag="KpButton", callback=Apply_Kp)
                telemetry.add_button(width=101.5, height=44, label="Apply Ki", tag="KiButton", callback=Apply_Ki)
                telemetry.add_button(width=101.5, height=44, label="Apply Kd", tag="KdButton", callback=Apply_Kd)
                telemetry.add_button(width=101.5, height=44, label="Apply SP", tag="SPButton", callback=Apply_SP)

            with telemetry.group(horizontal=True):
                Dashboard.Create_Child_Window_Small(101.5, 54.5, "Not Logging", "_Log")
                Dashboard.Create_Child_Window_Small(101.5, 54.5, "OFFLINE", "_PID")
                Dashboard.Create_Child_Window_Small(101.5, 54.5, "ACTIVE", "_Servo")
                Dashboard.Create_Child_Window_Small(101.5, 54.5, "Disconnected", "_Connect")

            with telemetry.group(horizontal=True):
                telemetry.add_button(width=101.5, height=54.5, label="Start Logging", tag="LogButton", callback=Toggle_Logging)
                telemetry.add_button(width=101.5, height=54.5, label="PID Control", tag="PIDButton", callback=Toggle_PID)
                telemetry.add_button(width=101.5, height=54.5, label="Servo Control", tag="ServoButton", callback=Toggle_Servo)
                telemetry.add_button(width=101.5, height=54.5, label="Connect", tag="ConnectButton", callback=Connect_COM)


telemetry.create_viewport(title="EVPID", width=1500, height=1300)
telemetry.setup_dearpygui()
telemetry.show_viewport()
telemetry.toggle_viewport_fullscreen()

while telemetry.is_dearpygui_running():
    if data is not None:
        try:
            data.get_values()
            logger.Logging(data)

            Dashboard.Show_Limit_Graph("DTime", "D", "Distance", data.times, data.dists, 30, 0)
            Dashboard.Show_Limit_Graph("ETime", "E", "Error", data.times, data.errors, 15, -15)
            Dashboard.Show_Limit_Graph("STime", "S", "Servo", data.times, data.angles, 140, 0)

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
        except:
            data.data.close()
            data = None
            telemetry.set_value("_Connect", "Disconnected")
            telemetry.set_item_label("ConnectButton", "Connect")

    telemetry.render_dearpygui_frame()

telemetry.destroy_context()
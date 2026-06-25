import serial
import dearpygui.dearpygui as telemetry

data = serial.Serial("COM5", 9600)


dists = []
errors = []
angles = []
times = []
P_Values = []
I_Values = []
D_Values = []
PID_Values = []


telemetry.create_context()

with telemetry.window(label="EVPID_Telemetry"):

    with telemetry.group(horizontal=True):

        with telemetry.plot(width=443, height=223):
            telemetry.add_plot_legend()
            telemetry.add_plot_axis(telemetry.mvXAxis, tag="DTime", no_tick_labels=True)
            telemetry.add_plot_axis(telemetry.mvYAxis, label="DISTANCE", tag="D")
            telemetry.add_line_series(times, dists, parent="D", tag="Distance")

        with telemetry.plot(width=443, height=223):
            telemetry.add_plot_legend()
            telemetry.add_plot_axis(telemetry.mvXAxis, tag="PTime", no_tick_labels=True)
            telemetry.add_plot_axis(telemetry.mvYAxis, label="PROPOTIONAL", tag="P")
            telemetry.add_line_series(times, P_Values, parent="P", tag="Pro")

        with telemetry.plot(width=443, height=223):
            telemetry.add_plot_legend()
            telemetry.add_plot_axis(telemetry.mvXAxis, tag="PIDTime", no_tick_labels=True)
            telemetry.add_plot_axis(telemetry.mvYAxis, label="PID", tag="PID")
            telemetry.add_line_series(times, PID_Values, parent="PID", tag="pid")
    
    with telemetry.group(horizontal=True):
        with telemetry.plot(width=443, height=223):
            telemetry.add_plot_legend()
            telemetry.add_plot_axis(telemetry.mvXAxis, tag="ETime", no_tick_labels=True)
            telemetry.add_plot_axis(telemetry.mvYAxis, label="ERROR", tag="E")
            telemetry.add_line_series(times, errors, parent="E", tag="Error")

        with telemetry.plot(width=443, height=223):
            telemetry.add_plot_legend()
            telemetry.add_plot_axis(telemetry.mvXAxis, tag="ITime", no_tick_labels=True)
            telemetry.add_plot_axis(telemetry.mvYAxis, label="INTEGRAL", tag="I")
            telemetry.add_line_series(times, I_Values, parent="I", tag="Int")

        with telemetry.child_window(width=443, height=223):

            with telemetry.group(horizontal=True):

                with telemetry.child_window(width=137, height=101.5):
                    telemetry.add_text("Distance")
                    telemetry.add_spacer(height=10)
                    telemetry.add_text("0.00 cm", tag="DistanceV")

                with telemetry.child_window(width=137, height=101.5):
                    telemetry.add_text("Error")
                    telemetry.add_spacer(height=10)
                    telemetry.add_text("0.00", tag="ErrorV")

                with telemetry.child_window(width=137, height=101.5):
                    telemetry.add_text("Servo_Angle")
                    telemetry.add_spacer(height=10)
                    telemetry.add_text("65.0", tag="AngleV")

            with telemetry.group(horizontal=True):

                with telemetry.child_window(width=101.5, height=101.5):
                    telemetry.add_text("P_Term")
                    telemetry.add_spacer(height=10)
                    telemetry.add_text("0.0", tag="PV")

                with telemetry.child_window(width=101.5, height=101.5):
                    telemetry.add_text("I_Term")
                    telemetry.add_spacer(height=10)
                    telemetry.add_text("0.0", tag="IV")

                with telemetry.child_window(width=101.5, height=101.5):
                    telemetry.add_text("D_Term")
                    telemetry.add_spacer(height=10)
                    telemetry.add_text("0.0", tag="DV")

                with telemetry.child_window(width=101.5, height=101.5):
                    telemetry.add_text("PID_Term")
                    telemetry.add_spacer(height=10)
                    telemetry.add_text("0.0", tag="PIDV")
        
    
    with telemetry.group(horizontal=True):

        with telemetry.plot(width=443, height=223):
            telemetry.add_plot_legend()
            telemetry.add_plot_axis(telemetry.mvXAxis, tag="STime", no_tick_labels=True)
            telemetry.add_plot_axis(telemetry.mvYAxis, label="ANGLE", tag="S")
            telemetry.add_line_series(times, angles, parent="S", tag="Servo")

        with telemetry.plot(width=443, height=223):
            telemetry.add_plot_legend()
            telemetry.add_plot_axis(telemetry.mvXAxis, tag="dtTime", no_tick_labels=True)
            telemetry.add_plot_axis(telemetry.mvYAxis, label="DERIVATIVE", tag="dt")
            telemetry.add_line_series(times, D_Values, parent="dt", tag="Der")

        with telemetry.child_window(width=443, height=223):

            with telemetry.group(horizontal=True):

                with telemetry.child_window(width=101.5, height=101.5):
                    telemetry.add_text("Kp")
                    telemetry.add_spacer(height=10)
                    telemetry.add_text("0.0", tag="Kp")

                with telemetry.child_window(width=101.5, height=101.5):
                    telemetry.add_text("Ki")
                    telemetry.add_spacer(height=10)
                    telemetry.add_text("0.0", tag="Ki")

                with telemetry.child_window(width=101.5, height=101.5):
                    telemetry.add_text("Kd")
                    telemetry.add_spacer(height=10)
                    telemetry.add_text("0.0", tag="Kd")

                with telemetry.child_window(width=101.5, height=101.5):
                    telemetry.add_text("SetPoint")
                    telemetry.add_spacer(height=10)
                    telemetry.add_text("0.0", tag="SetPoint")


telemetry.create_viewport(title="EVPID", width=1500, height=900)

telemetry.setup_dearpygui()
telemetry.show_viewport()


while telemetry.is_dearpygui_running():

    values = data.readline().decode("UTF-8").strip().split(",")

    dist = float(values[0])
    error = float(values[1])
    servo = float(values[2])
    time = float(values[3])
    P = float(values[4])
    I = float(values[5])
    D = float(values[6])
    PID = float(values[7])
    Kp = float(values[8])
    Ki = float(values[9])
    Kd = float(values[10])
    SetPoint = float(values[11])

    dists.append(dist)
    errors.append(error)
    angles.append(servo)
    times.append(time)
    P_Values.append(P)
    I_Values.append(I)
    D_Values.append(D)
    PID_Values.append(PID)
    

    dists = dists[-100:]
    errors = errors[-100:]
    angles = angles[-100:]
    times = times[-100:]
    P_Values = P_Values[-100:]
    I_Values = I_Values[-100:]
    D_Values = D_Values[-100:]
    PID_Values = PID_Values[-100:]

    telemetry.set_value("Distance", [times, dists])
    telemetry.fit_axis_data("DTime")
    telemetry.set_axis_limits("D", 0, 30)

    telemetry.set_value("Error", [times, errors])
    telemetry.fit_axis_data("ETime")
    telemetry.set_axis_limits("E", -15, 15)

    telemetry.set_value("Servo", [times, angles])
    telemetry.fit_axis_data("STime")
    telemetry.set_axis_limits("S", 0, 130)

    telemetry.set_value("Pro", [times, P_Values])
    telemetry.fit_axis_data("PTime")
    telemetry.fit_axis_data("P")

    telemetry.set_value("Der", [times, D_Values])
    telemetry.fit_axis_data("dtTime")
    telemetry.fit_axis_data("dt")

    telemetry.set_value("Int", [times, I_Values])
    telemetry.fit_axis_data("ITime")
    telemetry.fit_axis_data("I")

    telemetry.set_value("pid", [times, PID_Values])
    telemetry.fit_axis_data("PIDTime")
    telemetry.fit_axis_data("PID")

    telemetry.set_value("DistanceV", str(dist) + "cm")
    telemetry.set_value("ErrorV", str(error) + "cm")
    telemetry.set_value("AngleV", str(servo))
    telemetry.set_value("PV", str(P))
    telemetry.set_value("IV", str(I))
    telemetry.set_value("DV", str(D))
    telemetry.set_value("PIDV", str(PID))

    telemetry.set_value("Kp", str(Kp))
    telemetry.set_value("Ki", str(Ki))
    telemetry.set_value("Kd", str(Kd))
    telemetry.set_value("SetPoint", str(SetPoint))

    telemetry.render_dearpygui_frame()


telemetry.destroy_context()
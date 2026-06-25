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
            telemetry.add_plot_axis(telemetry.mvXAxis, tag="DTime")
            telemetry.add_plot_axis(telemetry.mvYAxis, label="Dist", tag="D")
            telemetry.add_line_series(times, dists, parent="D", tag="Distance")
        with telemetry.plot(width=443, height=223):
            telemetry.add_plot_legend()
            telemetry.add_plot_axis(telemetry.mvXAxis, tag="PTime")
            telemetry.add_plot_axis(telemetry.mvYAxis, label="P", tag="P")
            telemetry.add_line_series(times, dists, parent="P", tag="Pro")
        with telemetry.plot(width=443, height=223):
            telemetry.add_plot_legend()
            telemetry.add_plot_axis(telemetry.mvXAxis, tag="PIDTime")
            telemetry.add_plot_axis(telemetry.mvYAxis, label="PID", tag="PID")
            telemetry.add_line_series(times, dists, parent="PID", tag="pid")
    
    with telemetry.group(horizontal=True):
        with telemetry.plot(width=443, height=223):
            telemetry.add_plot_legend()
            telemetry.add_plot_axis(telemetry.mvXAxis, tag="ETime")
            telemetry.add_plot_axis(telemetry.mvYAxis, label="Error", tag="E")
            telemetry.add_line_series(times, errors, parent="E", tag="Error")
        with telemetry.plot(width=443, height=223):
            telemetry.add_plot_legend()
            telemetry.add_plot_axis(telemetry.mvXAxis, tag="ITime")
            telemetry.add_plot_axis(telemetry.mvYAxis, label="I", tag="I")
            telemetry.add_line_series(times, dists, parent="I", tag="Int")
    
    with telemetry.group(horizontal=True):
        with telemetry.plot(width=443, height=223):
            telemetry.add_plot_legend()
            telemetry.add_plot_axis(telemetry.mvXAxis, tag="STime")
            telemetry.add_plot_axis(telemetry.mvYAxis, label="Angle", tag="S")
            telemetry.add_line_series(times, angles, parent="S", tag="Servo")
        with telemetry.plot(width=443, height=223):
            telemetry.add_plot_legend()
            telemetry.add_plot_axis(telemetry.mvXAxis, tag="dtTime")
            telemetry.add_plot_axis(telemetry.mvYAxis, label="D", tag="dt")
            telemetry.add_line_series(times, dists, parent="dt", tag="Der")

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

    telemetry.render_dearpygui_frame()


telemetry.destroy_context()
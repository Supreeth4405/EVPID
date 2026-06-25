import serial
import dearpygui.dearpygui as telemetry

data = serial.Serial("COM5", 9600)


dists = []
errors = []
angles = []
times = []


telemetry.create_context()

with telemetry.window(label="EVPID_Telemetry"):
    with telemetry.plot(width=500, height=223):
        telemetry.add_plot_legend()
        telemetry.add_plot_axis(telemetry.mvXAxis, tag="DTime")
        telemetry.add_plot_axis(telemetry.mvYAxis, label="Dist", tag="D")
        telemetry.add_line_series(times, dists, parent="D", tag="Distance")
    with telemetry.plot(width=500, height=223):
        telemetry.add_plot_legend()
        telemetry.add_plot_axis(telemetry.mvXAxis, tag="ETime")
        telemetry.add_plot_axis(telemetry.mvYAxis, label="Error", tag="E")
        telemetry.add_line_series(times, errors, parent="E", tag="Error")
    with telemetry.plot(width=500, height=223):
        telemetry.add_plot_legend()
        telemetry.add_plot_axis(telemetry.mvXAxis, tag="STime")
        telemetry.add_plot_axis(telemetry.mvYAxis, label="Angle", tag="S")
        telemetry.add_line_series(times, angles, parent="S", tag="Servo")

telemetry.create_viewport(title="EVPID", width=600, height=900)

telemetry.setup_dearpygui()
telemetry.show_viewport()


while telemetry.is_dearpygui_running():

    values = data.readline().decode("UTF-8").strip().split(",")

    dist = float(values[0])
    error = float(values[1])
    servo = float(values[2])
    time = float(values[3])

    dists.append(dist)
    errors.append(error)
    angles.append(servo)
    times.append(time)

    dists = dists[-100:]
    errors = errors[-100:]
    angles = angles[-100:]
    times = times[-100:]

    telemetry.set_value("Distance", [times, dists])
    telemetry.fit_axis_data("DTime")
    telemetry.set_axis_limits("D", 0, 30)

    telemetry.set_value("Error", [times, errors])
    telemetry.fit_axis_data("ETime")
    telemetry.set_axis_limits("E", -15, 15)

    telemetry.set_value("Servo", [times, angles])
    telemetry.fit_axis_data("STime")
    telemetry.set_axis_limits("S", 0, 130)

    telemetry.render_dearpygui_frame()


telemetry.destroy_context()
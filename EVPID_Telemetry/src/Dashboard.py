import dearpygui.dearpygui as telemetry
import Customisations

def Plot_Graph(_Width, _Height, Label, X_Data, Y_Data, tagX, tagY, tagG):
    with telemetry.plot(width=_Width, height=_Height):
        telemetry.add_plot_legend()
        telemetry.add_plot_axis(telemetry.mvXAxis, tag=tagX, no_tick_labels=True)
        telemetry.add_plot_axis(telemetry.mvYAxis, label=Label, tag=tagY)
        telemetry.add_line_series(X_Data, Y_Data, parent=tagY, tag=tagG)
        Customisations.Graph_Colour(tagG)

def Show_Limit_Graph(tagX, tagY, tagG, X_Data, Y_Data, U_Limit, L_Limit):
    telemetry.set_value(tagG, [X_Data, Y_Data])
    telemetry.fit_axis_data(tagX)
    telemetry.set_axis_limits(tagY, L_Limit, U_Limit)

def Show_Graph(tagX, tagY, tagG, X_Data, Y_Data):
    telemetry.set_value(tagG, [X_Data, Y_Data])
    telemetry.fit_axis_data(tagX)
    telemetry.fit_axis_data(tagY)

def Create_Child_window(_Width, _Height, Label, Spacer, Tag, Default):
    with telemetry.child_window(width=_Width, height=_Height):
        heading = telemetry.add_text(Label)
        telemetry.bind_item_font(heading, Customisations.Label_Font)
        telemetry.add_spacer(height=Spacer)
        value = telemetry.add_text(Default, tag=Tag)
        telemetry.bind_item_font(value, Customisations.Value_Font)

def Create_Child_Window_Small(_Width, _Height, Label, Tag):
    with telemetry.child_window(width=_Width, height=_Height):
        heading = telemetry.add_text(Label, tag=Tag)
        telemetry.bind_item_font(heading, Customisations.Small_Label_Font)
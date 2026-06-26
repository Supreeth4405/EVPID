import dearpygui.dearpygui as telemetry


def Apply_Theme():
    with telemetry.theme() as theme:
        with telemetry.theme_component(telemetry.mvAll):
            telemetry.add_theme_style(telemetry.mvStyleVar_ChildRounding, 15)
            telemetry.add_theme_style(telemetry.mvStyleVar_FrameRounding, 10)
        with telemetry.theme_component(telemetry.mvAll):
            telemetry.add_theme_color(telemetry.mvThemeCol_Text,(0, 220, 0))
    telemetry.bind_theme(theme)

def Load_Fonts():
    with telemetry.font_registry():
        global Label_Font
        global Value_Font
        global Small_Label_Font
        Label_Font = telemetry.add_font("C:/Windows/Fonts/arial.ttf", 20)
        Value_Font = telemetry.add_font("C:/Windows/Fonts/arialbd.ttf", 32)
        Small_Label_Font = telemetry.add_font("C:/Windows/Fonts/arial.ttf", 16)

def Graph_Colour(tag):
    with telemetry.theme() as line_theme:
        with telemetry.theme_component(telemetry.mvLineSeries):
            telemetry.add_theme_color(telemetry.mvPlotCol_Line, (0, 220, 0), category=telemetry.mvThemeCat_Plots)
    telemetry.bind_item_theme(tag, line_theme)
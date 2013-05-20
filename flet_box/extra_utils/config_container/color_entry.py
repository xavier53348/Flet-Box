import flet as ft
from ..settings_var.settings_widget import GLOBAL_VAR

class ColorEntry(ft.Stack):
    """
    box_layout = ft.Container(content=ft.Text())

    Double_Widget = DoubleEntry
    Double_Widget(config_widget='value',widget = box_layout),
    """

    def __init__(self,config_widget='exemple [value,bgcolor,width,height] ....',widget='',id_name_widget_dict=None):
        super().__init__()
        self.widget              = widget
        self.widget_name         = config_widget
        self.id_name_widget_dict = id_name_widget_dict

        self.tmp_widget_name = " Open"

    def build(self):
        ColorEntry = ft.Container(
                            ink           = False,
                            bgcolor       = '#0c0d0e',
                            padding       = ft.padding.only(left=4, top=4, right=4, bottom=4),
                            margin        = ft.margin.all(0),
                            alignment     = ft.alignment.center,
                            border_radius = ft.border_radius.all(16),
                            border        = ft.border.all(2, ft.colors.BLACK),
                            width         = 165,
                            height        = 80,
                            content = ft.Column(
                                        wrap     = True,
                                        controls = [
                                            ft.Container(
                                                ink           = False,
                                                bgcolor       = "#0e0f11",
                                                padding       = ft.padding.only(left=8, top=0, right=8, bottom=0),
                                                alignment     = ft.alignment.center,
                                                border_radius = ft.border_radius.all(30),
                                                height        = 20,
                                                content =ft.Text(

                                                            value       = self.widget_name.capitalize().replace("_"," "),
                                                            font_family = "Consolas", #"Consolas ,RobotoSlab
                                                ),),
                                            ft.Container(
                                                    ink           = False,
                                                    padding       = ft.padding.only(left=2, top=0, right=8, bottom=0),
                                                    alignment     = ft.alignment.center,
                                                    border_radius = ft.border_radius.all(30),
                                                    border        = ft.border.all(1, ft.colors.BLACK38),
                                                    width         = 152,
                                                    height        = 36,
                                                gradient=ft.LinearGradient(
                                                                               begin = ft.alignment.top_center,
                                                                               end   = ft.alignment.bottom_center,
                                                                               colors=[
                                                                                       ft.colors.CYAN_800,
                                                                                       ft.colors.BLACK38,
                                                                                        ],
                                                                ),
                                                    content = ft.Row(
                                                                    spacing  = 4.5,
                                                                    controls = [
                                                                        ft.Container(

                                                                                    ink           = False,
                                                                                    bgcolor       = "#44CCCC00",
                                                                                    width         = 90,
                                                                                    height        = 30,
                                                                                    border_radius = ft.border_radius.all(30),
                                                                                    gradient=ft.LinearGradient(
                                                                                                                begin = ft.alignment.top_center,
                                                                                                                end   = ft.alignment.center_right,
                                                                                                                colors= [
                                                                                                                        ft.colors.BLACK12,
                                                                                                                        ft.colors.CYAN_900,
                                                                                                                        ft.colors.BLACK38,
                                                                                                                        ],),

                                                                                    content = ft.ElevatedButton(
                                                                                                    text = self.tmp_widget_name,
                                                                                                    bgcolor=ft.colors.TRANSPARENT,
                                                                                                    #======================= EVENTS ===========================
                                                                                                # on_hover = lambda x:self.modify_attributes(config_widget =self.widget_name ,value = ColorEntry),
                                                                                                on_click = lambda _: self.validate_click(
                                                                                                                                         widget_name        = self.widget_name,
                                                                                                                                         attribute_to_change= self.widget ,
                                                                                                                                         ),
                                                                                                    ),
                                                                        ),
                                                                        ft.Container(

                                                                                    ink           = False,
                                                                                    bgcolor       = ft.colors.TRANSPARENT,
                                                                                    width         = 50.5,
                                                                                    height        = 30,
                                                                                    border        = ft.border.all(1, ft.colors.CYAN_800),
                                                                                    border_radius = ft.border_radius.all(30),
                                                                                    on_click      = lambda x:self.modify_right_container_attributes(
                                                                                                                                                    data = self.widget_name,
                                                                                                                                                    value= ColorEntry
                                                                                                                                                    ),
                                                                        ),
                                                                 ],),
                                                    )
                                         ],
                            ),
                        )
        return ColorEntry

    def validate_click(self,widget_name ,attribute_to_change):

        #: ONLY PURPOSE IS HIDE CONFIG TO SHOW PALETTE COLORS AND IMAGEN
        self.color_pallete         = GLOBAL_VAR(get_global_var='COLOR_EDITOR_CONTAINER')
        self.color_pallete.visible = True
        self.color_pallete.update()

        #: SET WIDGET SELETED TO EDIT IN REAL TIME
        GLOBAL_VAR(set_global_var={
                   'WIDGET_SELECTION_EDITOR_CONTAINER':{
                                                       "widget_name": widget_name,
                                               "attribute_to_change": attribute_to_change,
                                                       }
                   })

    def modify_widget_attributes(color_selected):
        self.modify_attributes(config_widget=self.widget_name,value=color_selected)

    def modify_attributes(self,config_widget,value: str=""): #: LEFT BUTTON
        """
        NOTE:

        Will modify all attrib inside the widget that we selected

        on_change= lambda x:self.modify_attributes(config_widget =self.widget_name ,value = ColorEntry),

        EXEMPLE:

            width:      value
            height:     value
            bgcolor:    value
            value:      value

        self.widget.content.value = value if config_widget  == "value" else None
        will modify attributes of the widget class in real time
        change circle right color in streaming
        """
        #: ONLY FOR CONTAINER
        #: if  self.widget_name   == "bgcolor ":
        #:     value.content.controls[1].content.controls[1].bgcolor = value.content.controls[1].content.controls[0].content.value
        #:     value.content.controls[1].update()
        #: ONLY FOR CONTENT CONTAINER
        #: colors inside de box rounded

        # self.selected_button = value
        # print(self.selected_button,'self.selected_button')
        ...
        #: SET ATTRIBUTES
        if  self.widget_name   == "bgcolor":             self.widget.bgcolor              = self.selected_button
        if  self.widget_name   == "focused_bgcolor":     self.widget.focused_bgcolor      = self.selected_button
        if  self.widget_name   == "border_color":        self.widget.border_color         = self.selected_button
        if  self.widget_name   == "focused_border_color":self.widget.focused_border_color = self.selected_button
        if  self.widget_name   == "color":               self.widget.color                = self.selected_button
        if  self.widget_name   == "icon_color":          self.widget.icon_color           = self.selected_button
        if  self.widget_name   == "check_color":         self.widget.check_color          = self.selected_button
        if  self.widget_name   == "fill_color":          self.widget.fill_color           = self.selected_button

        if  self.widget_name   == "shadow_color":
            self.widget.shadow= ft.BoxShadow(
                                            spread_radius = 0,
                                            blur_radius   = 24,
                                            color         = self.selected_button,
                                            offset        = ft.Offset(0, 0),
                                            blur_style    = ft.ShadowBlurStyle.OUTER, # NORMAL # SOLID # OUTER # INNER
                                        )

        # value.content.controls[1].update()

        self.widget.update()

    def modify_right_container_attributes(self,data,value): #: RIGHT BUTTON
        #: ONLY FOR CONTAINER
        if  data   == "bgcolor":                self.widget.bgcolor             = ft.colors.TRANSPARENT
        if  data   == "focused_bgcolor":        self.widget.focused_bgcolor     = ft.colors.TRANSPARENT
        if  data   == "color":                  self.widget.color               = ft.colors.TRANSPARENT
        if  data   == "fill_color":             self.widget.fill_color          = ft.colors.TRANSPARENT
        if  data   == "icon_color":             self.widget.icon_color          = ft.colors.TRANSPARENT
        if  data   == "check_color":            self.widget.check_color         = ft.colors.TRANSPARENT
        if  data   == "focused_border_color":   self.widget.focused_border_color= ft.colors.TRANSPARENT
        if  data   == "border_color":           self.widget.border_color        = ft.colors.TRANSPARENT

        if  data   == "shadow_color":
            self.widget.shadow= ft.BoxShadow(
                                            spread_radius = 0,
                                            blur_radius   = 24,
                                            color         = ft.colors.TRANSPARENT,
                                            offset        = ft.Offset(0, 0),
                                            blur_style    = ft.ShadowBlurStyle.OUTER, # NORMAL # SOLID # OUTER # INNER
                                        )
        self.widget.update()

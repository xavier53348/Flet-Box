import flet as ft
from ..settings_var.settings_widget import GLOBAL_VAR
from ..config_container.color_entry import ColorEntry

click_avalidation: bool = False

class SmallPaleteColor(ft.Container):

    def __init__(self,pallete_color: str=''):
        super().__init__()
        self.pallete_color=pallete_color
        self.width  = 24
        self.height = 24

    def build(self):
        self.container = ft.Container(
                                ink          = False,
                                # tooltip      = self.pallete_color,
                                bgcolor      = self.pallete_color,
                                padding      = ft.padding.all(0),
                                margin       = ft.margin.all(0),
                                alignment    = ft.alignment.center,
                                border_radius= ft.border_radius.all(6),
                                # border       = ft.border.all(1.6, ft.colors.WHITE12),
                                on_hover     = lambda _: self.active_border_color(border_container = self.container),
                                on_click     = lambda _: self.modify_widget(),
                        )
        self.content= self.container

        self.on_click = lambda _:self.change_color_widget(color = self.pallete_color)


    def change_color_widget(self,color: str=""):
        ColorEntry.modify_widget_attributes(color_selected = color)

    def active_border_color(self,border_container):
        border_container.border = ft.border.all(2, ft.colors.TRANSPARENT) if border_container.border == ft.border.all(2, ft.colors.WHITE) else ft.border.all(2, ft.colors.WHITE)
        border_container.update()

    def modify_widget(self):
        tmp_widget_selected = GLOBAL_VAR(get_global_var="WIDGET_SELECTION_EDITOR_CONTAINER")
        self.widget_tag_name = tmp_widget_selected.get("widget_name")
        self.widget           = tmp_widget_selected.get("attribute_to_change")

        #: SET ATTRIBUTES
        if  self.widget_tag_name   == "bgcolor":               self.widget.bgcolor              = self.pallete_color
        if  self.widget_tag_name   == "focused_bgcolor":       self.widget.focused_bgcolor      = self.pallete_color
        if  self.widget_tag_name   == "border_color":          self.widget.border_color         = self.pallete_color
        if  self.widget_tag_name   == "focused_border_color":  self.widget.focused_border_color = self.pallete_color
        if  self.widget_tag_name   == "color":                 self.widget.color                = self.pallete_color
        if  self.widget_tag_name   == "icon_color":            self.widget.icon_color           = self.pallete_color
        if  self.widget_tag_name   == "check_color":           self.widget.check_color          = self.pallete_color
        if  self.widget_tag_name   == "fill_color":            self.widget.fill_color           = self.pallete_color

        if  self.widget_tag_name   == "shadow_color":
            self.widget.shadow= ft.BoxShadow(
                                            spread_radius = 0,
                                            blur_radius   = 24,
                                            color         = self.pallete_color,
                                            offset        = ft.Offset(0, 0),
                                            blur_style    = ft.ShadowBlurStyle.OUTER, # NORMAL # SOLID # OUTER # INNER
                                        )

        self.widget.update()

    def modify_right_container_attributes(self,data,value): #: RIGHT BUTTON
        #: ONLY FOR CONTAINER
        if  data   == "bgcolor":                self.widget.bgcolor = ft.colors.TRANSPARENT
        if  data   == "focused_bgcolor":        self.widget.focused_bgcolor= ft.colors.TRANSPARENT
        if  data   == "color":                  self.widget.color= ft.colors.TRANSPARENT
        if  data   == "fill_color":             self.widget.fill_color= ft.colors.TRANSPARENT
        if  data   == "icon_color":             self.widget.icon_color= ft.colors.TRANSPARENT
        if  data   == "check_color":            self.widget.check_color= ft.colors.TRANSPARENT
        if  data   == "focused_border_color":   self.widget.focused_border_color= ft.colors.TRANSPARENT
        if  data   == "border_color":           self.widget.border_color= ft.colors.TRANSPARENT

        if  data   == "shadow_color":
            self.widget.shadow= ft.BoxShadow(
                                            spread_radius = 0,
                                            blur_radius   = 24,
                                            color         = ft.colors.TRANSPARENT,
                                            offset        = ft.Offset(0, 0),
                                            blur_style    = ft.ShadowBlurStyle.OUTER, # NORMAL # SOLID # OUTER # INNER
                                        )
        self.widget.update()



class Screen_palette(ft.Container):

    def __init__(self,data='Erase this test'):
        super().__init__()

        self.padding  = ft.padding.all(8)
        self.margin   = ft.margin.all(0)    #outside box
        self.alignment= ft.alignment.center
        self.on_hover = lambda _: self.validate_click()
        self.border_radius = ft.border_radius.all(20)
        self.gradient=ft.LinearGradient( begin= ft.alignment.top_center,
                                        end   = ft.alignment.center_right,
                                        colors=[
                                                ft.colors.BLACK12,
                                                ft.colors.BLUE_900,
                                                ft.colors.PURPLE_800,
                                                ft.colors.BLUE_600,
                                                ft.colors.BLACK12,
                                                # ft.colors.RED_900,
                                        ],)
    def build(self):
        list_started = False

        screen_1=ft.Row(
                        scroll     = True,
                        wrap       = True,
                        spacing    = 0.08,
                        run_spacing= 0.08,
                        controls=[
                                 ],)
        self.content=screen_1

        for key, value in vars(ft.colors).items():
            if key == "PRIMARY":
                list_started = True
            if list_started:
                if key ==  'GREY_800':
                    break
                screen_1.controls.append(SmallPaleteColor(pallete_color= value))

    def validate_click(self):
        global click_avalidation

        self.color_pallete  = GLOBAL_VAR(get_global_var='COLOR_EDITOR_CONTAINER')

        if click_avalidation:
            click_avalidation = False
            self.color_pallete.visible = False
            self.color_pallete.update()

        else:
            click_avalidation = True


if __name__ == '__main__':

    def main(page: ft.Page):
        page.vertical_alignment = ft.MainAxisAlignment.CENTER
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        page.theme_mode = ft.ThemeMode.DARK         #ft.ThemeMode.LIGHT
        page.window_left = 0
        page.window_top = 0
        page.window_height=700
        page.window_width=290
        page.padding=0
        page.spacing=0
        page.add(Screen_palette())
        page.update()

    ft.app(
            target=main,
            )
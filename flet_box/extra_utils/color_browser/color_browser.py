
import flet as ft
import os
import pyperclip
import time

os.environ["FLET_WS_MAX_MESSAGE_SIZE"] = "8000000"


class Color_text(ft.Stack):
    # globalVar='Erase this test'

    def __init__(self,data='Erase this test'):
        super().__init__()
        self.TMP=data

    def build(self):
        Drop_Color_text=ft.IconButton(
                        visible=False,
                    content=ft.Container(
                                height   = 120,
                                width    = 120,
                                visible  = False,
                                on_click = lambda _:self.copy_to_clipboard(Drop_Color_text.content.content.controls[0].bgcolor),
                            content=ft.Column(
                                    controls = [
                                        ft.Container(
                                                height        = 120,
                                                width         = 120,
                                                ink           = False,
                                                bgcolor       = ft.colors.BLACK38,
                                                padding       = ft.padding.all(8),
                                                margin        = ft.margin.all(0),
                                                alignment     = ft.alignment.center,
                                                border_radius = ft.border_radius.all(30),
                                                border        = ft.border.all(2, ft.colors.BLACK12),
                                        ),
                                        ft.Text(
                                            visible=False,
                                            value      = 'testing',
                                            size       = 12,
                                            width      = 100,
                                            no_wrap    = True,
                                            text_align = "center",
                                        ),
                                    ],
                                    spacing              = 5,
                                    alignment            = "center",
                                    horizontal_alignment = "center",
                                ),
                                alignment=ft.alignment.center,
                            ),
                                )
        return Drop_Color_text

    def copy_to_clipboard(self,e):
        text_copy = e

        # personal scakbar
        pyperclip.copy(text_copy)
        alert_dialog.visible = True
        alert_dialog.content.value = f"Copy: {text_copy} "
        alert_dialog.update()
        time.sleep(0.5)
        alert_dialog.visible = False
        alert_dialog.update()

class ColorBrowser(ft.Stack):
    """
    lite module to find colors by name
    """

    def __init__(self,blur_effect = False, numb_widget_to_show=50):
        super().__init__()
        global alert_dialog

        # PREPARING THE LIST THAT WILL CONTENT ALL INCON INSIDE
        self.list_colors = self.preparing_list_colors()
        self.numb_widget_to_show = numb_widget_to_show

        if blur_effect:
            self.blur = 20
        else:
            self.blur = None
        self.Icontext = Color_text()

        # BARNER THAT WILL SHOW AFTER MAKE CLICK OVER THE WIDGET
        alert_dialog = ft.Container(
                                        visible       = False,
                                        height        = 40,
                                        width         = 240,
                                        bgcolor       = 'red',
                                        offset        = (0,-1.5),
                                        alignment     = ft.alignment.center,
                                        border_radius = ft.border_radius.all(16),
                                    content = ft.Text(
                                                        value = 'None',
                                                        )
                                        )
        # GRID VIEW INSIDE THE MAIN LAYOUT
        self.Search_Gridwiew = ft.Row(
                        visible  = False,
                        wrap     = True,
                        scroll='HIDDEN',
                    controls=[ Color_text() for _ in range(self.numb_widget_to_show) ],
                        )
        # MAIN CONTAINER SKELETON OF THE WIDGET OR MAIN LAYOUT
        self.Drop_ColorBrowser=ft.Container(
                    expand    = True,
                    ink       = False,
                    padding   = ft.padding.all(8),
                    margin    = ft.margin.all(8),
                    alignment = ft.alignment.center,

                    content   = ft.Column(
                        spacing              = 8,
                        alignment            = ft.MainAxisAlignment.SPACE_AROUND,
                        horizontal_alignment = ft.CrossAxisAlignment.CENTER,
                        scroll               = False,
                        controls=[
                                    ft.Container( # TEXT FIELD
                                                ink           = False,
                                                padding       = ft.padding.all(4),
                                                margin        = ft.margin.all(0),
                                                alignment     = ft.alignment.center,
                                                border_radius = ft.border_radius.all(30),
                                                blur          = self.blur,
                                                height        = 50,
                                            content=ft.TextField(
                                                                label                = "  Search Colors by name",
                                                                border               = ft.InputBorder.OUTLINE,
                                                                bgcolor              = ft.colors.BLACK12,
                                                                focused_bgcolor      = ft.colors.BLACK12,
                                                                border_color         = ft.colors.TEAL,
                                                                focused_border_color = ft.colors.TRANSPARENT,
                                                                border_radius        = 30,
                                                                text_size            = 15,
                                                                prefix_icon          = ft.icons.SEARCH,
                                                                content_padding      = ft.padding.only(left=16, top=2, right=16, bottom=2),
                                                            on_submit            = lambda _: self.search_icons(_),
                                                                ),
                                    ),#<=== NOTE COMA <==> ERASE COMA IF MAKE 1 ERROR
                                    ft.Container( # GRID VIEW
                                                ink           = False,
                                                bgcolor       = ft.colors.BLACK38,
                                                padding       = ft.padding.all(8),
                                                margin        = ft.margin.all(0),
                                                alignment     = ft.alignment.center,
                                                border_radius = ft.border_radius.all(30),
                                                border        = ft.border.all(0.8, ft.colors.TEAL),
                                                blur          = self.blur,
                                                height        = 500,
                                            content       = self.Search_Gridwiew,
                                    ),#<=== NOTE COMA
                                    alert_dialog,
                                 ],
                    ),#<=== NOTE COMA [NOTE]
        )#<=== NOTE COMA

    def build(self):

        return self.Drop_ColorBrowser

    def preparing_list_colors(self):

        # WE CALL ALL ICONS TO SAVE IN ICON_LIST TO MAKE ALOOP OVERIT
        # AND EXTRACT EXATCLY THE ICO THAT WE ARE FINDING
        colors_list  = list()
        list_started = False

        for key, value in vars(ft.colors).items():
            if key == "PRIMARY":
                list_started = True
            if list_started:
                colors_list.append(value)

        return colors_list

    def search_icons(self,e):

        # ALL DATA THAT WE PASE BY TEXT_INPUT WILL BE IN LOWER CASE
        search_term = e.control.value.lower()

        # only in production
        # print(search_term)

        def run_upload_colors():
            global num_count
            num_count = 0

            for _ in self.list_colors:
                if str(_).startswith(search_term) and num_count < len(self.Search_Gridwiew.controls):

                    # ONLY SHOW IN SCREEN THE AMOUNT THAT WE FIND BY OUR SEARCH
                    # THE REST WILL NOW SHOW IN THE NEXT CODE
                    self.color_widget = self.Search_Gridwiew.controls[num_count].controls[0]

                    # CHANGE ICO AND NAME ICO PROPERTY
                    self.color_widget.content.content.controls[0].bgcolor = _
                    self.color_widget.content.content.controls[1].value   = _

                    # CHANGE PROPERTY VISIBLE
                    self.color_widget.visible                             = True
                    self.Search_Gridwiew.visible                          = True
                    self.Search_Gridwiew.controls[num_count].visible      = True
                    self.color_widget.content.content.controls[0].visible = True
                    self.color_widget.content.content.controls[1].visible = True

                    # NUMBER OF COUNT WIDGET WILL INCREASE TO HAVE CONTROL OF ALL DRAW WIDGETS
                    num_count+= 1

            # THIS CODE IS IF THE WIDET THAT WE CALL HAVE LESS THAN ALL AMOUNT OF WIDGET IN BOX
            # EXEMPLE 50 IF WE CALL 20 THE REST OF 30 WILL BE VISIBLE = OFF
            # WE DON'T WANT SHOW INECCESARY WIDGET IN SCREEN

            for _ in range(num_count,self.numb_widget_to_show):
                # will take all widget that no exist in search icon in mode invisible
                self.color_widget = self.Search_Gridwiew.controls[_].controls[0]

                self.color_widget.visible = False
                self.Search_Gridwiew.controls[_].visible = False
                self.color_widget.content.content.controls[0].visible = False
                self.color_widget.content.content.controls[1].visible = False

            # UPDATE ALL WIDGETS INSIDE BOX JUST ONE TIME
            for _ in self.Search_Gridwiew.controls:
                _.update()
            self.Search_Gridwiew.update()

        run_upload_colors()

if __name__ == '__main__':
    def main(page: ft.Page):
        page.scroll                    = "HIDDEN" #AUTO ADAPTIVE ALWAYS HIDDEN
        page.vertical_alignment        = ft.MainAxisAlignment.CENTER
        page.horizontal_alignment      = ft.CrossAxisAlignment.CENTER
        page.theme_mode                = ft.ThemeMode.DARK         #ft.ThemeMode.LIGHT
        page.window_bgcolor            = ft.colors.RED_100
        page.window_left               = 3
        page.window_top                = 3
        page.window_height             = 800
        page.window_width              = 400
        page.padding                   = 0
        page.spacing                   = 0
        page.add(ColorBrowser())
    ft.app(target=main)
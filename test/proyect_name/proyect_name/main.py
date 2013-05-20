from builder.app_manager  import builder_app ,GLOBAL_VAR
# from controls.app_style_manager import styles
from controls.app_screen_manager import screens
import flet as ft


def change_size(page_width: float, page_height: float):
    #: RESIZE HEIGHT FROM SCREEN
    all_screens:    dict = GLOBAL_VAR(get_global_var='all_screens')
    current_screen: dict = GLOBAL_VAR(get_global_var='current_screen')

    #: UPDATE SIZE STREAMINGE
    data = all_screens.get(current_screen)
    data.height , data.width  = page_height , page_width
    data.update()

def main(page: ft.Page):

    # page.scroll               = "HIDDEN"              #: AUTO ADAPTIVE ALWAYS HIDDEN
    page.vertical_alignment   = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    #:  COLOR
    page.theme_mode           = ft.ThemeMode.DARK
    # page.bgcolor              = ft.colors.BLACK
    # page.window_bgcolor       = ft.colors.TRANSPARENT

    #: POSITION OF SCREENS
    page.window_left          = 8
    page.window_top           = 8
    # page.window_center()

    #: SIZE
    page.window_height        = 620  # 566 620
    page.window_width         = 320  # 295 320
    page.padding              = 0
    page.spacing              = 0
    page.expand               = True

    #: SCREEN BUILDER
    tmp_screens = builder_app(screen=screens, main_page=page ) #: it's necessary to call all screens
    all_screens = tmp_screens.get('show_all_screens')                           #: return one dict with all  screens inside
    show_screen = tmp_screens.get('builder_app')                                #: return exactly first screen


    #: UPDATE SIZE OF MAIN PHGONE SCREEN
    show_screen.height = page.window_height
    show_screen.width  = page.window_width
    page.on_resize     = lambda _: change_size(page_width=page.window_width, page_height=page.window_height)

    #: SET FROM CONTAINER BGCOLOR
    # page.bgcolor = styles['_2921']['bgcolor']
    # styles['_2921']['bgcolor'] ="red"

    # print(styles.get('_2921').get('bgcolor'))
    #: WE SET HOT SCOPE VAR


    page.appbar = ft.AppBar(
        # bgcolor=ft.colors.WHITE12,
        bgcolor=ft.LinearGradient( begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=[ft.colors.BLUE, ft.colors.YELLOW],),

        # bgcolor=ft.colors.WHITE12,
        leading=ft.IconButton(icon=ft.icons.POLYMER,icon_size=14,on_click=lambda _:print('hello')),
        leading_width=40,
        title=ft.Text("Name app ",size=14),
        center_title=False,
        toolbar_height=40,
        # bgcolor=ft.colors.SURFACE_VARIANT,
        actions=[

            ft.IconButton(ft.icons.WB_SUNNY_OUTLINED,icon_size=14),
            ft.IconButton(ft.icons.FILTER_3,icon_size=14),
            ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem(text="Item 1"),
                    ft.PopupMenuItem(),  # divider
                    ft.PopupMenuItem(
                        text="Checked item", checked=False,height=20
                        # on_click=check_item_clicked
                    ),
                ]
            ),
        ],
    )


    page.add(show_screen)
    page.update()

    # styles['_2921']['bgcolor'] ="Cyan"

def run_app():
    """
    - NO ERASE THIS FUNCTION
    - ONLY RUN CREATING PYPY PACKAGE
    """
    ft.app(
            target=main,
            )

if __name__ == '__main__':

    ft.app(
            target=main,
            assets_dir="assets"
            )
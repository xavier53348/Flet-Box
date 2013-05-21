import flet as ft

class Container_Widget(ft.UserControl):
    # globalVar='Erase this test'

    def __init__(self,data='Erase this test'):
        super().__init__()
        # self.title='data'
        self.title=data

    def build(self):
        Drop_NameApp=ft.Container(
                                ##################### PROPERTY ROW
                                ##################### [rotate,offset] , [scale,aspect_ratio] , [visible,disabled]
                                # expand=True,
                                ink=False,                                                      # click effect ripple
                                bgcolor="cyan",                                              # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                                padding= ft.padding.all(8),    # inside box                     # padding.only(left=8, top=8, right=8, bottom=8),
                                margin = ft.margin.all(8),     # outside box                    # margin.only (left=8, top=8, right=8, bottom=8),
                                alignment=ft.alignment.center,                                  # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right.    posicionamiento adentro widget
                                # border_radius= ft.border_radius.all(30),                      # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                                border=ft.border.all(2, ft.colors.BLACK),                       # ft.border.only(Left=8, top=8, right=8, bottom=8),
                                # ===================
                                # image_src = f"/home/mjay/Pictures/3d_neon_pink-2560x1440.jpg",
                                # image_opacity=0.1,
                                # image_fit='COVER',                                            # CONTAIN, COVER, FILL, FIT_HEIGHT, FIT_WIDTH, SCALE_DOWN
                                # ===================
                                width=150,
                                # height=150,
                                # tooltip='Container',
                                ############################
                            content=ft.Column(
                                            controls=[
                                                    ft.Text(f"{self.title}"),
                                                    ft.Text(f"{self.title}"),
                                                    ft.Text(f"{self.title}"),
                                                     ],
                                            ),
                            on_hover=lambda _:print(Drop_NameApp._Control__uid),
                        )
        return Drop_NameApp
######## ContainerWidget = Container_Widget(),# <======= Comma

def main(page: ft.Page):
    ###################### CONFIGURATION
    # page.title = "Containers - clickable and not"
    # page.window_title_bar_hidden = True
    # page.window_frameless = True
    # page.window_focused=True
    page.scroll=True
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    ######################  COLOR
    page.theme_mode = ft.ThemeMode.DARK         #ft.ThemeMode.LIGHT
    # page.bgcolor = ft.colors.TRANSPARENT
    # page.window_bgcolor =  ft.colors.TRANSPARENT
    ###################### POSITION OF SC
    page.window_left = 8
    page.window_top = 8
    # page.window_center()
    ###################### SIZE
    page.window_height=350
    page.window_width=300
    page.padding=8
    page.spacing=8
    page.expand=True
    ######################
    ContainerWidget = Container_Widget()
    screen_1=ft.Container(
                    ##################### PROPERTY
                    # expand=True,
                    ink=True,                                           # click effect ripple
                    bgcolor="Teal",                                # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                    padding= ft.padding.all(8),    # inside box         # padding.only(left=8, top=8, right=8, bottom=8),
                    margin = ft.margin.all(8),     # outside box        # margin.only (left=8, top=8, right=8, bottom=8),
                    alignment=ft.alignment.center,                      # top_left, top_center, top_right, center_left, center, center_right, bottom_left, bottom_center, bottom_right.    posicionamiento adentro widget
                    # border_radius= ft.border_radius.all(30),          # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                    # border=ft.border.all(3, ft.colors.BLUE),          # ft.border.only(Left=8, top=8, right=8, bottom=8),
                    # image_src=f"/icons/icon-512.png",
                    # width=150,
                    # height=150,
                    tooltip='Container',
                    ##################### EFFECTS
                    # gradient=ft.LinearGradient( begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=[ft.colors.BLUE, ft.colors.YELLOW],),
                    # gradient=ft.RadialGradient( colors=[ft.colors.YELLOW, ft.colors.BLUE],),
                    ##################### WIDGETS
                    content=ft.Container(
                                ##################### PROPERTY COLUMN
                                ##################### [rotate,offset] , [scale,aspect_ratio] , [visible,disabled]
                                # expand=True,
                                ink=False,                                                      # click effect ripple
                                # bgcolor="#3f449a",                                              # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                                padding= ft.padding.all(8),    # inside box                        # padding.only(left=8, top=8, right=8, bottom=8),
                                margin = ft.margin.all(8),    # outside box                       # margin.only (left=8, top=8, right=8, bottom=8),
                                alignment=ft.alignment.center,                                  # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right.    posicionamiento adentro widget
                                # border_radius= ft.border_radius.all(30),                      # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                                # border=ft.border.all(2, ft.colors.BLACK),                     # ft.border.only(Left=8, top=8, right=8, bottom=8),
                                # ===================
                                # image_src = f"/home/mjay/Pictures/3d_neon_pink-2560x1440.jpg",
                                # image_opacity=0.1,
                                # image_fit='COVER',                                            # CONTAIN, COVER, FILL, FIT_HEIGHT, FIT_WIDTH, SCALE_DOWN
                                # ===================
                                # width=150,
                                # height=150,
                                # tooltip='Container',
                                ##################### EFFECTS
                                # gradient=ft.LinearGradient( begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=[ft.colors.BLUE, ft.colors.YELLOW],),
                                # gradient=ft.RadialGradient( colors=[ft.colors.YELLOW, ft.colors.BLUE],),
                                ##################### WIDGETS
                                content=ft.Column(
                                    ##################### PROPERTY BOX
                                    # expand=True,
                                    # alignment=ft.MainAxisAlignment.SPACE_AROUND,              # horizontal <=> START,CENTER,END SPACE_BETWEEN SPACE_AROUND SPACE_EVENLY
                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,        # vertical       START,CENTER END
                                    ##################### LET MAKE SCROLL IN LONG QUANTITY
                                    # scroll=True,                                              # center widget
                                    # tight=True,
                                    ##################### ADAPT TO SCREEN
                                    # wrap=True,                                                  # justify in all screen
                                    # spacing=8,                                                # space widget left right
                                    # run_spacing=8,                                            # space widget up down
                                    ##################### WIDGETS
                                    controls=[
                                                ContainerWidget,
                                                ft.ElevatedButton("modify_widget",tooltip='modify_widget',on_click=lambda _:check_data(data = 'modify_widget')),
                                                ft.ElevatedButton("get_attribute_by_id",tooltip='get_attribute_by_id',on_click=lambda _:check_data(data = 'get_attribute_by_id')),
                                                ft.ElevatedButton("erase",tooltip='erase',on_click=lambda _:check_data(data = 'erase')),
                                                ft.ElevatedButton("add",tooltip='add',on_click=lambda _:check_data(data = 'add')),
                                                ft.ElevatedButton("replace",tooltip='replace',on_click=lambda _:check_data(data = 'replace')),
                                             ],
                                ),#<=== NOTE COMA [NOTE]                     for x in range(1,50): widget.content.controls.append(ft.ElevatedButton("press buttom",tooltip='buttom'))
                                ##################### EVENTS
                                # on_click=lambda _:print(_),                            # on_hover=print('on click over'), on_long_press=print('long press'),
                    ),#<=== NOTE COMA

                    ##################### EVENTS
                    # on_click=lambda _:print(_),                        # on_hover=print('on click over'), on_long_press=print('long press'),
                )


    page.add(screen_1)
    page.update()

    def check_data(data):
        # id__widget = page.get_control(ContainerWidget._Control__uid)

        if  data == 'modify_widget':
            try:
                id_widget         = page.get_control('_5').controls[0]
                id_widget.bgcolor = 'red'
            except IndexError:
                print('widget has been erased')

        elif data == 'get_attribute_by_id':
            id_widget = page.get_control('_5')
            print(id_widget)

        elif data == 'erase':
            id_widget          = page.get_control(id='_5')
            id_widget.controls = None

        elif data == 'add':
            id_widget          = page.get_control(id='_5')
            id_widget.controls[0].content.controls.append(ft.ElevatedButton('hello'),)

        elif data == 'replace':
            id_widget          = page.get_control(id='_5')
            id_widget.controls=[ft.Icon('Home'),]


        id_widget.update()
if __name__ == '__main__':
    ft.app(target=main)
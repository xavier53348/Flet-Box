import flet as ft


class Make_data(ft.UserControl):
    # globalVar='Erase this test'

    def __init__(self,data='Erase this test'):
        super().__init__()
        # self.title='data'
        self.title=data

    def build(self):

        global Drop_Make_data
        Drop_Make_data=ft.Container(
                    ##################### PROPERTY
                    ##################### [rotate,offset] , [scale,aspect_ratio] , [visible,disabled]
                    # expand=True,
                    # ink=False,                                                # click effect ripple
                    # # bgcolor="#44CCCC00",                                    # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                    # padding= ft.padding.all(8),    # inside box                # padding.only(left=8, top=8, right=8, bottom=8),
                    # margin = ft.margin.all(8),    #outside box                # margin.only (left=8, top=8, right=8, bottom=8),
                    # alignment=ft.alignment.center,                            # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right.    posicionamiento adentro widget
                    # border_radius= ft.border_radius.all(30),            # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                    # border=ft.border.all(2, ft.colors.BLACK),             # ft.border.only(Left=8, top=8, right=8, bottom=8),
                    # # ===================
                    # image_src = f"/home/mjay/Pictures/3d_neon_pink-2560x1440.jpg",
                    # image_opacity=0.1,
                    # image_fit='COVER',                                            # CONTAIN, COVER, FILL, FIT_HEIGHT, FIT_WIDTH, SCALE_DOWN
                    # # ===================
                    # width=150,
                    # height=150,
                    # tooltip='Container',
                    # ##################### EFFECTS
                    gradient=ft.LinearGradient( begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=[ft.colors.BLUE, ft.colors.YELLOW],),
                    # gradient=ft.RadialGradient( colors=[ft.colors.YELLOW, ft.colors.BLUE],),
                    ##################### WIDGETS
                    content=ft.Column(
                                    ##################### PROPERTY BOX
                                    # expand=True,
                                    # alignment=ft.MainAxisAlignment.SPACE_AROUND,              # horizontal <=> START,CENTER,END SPACE_BETWEEN SPACE_AROUND SPACE_EVENLY
                                    # vertical_alignment=ft.CrossAxisAlignment.CENTER,          # vertical       START,CENTER END
                                    ##################### LET MAKE SCROLL IN LONG QUANTITY
                                    # scroll=True,                                              # center widget
                                    # tight=True,
                                    ##################### ADAPT TO SCREEN
                                    # wrap=True,                                                  # justify in all screen
                                    # spacing=8,                                                # space widget left right
                                    # run_spacing=8,                                            # space widget up down
                                    ##################### WIDGETS
                                    controls=[
                                                ft.ElevatedButton("write data",tooltip='buttom',on_click= lambda _:self.write_data(_)),
                                                ft.ElevatedButton("press row",tooltip='buttom',on_click= lambda _:self.write_data(_)),
                                                ft.ElevatedButton("press row",tooltip='buttom',on_click= lambda _:self.write_data(_)),
                                             ],),
                    ##################### EVENTS
                    # on_click=lambda _:print(_),                            # on_hover=print('on click over'), on_long_press=print('long press'),
        )#<=== NOTE COMA
        return Drop_Make_data
    ######## Make_data = Make_data(),# <======= Comma

    def style_widget(self):
        style_box = {
                    'width': 120,
                    'height':120,
                    'border_radius':ft.border_radius.all(30),            # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                    # border_radius= ft.border_radius.all(30),            # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),

                    }
        return style_box

    def write_data(self,e):

        # widget= ft.Container(**self.style_widget(),)
        # widget= ft.Container(width=120,border_radius= ft.border_radius.all(30),)

        # string_data = f"""{Drop_Make_data},#<<<REPLACE"""



        # STEPS
        # EXEMPLE '_1':ft.Container()
        #
        #  ADD WIDGET
        #  '_1' : Container(),#REPLACE              ),#REPLACE = #REPLACE_2')
        #  '_1' : Container(content=#REPLACE_2')     #REPLACE will be replaced by '
        #  '_1' : Container(content='_2')
        #
        # REPLACE WIDGET
        #

        # if control name is container ,#<<<REPLACE = content=#<<<REPLACE_1'),
        # Drop_Make_data._get_control_name()
        # print(Drop_Make_data._get_control_name().capitalize())
        # with open('SCREENS_DB.py' , 'w') as f:
        #     f.write(f"{widget.__str__()}")

        """
         Drop_Make_data=ft.Container(
                            content=ft.Column(
                                            controls=[
                                                        ft.ElevatedButton("write data",tooltip='buttom',on_click= lambda _:self.write_data(_)),
                                                     ],),
                            )

        Drop_Make_data='_1'

        '_1':None
        '_1':'_2':None
        '_1':'_2':None


        level 1  2  3  4



        'level_1'
        'level_2'
        'level_3'
        'level_4'
        'level_5'
        'level_6'

                """

        print(Drop_Make_data)
        # print(Drop_Make_data.invoke_method('on_click'))
        # print(Drop_Make_data._wrap_attr_dict({'new_value':Drop_Make_data}))

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
    page.window_height=320
    page.window_width=320
    page.padding=8
    page.spacing=8
    page.expand=True

    print(page.update)
    ######################
    global screen_1
    screen_1=ft.Container(
                    ##################### PROPERTY
                    # expand=True,
                    ink=True,                                           # click effect ripple
                    bgcolor="#44CCCC00",                                # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                    padding= ft.padding.all(8),    # inside box         # padding.only(left=8, top=8, right=8, bottom=8),
                    margin = ft.margin.all(8),     # outside box        # margin.only (left=8, top=8, right=8, bottom=8),
                    alignment=ft.alignment.center,                      # top_left, top_center, top_right, center_left, center, center_right, bottom_left, bottom_center, bottom_right.    posicionamiento adentro widget
                    # border_radius= ft.border_radius.all(30),          # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                    # border=ft.border.all(3, ft.colors.BLUE),          # ft.border.only(Left=8, top=8, right=8, bottom=8),
                    # image_src=f"/icons/icon-512.png",
                    # width=150,
                    # height=150,
                    # tooltip='Container',
                    ##################### EFFECTS
                    # gradient=ft.LinearGradient( begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=[ft.colors.BLUE, ft.colors.YELLOW],),
                    # gradient=ft.RadialGradient( colors=[ft.colors.YELLOW, ft.colors.BLUE],),
                    ##################### WIDGETS
                    content=Make_data(),
                    ##################### EVENTS
                    # on_click=lambda _:print(_),                        # on_hover=print('on click over'), on_long_press=print('long press'),
                )


    page.add(screen_1)
    page.update()



if __name__ == '__main__':
    ft.app(target=main)
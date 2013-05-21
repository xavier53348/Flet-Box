import flet as ft

class Build_Phone_Editor(ft.UserControl):
     """Center Box that contain the phone to add Widget"""

     def __init__(self,data='Erase this test'):
          super().__init__()
          # self.title='data'
          self.title=data
          # self.dropDragg= DropDragg()

     def build(self):
          Drop_Build_Phone_Editor = ft.Container( ###################### PHONE CONTAINER
                                        ##################### PROPERTY COLUMN
                                        ##################### [rotate,offset] , [scale,aspect_ratio] , [visible,disabled]
                                        # expand=True,
                                        ink=False,                                                      # click effect ripple
                                        bgcolor="#3f449a",                                              # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                                        padding= ft.padding.all(0),    # inside box                        # padding.only(left=8, top=8, right=8, bottom=8),
                                        margin = ft.margin.all(0),    # outside box                       # margin.only (left=8, top=8, right=8, bottom=8),
                                        alignment=ft.alignment.center,                                  # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right.    posicionamiento adentro widget
                                        border_radius= ft.border_radius.all(30),                      # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                                        border=ft.border.all(4, ft.colors.BLACK),                     # ft.border.only(Left=8, top=8, right=8, bottom=8),
                                        # ===================
                                        # image_src = f"/home/mjay/Pictures/3d_neon_pink-2560x1440.jpg",
                                        # image_opacity=0.1,
                                        # image_fit='COVER',                                            # CONTAIN, COVER, FILL, FIT_HEIGHT, FIT_WIDTH, SCALE_DOWN
                                        # ===================
                                        width=260,
                                        height=525,
                                        # tooltip='Container',
                                        ##################### EFFECTS
                                        # gradient=ft.LinearGradient( begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=[ft.colors.CYAN, ft.colors.BLACK],),
                                        # gradient=ft.RadialGradient( colors=[ft.colors.YELLOW, ft.colors.BLUE],),
                                        ##################### WIDGETS
                                        content=ft.Column(
                                           ##################### PROPERTY BOX
                                           # expand=True,
                                           # alignment=ft.MainAxisAlignment.SPACE_AROUND,              # horizontal <=> START,CENTER,END SPACE_BETWEEN SPACE_AROUND SPACE_EVENLY
                                           # horizontal_alignment=ft.CrossAxisAlignment.CENTER,        # vertical       START,CENTER END
                                           ##################### LET MAKE SCROLL IN LONG QUANTITY
                                           # scroll=True,                                              # center widget
                                           # tight=True,
                                           ##################### ADAPT TO SCREEN
                                           wrap=True,                                                  # justify in all screen
                                           # spacing=8,                                                # space widget left right
                                           # run_spacing=8,                                            # space widget up down
                                           ##################### WIDGETS
                                           controls=[
                                                       # ft.ElevatedButton("press column",tooltip='buttom'),
                                                       # ft.ElevatedButton("press column",tooltip='buttom'),
                                                       # ft.ElevatedButton("press column",tooltip='buttom'),
                                                    ],
                                        ),#<=== NOTE COMA [NOTE]                     for x in range(1,50): widget.content.controls.append(ft.ElevatedButton("press buttom",tooltip='buttom'))
                                        ##################### EVENTS
                                        # on_click=lambda _:print(_),                            # on_hover=print('on click over'), on_long_press=print('long press'),
                                        )#<=== NOTE COMA

          return Drop_Build_Phone_Editor
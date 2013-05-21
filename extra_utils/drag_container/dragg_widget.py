import flet as ft



class DraggWidget(ft.UserControl):
    # globalVar='Erase this test'

    def __init__(self,data='Erase this test'):
        super().__init__()
        # self.title='data'
        self.title=data

    def build(self):
        Drop_DraggWidget=ft.Container(
                                ##################### PROPERTY ROW
                                ##################### [rotate,offset] , [scale,aspect_ratio] , [visible,disabled]
                                # expand=True,
                                ink=False,                                                      # click effect ripple
                                bgcolor="#3f9a64",                                              # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
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
                                width=50,
                                height=50,
                                # tooltip='Container',
                                ############################
                            content=ft.Text(f"solor")
                        )

        return Drop_DraggWidget
######## DraggWidget = DraggWidget(),# <======= Comma
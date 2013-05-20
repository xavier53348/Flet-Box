
from ..settings_var.settings_widget import GLOBAL_VAR
import flet as ft


class WrapWidgetNode():
    container_string_node = ''
    contents__string_node = ''
    tmp_controls_all_node = []

    def __init__(self,):
        super().__init__()
        self.show_tree_nodews()


    def show_tree_nodews(self):
        """
        BUILDER TREE WITH ALL WIDGET INSIDE CALLING ONE BY ONE
        TO MAKE A TREE WITH ALL WIDGETS OREDERER

        """
        self.all_widgets = GLOBAL_VAR(get_global_var='EXPORT_DATA_PHONE')

        list_controls  = ['row','column','stack',]
        # ##################### >>> 0
        # self.container_string_node = self.main_node
        # self.contents__string_node = self.container_string_node.content
        # self.all_data_list.append(f"⫹ 0 ⫺ {self.container_string_node._get_control_name()}")
        # self.all_data_list.append(f"⫹ 0 ⫺ {self.contents__string_node._get_control_name()}")
        # ####################################################################################
        self.all_data_list = []

        for _ in self.all_widgets:
            self.main_node = self.all_widgets.get(_)
            self.container_string_node = self.main_node
            self.contents__string_node = self.container_string_node.content

            # self.all_data_list.append(f"⫹ 0 ⫺ {self.container_string_node._get_control_name()}")
            self.all_data_list.append(f"⫹ 🯰 ⫺ █━ {self.contents__string_node._get_control_name()}")

            if self.contents__string_node._get_control_name() in list_controls:
                """ IF IT'S TRUE GET ALL CONTROLS"""
                tmp_controls_all_node = self.contents__string_node.controls

                for _ in tmp_controls_all_node:
                    self.container_string_node = _.controls[0].content
                    self.contents__string_node = self.container_string_node.content

                    # self.all_data_list.append(f"⫹ 1 ⫺    {self.container_string_node._get_control_name()}")
                    self.all_data_list.append(f"⫹ 🯱 ⫺ █░░▐━ {self.contents__string_node._get_control_name()}")

                    if self.contents__string_node._get_control_name() in list_controls:
                        """ IF TRUE GET ALL CONTROLS"""
                        tmp_controls_all_node = self.contents__string_node.controls

                        for _ in tmp_controls_all_node:
                            self.container_string_node = _.controls[0].content
                            self.contents__string_node = self.container_string_node.content

                            # self.all_data_list.append(f"⫹ 2 ⫺        {self.container_string_node._get_control_name()}")
                            self.all_data_list.append(f"⫹ 🯲 ⫺ █░░▐  ▐━ {self.contents__string_node._get_control_name()}")

                            if self.contents__string_node._get_control_name() in list_controls:
                                """ IF TRUE GET ALL CONTROLS"""
                                tmp_controls_all_node = self.contents__string_node.controls

                                for _ in tmp_controls_all_node:
                                    self.container_string_node = _.controls[0].content
                                    self.contents__string_node = self.container_string_node.content

                                    # self.all_data_list.append(f"⫹ 3 ⫺            {self.container_string_node._get_control_name()}")
                                    self.all_data_list.append(f"⫹ 🯳 ⫺ █░░▐  ▐  ▐━ {self.contents__string_node._get_control_name()}")

                                    if self.contents__string_node._get_control_name() in list_controls:
                                        """ IF TRUE GET ALL CONTROLS"""
                                        tmp_controls_all_node = self.contents__string_node.controls

                                        for _ in tmp_controls_all_node:
                                            self.container_string_node = _.controls[0].content
                                            self.contents__string_node = self.container_string_node.content

                                            # self.all_data_list.append(f"⫹ 4 ⫺                {self.container_string_node._get_control_name()}")
                                            self.all_data_list.append(f"⫹ 🯴 ⫺ █░░▐  ▐  ▐  ▐━ {self.contents__string_node._get_control_name()}")

                                            if self.contents__string_node._get_control_name() in list_controls:
                                                """ IF TRUE GET ALL CONTROLS"""
                                                tmp_controls_all_node = self.contents__string_node.controls

                                                for _ in tmp_controls_all_node:
                                                    self.container_string_node = _.controls[0].content
                                                    self.contents__string_node = self.container_string_node.content

                                                    # self.all_data_list.append(f"⫹ 5 ⫺                    {self.container_string_node._get_control_name()}")
                                                    self.all_data_list.append(f"⫹ 🯵 ⫺ █░░▐  ▐  ▐  ▐  ▐━ {self.contents__string_node._get_control_name()}")

                                                    if self.contents__string_node._get_control_name() in list_controls:
                                                        """ IF TRUE GET ALL CONTROLS"""
                                                        tmp_controls_all_node = self.contents__string_node.controls

                                                        for _ in tmp_controls_all_node:
                                                            self.container_string_node = _.controls[0].content
                                                            self.contents__string_node = self.container_string_node.content

                                                            # self.all_data_list.append(f"⫹ 6 ⫺                        {self.container_string_node._get_control_name()}")
                                                            self.all_data_list.append(f"⫹ 🯶 ⫺ █░░▐  ▐  ▐  ▐  ▐  ▐━ {self.contents__string_node._get_control_name()}")

                                                            if self.contents__string_node._get_control_name() in list_controls:
                                                                """ IF TRUE GET ALL CONTROLS"""
                                                                tmp_controls_all_node = self.contents__string_node.controls

                                                                for _ in tmp_controls_all_node:
                                                                    self.container_string_node = _.controls[0].content
                                                                    self.contents__string_node = self.container_string_node.content

                                                                    # self.all_data_list.append(f"⫹ 7 ⫺                            {self.container_string_node._get_control_name()}")
                                                                    self.all_data_list.append(f"⫹ 🯷 ⫺ █░░▐  ▐  ▐  ▐  ▐  ▐  ▐━ {self.contents__string_node._get_control_name()}")

                                                                    if self.contents__string_node._get_control_name() in list_controls:
                                                                        """ IF TRUE GET ALL CONTROLS"""
                                                                        tmp_controls_all_node = self.contents__string_node.controls

                                                                        for _ in tmp_controls_all_node:
                                                                            self.container_string_node = _.controls[0].content
                                                                            self.contents__string_node = self.container_string_node.content

                                                                            # self.all_data_list.append(f"⫹ 8 ⫺                                {self.container_string_node._get_control_name()}")
                                                                            self.all_data_list.append(f"⫹ 🯸 ⫺ █░░▐  ▐  ▐  ▐  ▐  ▐  ▐  ▐━ {self.contents__string_node._get_control_name()}")

                                                                            if self.contents__string_node._get_control_name() in list_controls:
                                                                                """ IF TRUE GET ALL CONTROLS"""
                                                                                tmp_controls_all_node = self.contents__string_node.controls

                                                                                for _ in tmp_controls_all_node:
                                                                                    self.container_string_node = _.controls[0].content
                                                                                    self.contents__string_node = self.container_string_node.content

                                                                                    # self.all_data_list.append(f"⫹ 9 ⫺                                    {self.container_string_node._get_control_name()}")
                                                                                    self.all_data_list.append(f"⫹ 🯹 ⫺ █░░▐  ▐  ▐  ▐  ▐  ▐  ▐  ▐  ▐━ {self.contents__string_node._get_control_name()}")

                                                                                    if self.contents__string_node._get_control_name() in list_controls:
                                                                                        """ IF TRUE GET ALL CONTROLS"""
                                                                                        tmp_controls_all_node = self.contents__string_node.controls

                                                                                        for _ in tmp_controls_all_node:
                                                                                            self.container_string_node = _.controls[0].content
                                                                                            self.contents__string_node = self.container_string_node.content

                                                                                            # self.all_data_list.append(f"⫹ 1 ⫺0                                        {self.container_string_node._get_control_name()}")
                                                                                            self.all_data_list.append(f"⫹🯱🯰 ⫺ █░░▐  ▐  ▐  ▐  ▐  ▐  ▐  ▐  ▐  └──{self.contents__string_node._get_control_name()}")

        ####################################################################################
        for _ in self.all_data_list:
            print(_)
        # print(self.all_data_list)

        # return self.all_data_list

class HandlerDraggBox(ft.UserControl):
    # globalVar='Erase this test'

    def __init__(self,data='Erase this test'):
        super().__init__()
        # self.title='data'
        self.title=data

    def build(self):
        Drop_HandlerDraggBox=ft.Container(
                    ##################### PROPERTY
                    ##################### [rotate,offset] , [scale,aspect_ratio] , [visible,disabled]
                    # expand=True,
                    ink=False,                                                # click effect ripple
                    bgcolor= ft.colors.BLACK38,                                    # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                    padding= ft.padding.all(0),    # inside box                # padding.only(left=8, top=8, right=8, bottom=8),
                    margin = ft.margin.all(0),    #outside box                # margin.only (left=8, top=8, right=8, bottom=8),
                    alignment=ft.alignment.center,                            # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right.    posicionamiento adentro widget
                    border_radius= ft.border_radius.all(30),            # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                    # border=ft.border.all(2, ft.colors.BLACK),             # ft.border.only(Left=8, top=8, right=8, bottom=8),
                    # ===================
                    # image_src = f"/home/mjay/Pictures/3d_neon_pink-2560x1440.jpg",
                    # image_opacity=0.1,
                    # image_fit='COVER',                                            # CONTAIN, COVER, FILL, FIT_HEIGHT, FIT_WIDTH, SCALE_DOWN
                    # ===================
                    # width=150,
                    height=20,
                    # tooltip='Container',
                    ##################### EFFECTS
                    # gradient=ft.LinearGradient( begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=[ft.colors.BLUE, ft.colors.YELLOW],),
                    # gradient=ft.RadialGradient( colors=[ft.colors.YELLOW, ft.colors.BLUE],),
                    ##################### WIDGETS
                    content=ft.Row(
                                    ##################### PROPERTY BOX
                                    # expand=True,
                                    alignment=ft.MainAxisAlignment.CENTER,              # horizontal <=> START,CENTER,END SPACE_BETWEEN SPACE_AROUND SPACE_EVENLY
                                    vertical_alignment=ft.CrossAxisAlignment.CENTER,          # vertical       START,CENTER END
                                    ##################### LET MAKE SCROLL IN LONG QUANTITY
                                    # scroll=True,                                              # center widget
                                    # tight=True,
                                    ##################### ADAPT TO SCREEN
                                    # wrap=True,                                                  # justify in all screen
                                    # spacing=8,                                                # space widget left right
                                    # run_spacing=8,                                            # space widget up down
                                    ##################### WIDGETS
                                    controls=[
                                                ft.TextButton("press row",tooltip='buttom',on_click=lambda _:self.show_tree_nodes(_)),
                                                ft.TextButton("press row",tooltip='buttom',on_click=lambda _:self.show_tree_nodes(_)),
                                                ft.TextButton("press row",tooltip='buttom',on_click=lambda _:self.show_tree_nodes(_)),
                                                ft.Container(width=40),

                                             ],),
                    ##################### EVENTS
                    # on_click=lambda _:self.all_data_list.append(_),                            # on_hover=self.all_data_list.append('on click over'), on_long_press=self.all_data_list.append('long press'),
        )#<=== NOTE COMA
        return Drop_HandlerDraggBox

    def show_tree_nodes(self,e):

        WrapWidgetNode( )
######## HandlerDraggBox = HandlerDraggBox(),# <======= Comma

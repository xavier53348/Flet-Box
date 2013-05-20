
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
        #: self.container_string_node = self.main_node
        #: self.contents__string_node = self.container_string_node.content
        #: self.all_data_list.append(f"⫹ 0 ⫺ {self.container_string_node._get_control_name()}")
        #: self.all_data_list.append(f"⫹ 0 ⫺ {self.contents__string_node._get_control_name()}")

        self.all_data_list = []

        for _ in self.all_widgets:
            self.main_node = self.all_widgets.get(_)
            self.container_string_node = self.main_node
            self.contents__string_node = self.container_string_node.content

            #: self.all_data_list.append(f"⫹ 0 ⫺ {self.container_string_node._get_control_name()}")
            self.all_data_list.append(f"⫹ 🯰 ⫺ █━ {self.contents__string_node._get_control_name()}")

            if self.contents__string_node._get_control_name() in list_controls:
                """ IF IT'S TRUE GET ALL CONTROLS"""
                tmp_controls_all_node = self.contents__string_node.controls

                for _ in tmp_controls_all_node:
                    self.container_string_node = _.controls[0].content
                    self.contents__string_node = self.container_string_node.content

                    #: self.all_data_list.append(f"⫹ 1 ⫺    {self.container_string_node._get_control_name()}")
                    self.all_data_list.append(f"⫹ 🯱 ⫺ █░░▐━ {self.contents__string_node._get_control_name()}")

                    if self.contents__string_node._get_control_name() in list_controls:
                        """ IF TRUE GET ALL CONTROLS"""
                        tmp_controls_all_node = self.contents__string_node.controls

                        for _ in tmp_controls_all_node:
                            self.container_string_node = _.controls[0].content
                            self.contents__string_node = self.container_string_node.content

                            #: self.all_data_list.append(f"⫹ 2 ⫺        {self.container_string_node._get_control_name()}")
                            self.all_data_list.append(f"⫹ 🯲 ⫺ █░░▐  ▐━ {self.contents__string_node._get_control_name()}")

                            if self.contents__string_node._get_control_name() in list_controls:
                                """ IF TRUE GET ALL CONTROLS"""
                                tmp_controls_all_node = self.contents__string_node.controls

                                for _ in tmp_controls_all_node:
                                    self.container_string_node = _.controls[0].content
                                    self.contents__string_node = self.container_string_node.content

                                    #: self.all_data_list.append(f"⫹ 3 ⫺            {self.container_string_node._get_control_name()}")
                                    self.all_data_list.append(f"⫹ 🯳 ⫺ █░░▐  ▐  ▐━ {self.contents__string_node._get_control_name()}")

                                    if self.contents__string_node._get_control_name() in list_controls:
                                        """ IF TRUE GET ALL CONTROLS"""
                                        tmp_controls_all_node = self.contents__string_node.controls

                                        for _ in tmp_controls_all_node:
                                            self.container_string_node = _.controls[0].content
                                            self.contents__string_node = self.container_string_node.content

                                            #: self.all_data_list.append(f"⫹ 4 ⫺                {self.container_string_node._get_control_name()}")
                                            self.all_data_list.append(f"⫹ 🯴 ⫺ █░░▐  ▐  ▐  ▐━ {self.contents__string_node._get_control_name()}")

                                            if self.contents__string_node._get_control_name() in list_controls:
                                                """ IF TRUE GET ALL CONTROLS"""
                                                tmp_controls_all_node = self.contents__string_node.controls

                                                for _ in tmp_controls_all_node:
                                                    self.container_string_node = _.controls[0].content
                                                    self.contents__string_node = self.container_string_node.content

                                                    #: self.all_data_list.append(f"⫹ 5 ⫺                    {self.container_string_node._get_control_name()}")
                                                    self.all_data_list.append(f"⫹ 🯵 ⫺ █░░▐  ▐  ▐  ▐  ▐━ {self.contents__string_node._get_control_name()}")

                                                    if self.contents__string_node._get_control_name() in list_controls:
                                                        """ IF TRUE GET ALL CONTROLS"""
                                                        tmp_controls_all_node = self.contents__string_node.controls

                                                        for _ in tmp_controls_all_node:
                                                            self.container_string_node = _.controls[0].content
                                                            self.contents__string_node = self.container_string_node.content

                                                            #: self.all_data_list.append(f"⫹ 6 ⫺                        {self.container_string_node._get_control_name()}")
                                                            self.all_data_list.append(f"⫹ 🯶 ⫺ █░░▐  ▐  ▐  ▐  ▐  ▐━ {self.contents__string_node._get_control_name()}")

                                                            if self.contents__string_node._get_control_name() in list_controls:
                                                                """ IF TRUE GET ALL CONTROLS"""
                                                                tmp_controls_all_node = self.contents__string_node.controls

                                                                for _ in tmp_controls_all_node:
                                                                    self.container_string_node = _.controls[0].content
                                                                    self.contents__string_node = self.container_string_node.content

                                                                    #: self.all_data_list.append(f"⫹ 7 ⫺                            {self.container_string_node._get_control_name()}")
                                                                    self.all_data_list.append(f"⫹ 🯷 ⫺ █░░▐  ▐  ▐  ▐  ▐  ▐  ▐━ {self.contents__string_node._get_control_name()}")

                                                                    if self.contents__string_node._get_control_name() in list_controls:
                                                                        """ IF TRUE GET ALL CONTROLS"""
                                                                        tmp_controls_all_node = self.contents__string_node.controls

                                                                        for _ in tmp_controls_all_node:
                                                                            self.container_string_node = _.controls[0].content
                                                                            self.contents__string_node = self.container_string_node.content

                                                                            #: self.all_data_list.append(f"⫹ 8 ⫺                                {self.container_string_node._get_control_name()}")
                                                                            self.all_data_list.append(f"⫹ 🯸 ⫺ █░░▐  ▐  ▐  ▐  ▐  ▐  ▐  ▐━ {self.contents__string_node._get_control_name()}")

                                                                            if self.contents__string_node._get_control_name() in list_controls:
                                                                                """ IF TRUE GET ALL CONTROLS"""
                                                                                tmp_controls_all_node = self.contents__string_node.controls

                                                                                for _ in tmp_controls_all_node:
                                                                                    self.container_string_node = _.controls[0].content
                                                                                    self.contents__string_node = self.container_string_node.content

                                                                                    #: self.all_data_list.append(f"⫹ 9 ⫺                                    {self.container_string_node._get_control_name()}")
                                                                                    self.all_data_list.append(f"⫹ 🯹 ⫺ █░░▐  ▐  ▐  ▐  ▐  ▐  ▐  ▐  ▐━ {self.contents__string_node._get_control_name()}")

                                                                                    if self.contents__string_node._get_control_name() in list_controls:
                                                                                        """ IF TRUE GET ALL CONTROLS"""
                                                                                        tmp_controls_all_node = self.contents__string_node.controls

                                                                                        for _ in tmp_controls_all_node:
                                                                                            self.container_string_node = _.controls[0].content
                                                                                            self.contents__string_node = self.container_string_node.content

                                                                                            #: self.all_data_list.append(f"⫹ 1 ⫺0                                        {self.container_string_node._get_control_name()}")
                                                                                            self.all_data_list.append(f"⫹🯱🯰 ⫺ █░░▐  ▐  ▐  ▐  ▐  ▐  ▐  ▐  ▐  └──{self.contents__string_node._get_control_name()}")


        for _ in self.all_data_list:
            print(_)
        #: print(self.all_data_list)
        #: return self.all_data_list

class HandlerDraggBox(ft.UserControl):
    def __init__(self,data='Erase this test'):
        super().__init__()
        self.title=data

    def build(self):
        Drop_HandlerDraggBox=ft.Container(

                    ink=False,
                    bgcolor= ft.colors.BLACK38,
                    padding= ft.padding.all(0),
                    margin = ft.margin.all(0),    #outside box
                    alignment=ft.alignment.center,
                    border_radius= ft.border_radius.all(30),
                    height=20,
                    content=ft.Row(
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                    controls=[
                                                ft.TextButton("press row",tooltip='buttom',on_click=lambda _:self.show_tree_nodes(_)),
                                                ft.TextButton("press row",tooltip='buttom',on_click=lambda _:self.show_tree_nodes(_)),
                                                ft.TextButton("press row",tooltip='buttom',on_click=lambda _:self.show_tree_nodes(_)),
                                                ft.Container(width=40),

                                             ],),
        )#<=== NOTE COMA
        return Drop_HandlerDraggBox

    def show_tree_nodes(self,e):
        WrapWidgetNode()

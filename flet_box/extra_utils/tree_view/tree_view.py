from ..settings_var.save_export import WrapWidgetNode
from extra_utils.settings_var.settings_widget import GLOBAL_VAR

import flet as ft
visible = False

class TreeView(ft.Stack):

    def __init__(self,tree_view='  CLICK OVER TO UPDATE TREEVIEW'):
        super().__init__()

        self.tree_view = tree_view
        self.data_view = WrapWidgetNode()

    def build(self):
        global Drop_TreeView
        Drop_TreeView=ft.Container(
                                visible       = False,
                                ink           = False,
                                bgcolor       = ft.colors.BLACK38,
                                padding       = ft.padding.only(left=8, top=24, right=8, bottom=24),
                                margin        = ft.margin.only(left=0, top=16, right=8, bottom=16),
                                alignment     = ft.alignment.center,
                                border_radius = ft.border_radius.all(30),
                                border        = ft.border.all(2, ft.colors.BLACK),
                                width=250,
                                on_click=lambda _:self.update_data(widget = self.data_view),
                            content = ft.Column(
                                                scroll="HIDDEN",
                                                controls = [
                                                            ft.Text(
                                                                    value=f"{self.tree_view}",
                                                                    size=18,
                                                                    text_align        = ft.TextAlign.CENTER,
                                                                    font_family     = "Consolas", #"Consolas ,RobotoSlab
                                                            )],),
                        )

        return Drop_TreeView

    def update_data(self,widget):

        #: INPUT DATA IN TREEVIEW
        Drop_TreeView.alignment = ft.alignment.top_left
        Drop_TreeView.update()

        # current_screen = GLOBAL_VAR(get_global_var='SELECTED_SCREEN').uid

        # data_phone = GLOBAL_VAR(get_global_var='EXPORT_DATA_PHONE').get(current_screen)
        # tree_view_data = widget.show_tree_nodews(widget_show=data_phone)

        # tree_view_data = widget.show_tree_nodews(widget_show=GLOBAL_VAR(get_global_var='EXPORT_DATA_PHONE'))
        # print(GLOBAL_VAR(get_global_var='EXPORT_DATA_PHONE'),'EXPORT_DATA_PHONE')

        # ========================================================================================
        #: CREATE NEW SCREEN IN ALL SCREENS DICT VERY IMPORTATN CONTAIN ALL SCREENS IN
        current_screen_id = GLOBAL_VAR(get_global_var ='SELECTED_SCREEN').uid
        data_to_treview   = GLOBAL_VAR(get_global_var ='ALL_SCREEN_IN_DICT').get(current_screen_id)
        if not data_to_treview: data_to_treview = dict()
        tree_view_data    = widget.show_tree_nodews(widget_show = data_to_treview)
        # ========================================================================================

        Drop_TreeView.content.controls[0].value      = tree_view_data
        Drop_TreeView.content.controls[0].size       = 11
        Drop_TreeView.content.controls[0].text_align = ft.TextAlign.LEFT
        Drop_TreeView.content.update()

        # print(GLOBAL_VAR(get_global_var='ALL_SCREEN_IN_DICT'),'ALL SCREENS')

    def visible_view():

        global visible
        visible = True if not visible else False
        Drop_TreeView.visible=visible
        Drop_TreeView.update()

if __name__ == '__main__':

    def main(page: ft.Page):

        page.scroll               = "HIDDEN" #AUTO ADAPTIVE ALWAYS HIDDEN
        page.vertical_alignment   = ft.MainAxisAlignment.CENTER
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        page.theme_mode           = ft.ThemeMode.DARK         #ft.ThemeMode.LIGHT
        page.window_bgcolor       = ft.colors.RED_100
        page.window_left          = 3
        page.window_top           = 3
        page.window_height        = 800
        page.window_width         = 400
        page.padding              = 0
        page.spacing              = 0

        page.add(TreeView())
    ft.app(target=main)
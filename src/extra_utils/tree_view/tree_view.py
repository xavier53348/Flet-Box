####################################################
from ..settings_var.save_export import WrapWidgetNode
###################### CALL GLOBAL VAR #############
from extra_utils.settings_var.settings_widget import GLOBAL_VAR
####################################################
import flet as ft
####################################################

visible = False

class TreeView(ft.UserControl):
    # globalVar='Erase this test'

    def __init__(self,tree_view='  CLICK OVER TO UPDATE TREEVIEW'):
        super().__init__()
        self.tree_view = tree_view

        self.data_view = WrapWidgetNode()

    def build(self):
        global Drop_TreeView
        Drop_TreeView=ft.Container(
                                ##################### PROPERTY ROW
                                ##################### [rotate,offset] , [scale,aspect_ratio] , [visible,disabled]
                                # expand=True,
                                visible       = False,
                                ink           = False,                                         # click effect ripple
                                bgcolor       = ft.colors.BLACK38,                             # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                                padding       = ft.padding.only(left=8, top=24, right=8, bottom=24),    # inside box             # padding.only(left=8, top=8, right=8, bottom=8),
                                margin        = ft.margin.only(left=0, top=16, right=8, bottom=16),     # outside box            # margin.only (left=8, top=8, right=8, bottom=8),
                                alignment     = ft.alignment.center,                           # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right.    posicionamiento adentro widget
                                border_radius = ft.border_radius.all(30),                      # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                                border        = ft.border.all(2, ft.colors.BLACK),             # ft.border.only(Left=8, top=8, right=8, bottom=8),
                                # ===================
                                # image_src = f"/home/mjay/Pictures/3d_neon_pink-2560x1440.jpg",
                                # image_opacity=0.1,
                                # image_fit='COVER',                                            # CONTAIN, COVER, FILL, FIT_HEIGHT, FIT_WIDTH, SCALE_DOWN
                                # ===================
                                width=250,
                                # height=150,
                                # tooltip='Container',
                                on_click=lambda _:self.update_data(widget = self.data_view),
                                ############################
                            content = ft.Column(
                                                scroll="HIDDEN",
                                                controls = [
                                                            ft.Text(
                                                                    # bgcolor='red',
                                                                    value=f"{self.tree_view}",
                                                                    size=18,
                                                                    text_align        = ft.TextAlign.CENTER,                                    # LEFT (default),RIGHT,CENTER,JUSTIFY,START,END
                                                                    ##################### PROPERTY
                                                                    # weight          = ft.FontWeight.BOLD,                                    # NORMAL (default), BOLD, W_100, W_200,  W_300, W_400, W_500, W_600, W_700, W_800,W_900
                                                                    # italic          = True,
                                                                    font_family     = "Consolas", #"Consolas ,RobotoSlab
                                                                    ##################### COLOR
                                                                    # style           = ft.TextThemeStyle.HEADLINE_SMALL,
                                                            )],),
                        )
        return Drop_TreeView

######## TreeView = TreeView(),# <======= Comma
    def update_data(self,widget):

        # INPUT DATA IN TREEVIEW
        Drop_TreeView.alignment = ft.alignment.top_left
        Drop_TreeView.update()
        tree_view_data = widget.show_tree_nodews(widget_show=GLOBAL_VAR(get_global_var='EXPORT_DATA_PHONE'))
        Drop_TreeView.content.controls[0].value      = tree_view_data
        Drop_TreeView.content.controls[0].size       = 11
        Drop_TreeView.content.controls[0].text_align = ft.TextAlign.LEFT
        Drop_TreeView.content.update()

    def visible_view():
        global visible
        visible = True if not visible else False
        Drop_TreeView.visible=visible
        Drop_TreeView.update()

if __name__ == '__main__':
    def main(page: ft.Page):
        ######################
        page.scroll                    = "HIDDEN" #AUTO ADAPTIVE ALWAYS HIDDEN
        page.vertical_alignment        = ft.MainAxisAlignment.CENTER
        page.horizontal_alignment      = ft.CrossAxisAlignment.CENTER
        ######################  COLOR
        page.theme_mode                = ft.ThemeMode.DARK         #ft.ThemeMode.LIGHT
        page.window_bgcolor            = ft.colors.RED_100
        ###################### POSITION OF SC
        page.window_left               = 3
        page.window_top                = 3
        page.window_height             = 800
        page.window_width              = 400
        page.padding                   = 0
        page.spacing                   = 0
        page.add(TreeView())
        ######################
    ft.app(target=main)
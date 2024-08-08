from ..settings_var.settings_widget import GLOBAL_VAR

from ..settings_var.save_export import WrapWidgetNode
from ..tree_view.tree_view import TreeView

import flet as ft

class MenuLeftContainer(ft.Stack):

     def __init__(self,main_page='Erase this test'):
          super().__init__()

          self.main_page     = main_page
          self.icon_browser  = GLOBAL_VAR(get_global_var='ICON_BROWSER_CONTAINER')
          self.color_browser = GLOBAL_VAR(get_global_var='COLOR_BROWSER_CONTAINER')
          self.gpt_browser   = GLOBAL_VAR(get_global_var='GPT_BROWSER_CONTAINER')
          self.text_editor   = GLOBAL_VAR(get_global_var='TEXT_EDITOR_CONTAINER')

          self.data_view = WrapWidgetNode()

     def build(self):

          Drop_MenuLeftContainer =  ft.Container(

                                             expand          = True,
                                             ink             = False,
                                             bgcolor         = ft.colors.BLACK38,
                                             padding         = ft.padding.only(left=0, top=8, right=0, bottom=8),
                                             margin          = ft.margin.all(0),
                                             alignment       = ft.alignment.center,
                                             width           = 60,
                                             gradient        = ft.LinearGradient( begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=[ft.colors.BLACK12,ft.colors.CYAN, ft.colors.BLACK12],),

                                        content=ft.Column(
                                                            horizontal_alignment = ft.CrossAxisAlignment.CENTER,
                                                            controls =[
                                                                        ft.IconButton(icon=ft.icons.SUPERVISED_USER_CIRCLE),

                                                                        ft.Container(
                                                                                    expand    = True,
                                                                                    ink       = False,
                                                                                    padding   = ft.padding.all(0),
                                                                                    margin    = ft.margin.all(0),
                                                                                    alignment = ft.alignment.center,
                                                                                    content=ft.Column(
                                                                                        alignment            = ft.MainAxisAlignment.CENTER,
                                                                                        horizontal_alignment = ft.CrossAxisAlignment.CENTER,
                                                                                        spacing              = 8,
                                                                                        controls=[
                                                                                                    ft.Container(alignment=ft.alignment.center,tooltip='ICONS',content=ft.IconButton(icon=ft.icons.ADD_REACTION_OUTLINED , on_click=lambda _:self.show_widgets(show_widget='icon_browser')),
                                                                                                        bgcolor       = ft.colors.BLACK45,
                                                                                                        height        = 45,
                                                                                                        width         = 45,
                                                                                                        border_radius = ft.border_radius.all(16)
                                                                                                        ),
                                                                                                    ft.Container(alignment=ft.alignment.center,tooltip='COLORS',content=ft.IconButton(icon=ft.icons.COLOR_LENS_OUTLINED , on_click=lambda _:self.show_widgets(show_widget='color_browser')),
                                                                                                        bgcolor       = ft.colors.BLACK45,
                                                                                                        height        = 45,
                                                                                                        width         = 45,
                                                                                                        border_radius = ft.border_radius.all(16)
                                                                                                        ),
                                                                                                    ft.Container(alignment=ft.alignment.center,tooltip='CODE'     ,content=ft.IconButton(icon=ft.icons.CODE_ROUNDED , on_click=lambda _:self.show_widgets(show_widget='text_editor')),
                                                                                                        bgcolor       = ft.colors.BLACK45,
                                                                                                        height        = 45,
                                                                                                        width         = 45,
                                                                                                        border_radius = ft.border_radius.all(16)
                                                                                                        ),
                                                                                                    ft.Container(alignment=ft.alignment.center,tooltip='TREE'     ,content=ft.IconButton(icon=ft.icons.ACCOUNT_TREE_ROUNDED , on_click=lambda _:self.show_widgets(show_widget='tree_view')),
                                                                                                        bgcolor       = ft.colors.BLACK45,
                                                                                                        height        = 45,
                                                                                                        width         = 45,
                                                                                                        border_radius = ft.border_radius.all(16)
                                                                                                        ),
                                                                                                    ft.Container(alignment=ft.alignment.center,tooltip='GIT-HUB'  ,content=ft.IconButton(icon=ft.icons.DEVELOPER_MODE , on_click=lambda _:self.on_developing('Git-Hub')),
                                                                                                        bgcolor       = ft.colors.BLACK45,
                                                                                                        height        = 45,
                                                                                                        width         = 45,
                                                                                                        border_radius = ft.border_radius.all(16)
                                                                                                        ),
                                                                                                    ft.Container(alignment=ft.alignment.center,tooltip='CHAT-GPT' ,content=ft.IconButton(icon=ft.icons.DATA_OBJECT_OUTLINED ,  on_click=lambda _:self.show_widgets(show_widget='gpt_browser')),
                                                                                                        bgcolor       = ft.colors.BLACK45,
                                                                                                        height        = 45,
                                                                                                        width         = 45,
                                                                                                        border_radius = ft.border_radius.all(16)
                                                                                                        ),
                                                                                                 ],
                                                                                    ),
                                                                        ),
                                                                        ft.IconButton(icon=ft.icons.SETTINGS),
                                                                     ],),
                                        )
          return Drop_MenuLeftContainer

     def show_widgets(self,show_widget):

          if show_widget == "icon_browser":
               self.icon_browser.visible  = True if not self.icon_browser.visible else False
               self.icon_browser.update()

          if show_widget == "color_browser":
               self.color_browser.visible  = True if not self.color_browser.visible else False
               self.color_browser.update()

          if show_widget == "gpt_browser":
               self.gpt_browser.visible  = True if not self.gpt_browser.visible else False
               self.gpt_browser.update()

          if show_widget == "tree_view":
               #: THIS METOD visible_view() WILL return
               #: INPUT DATA IN TREEVIEW
               #: tree_view_data = self.data_view.show_tree_nodews(widget_show=GLOBAL_VAR(get_global_var='EXPORT_DATA_PHONE'))
               #: TreeView.update_data(data=tree_view_data)
               TreeView.visible_view()

          if show_widget == "text_editor":
            self.text_editor.visible = True if not self.text_editor.visible else False
            self.text_editor.update()

     def on_developing(self,name_seccion):

          page = GLOBAL_VAR(get_global_var='PAGE')

          self.data = f"""
          Hello, User!

          {name_seccion.upper()}: is not aviable yet, please keep calm will be soon...
          thanks very much
          """
          dlg = ft.AlertDialog(
                              title=ft.Text(self.data,size=15), on_dismiss=lambda e: print("Dialog dismissed!")
                              )
          page.dialog = dlg
          dlg.open = True
          page.update()

     def action_windows(self,action):

          if action == 'Close':
            self.main_page.window_close()

          elif action == 'Minimize':
            self.main_page.window_minimized = True

          elif action == 'Resize':
            self.main_page.window_maximizable =True
          self.main_page.update()

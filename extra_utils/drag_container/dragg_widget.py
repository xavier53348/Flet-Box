from extra_utils.settings_var.settings_widget import global_var
import flet as ft

class DraggWidget(ft.UserControl): # <======= dragg widget
     """
     NOTE:

     1. ONLY FUNCTION IS TAKE DRAGGABLE WIDGET AND TRASLATE TO DRAGGABLE_PHONE
     2. SET IN VARIABLE GLOBAL THE SELECTED DRAGGABLE WIDGET
     3. CLEAN THE LIST listWidgetUpdate
     """
     def __init__(self,data='Erase this test',color='BLACK',icons='/icons/icon-512.png'):
          super().__init__()
          # self.title='data'
          self.widget    = data
          self.takeClick = False
          self.myColor   = color
          self.icons     = icons

     def build(self):

          self.DropTakeDragg=ft.Draggable(
                                   ################# FRON CONTAINER
                                   group   = "GroupDragg",
                                   content = ft.Container(
                                                       width=80,
                                                       height=80,
                                                       bgcolor=self.myColor,
                                                       border_radius=13,
                                                       # image_src=f"{self.icons}",
                                                       tooltip=self.widget,
                                                       border=ft.border.all(0.5, "#131926"),                     # ft.border.only(Left=8, top=8, right=8, bottom=8),
                                                       gradient=ft.LinearGradient( begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=[ "#0d0e0e",'#08142c'], ),
                                                  on_click=lambda _: self.SelectedWidget(self.widget), # on_hover=lambda _: print('on_hover'),   # on_long_press=lambda _: print('on_long_press'),
                                                  content= ft.Icon(name=self.icons, color=ft.colors.BLUE, size=50),
                                   ),
                                   ################# BACK CONTAINER
                                   content_when_dragging=ft.Container(
                                                       padding=2,
                                                       width=80,
                                                       height=80,
                                                       bgcolor='#131926',   # ft.colors.BLACK,
                                                       border_radius=13,
                                                    # content=ft.Text("Back"),
                                   ),
                                   ################# TRASLATE CONTAINER
                                   content_feedback=ft.Container(
                                                       alignment=ft.alignment.bottom_center,
                                                       width=70,
                                                       height=70,
                                                       bgcolor=self.myColor,
                                                       border_radius=13,
                                                       # image_src=f"{self.icons}",
                                                    # content=ft.Text("Drop",size=12),
                                                    content = ft.Container(alignment=ft.alignment.center,content = ft.Icon(name=self.icons, color=ft.colors.BLUE, size=25)),
                                   ),
          )# <======= coma
          return self.DropTakeDragg

     def SelectedWidget(self,data):
          """
          NOTE:

          1. SET IN GLOBAL VAR THE SELECTED WIDGET
          2. RESET THE LIST listWidgetUpdate

          """
          widget_selected = global_var(data_global={
                                                  'selectWidgetBox':data,
                                                  'listWidgetUpdate':[],
                                                   })
          print(data)

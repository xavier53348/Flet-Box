from extra_utils.settings_var.settings_widget import global_var, get_global_var
from extra_utils.drag_container.infinity_box_layer_one import InfinityBoxLayerOne

import flet as ft

# selectWidgetBox = get_global_var(get_var='selectWidgetBox')

class DropDragg(ft.UserControl):
     """
     ONLY FUNCTION IS ADD TO PHONE_SCREEN A DRAGABLE WIDGET THAT WILL BE A DRAGABLE_LOOP
     """

     def __init__(self,data='Erase this test'):
          super().__init__()
          # self.title='data'
          self.title=data

     def build(self):
          self.DropDragg=ft.Container(
                                        ##################### PROPERTY ROW
                                        ink           = False,                                                 # click effect ripple
                                        padding       = ft.padding.only(left=0, top=0, right=0, bottom=0),     # inside box                        # padding.only(left=8, top=8, right=8, bottom=8),
                                        margin        = ft.margin.all(0),  # outside box                       # margin.only (left=8, top=8, right=8, bottom=8),
                                        alignment     = ft.alignment.center,                                   # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right
                                        border_radius = ft.border_radius.all(36),                              # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                                        border        = ft.border.all(6, ft.colors.BLACK),                     # ft.border.only(Left=8, top=8, right=8, bottom=8),
                                        width         = 260,
                                        height        = 525,
                                        bgcolor       = '#070707',
                                        ##################### EFFECTS
                                        # gradient      = ft.LinearGradient( begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=[ft.colors.TEAL, ft.colors.BLACK45],),
                                        ##################### WIDGETS
                                   content = ft.DragTarget(
                                                       ######################################
                                                       ################# Traslate Container
                                                       group   = "GroupDragg",
                                                       content = ft.Container(
                                                                      border_radius = ft.border_radius.all(30),# ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                                                                      padding       = 0,
                                                                      margin        = -0.3,
                                                                      alignment     = ft.alignment.center,     # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right.    posicionamiento adentro widget
                                                                      #################
                                                                 content = ft.Column(
                                                                                scroll   = 'HIDDEN',
                                                                                spacing  = 2,
                                                                                controls = [
                                                                                           # ft.ElevatedButton(),
                                                                                           ],
                                                                           ),# <=== Row(),Stack(),Grid() # BoxWidget to drop inside
                                                                 #################  EVENTS Container
                                                                 # on_click      = lambda _:print(_),
                                                                 # on_hover      = print('on click over'),
                                                                 # on_long_press = print('long press'),
                                                                 ##################################
                                                            ),
                                                       ################# EVENTS  DragTarget
                                                       on_will_accept = self.drag_will_accept,           # Traslate Drop
                                                       on_leave       = self.drag_leave,                 # Leafing Drop Line Border
                                                       on_accept      = lambda _:self.drag_accept(_),    # Accept Drop
                                                    ##################################
                                        ),#<========comma # DragTarget.content.controls.append() # DragTarget.content.controls.remove()

                                        # on_hover=lambda _: print(_.control.uid),
                                        # self.DropDragg.controls.update()
                                        # self.controls
                                        )
          # print(self.DropDragg._remove_control_recursively)
          return self.DropDragg

     def drag_accept(self,widgetDropBox):
          self.InfinityBox = InfinityBoxLayerOne
          self.page        = get_global_var(get_var='page')
          selectWidgetBox  = get_global_var(get_var='selectWidgetBox')

          ######################### filter if drag make fake cat no add WIDGET
          destiny_box = self.page.get_control(self.DropDragg.uid)
          # print(f'destiny_box: {destiny_box.uid} <<<<<<')
          if selectWidgetBox:
               # destiny_box.content.content.content.controls.append(self.InfinityBox(selectWidgetBox))
               self.DropDragg.content.content.content.controls.append(self.InfinityBox(selectWidgetBox))

          ########################## border
          widgetDropBox.control.content.border = True
          widgetDropBox.control.content.border=ft.border.all(2, ft.colors.BLACK)
          widgetDropBox.control.update()

     def drag_will_accept(self,widgetDropBox):
          widgetDropBox.control.content.border = None
          widgetDropBox.control.content.border=ft.border.all(2, ft.colors.RED)
          widgetDropBox.control.update()

     def drag_leave(self,widgetDropBox):
          widgetDropBox.control.content.border = True
          widgetDropBox.control.content.border=ft.border.all(2, ft.colors.BLACK)
          widgetDropBox.control.update()
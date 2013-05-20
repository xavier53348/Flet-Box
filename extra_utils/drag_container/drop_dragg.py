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
                                        # expand=True,
                                        ink=False,                                                      # click effect ripple
                                        bgcolor="#e2e7f2",                                              # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                                        padding= ft.padding.only(left=0, top=28, right=0, bottom=0), # inside box                        # padding.only(left=8, top=8, right=8, bottom=8),
                                        margin = ft.margin.all(0),  # outside box                       # margin.only (left=8, top=8, right=8, bottom=8),
                                        alignment=ft.alignment.center,                                  # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right
                                        border_radius= ft.border_radius.all(55),                      # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                                        border=ft.border.all(13, ft.colors.BLACK),                     # ft.border.only(Left=8, top=8, right=8, bottom=8),
                                        # image_src=f"/icons/icon-512.png",
                                        # image_fit="FILL",                                             # CONTAIN, COVER, FILL, FIT_HEIGHT, FIT_WIDTH, SCALE_DOWN
                                        # width=340,
                                        # height=150,
                                        # tooltip='Container',
                                        ##################### EFFECTS
                                        # blur=(4, 4),              # (Vertical,Horizontal)             # blur=ft.Blur(10, 0, ft.BlurTileMode.MIRROR)
                                        # gradient=ft.LinearGradient( begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=[ft.colors.BLUE, ft.colors.YELLOW],),
                                        # gradient=ft.RadialGradient( colors=[ft.colors.YELLOW, ft.colors.BLUE],),
                                        ##################### WIDGETS

                                   content=ft.DragTarget(
                                                    ######################################
                                                    ################# Traslate Container
                                                    group="GroupDragg",
                                                    content=ft.Container(
                                                                      # expand=True,
                                                                      # bgcolor="red",
                                                                      padding=0,
                                                                      margin=0,
                                                                      alignment=ft.alignment.center,                                  # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right.    posicionamiento adentro widget
                                                                      border_radius= ft.border_radius.only(top_left=0, top_right=0, bottom_left=45, bottom_right=45),
                                                                      # border=ft.border.all(2, ft.colors.BLACK),
                                                                      width=285,
                                                                      gradient=ft.LinearGradient( begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=[ ft.colors.CYAN,ft.colors.PURPLE,], ),
                                                                      # gradient=ft.LinearGradient( begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=[ft.colors.BLUE, ft.colors.YELLOW],),
                                                                      #################
                                                                 content=ft.Column(
                                                                                     scroll='ALWAYS',
                                                                                controls=[
                                                                                          # ft.ElevatedButton(),
                                                                                          ],
                                                                                ),# <=== Row(),Stack(),Grid() # BoxWidget to drop inside
                                                                 #################  EVENTS Container
                                                                 # on_click=     lambda _:print(_),
                                                                 # on_hover=     print('on click over'),
                                                                 # on_long_press=print('long press'),
                                                                 ##################################
                                                            ),
                                                    ################# EVENTS  DragTarget
                                                    on_will_accept=   self.drag_will_accept,           # Traslate Drop
                                                    on_leave=         self.drag_leave,                 # Leafing Drop Line Border
                                                    on_accept=        lambda _:self.drag_accept(_),                # Accept Drop
                                                    ##################################
                                        )#<========comma # DragTarget.content.controls.append() # DragTarget.content.controls.remove()
                                        # self.DropDragg.controls.update()
                                        # self.controls
                                        )

          return self.DropDragg

     def drag_accept(self,widgetDropBox):
          self.InfinityBox = InfinityBoxLayerOne
          self.page        = get_global_var(get_var='page')
          selectWidgetBox  = get_global_var(get_var='selectWidgetBox')

          ######################### filter if drag make fake cat no add WIDGET
          # destiny_box      = self.page.get_control(self.DropDragg.uid)
          # print(f'destiny_box: {destiny_box} <<<<<<')
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

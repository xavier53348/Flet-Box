from ..drag_container.dragg_widget import DraggWidget
from ..drag_container.infinity_box_layer_one import InfinityBoxLayerOne
from ..drag_container.drop_dragg import DropDragg
from ..settings_var.settings_widget import global_var, get_global_var

import flet as ft

selectWidgetBox = get_global_var('selectWidgetBox')

class Build_Phone_Editor(ft.UserControl):
     """Center Box that contain the phone to add Widget"""

     def __init__(self,group='GroupDragg',main_page='a'):
          super().__init__()
          self.group = group
          self.dropDragg= DropDragg()
          self.main_page = main_page
     def build(self):
          self.Drop_Build_Phone_Editor = ft.DragTarget(
                                             group='GroupDragg',

                                             content=ft.Container( ###################### PHONE CONTAINER
                                                            ##################### PROPERTY COLUMN
                                                            ink             = False,                                            # click effect ripple
                                                            bgcolor         = ft.colors.TEAL,                                   # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                                                            padding         = ft.padding.all(0),    # inside box                # padding.only(left=8, top=8, right=8, bottom=8),
                                                            margin          = ft.margin.all(0),    # outside box                # margin.only (left=8, top=8, right=8, bottom=8),
                                                            alignment       = ft.alignment.center,                              # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right.    posicionamiento adentro widget
                                                            border_radius   = ft.border_radius.all(30),                         # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                                                            border          = ft.border.all(4, ft.colors.BLACK),                # ft.border.only(Left=8, top=8, right=8, bottom=8),
                                                            #               ===================
                                                            # image_src     = f"splash.jpg",
                                                            # image_opacity = 0.1,
                                                            # image_fit     = 'COVER',                                          # CONTAIN, COVER, FILL, FIT_HEIGHT, FIT_WIDTH, SCALE_DOWN
                                                            #               ===================
                                                            width           = 260,
                                                            height          = 525,
                                                            # tooltip       = 'Container',
                                                            ##################### EFFECTS
                                                            # gradient      = ft.LinearGradient( begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=[ft.colors.CYAN, ft.colors.BLACK],),
                                                            # gradient      = ft.RadialGradient( colors=[ft.colors.YELLOW, ft.colors.BLUE],),
                                                            ##################### WIDGETS
                                                            content=ft.Column(
                                                                           ##################### PROPERTY BOX
                                                                           # expand=True,
                                                                           # alignment=ft.MainAxisAlignment.SPACE_AROUND,       # horizontal <=> START,CENTER,END SPACE_BETWEEN SPACE_AROUND SPACE_EVENLY
                                                                           horizontal_alignment = ft.CrossAxisAlignment.CENTER, # vertical       START,CENTER END
                                                                           controls=[
                                                                           ],
                                                                           ),#<=== NOTE COMA [NOTE]                     # for x in range(1,50): widget.content.controls.append(ft.ElevatedButton("press buttom",tooltip='buttom'))
                                                            ##################### EVENTS
                                                            # on_click=lambda _:print(_),                               # on_hover=print('on click over'), on_long_press=print('long press'),
                                                            ),#<=== NOTE COMA
                                             ##################### EVENTS
                                             on_will_accept = self.drag_will_accept,           # Traslate Drop
                                             on_leave       = self.drag_leave,                 # Leafing Drop Line Border
                                             on_accept      = lambda _:self.drag_accept(_),    # Accept Drop
                                                  )
          return self.Drop_Build_Phone_Editor

     def drag_accept(self,widgetDropBox):
          # global selectWidgetBox

          selectWidgetBox  = get_global_var(get_var = 'selectWidgetBox')
          self.InfinityBox = InfinityBoxLayerOne(dataPassed = selectWidgetBox)
          destiny_box      = self.page.get_control(self.dropDragg.uid)

          # print(f"selectWidgetBox: {selectWidgetBox}")
          # print(f"InfinityBox: {self.InfinityBox.build()}")
          # print(self.dropDragg)
          # ######################### filter if drag make fake cat no add WIDGET
          if selectWidgetBox:
               # self.select = self.widgets.get(selectWidgetBox)
               destiny_box.content.content.controls.append(self.InfinityBox(selectWidgetBox))
               selectWidgetBox = None         # get back natural state

          # ########################## border
          widgetDropBox.control.content.border  = True
          widgetDropBox.control.content.border  = ft.border.all(2, ft.colors.BLACK)
          # widgetDropBox.control.update()
          # ########################## reset
          # source_box.content_feedback.content = None            # reset widghet source original state
          # self.page.update()

     def drag_will_accept(self,widgetDropBox):
          # print('hello')
          # ource_box  = self.page.get_control(widgetDropBox.src_id)

          widgetDropBox.control.content.border = None
          widgetDropBox.control.content.border = ft.border.all(2, ft.colors.RED)
          widgetDropBox.control.update()
          self.page.update()

     def drag_leave(self,widgetDropBox):
          widgetDropBox.control.content.border = True
          widgetDropBox.control.content.border = ft.border.all(2, ft.colors.BLACK)
          widgetDropBox.control.update()
          self.page.update()
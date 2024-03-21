from extra_utils.drag_container.dragg_widget import DraggWidget
from extra_utils.drag_container.infinity_box_layer_one import InfinityBoxLayerOne
from extra_utils.drag_container.drop_dragg import DropDragg
from extra_utils.settings_var.settings_widget import global_var, get_global_var


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
                                                            ##################### [rotate,offset] , [scale,aspect_ratio] , [visible,disabled]
                                                            # expand=True,
                                                            ink=False,                                                      # click effect ripple
                                                            bgcolor=ft.colors.TEAL,                                              # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                                                            padding= ft.padding.all(0),    # inside box                        # padding.only(left=8, top=8, right=8, bottom=8),
                                                            margin = ft.margin.all(0),    # outside box                       # margin.only (left=8, top=8, right=8, bottom=8),
                                                            alignment=ft.alignment.center,                                  # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right.    posicionamiento adentro widget
                                                            border_radius= ft.border_radius.all(30),                      # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                                                            border=ft.border.all(4, ft.colors.BLACK),                     # ft.border.only(Left=8, top=8, right=8, bottom=8),
                                                            # ===================
                                                            # image_src = f"splash.jpg",
                                                            # image_opacity=0.1,
                                                            # image_fit='COVER',                                            # CONTAIN, COVER, FILL, FIT_HEIGHT, FIT_WIDTH, SCALE_DOWN
                                                            # ===================
                                                            width=260,
                                                            height=525,
                                                            # tooltip='Container',
                                                            ##################### EFFECTS
                                                            # gradient=ft.LinearGradient( begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=[ft.colors.CYAN, ft.colors.BLACK],),
                                                            # gradient=ft.RadialGradient( colors=[ft.colors.YELLOW, ft.colors.BLUE],),
                                                            ##################### WIDGETS
                                                            content=ft.Column(
                                                                           ##################### PROPERTY BOX
                                                                           # expand=True,
                                                                           # alignment=ft.MainAxisAlignment.SPACE_AROUND,              # horizontal <=> START,CENTER,END SPACE_BETWEEN SPACE_AROUND SPACE_EVENLY
                                                                           horizontal_alignment=ft.CrossAxisAlignment.CENTER,        # vertical       START,CENTER END
                                                                           controls=[
                                                                           ],
                                                                           ),#<=== NOTE COMA [NOTE]                     for x in range(1,50): widget.content.controls.append(ft.ElevatedButton("press buttom",tooltip='buttom'))
                                                            ##################### EVENTS
                                                            # on_click=lambda _:print(_),                            # on_hover=print('on click over'), on_long_press=print('long press'),
                                                            ),#<=== NOTE COMA
                                             on_will_accept = self.drag_will_accept,           # Traslate Drop
                                             on_leave       = self.drag_leave,                 # Leafing Drop Line Border
                                             on_accept      = lambda _:self.drag_accept(_),                # Accept Drop
                                                  )
          return self.Drop_Build_Phone_Editor

     def drag_accept(self,widgetDropBox):
          # global selectWidgetBox

          selectWidgetBox = get_global_var(get_var='selectWidgetBox')
          self.InfinityBox = InfinityBoxLayerOne(dataPassed=selectWidgetBox)
          destiny_box = self.page.get_control(self.dropDragg.uid)

          # print(f"selectWidgetBox: {selectWidgetBox}")
          # print(f"InfinityBox: {self.InfinityBox.build()}")
          # print(self.dropDragg)
          # ######################### filter if drag make fake cat no add WIDGET
          if selectWidgetBox:
               # self.select = self.widgets.get(selectWidgetBox)
               destiny_box.content.content.controls.append(self.InfinityBox(selectWidgetBox))
               selectWidgetBox=None         # get back natural state

          # ########################## border
          widgetDropBox.control.content.border = True
          widgetDropBox.control.content.border=ft.border.all(2, ft.colors.BLACK)
          # widgetDropBox.control.update()
          # ########################## reset
          # source_box.content_feedback.content=None            # reset widghet source original state
          # self.page.update()

     def drag_will_accept(self,widgetDropBox):
          # print('hello')
          # ource_box  = self.page.get_control(widgetDropBox.src_id)

          widgetDropBox.control.content.border = None
          widgetDropBox.control.content.border=ft.border.all(2, ft.colors.RED)
          widgetDropBox.control.update()
          self.page.update()

     def drag_leave(self,widgetDropBox):
          widgetDropBox.control.content.border = True
          widgetDropBox.control.content.border=ft.border.all(2, ft.colors.BLACK)
          widgetDropBox.control.update()
          self.page.update()



# class Build_Phone_Editor(ft.UserControl):
#      """Center Box that contain the phone to add Widget"""

#      def __init__(self,group='data',main_page='a'):
#           super().__init__()
#           self.group = group
#           # self.dropDragg= DropDragg()
#           self.main_page = main_page
#      def build(self):
#           self.Drop_Build_Phone_Editor = ft.DragTarget(
#                                              group='data',
#                                              on_accept=lambda _:self.on_accept_add_widget(_),
#                                              # on_accept=lambda _:print(f' data: {_}'),
#                                              on_will_accept=lambda _:self.drag_will_accept(_),

#                                              content=ft.Container( ###################### PHONE CONTAINER
#                                                             ##################### PROPERTY COLUMN
#                                                             ##################### [rotate,offset] , [scale,aspect_ratio] , [visible,disabled]
#                                                             # expand=True,
#                                                             ink=False,                                                      # click effect ripple
#                                                             bgcolor=ft.colors.TEAL,                                              # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
#                                                             padding= ft.padding.all(0),    # inside box                        # padding.only(left=8, top=8, right=8, bottom=8),
#                                                             margin = ft.margin.all(0),    # outside box                       # margin.only (left=8, top=8, right=8, bottom=8),
#                                                             alignment=ft.alignment.center,                                  # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right.    posicionamiento adentro widget
#                                                             border_radius= ft.border_radius.all(30),                      # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
#                                                             border=ft.border.all(4, ft.colors.BLACK),                     # ft.border.only(Left=8, top=8, right=8, bottom=8),
#                                                             # ===================
#                                                             # image_src = f"/home/mjay/Pictures/3d_neon_pink-2560x1440.jpg",
#                                                             # image_opacity=0.1,
#                                                             # image_fit='COVER',                                            # CONTAIN, COVER, FILL, FIT_HEIGHT, FIT_WIDTH, SCALE_DOWN
#                                                             # ===================
#                                                             width=260,
#                                                             height=525,
#                                                             # tooltip='Container',
#                                                             ##################### EFFECTS
#                                                             # gradient=ft.LinearGradient( begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=[ft.colors.CYAN, ft.colors.BLACK],),
#                                                             # gradient=ft.RadialGradient( colors=[ft.colors.YELLOW, ft.colors.BLUE],),
#                                                             ##################### WIDGETS
#                                                             content=ft.Column(
#                                                                            ##################### PROPERTY BOX
#                                                                            # expand=True,
#                                                                            # alignment=ft.MainAxisAlignment.SPACE_AROUND,              # horizontal <=> START,CENTER,END SPACE_BETWEEN SPACE_AROUND SPACE_EVENLY
#                                                                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,        # vertical       START,CENTER END
#                                                                            controls=[
#                                                                            ],
#                                                                            ),#<=== NOTE COMA [NOTE]                     for x in range(1,50): widget.content.controls.append(ft.ElevatedButton("press buttom",tooltip='buttom'))
#                                                             ##################### EVENTS
#                                                             # on_click=lambda _:print(_),                            # on_hover=print('on click over'), on_long_press=print('long press'),
#                                                             ),#<=== NOTE COMA

#                                                   )
#           return self.Drop_Build_Phone_Editor
#      def drag_will_accept(self,e):
#           # print(f"from: {self.main_page.get_control(e.target)}")
#           # print(f"to: {e.control}")

#           my_list = []
#           my_list.append(e.control)
#           print(f"drag_will_accept: {e.control}")
#           print(my_list,'asasda')
#           # print(f"drag_will_accept: {e.control.content.bgcolor}")
#           # e.control.content.content = ft.Text()
#           # pass
#           # e.control.content.border = ft.border.all(2, ft.colors.BLACK45 if e.data == "true" else ft.colors.RED)
#           # e.control.update()

#      def on_accept_add_widget(self,e):
#           e.control.content.border = ft.border.all(2, ft.colors.BLACK45 if e.data == "true" else ft.colors.BLUE)
#           print('======')
#           ##################### FROM SELECT DRAGG CONTAINER
#           # print(f"from: {self.main_page.get_control(e.src_id).group}")
#           print(f"from: {self.main_page.get_control(e.src_id)}")
#           # self.main_page.get_control(e.src_id).group='hello'   # <=== modifica el widget drag
#           # self.main_page.get_control(e.src_id).update()

#           ##################### TO SELECT DROP CONTAINER
#           # print(f"to: {e.control.group}")
#           print(f"to: {e.control}")
#           # e.control.group='hello'                              # <=== modifica el widget drag
#           # e.control.update()

#           ##################### TESTING ADD
#           # e.control.content.content.controls.append(self.widget_tmp)
#           # print(e.control)
#           print(f"on_accept_add_widget: {e.control.content.bgcolor}")

#           e.control.update()

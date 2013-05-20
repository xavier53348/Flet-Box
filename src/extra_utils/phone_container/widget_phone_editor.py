####################################################
from ..drag_container.infinity_box_layer_one import InfinityBoxLayerOne
####################################################
import flet as ft
###################### CALL GLOBAL VAR #############
from ..settings_var.settings_widget import GLOBAL_VAR
####################################################

class Build_Phone_Editor(ft.UserControl):
     """
     NOTE:

     ONLY FUNCTION OF THIS MODULE
     - ADD TO PHONE_SCREEN A DRAGABLE WIDGET THAT WILL BE A DRAGABLE_LOOP
     """

     def __init__(self,data='Erase this test'):
          super().__init__()
          # self.title='data'
          self.title=data

     def build(self):
          self.Build_Phone_Editor=ft.Container(
                                        ##################### PROPERTY ROW
                                        ink           = False,                                                 # click effect ripple
                                        padding       = ft.padding.only(left=0, top=0, right=0, bottom=0),     # inside box                        # padding.only(left=8, top=8, right=8, bottom=8),
                                        margin        = ft.margin.all(0),  # outside box                       # margin.only (left=8, top=8, right=8, bottom=8),
                                        alignment     = ft.alignment.center,                                   # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right
                                        border_radius = ft.border_radius.all(40),                              # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                                        border        = ft.border.all(2, ft.colors.WHITE),                     # ft.border.only(Left=8, top=8, right=8, bottom=8),
                                        width         = 295,
                                        height        = 566,
                                        # bgcolor       = ft.colors.BLACK,
                                        bgcolor       = '#070707',
                                        # image_src               = f"iphone.png",
                                        # image_fit               = ft.ImageFit.COVER,                      # CONTAIN, COVER, FILL, FIT_HEIGHT, FIT_WIDTH, SCALE_DOWN
                                        ##################### EFFECTS
                                        # gradient      = ft.LinearGradient( begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=[ft.colors.TEAL, ft.colors.BLACK45],),
                                        ##################### WIDGETS
                                   content = ft.DragTarget(
                                                       ######################################
                                                       ################# Traslate Container
                                                       group   = "GroupDragg",
                                                       content = ft.Container(
                                                                      border_radius = ft.border_radius.all(40),# ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                                                                      border        = ft.border.all(7.5, ft.colors.BLACK),                     # ft.border.only(Left=8, top=8, right=8, bottom=8),
                                                                      padding       = 0,
                                                                      # margin        = -0.3,
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
                                        # self.Build_Phone_Editor.controls.update()
                                        # self.controls

                                        )

          ################################## SET GLOBAL VAR // PHONE CONTAINER AND PHONE CONTENT //
          self.phone_container         = self.Build_Phone_Editor.content.content
          self.phone_container_content = self.Build_Phone_Editor.content.content.content

          GLOBAL_VAR(set_global_var={'PHONE_CONTAINER':self.phone_container})
          GLOBAL_VAR(set_global_var={'PHONE_CONTAINER_CONTENT':self.phone_container_content})
          ####################################################################################

          return self.Build_Phone_Editor
          # return self.my_cover_flow

     def drag_accept(self,widgetDropBox):
          self.InfinityBox = InfinityBoxLayerOne
          self.page        = GLOBAL_VAR(get_global_var = 'PAGE')
          selectWidgetBox  = GLOBAL_VAR(get_global_var = 'SELECT_DRAGG')


          ######################### filter if drag make fake cat no add WIDGET
          destiny_box = self.page.get_control(self.Build_Phone_Editor.uid)
          # print(f'destiny_box: {destiny_box.uid} <<<<<<')

          ####################################################################################
          # IF SELECT_DRAGG WIDGET IS FAKE SELECTED WILL BE SET IN GLOVAL VAR NONE
          # RETURNING NONE
          # WITH THIS CONDITION WE EVOID ADD FAKE WIDGETS EMPY
          # IS NECESARRY RESET SELECT_DRAGG TO NONE EVERY TIME THAT WE ADD ONE WIDGET NEW

          if not selectWidgetBox == None:
               # destiny_box.content.content.content.controls.append(self.InfinityBox(selectWidgetBox))
               self.Build_Phone_Editor.content.content.content.controls.append(self.InfinityBox(selectWidgetBox))
               ########################## border
               widgetDropBox.control.content.border = True
               widgetDropBox.control.content.border=ft.border.all(7, ft.colors.BLACK)
               widgetDropBox.control.update()
               GLOBAL_VAR(set_global_var={'SELECT_DRAGG':None})

          ####################################################################################

     def drag_will_accept(self,widgetDropBox):
          widgetDropBox.control.content.border = None
          widgetDropBox.control.content.border=ft.border.all(4, ft.colors.RED)
          widgetDropBox.control.update()

     def drag_leave(self,widgetDropBox):
          widgetDropBox.control.content.border = True
          widgetDropBox.control.content.border=ft.border.all(7, ft.colors.BLACK)
          widgetDropBox.control.update()
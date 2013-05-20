from ..drag_container.infinity_box_layer_one import InfinityBoxLayerOne
from ..settings_var.settings_widget import GLOBAL_VAR
import flet as ft

class Build_Phone_Editor(ft.Stack):
     """
     NOTE:

     ONLY FUNCTION OF THIS MODULE
     - ADD TO PHONE_SCREEN A DRAGABLE WIDGET THAT WILL BE A DRAGABLE_LOOP
     """
     def __init__(self,data='Erase this test'):
          super().__init__()

          self.title=data

     def build(self):

          self.Build_Phone_Editor=ft.Container(
                                        # ink           = False,
                                        # padding       = ft.padding.only(left=0, top=0, right=0, bottom=0),
                                        # margin        = ft.margin.all(0),
                                        # alignment     = ft.alignment.center,
                                        border_radius = ft.border_radius.all(42),
                                        # border        = ft.border.all(0, ft.colors.WHITE),
                                        width         = 295,
                                        height        = 566,
                                        alignment     = ft.alignment.center,
                                        # bgcolor       = '#070707', #070707
                                        # image_src     = 'logo.jpg',
                                        # image_fit     = "COVER",
                                        # blur          = (12,12),
                                        # expand=True,

                                   content = ft.DragTarget(
                                                       group   = "GroupDragg",
                                                       content = ft.Container(
                                                                      border_radius = ft.border_radius.all(40),
                                                                      border        = ft.border.all(7.5, ft.colors.BLACK),
                                                                      padding       = ft.padding.only(left=0, top=0, right=0, bottom=0),
                                                                      alignment     = ft.alignment.center,
                                                                      bgcolor       = ft.colors.BLACK38, #07070   7
                                                                      # blur          = (8,8),
                                                                      # image_src     = 'logo.jpg',
                                                                      # image_fit     = "COVER",
                                                                 content = ft.Column(
                                                                                scroll   = 'HIDDEN',
                                                                                spacing  = 2,
                                                                                controls = [
                                                                                           ],
                                                                           ),
                                                            ),
                                                       on_will_accept = self.drag_will_accept,
                                                       on_leave       = self.drag_leave,
                                                       on_accept      = lambda _:self.drag_accept(_),
                                        ),#<========comma
                                   )

          self.phone = ft.Container(
                            ink           = False,
                            padding       = ft.padding.only(left=0, top=0, right=0, bottom=0),
                            margin        = ft.margin.all(0),
                            alignment     = ft.alignment.center,
                            border_radius = ft.border_radius.all(42),
                            border        = ft.border.all(2.5, ft.colors.WHITE),
                            width         = 295,
                            height        = 566,
                            content=self.Build_Phone_Editor,
            )


          self.phone_main              = self.Build_Phone_Editor
          self.phone_container         = self.Build_Phone_Editor.content.content
          self.phone_container_content = self.Build_Phone_Editor.content.content.content
          # self.Build_Phone_Editor

          GLOBAL_VAR(set_global_var={'PHONE_MAIN':self.phone_main})
          GLOBAL_VAR(set_global_var={'PHONE_CONTAINER':self.phone_container})
          GLOBAL_VAR(set_global_var={'PHONE_CONTAINER':self.phone_container})
          GLOBAL_VAR(set_global_var={'PHONE_CONTAINER_CONTENT':self.phone_container_content})


          return self.phone
          # return self.Build_Phone_Editor
          #: return self.my_cover_flow

     def drag_accept(self,widgetDropBox):

          self.InfinityBox = InfinityBoxLayerOne
          self.page        = GLOBAL_VAR(get_global_var = 'PAGE')
          selectWidgetBox  = GLOBAL_VAR(get_global_var = 'SELECT_DRAGG')
          destiny_box = self.page.get_control(self.Build_Phone_Editor.uid)

          #: print(f'destiny_box: {destiny_box.uid} <<<<<<')

          #: IF SELECT_DRAGG WIDGET IS FAKE SELECTED WILL BE SET IN GLOVAL VAR NONE
          #: RETURNING NONE
          #: WITH THIS CONDITION WE EVOID ADD FAKE WIDGETS EMPY
          #: IS NECESARRY RESET SELECT_DRAGG TO NONE EVERY TIME THAT WE ADD ONE WIDGET NEW

          if not selectWidgetBox == None:
               ADD_WIDGET_SELECTED = self.InfinityBox(selectWidgetBox)

               self.Build_Phone_Editor.content.content.content.controls.append(ADD_WIDGET_SELECTED)

               widgetDropBox.control.content.border = True
               widgetDropBox.control.content.border=ft.border.all(7, ft.colors.BLACK)
               widgetDropBox.control.update()
               GLOBAL_VAR(set_global_var={'SELECT_DRAGG':None})

               self.id_widget   = ADD_WIDGET_SELECTED.controls[0].content.id
               self.name_widget = ADD_WIDGET_SELECTED.controls[0].content
               #: self.name_widget = ADD_WIDGET_SELECTED.controls[0].content._get_control_name()

               self.get_data_dict_to_update = GLOBAL_VAR(get_global_var='EXPORT_DATA_PHONE')
               self.get_data_dict_to_update.update({self.id_widget:self.name_widget})

               #: print(self.get_data_dict_to_update)
               #: print(ADD_WIDGET_SELECTED.controls[0].content._get_control_name(),'<==== DROPED WIDGET')
               #: print(ADD_WIDGET_SELECTED.controls[0].content.content._get_control_name(),'<==== DROPED WIDGET')

     def drag_will_accept(self,widgetDropBox):
          widgetDropBox.control.content.border = None
          widgetDropBox.control.content.border=ft.border.all(4, ft.colors.RED)
          widgetDropBox.control.update()

     def drag_leave(self,widgetDropBox):
          widgetDropBox.control.content.border = True
          widgetDropBox.control.content.border=ft.border.all(7, ft.colors.BLACK)
          widgetDropBox.control.update()
from ..drag_container.infinity_box_layer_one import InfinityBoxLayerOne
from ..settings_var.settings_widget import GLOBAL_VAR
from .nested_dict import create_nested_dict

import flet as ft


add_widget_to_dict_to_treview = dict()
all_widget: dict = {}


class Build_Phone_Editor(ft.Stack):
     """
     NOTE:

     ONLY FUNCTION OF THIS MODULE
     - ADD TO PHONE_SCREEN A DRAGABLE WIDGET THAT WILL BE A DRAGABLE_LOOP
     """
     def __init__(self,
                  color_data=ft.colors.TRANSPARENT,
                  screen_name_id: str=""):
          super().__init__()

          self.colored_widget = color_data
          self.screen_name_id = screen_name_id

     def build(self):

          self.Build_Phone_Editor=ft.Container(
                                        # ink           = False,
                                        # padding       = ft.padding.only(left=0, top=0, right=0, bottom=0),
                                        # margin        = ft.margin.all(0),
                                        # alignment     = ft.alignment.center,
                                        border_radius = ft.border_radius.all(42),
                                        # border        = ft.border.all(0, ft.colors.WHITE),
                                        # width         = 295,
                                        # height        = 566,
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
                                                                      # bgcolor       = ft.colors.BLACK38, #07070   7
                                                                      bgcolor=self.colored_widget,
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
                                        ),
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

          # self.phone_main              = self.Build_Phone_Editor
          # self.phone_container         = self.Build_Phone_Editor.content.content
          # self.phone_container_content = self.Build_Phone_Editor.content.content.content
          # self.Build_Phone_Editor

          #: RUN BY DEFAULD
          # GLOBAL_VAR(set_global_var={'SELECTED_SCREEN':self.Build_Phone_Editor})
          # GLOBAL_VAR(set_global_var={'PHONE_MAIN':self.phone_main})
          # GLOBAL_VAR(set_global_var={'PHONE_CONTAINER':self.phone_container})
          # GLOBAL_VAR(set_global_var={'PHONE_CONTAINER_CONTENT':self.phone_container_content})


          # print(f"'PHONE_MAIN': {self.phone_main} UID: {self.phone_main.uid}")
          # print(f"'PHONE_CONTAINER': {self.phone_container}")
          # print(f"'PHONE_CONTAINER_CONTENT': {self.phone_container_content}")
          return self.phone

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
               self.current_screen = GLOBAL_VAR(get_global_var='SELECTED_SCREEN').uid


               # self.get_data_dict_to_update.update({self.current_screen:{}})


               # self.get_data_dict_to_update[self.current_screen]={self.id_widget:{}}
               # self.get_data_dict_to_update[self.current_screen][self.id_widget]=self.name_widget
               # print(self.get_data_dict_to_update)






               #: UPDATE EXPORT DATA TO CURRENT WIDGET TO WORK WITH TRREVIEW
               # self.get_data_dict_to_update.update(
               #                                     {
               #                                     # NAME ID:        WIDGET
               #                                     self.id_widget : self.name_widget
               #                                     }
               #                                     )
               # ============================== SCREEN PHONE IN DICT ====================================
               # GET SELECTED SCREEN ID


               create_nested_dict(
                                  nested_dict = all_widget,
                                  data_1      = self.current_screen,
                                  data_2      = self.id_widget,
                                  value       = self.name_widget,
                                  )
               # self.get_data_dict_to_update.update(all_widget)
               # GLOBAL_VAR(set_global_var={'EXPORT_DATA_PHONE':all_widget})
               GLOBAL_VAR(set_global_var={'ALL_SCREEN_IN_DICT':all_widget})



               # self.current_screen = GLOBAL_VAR(get_global_var='SELECTED_SCREEN').uid

               # self.get_data_dict_to_update.update(
               #                                     {
               #                                     # NAME ID:        WIDGET
               #                                     # self.current_screen : ft.Text()
               #                                     self.id_widget : self.name_widget
               #                                     }
               #                                     )

               # print(self.get_data_dict_to_update)

               # self.get_data_dict_to_update.update(
               #                                     {
               #                                     # NAME ID:        WIDGET
               #                                     self.id_widget : ft.Text()
               #                                     # self.id_widget : self.name_widget
               #                                     })


               # GLOBAL_VAR(set_global_var={
               #                                                  # CURRENT SCREEN ID    # NAME ID:      # ALL WIDGETS INSIDE
               #                            # 'ALL_SCREEN_IN_DICT': {self.current_screen: {self.id_widget:ft.Container(content=ft.Text())} },
               #                            'ALL_SCREEN_IN_DICT': {self.current_screen: self.get_data_dict_to_update },
               #                          }
               #            )
               # ========================================================================================
               # self.all_screens_id = GLOBAL_VAR(get_global_var='ALL_SCREEN_IN_DICT')
               # self.all_screens_id.update(
               #                            {
               #                            self.current_screen:{
               #                                                     self.id_widget:self.get_data_dict_to_update
               #                                              }
               #                            }
               #                            )


               # print(self.all_screens_id)

               # data = self.all_screens_id.get(self.current_screen)
               # data.update({})

               # print(self.current_screen)
               # print(self.all_screens_id)
               # print(data)
               # print(self.all_screens.get(self.current_screen))
               #: print(ADD_WIDGET_SELECTED.controls[0].content._get_control_name(),'<==== DROPED WIDGET')
               #: print(ADD_WIDGET_SELECTED.controls[0].content.content._get_control_name(),'<==== DROPED WIDGET')
               # self.new_data.update({self.current_screen: {self.id_widget : ft.Text()}})

     def drag_will_accept(self,widgetDropBox):
          #: IF IT'S OVER WIDGET DROPED INSIDE PHONE BOX MARK BORDER COLOR

          widgetDropBox.control.content.border = None
          widgetDropBox.control.content.border=ft.border.all(4, ft.colors.RED)
          widgetDropBox.control.update()

     def drag_leave(self,widgetDropBox):
          #: IF LEAVE OF THE WIDGET DROPED INSIDE PHONE BOX BORDER COLOR WILL RESET
          widgetDropBox.control.content.border = True
          widgetDropBox.control.content.border=ft.border.all(7, ft.colors.BLACK)
          widgetDropBox.control.update()
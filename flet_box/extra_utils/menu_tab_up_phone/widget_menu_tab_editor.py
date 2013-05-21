import time
import json
import os
import flet as ft

from ..menu_tab_up_phone.basic_menu_tab_up import BasicMenuUp
from ..settings_var.save_export import MakeJasonFile
from .skeleton_class_screens import get_skeleton
from ..settings_var.settings_widget import GLOBAL_VAR
from ..screen_manager.write_file_proyect import write_file, file_saved


class MenuUpContainer(ft.Stack):

     def __init__(self,main_page='Erase this test'):
          super().__init__()

          self.main_page=main_page
          self.widget = MakeJasonFile()

     def build(self):

          Basic_MenuUp = BasicMenuUp()

          Drop_MenuUpContainer = ft.Container(
                                   ink             = False,
                                   bgcolor         = ft.colors.BLACK38,
                                   padding         = ft.padding.all(0),
                                   margin          = ft.margin.all(0),
                                   alignment       = ft.alignment.center,
                                   border_radius   = ft.border_radius.all(30),
                                   height          = 40,
                              content = ft.WindowDragArea(
                                             content  = ft.Row(
                                                            expand   = True,
                                                            spacing  = 0,
                                                            controls = [
                                                                 ft.Row(
                                                                      controls=[

                                                                                ft.Container(
                                                                                          padding =  ft.padding.only(left=16, top=0, right=0, bottom=0),
                                                                                          height  = 32 ,
                                                                                          bgcolor = 'Black',
                                                                                          content = ft.Image(
                                                                                                         src           = 'logo.jpg',
                                                                                                         border_radius = ft.border_radius.all(0),
                                                                                                         fit           = ft.ImageFit.CONTAIN,
                                                                                                         )
                                                                                           ),
                                                                                ft.Container(
                                                                                          ink           = False,
                                                                                          bgcolor       = ft.colors.BLACK26,
                                                                                          padding       = ft.padding.only(left=2, top=0, right=16, bottom=0),
                                                                                          margin        = ft.margin.all(0),
                                                                                          alignment     = ft.alignment.center,
                                                                                          border_radius = ft.border_radius.only(top_left=0, top_right=30, bottom_left=0, bottom_right=30),
                                                                                          content = ft.Text(
                                                                                                         value       = "LET BOX\n",
                                                                                                         text_align  = ft.TextAlign.LEFT,
                                                                                                         weight      = ft.FontWeight.BOLD,
                                                                                                         font_family = "Consolas", #"Consolas ,RobotoSlab
                                                                                                         size        = 20,
                                                                                                         spans = [ ft.TextSpan( "Powered by Flet Framework",
                                                                                                                             ft.TextStyle(

                                                                                                                                       size     = 10,
                                                                                                                                       color    = ft.colors.TEAL,
                                                                                                                                       weight   = ft.FontWeight.BOLD,
                                                                                                                                       ),),],
                                                                               ),),
                                                                 ],),

                                                                 ft.Container(
                                                                      width=125,
                                                                 ),#<=== NOTE COMA

                                                                 Basic_MenuUp,
                                                                 ft.Container(
                                                                             expand=True,
                                                                 ),#<=== NOTE COMA

                                                                 ft.Container(
                                                                      border_radius = ft.border_radius.all(30),
                                                                      bgcolor       = ft.colors.BLACK38,
                                                                      gradient      = ft.LinearGradient( begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=[ft.colors.TEAL, ft.colors.BLACK12],),
                                                                      content = ft.Row(
                                                                                     spacing=0,
                                                                                     controls=[
                                                                                          ft.Container(
                                                                                                      tooltip       = 'SAVE PROYECT',
                                                                                                      ink           = True,
                                                                                                      ink_color     = ft.colors.RED,
                                                                                                      bgcolor       = ft.colors.RED_900,
                                                                                                      margin        = ft.margin.only(left=2, top=2, right=8, bottom=2),
                                                                                                      alignment     = ft.alignment.center,
                                                                                                      border_radius = ft.border_radius.all(30),
                                                                                                      border        = ft.border.all(2, ft.colors.BLACK12),
                                                                                                      width         = 60,
                                                                                               on_click=lambda _: self.save_proyect_app(),
                                                                                               content=ft.Icon(name = ft.icons.SAVE_AS_ROUNDED,),
                                                                                          ),

                                                                                          ft.IconButton(
                                                                                                        ft.icons.CIRCLE,
                                                                                                        icon_color='Yellow',
                                                                                                        tooltip="Minimize",
                                                                                               on_click = lambda _: self.action_windows(action = "Minimize"),
                                                                                                        ),
                                                                                          ft.IconButton(
                                                                                                        ft.icons.CIRCLE,

                                                                                                        icon_color='Green',
                                                                                                        tooltip="Resize",

                                                                                                        content=ft.Text(value='X',color='White'),
                                                                                               on_click = lambda _: self.action_windows(action = "Resize"),
                                                                                                        ),
                                                                                          ft.IconButton(
                                                                                                        ft.icons.CIRCLE,

                                                                                                        icon_color='Red',

                                                                                                        tooltip="Close",
                                                                                               on_click = lambda _: self.action_windows(action = "Close"),

                                                                                     ),])
                                                                           ),


                                                                      ]

                                                                      ),
                                                            ))
          return Drop_MenuUpContainer

     def yes_click(self,data,alert):
          if data == 'yes':
               self.main_page.window_close()
          elif data == 'close':
               alert.open = False
               self.main_page.update()

     def action_windows(self,action):

          if   action == 'Close':
               confirm_dialog = ft.AlertDialog(
                                        modal   = True,
                                        title   = ft.Text("Please confirm"),
                                        content = ft.Text("Do you really want to exit this app?"),
                                   actions=[
                                              ft.ElevatedButton("Yes",on_click=lambda _:self.yes_click(data='yes',alert=confirm_dialog),bgcolor=ft.colors.RED_900),
                                              ft.OutlinedButton("No", on_click=lambda _:self.yes_click(data='close',alert=confirm_dialog)
                                             ),
                                        ],
                                        actions_alignment="end",
                                        )
               self.main_page.dialog = confirm_dialog
               confirm_dialog.open = True

          elif action == 'Minimize':
               self.main_page.window_minimized   = True

          elif action == 'Resize':
               self.main_page.window_maximizable = True

          self.main_page.update()



     def delete_attributes(self,list_atributes: list=[],dict_to_edit: dict={}):
          for _ in list_atributes:
               #: IF EXIST DATA or DATA == ""
               if dict_to_edit.get(_):
                    del dict_to_edit[_]

          return dict_to_edit


     def rename_dict_key(self,list_atributes: list="",dict_to_edit: dict={} , attributes_to_change: dict ={}):
          #: RENAME KEYS FROM DICT EG:
          #: imagesrc image_src

          attributes_to_change = {
                         "imagesrc":"image_src",
                     "imageopacity":"image_opacity",
                         "imagefit":"image_fit",
                     "borderradius":"border_radius",
              "horizontalalignment":"horizontal_alignment"
          }

          for _ in list_atributes:
               if dict_to_edit.get(_):
                    #: GET NEW NAME
                    new_name = attributes_to_change.get(_)
                    # RENAME OLD BY NEW KEY
                    dict_to_edit[new_name]=dict_to_edit.get(_)

                    #: DELETE OLD KEY
                    del dict_to_edit[_]

               else:
                    if dict_to_edit.get(_) == "":
                         del dict_to_edit[_]

          return dict_to_edit

     def create_frame_app(self,main_node_phone: str="OBJECT WIDGET",main_node_phone_id: str="ID OBJECT WIDGET"):

          # tmp_data_dict_attributes: dict={}

          all_data: dict = {

                         "MAIN_CONTAINER":str(),
                 "MAIN_EFFECTS_CONTAINER":str(),
                       "COLUMN_CONTAINER":str(),

                         }
          tmp_data: dict = {}

          #: INSTANCE MAIN PHONE
          self.main_phone = main_node_phone

          #: BUILD FRAME PHONE
          PHONE_MAIN         = self.main_phone
          PHONE_CONTAINER    = self.main_phone.content.content.content
          COLUMN_CONTAINER   = self.main_phone.content.content.content.content
          ALL_SCREEN_IN_DICT = self.main_phone.content.content.content.content.controls

          #: =========================================================================
          #: // NEW COPY ATTRIBUTES PHONE_MAIN                             DATA PHONE: [1]
          PHONE_MAIN.copy_attrs(dest=tmp_data)

          #: MAIN PHONE
          atributes_to_delete = [
                              "borderradius",
                              "border",
                              "ink",
                              "n",
                              "onhover",
                              "visible",
                              "onclick",
                              ]
          atributes_to_rename = [
                              "borderradius",
                              "imagesrc",
                              "imageopacity",
                              "imagefit",
                              ]
          tmp_data = self.delete_attributes(
                                             list_atributes  = atributes_to_delete,
                                             dict_to_edit    = tmp_data
                                             )
          tmp_data = self.rename_dict_key(
                                               list_atributes= atributes_to_rename,
                                               dict_to_edit  = tmp_data
                                          )
          #: =========================================================================
          #: RUN ONLY IN PRODUCTION                                        DATA PHONE: [1]
          # print(tmp_data,' DATA PHONE: [1]')
          if tmp_data.get('n'): del tmp_data['n']

          #: SET NEW DATA OF CONTAIER
          all_data["MAIN_CONTAINER"] = tmp_data
          tmp_data: dict = {}          #: RESET TO EMPTY
          #: =========================================================================
          #: // NEW COPY ATTRIBUTES PHONE_MAIN                             DATA PHONE: [2]
          PHONE_CONTAINER.copy_attrs(dest=tmp_data)

          #: MAIN PHONE
          atributes_to_delete = [
                              "borderradius",
                              "border",
                              'n'
                              "onclick",
                              "onhover",
                              ]
          # atributes_to_rename = [
          #                     # "borderradius",
          #                     # "imagesrc",
          #                     # "imageopacity",
          #                     # "imagefit",
          #                     ]
          tmp_data = self.delete_attributes(
                                             list_atributes  = atributes_to_delete,
                                             dict_to_edit    = tmp_data
                                             )
          # tmp_data = self.rename_dict_key(
          #                                      list_atributes= atributes_to_rename,
          #                                      dict_to_edit  = tmp_data
          #                                 )

          #: =========================================================================
          #: RUN ONLY IN PRODUCTION                                        DATA PHONE: [2]
          # print(tmp_data,' DATA PHONE: [2]')
          if tmp_data.get('n'): del tmp_data['n']

          #: SET NEW DATA OF CONTAIER
          all_data["MAIN_EFFECTS_CONTAINER"] = tmp_data
          tmp_data: dict = {}          #: RESET TO EMPTY
          #: =========================================================================
          #: // NEW COPY ATTRIBUTES PHONE_MAIN                             DATA PHONE: [3]
          COLUMN_CONTAINER.copy_attrs(dest=tmp_data)

          #: MAIN PHONE
          atributes_to_delete = [
                              'n'
                              "onhover",
                              "onclick",
                              ]
          atributes_to_rename = [
                              "horizontalalignment",
                              ]
          tmp_data = self.delete_attributes(
                                             list_atributes  = atributes_to_delete,
                                             dict_to_edit    = tmp_data
                                             )
          tmp_data = self.rename_dict_key(
                                               list_atributes= atributes_to_rename,
                                               dict_to_edit  = tmp_data
                                          )

          #: =========================================================================
          #: RUN ONLY IN PRODUCTION                                        DATA PHONE: [3]
          # print(tmp_data,' DATA PHONE: [2]')
          if tmp_data.get('n'): del tmp_data['n']

          #: SET NEW DATA OF CONTAIER
          all_data["COLUMN_CONTAINER"] = tmp_data
          tmp_data: dict = {}          #: RESET TO EMPTY
          #: =========================================================================

          #: BUILD ALL DATA TO EXPORT
          main_pone_style = json.dumps(all_data, indent=4 ).replace('\\', '').replace('borderradius', 'border_radius').replace('horizontalalignment', 'horizontal_alignment')
          main_screen_attributes: str = f"{main_pone_style}".replace('"{',"{").replace('}"',"}")

          #: RECODING TO MAKE MAIN SCREEN FROM SKELETON CLASS SCREEN THIS IS MAIN_SCREEN_BUILDER
          main_widget_form_skeleton: str = get_skeleton(name='class_flet_box')
          main_widget_form_skeleton = main_widget_form_skeleton.replace('CHANGE_STYLE', main_screen_attributes)                 #: SET ATRIBUTES

          #: CONTENT OF THE PHONE WILL WALK THOUGH HONE TO GET ALL DATA
          data_to_treview   = GLOBAL_VAR(get_global_var ='ALL_SCREEN_IN_DICT').get(main_node_phone_id)
          build_json_file   = self.widget.build_json_file(widget_show=data_to_treview)

          #: WILL RELACE [ CHANGE_ATTRIBUTES ] BY NEW ATTRIBUTES
          main_widget_form_skeleton  = main_widget_form_skeleton.replace('CHANGE_ATTRIBUTES',build_json_file.get('main_code'))    #: SET BOX CONTENT

          # #: RECODING TO MAKE STYLE SCREEN FROM SKELETON CLASS SCREEN
          main_style_code = f"#: THIS IS NOT JSON FILE IT'S PYTHON DICTIONARY{build_json_file.get('style_code')}"

          # #: RECODING TO MAKE EVENT MANAGER SCREEN FROM SKELETON CLASS SCREEN
          event_manager: str = get_skeleton(name='event_manager')
          main_event_code = f"{event_manager}{build_json_file.get('event_code')}"


          #: GET CURRENT NAME ID FOT EACH PROYECT
          id_name = GLOBAL_VAR(get_global_var=main_node_phone_id)
          # print(f"name id: {self.current_name}")


          #: RUN ONLY PRODUCTON
          # print(all_data)
          # print(f'ID: {self.main_phone.uid} PHONE_MAIN 1')
          # print(f'ID: {self.main_phone.content.content.content.uid } PHONE_CONTAINER 2')
          # print(f'ID: {self.main_phone.content.content.content.content.uid } PHONE_CONTAINER 4')

          # print(build_json_file.get('main_code'))
          # print(build_json_file.get('event_code'))
          # print(build_json_file.get('style_code'))
          # print(build_json_file)

          return    (
                    main_widget_form_skeleton ,
                    main_style_code ,
                    main_event_code ,
                    id_name,
                    )

          #: RESET COLOR
          # if selected_widget_clicked:
          #      selected_widget_clicked.border = ft.border.all(0, ft.colors.TRANSPARENT)
          #      selected_widget_clicked.update()


     def save_proyect_app(self):
          # #: SET GLOBAL VAR // LIST_SELECTED_WIDGETS // TO RESET AFTER PRESS SELECTED IN PHONE CONTAINER
          # selected_widget_clicked = GLOBAL_VAR( get_global_var='LIST_SELECTED_WIDGETS')

          # #: RESET COLOR
          # if selected_widget_clicked.border:
          #      selected_widget_clicked.border = ft.border.all(0, ft.colors.TRANSPARENT)
          #      selected_widget_clicked.update()

          #: GET LIST WITH ALL SCREENS
          self.get_row_screens = GLOBAL_VAR(get_global_var='row_phone').controls
          self.names_screens: list = []

          #: WRITE APP IN REAL TIME
          self.app_events_manager  = f'test/proyect_name/proyect_name/controls/'

          #: LIST SCREENS
          for tmp_widgets in self.get_row_screens:
               #: ALL FRAME OF PHONE    ALL CODE     ALL EVENT         ID SCREEN
               ( streaming_phone_data , style_code , main_event_code , id_name )= self.create_frame_app(
                                                                                           main_node_phone    = tmp_widgets,
                                                                                           main_node_phone_id = tmp_widgets.uid
                                                                                           )

               #: IF NO EXITS [ CREATE ] IF EXIST    [ OVERWRITE]
               write_file(
                         path_name  = self.app_events_manager,
                         file_name  = id_name,

                         main_code  = streaming_phone_data,
                         style_code = style_code,
                         event_code = main_event_code,
                          )

               self.names_screens.append(id_name)
               #: RUN ONLY IN PRODUCTION
               # print(streaming_phone_data)
               # print(style_code)
               # print(main_event_code)
               # print(id_name)




          #: NEED MAKE SCREEN BUILDER MANAGER APP
          self.write_screen_managet_app(screens_list_name=self.names_screens,
                                        path_to_write    =self.app_events_manager)

          #: NEED ACTIVATE ALER OF SELECTED WIDGET
          self.show_info_complete()

     def write_screen_managet_app(
                                   self,
                                   screens_list_name:  list=[],
                                   path_to_write:      list=[]
                                   ):

         list_screens = screens_list_name
         all_dict_imports = list()
         all_data = "#: ALL SCREENS IN APP\n"

         for _ in list_screens:
              #: SAVE ALL IMPORT PATH
             tmp_screen_data = f"from .views.{_} import {_}\n"
             tmp_events_data = f"from .views.{_}_events import *\n\n"

              #: ADD STR TO MIX DATA
             all_data+=tmp_screen_data+tmp_events_data

              #: SAVE ALL IMPORT SCREENS
             tmp_data = f"'{_}': {_}(),\n"
             all_dict_imports.append(tmp_data)

          #: ADD STR TO MIX DATA
         tabulation = "\t"*4
         all_data += "screens: dict={\n"
         for _ in all_dict_imports: all_data += f"{tabulation}{_}"
         all_data += tabulation +"}"

         full_screen_path = os.path.join(path_to_write,"app_screen_manager.py")

         file_saved(
                    full_path = full_screen_path,
                    data_code = all_data,
                    )


     def show_info_complete(self):
         selected_widget         = GLOBAL_VAR( get_global_var='ALERT_WIDGET')
         selected_widget.offset  = (1.59,-7.5)
         selected_widget.visible = True
         selected_widget.update()
         time.sleep(1)
         selected_widget.visible = False
         selected_widget.update()
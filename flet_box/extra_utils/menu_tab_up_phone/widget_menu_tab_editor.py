from ..menu_tab_up_phone.basic_menu_tab_up import BasicMenuUp
from ..settings_var.save_export import MakeJasonFile
from .skeleton_class_screens import get_skeleton
from ..settings_var.settings_widget import GLOBAL_VAR
from ..screen_manager.write_file_proyect import write_file

import time
import json
import flet as ft

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
                                                                                               on_click=lambda _: self.save_proyect(),
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

     def save_proyect(self):
          #: RESET DATA AND COLOR

          #: SET GLOBAL VAR // LIST_SELECTED_WIDGETS // TO RESET AFTER PRESS SELECTED IN PHONE CONTAINER
          selected_widget_clicked = GLOBAL_VAR( get_global_var='LIST_SELECTED_WIDGETS')

          #: SET GLOBAL VAR // SELECTED_WIDGET // IN DRAGG_DROPP BOX
          widget_selected = GLOBAL_VAR( set_global_var={
                                                        # 'SELECT_DRAGG' :data,
                                                        'LIST_SELECTED_WIDGETS':[]  ,
                                                        })
          #: RESET COLOR
          if selected_widget_clicked:
               selected_widget_clicked.border = ft.border.all(0, ft.colors.TRANSPARENT)
               selected_widget_clicked.update()

          #: MIX ALL DATA FROM WITGETS
          build_json_file  = self.widget.build_json_file(widget_show=GLOBAL_VAR(get_global_var='EXPORT_DATA_PHONE'))
          PHONE_MAIN       = GLOBAL_VAR(get_global_var='PHONE_MAIN')
          PHONE_CONTAINER  = GLOBAL_VAR(get_global_var='PHONE_CONTAINER')
          COLUMN_CONTAINER = PHONE_CONTAINER.content

          all_data: dict = {

                         "MAIN_CONTAINER":str(),
                 "MAIN_EFFECTS_CONTAINER":str(),
                       "COLUMN_CONTAINER":str(),

                         }
          tmp_data: dict = {}

          def rename_dict_key(old_key_name: str ="",new_key_name: str=""):
               #: RENAME KEYS FROM DICT EG:
               #: imagesrc image_src
               if tmp_data.get(old_key_name) == "" :
                    del tmp_data[old_key_name]
               else:
                    if not tmp_data.get(old_key_name) == None:
                         tmp_data[new_key_name] = tmp_data[old_key_name]
                         del tmp_data[old_key_name]

          #: // NEW COPY ATTRIBUTES PHONE_MAIN
          PHONE_MAIN.copy_attrs(dest=tmp_data)
          del tmp_data['n']
          del tmp_data['borderradius']


          if tmp_data.get('gradient') == "": del tmp_data['gradient']
          rename_dict_key(old_key_name="imagesrc",    new_key_name= "image_src")
          rename_dict_key(old_key_name="imageopacity",new_key_name= "image_opacity")
          rename_dict_key(old_key_name="imagefit",    new_key_name= "image_fit")

          #: UPDATE DATA TO MAIN PHONE
          all_data["MAIN_CONTAINER"]=tmp_data
          tmp_data: dict = {}         #: RESET TO EMPTY

          #: // NEW COPY ATTRIBUTES PHONE_CONTAINER
          PHONE_CONTAINER.copy_attrs(dest=tmp_data)
          del tmp_data['n']
          del tmp_data['border']
          del tmp_data['borderradius']

          #: DELETE EMPTY DATA
          if tmp_data.get('padding')   == "": del tmp_data['padding']
          elif tmp_data.get('bgcolor') == "": del tmp_data['bgcolor']
          elif tmp_data.get('blur')    == "": del tmp_data['blur']

          #: UPDATE DATA
          all_data["MAIN_EFFECTS_CONTAINER"]=tmp_data
          tmp_data: dict = {}         #: RESET TO EMPTY

          #: // NEW COPY ATTRIBUTES COLUMN_CONTAINER
          COLUMN_CONTAINER.copy_attrs(dest=tmp_data)
          del tmp_data['n']

          #: DELETE EMPTY DATA
          if tmp_data.get('spacing')     == "": del tmp_data['spacing']
          elif tmp_data.get('wrap')      == "": del tmp_data['wrap']
          elif tmp_data.get('tight')     == "": del tmp_data['tight']
          elif tmp_data.get('scroll')    == "": del tmp_data['scroll']
          elif tmp_data.get('alignment') == "": del tmp_data['alignment']
          rename_dict_key(old_key_name="horizontalalignment",new_key_name="horizontal_alignment")

          #: UPDATE DATA
          all_data["COLUMN_CONTAINER"]=tmp_data
          tmp_data: dict = {}         #: RESET TO EMPTY

          #:REREFACTORING STRINGS TO MAKE CLEAN ATTRIBUTES CODE
          main_pone_style = json.dumps(all_data, indent=4 ).replace('\\', '').replace('borderradius', 'border_radius').replace('horizontalalignment', 'horizontal_alignment')
          main_screen_attributes: str = f"{main_pone_style}".replace('"{',"{").replace('}"',"}")

          #: RECODING TO MAKE MAIN SCREEN FROM SKELETON CLASS SCREEN
          main_widget_form: str = get_skeleton(name='class_flet_box')
          main_widget_form = main_widget_form.replace('CHANGE_STYLE', main_screen_attributes)                 #: SET ATRIBUTES
          main_widget_form = main_widget_form.replace('CHANGE_ATTRIBUTES',build_json_file.get('main_code'))    #: SET BOX CONTENT

          #: RECODING TO MAKE STYLE SCREEN FROM SKELETON CLASS SCREEN
          main_style_code = f"#: THIS IS NOT JSON FILE IT'S PYTHON DICTIONARY{build_json_file.get('style_code')}"

          #: RECODING TO MAKE EVENT MANAGER SCREEN FROM SKELETON CLASS SCREEN
          event_manager: str = get_skeleton(name='event_manager')
          main_event_code = f"{event_manager}{build_json_file.get('event_code')}"

          #: RUN ONY IN PRODUCTION
          # print(all_data)
          # print(all_data.keys())
          # print(build_json_file.get('main_code'))
          # print(build_json_file.get('event_code'))
          # print(build_json_file.get('style_code'))

          # print(main_widget_form)
          # print(main_event_code)
          # print(main_style_code)

          # CONTAINER_STYLE
          path_screens        = 'test/proyect_name/proyect_name/controls/views'
          app_events_manager  = 'test/proyect_name/proyect_name/controls/'

          #: WRITE STYLE CODE
          main_widget_form = main_widget_form.replace('SYTLE_RENAME', 'main_screen_style') #: SET name_syle_attributes
          write_file(
                    file_path     = path_screens,
                    file_name     = "main_screen_style.py",
                    data_to_write = main_style_code
                    )

          #: WRITE SCREEN CODE
          write_file(
                    file_path     = path_screens,
                    file_name     = "main_screen.py",
                    data_to_write = main_widget_form
                    )

          #: WRITE EVENT CODE
          write_file(
                    file_path     = app_events_manager,
                    file_name     = "app_events_manager.py",
                    data_to_write = main_event_code
                    )



          # with open(app_screens,'w') as f:
          #      f.write(app_skeleton.get('main_code'))

          # with open(app_style,'w') as f:
          #      f.write(app_skeleton.get('app_style'))

          # with open(app_events_manager,'w') as f:
          #      f.write(app_skeleton.get('app_event_manager'))


          #: run only in production
          # print(app_skeleton.get('app_event_manager'))
          # print(app_skeleton.get('app_style'))
          # print(app_skeleton.get('main_code'))

          #: NEED ACTIVATE ALER OF SELECTED WIDGET
          selected_widget         = GLOBAL_VAR( get_global_var='ALERT_WIDGET')
          selected_widget.offset  = (1.59,-7.5)
          selected_widget.visible = True
          selected_widget.update()
          time.sleep(1)
          selected_widget.visible = False
          selected_widget.update()



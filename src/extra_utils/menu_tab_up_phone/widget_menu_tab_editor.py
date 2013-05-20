from ..menu_tab_up_phone.basic_menu_tab_up import BasicMenuUp
from ..settings_var.save_export import MakeJasonFile
from ..settings_var.settings_widget import GLOBAL_VAR

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

          # #: MIX ALL DATA FROM WITGETS
          build_json_file  = self.widget.build_json_file(widget_show=GLOBAL_VAR(get_global_var='EXPORT_DATA_PHONE'))
          PHONE_MAIN       = GLOBAL_VAR(get_global_var='PHONE_MAIN')
          PHONE_CONTAINER  = GLOBAL_VAR(get_global_var='PHONE_CONTAINER')
          COLUMN_CONTAINER = PHONE_CONTAINER.content

          # all_data , tmp_data = dict() ,dict()

          # #: NEW COPY ATTRIBUTES
          # PHONE_MAIN.copy_attrs(dest=tmp_data)
          # del tmp_data['n']

          # #: UPDATE DATA
          # all_data[PHONE_MAIN.uid]=tmp_data

          # #: NEW COPY ATTRIBUTES
          # PHONE_CONTAINER.copy_attrs(dest=tmp_data)
          # del tmp_data['n']

          # #: UPDATE DATA
          # all_data[PHONE_CONTAINER.uid]=tmp_data
          # # main_pone_style = json.dumps(all_data, indent=4 ).replace('\\', '').replace('borderradius', 'border_radius')

          # print(all_data.keys())

          app_skeleton ={

'app_event_manager':f'''

"""
NOTE: This is a global event that all events will be refer to this event_manager

Exemple:

is_gloval = 'hello world'     #: Global scope

def event_2933(data):
     global is_local          #: Set a local scope to global

     is_local = 'hello world'
"""

from builder.app_manager import got_to_screen

          {build_json_file.get('event_code')}''',

'app_style': build_json_file.get('style_code'),

'main_code': """

from .app_style import styles
from .app_events_manager import *
import flet as ft

def json_style(code):
    return styles.get(code)

#: only edit this seccion

screens = {

'main_screen':

ft.Container(
    **json_style('MAIN_STYLE'),

    content = ft.Container(
        **json_style('CONTAINER_STYLE'),

        content = ft.Column(
            **json_style('COLUMN_STYLE'),
            controls = [

REPLACE_THIS

                  ]),
),),
}

""".replace('MAIN_STYLE',PHONE_MAIN.uid).replace('CONTAINER_STYLE',PHONE_CONTAINER.uid).replace('COLUMN_STYLE',COLUMN_CONTAINER.uid).replace('REPLACE_THIS',build_json_file.get('main_code').strip('\n\n')),

          }
          # CONTAINER_STYLE
          app_screens        = '/home/mjay/Desktop/git_hub/flet_box/__PROYECT__/proyect_name/proyect_name/controls/app_screens.py'
          app_style          = '/home/mjay/Desktop/git_hub/flet_box/__PROYECT__/proyect_name/proyect_name/controls/app_style.py'
          app_events_manager = '/home/mjay/Desktop/git_hub/flet_box/__PROYECT__/proyect_name/proyect_name/controls/app_events_manager.py'

          with open(app_screens,'w') as f:
               f.write(app_skeleton.get('main_code'))

          with open(app_style,'w') as f:
               f.write(app_skeleton.get('app_style'))

          with open(app_events_manager,'w') as f:
               f.write(app_skeleton.get('app_event_manager'))


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
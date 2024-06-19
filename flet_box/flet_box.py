import flet as ft

from extra_utils import Build_Editor         #: LEFT DRAGG CONTAINER
from extra_utils import Build_Drag_Editor
from extra_utils import TreeView             #: TREEVIEW CONTAINER
from extra_utils import TreeViewTextEditor
from extra_utils import Build_Phone_Editor   #: PHONE CONTAINER
from extra_utils import MenuUpContainer      #: TAB MENU CONTAINER
from extra_utils import MenuLeftContainer
from extra_utils import LiteMenuUpContainer  #: LITE MENU RIGHT PHONE AND DOWN
from extra_utils import LiteMenuDownContainer
from extra_utils import IconBrowser          #: ICON AND COLOR BROWSER CONTAINER
from extra_utils import ColorBrowser
from extra_utils import GptBrowser
from extra_utils import AboutPage            #: ABOUT CONTAINER
from extra_utils import GLOBAL_VAR           #: CALL GLOBAL VAR  GLOBAL VARS
from extra_utils import AlertSelected        #: ALERT DIALOG
from extra_utils import Screen_palette
from extra_utils import ScreenPhotoSelection

from extra_utils import ScreenManager ,screen_manager  #: SCREEN MANAGER

def main(page: ft.Page):
     #: CONFIGURATION
     #: page.title                   = "Containers - clickable and not"
     page.window_title_bar_hidden         = True
     page.window_title_bar_buttons_hidden = True
     page.window_focused                  = True
     page.scroll                          = "HIDDEN" #AUTO ADAPTIVE ALWAYS HIDDEN
     page.vertical_alignment              = ft.MainAxisAlignment.CENTER
     page.horizontal_alignment            = ft.CrossAxisAlignment.CENTER
     #:  COLOR
     page.theme_mode                      = ft.ThemeMode.DARK         #ft.ThemeMode.LIGHT
     page.window_bgcolor                  = ft.colors.RED_100

     #: POSITION OF SC
     page.window_left                     = 3
     page.window_top                      = 3

     #: SIZE
     page.window_height                   = 768
     page.window_width                    = 1360
     page.padding                         = 0
     page.spacing                         = 0

     #: GLOBAL_VAR PAGE
     GLOBAL_VAR(set_global_var={'PAGE':page})
     #: GLOBAL_VAR PAGE

     drag_container_to_phone = Build_Drag_Editor()

     #: PHONE BOX CONTAINER TO GLOBAL VAR WITH NAME "main_screen"
     # phone_testing           = Build_Phone_Editor(color_data="Red")
     phone_testing           = Build_Phone_Editor(color_data=ft.colors.TRANSPARENT).build()
     # phone_testing           = Build_Phone_Editor(color_data=ft.colors.TRANSPARENT).build()

     # print(phone_testing.build().content)

     GLOBAL_VAR(set_global_var= {'main_screen':phone_testing})
     GLOBAL_VAR(set_global_var= {'SELECTED_SCREEN':phone_testing})


     screen_manager(set_screen= True)

     #: ITS VERY IMPORTANT GET WIDGET INSIDE BECOUSE WILL MODIFY MAIN PHONE BOX CONTAINER
     right_config_container  = Build_Editor()
     GLOBAL_VAR(set_global_var= {'build_Editor':right_config_container})

     #: ICON BROWSER
     Icon_Browser = IconBrowser(blur_effect=True)
     IconBrowserContainer = ft.Container(
               visible= False,
               right  = 240,
               left   = 240,
               top    = 80,
               bottom = 80,
          content=Icon_Browser,
          )
     GLOBAL_VAR(set_global_var={'ICON_BROWSER_CONTAINER':IconBrowserContainer})
     #: COLOR BROWSER
     Color_Browser = ColorBrowser(blur_effect=True)

     ColorBrowserContainer = ft.Container(
               visible= False,
               right  = 240,
               left   = 240,
               top    = 80,
               bottom = 80,
          content=Color_Browser,
          )
     GLOBAL_VAR(set_global_var={'COLOR_BROWSER_CONTAINER':ColorBrowserContainer})

     #: GPT BROWSER
     Gpt_Browser = GptBrowser(blur_effect=True)

     GptBrowserContainer = ft.Container(
               visible= False,
               right  = 240,
               left   = 240,
               top    = 80,
               bottom = 80,
          content=Gpt_Browser,
          )
     GLOBAL_VAR(set_global_var={'GPT_BROWSER_CONTAINER':GptBrowserContainer})

     #: ABOUT
     About_Page = AboutPage()

     AboutContainer = ft.Container(
               visible= False,
               right  = 80,
               left   = 80,
               top    = 60,
               bottom = 60,
          content=About_Page,
          )
     GLOBAL_VAR(set_global_var={'ABOUT_CONTAINER':AboutContainer})

     #: TEXT EDITOR
     TextEditor = TreeViewTextEditor()

     TextEditorContainer = ft.Container(
               visible= False,
               expand=True,
               right  = 0,
               left   = 0,
               top    = 0,
               bottom = 0,
          content=TextEditor,
          )
     GLOBAL_VAR(set_global_var={'TEXT_EDITOR_CONTAINER':TextEditorContainer})

     #: COLOR EDITOR
     ColorEditor = Screen_palette()

     ColorEditorContainer = ft.Container(
               visible= False,
               expand = True,
               right  = 8,
               left   = 985,
               top    = 70,
               bottom = 18,
               bgcolor= ft.colors.BLACK,
               # blur=(16,16),
               border_radius= ft.border_radius.only(top_left=28, top_right=28, bottom_left=28, bottom_right=28),
          content=ColorEditor,
          )
     GLOBAL_VAR(set_global_var={'COLOR_EDITOR_CONTAINER':ColorEditorContainer})

     #: IMAGEN EDITOR
     ImagenEditor = ScreenPhotoSelection()

     ImagenEditorContainer = ft.Container(
               visible= False,
               expand = True,
               right  = 8,
               left   = 985,
               top    = 70,
               bottom = 18,
               bgcolor= ft.colors.BLACK,
               # blur=(16,16),
               border_radius= ft.border_radius.only(top_left=28, top_right=28, bottom_left=28, bottom_right=28),
          content=ImagenEditor,
          )
     GLOBAL_VAR(set_global_var={'IMAGEN_EDITOR_CONTAINER':ImagenEditorContainer})

     right_config_container = ft.Container( #: RIGHT CONFIG CONTAINER
               ink             = False,
               bgcolor         = ft.colors.BLACK38,
               padding         = ft.padding.all(0),
               margin          = ft.margin.all(0),
               alignment       = ft.alignment.center,
               border_radius   = ft.border_radius.all(30),
               width           = 375,

               # EFFECS COLORS
               border=ft.border.all(0.6, ft.colors.WHITE12),
               shadow = ft.BoxShadow(
                       spread_radius=1,
                       blur_radius=16,
                       color=ft.colors.with_opacity(0.8,ft.colors.BLACK26),
                       offset=ft.Offset(0, 0),
                       blur_style=ft.ShadowBlurStyle.OUTER,
                 ),
          content=ft.Column(
                    controls = [
                                 right_config_container,
                                   ],
                              ),
                          )

     #: SCREEN MANAGER
     Screen_Manager = ScreenManager()

     ScreenContainer = ft.Container(
                              visible= False,
                              right  = 8,
                              left   = 8,
                              top    = 8,
                              bottom = 8,
                         content=Screen_Manager,
                         )

     GLOBAL_VAR(set_global_var={'SCREEN_CONTAINER':ScreenContainer})

     #: THIS SPACE WILL SHOW DEPENDING SIZE OF THE PHONE OR SCREEN
     space_widget_1 = ft.Container( expand = True)
     space_widget_2 = ft.Container( expand = True)

     #: ROW_PHONE IT'S MAIN ROW THAT HAVE PHONE WIDGET INSIDE WILL BE HOT RELOAD EVERY TIME WE CALL
     #: THAT'S WHY I WILL PAS TO A GLOVAL VAR NAME "SCREEN_CONTAINER"

     row_phone = ft.Row(
                        scroll=True,
               controls= [
                    # screen_manager(get_screen='main_screen')
                    phone_testing,
                    ],
                  )

     container_phone = ft.Container(
                                    # bgcolor="red",
                                    # width=295,
                                    width=295,
                                    height=566,
                                    border_radius = ft.border_radius.all(42),
                                    alignment = ft.alignment.center,
                                    shadow = ft.BoxShadow(
                                           spread_radius=1,
                                           blur_radius=24,
                                           color=ft.colors.with_opacity(0.8,ft.colors.BLUE_900),
                                           offset=ft.Offset(0, 0),
                                           blur_style=ft.ShadowBlurStyle.OUTER,
                                     ),

                         content=row_phone
                                    )
     #: WE SET AS GLOBAL VAR
     GLOBAL_VAR(set_global_var={"row_phone":row_phone})

     screen_1 = ft.Container(
                    ink             = False,
                    bgcolor         = ft.colors.BLACK54,
                    padding         = ft.padding.only(left=0, top=0, right=0, bottom=0),
                    margin          = ft.margin.all(0),    #outside box
                    alignment       = ft.alignment.center,
                    border          = ft.border.all(6, ft.colors.BLACK12),
                    height          = 768, #768
               content=ft.Row(
                         controls=[
                              MenuLeftContainer(),
                              ft.Container(
                                        expand    = True,
                                        ink       = False,
                                        padding   = ft.padding.only(left=0, top=4, right=0, bottom=4),
                                        margin    = ft.margin.all(0),
                                        alignment = ft.alignment.center,
                                   content=ft.Column(
                                                  expand = True,
                                              controls=[

                                                     MenuUpContainer(main_page = page),

                                                     ft.Container( #: CENTER MAIN CONTAINER THAT HAVE ['LEFT DRAG', 'MIDDLE PHONE' ,'RIGHT CONFIG']
                                                            ink       = False,
                                                            padding   = ft.padding.all(0),
                                                            margin    = ft.margin.all(0),    #outside box
                                                            alignment = ft.alignment.center,
                                                            height    = 680,
                                                         content = ft.Row(
                                                                     controls=[
                                                                       drag_container_to_phone,
                                                                       ft.Container( #: MIDDLE CONTAINER
                                                                                expand    = True,
                                                                                ink       = False,
                                                                                padding   = ft.padding.all(0),
                                                                                margin    = ft.margin.all(0),
                                                                                alignment = ft.alignment.center,
                                                                                height    = 675,
                                                                           content=ft.Column(
                                                                                          horizontal_alignment   = ft.CrossAxisAlignment.CENTER,
                                                                                          spacing              = 2,
                                                                                          run_spacing          = 2,
                                                                                     controls=[
                                                                                          ft.Container(
                                                                                               padding = ft.padding.all(0),
                                                                                               margin  = ft.margin.all(0),
                                                                                               height  = 620,
                                                                                               # width=400,
                                                                                               # bgcolor='Red',
                                                                                               #: IT'S A ROW THAT HAVE THE MAIN PHONE INSIDE
                                                                                               content = ft.Row(
                                                                                                              spacing     = 0,
                                                                                                              run_spacing = 0,
                                                                                                              controls = [
                                                                                                              space_widget_1,
                                                                                                              TreeView(),
                                                                                                              #: CALL WIDGET SCREEN IN DICT INSIDE screen_manager
                                                                                                              container_phone,

                                                                                                              space_widget_1,
                                                                                                              LiteMenuUpContainer(
                                                                                                                   menu_left_container    = drag_container_to_phone,
                                                                                                                   # phone_widget_container = screen_manager(get_screen='main_screen'),
                                                                                                                   # menu_right_container   = screen_manager(get_screen='main_screen').build(),
                                                                                                                   # main_page              = page,
                                                                                                                   space_widget           = [space_widget_1,space_widget_2],
                                                                                                                   ),
                                                                                                              ],),
                                                                                                        ),
                                                                                          LiteMenuDownContainer(),
                                                                                                ],
                                                                                     ),
                                                                                ),
                                                                                right_config_container,
                                                                              ],),
                                                            ),
                                                      AlertSelected(),
                                                       ],
                                              ),
                                   ),
                         ],),
          )

     data_stack = ft.Stack(
                    controls = [
                                   screen_1,
                                   IconBrowserContainer,
                                   ColorBrowserContainer,
                                   GptBrowserContainer,
                                   AboutContainer,
                                   TextEditorContainer,
                                   ScreenContainer,
                                   ColorEditorContainer,
                                   ImagenEditorContainer,
                         ]
          )

     #: only use in production
     page.add(data_stack)

     # AFTER ADD TAKE ID
     # GLOBAL_VAR(set_global_var={'phone_testing':phone_testing})
     # print(phone_testing.uid,'<<<<<')
     GLOBAL_VAR(set_global_var= {'ALL_SCREEN_IN_DICT':{phone_testing.uid:dict()}})
     # print(GLOBAL_VAR(get_global_var='ALL_SCREEN_IN_DICT'))
     # print(GLOBAL_VAR(get_global_var='main_screen').uid,'UID')
     GLOBAL_VAR(set_global_var={GLOBAL_VAR(get_global_var='main_screen').uid:"main_screen"})
     screen_manager(set_screen=row_phone.controls[0].uid)
     # print(GLOBAL_VAR(get_global_var='main_screen'))

     page.update()

def run_app():
     #: ONLY FOR PYINSTALLER
     ft.app(
               target = main,
          )

if __name__ == '__main__':
     ft.app(
               target = main,
          )


#: LEFT DRAGG CONTAINER
from extra_utils.config_container.widget_editor                  import Build_Editor
from extra_utils.drag_container.widget_drag_editor               import Build_Drag_Editor
#: TREEVIEW CONTAINER
from extra_utils.tree_view.tree_view                             import TreeView
from extra_utils.tree_view.tree_view_text_editor                 import TreeViewTextEditor
#: PHONE CONTAINER
from extra_utils.phone_container.widget_phone_editor             import Build_Phone_Editor
#: TAB MENU CONTAINER
from extra_utils.menu_tab_up_phone.widget_menu_tab_editor        import MenuUpContainer
from extra_utils.menu_tab_left_phone.widget_menu_left_editor     import MenuLeftContainer
#: LITE MENU RIGHT PHONE AND DOWN
from extra_utils.lite_menu_bar_right_phone.right_bar_menu_phone  import LiteMenuUpContainer
from extra_utils.lite_menu_bar_down_phone.footer_bar_menu_phone  import LiteMenuDownContainer
from extra_utils.lite_menu_bar_down_phone.selected_widget        import SelectedWidget
#: ICON AND COLOR BROWSER CONTAINER
from extra_utils.icon_browser.icon_browser                       import IconBrowser
from extra_utils.color_browser.color_browser                     import ColorBrowser
from extra_utils.chat_gpt_browser.gpt_browser                    import GptBrowser
#: ABOUT CONTAINER
from extra_utils.about.about                                     import AboutPage
#: CALL GLOBAL VAR  GLOBAL VARS
from extra_utils.settings_var.settings_widget                    import GLOBAL_VAR
#: ALERT DIALOG
from extra_utils.alert.alert_selected                            import AlertSelected
#: SCREEN MANAGER
from extra_utils.screen_manager.screen_manager                   import ScreenManager ,screen_manager

import flet as ft

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

     right_config_container = ft.Container( #: RIGHT CONFIG CONTAINER
               ink             = False,
               bgcolor         = ft.colors.BLACK38,
               padding         = ft.padding.all(0),
               margin          = ft.margin.all(0),
               alignment       = ft.alignment.center,
               border_radius   = ft.border_radius.all(30),
               width           = 368,
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
                                    width=295,
                                    # width=560,
                                    # height=620,
                                    alignment = ft.alignment.center,
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
                    height          = 768,
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
                         ]
          )

     #: only use in production
     # print(page.views)


     page.add(data_stack)

     # AFTER ADD TAKE ID
     # GLOBAL_VAR(set_global_var={'phone_testing':phone_testing})
     # print(phone_testing.uid,'<<<<<')
     GLOBAL_VAR(set_global_var= {'ALL_SCREEN_IN_DICT':{phone_testing.uid:dict()}})
     # print(GLOBAL_VAR(get_global_var='ALL_SCREEN_IN_DICT'))

     page.update()

def run_app():
     #: ONLY FOR PYINSTALLER
     ft.app(
               target = main,
          )

if __name__ == '__main__':
     ft.app(
               target         = main,
          )
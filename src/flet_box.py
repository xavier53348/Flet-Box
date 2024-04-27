#: LEFT DRAGG CONTAINER
from extra_utils.config_container.widget_editor                  import Build_Editor
from extra_utils.drag_container.widget_drag_editor               import Build_Drag_Editor
from extra_utils.drag_container.drag_handler_container           import HandlerDraggBox
#: TREEVIEW CONTAINER
from extra_utils.tree_view.tree_view                             import TreeView
from extra_utils.tree_view.tree_view_text_editor                 import TreeViewTextEditor
#:  PHONE CONTAINER
from extra_utils.phone_container.widget_phone_editor             import Build_Phone_Editor
#:  TAB MENU CONTAINER
from extra_utils.menu_tab_up_phone.widget_menu_tab_editor        import MenuUpContainer
from extra_utils.menu_tab_left_phone.widget_menu_left_editor     import MenuLeftContainer
#:  LITE MENU RIGHT PHONE AND DOWN
from extra_utils.lite_menu_bar_up_phone.head_bar_menu_phone      import LiteMenuUpContainer
from extra_utils.lite_menu_bar_down_phone.footer_bar_menu_phone  import LiteMenuDownContainer
from extra_utils.lite_menu_bar_down_phone.selected_widget        import SelectedWidget
#:  ICON AND COLOR BROWSER CONTAINER
from extra_utils.icon_browser.icon_browser                       import IconBrowser
from extra_utils.color_browser.color_browser                     import ColorBrowser
from extra_utils.chat_gpt_browser.gpt_browser                    import GptBrowser
#:  ABOUT CONTAINER
from extra_utils.about.about                                     import AboutPage
#:  CALL GLOBAL VAR  GLOBAL VARS
from extra_utils.settings_var.settings_widget                    import GLOBAL_VAR

import flet as ft

def main(page: ft.Page):
     #: CONFIGURATION
     #: page.title                   = "Containers - clickable and not"
     page.window_title_bar_hidden         = True
     page.window_title_bar_buttons_hidden = True
     page.window_focused                  = True
     page.scroll                    = "HIDDEN" #AUTO ADAPTIVE ALWAYS HIDDEN
     page.vertical_alignment        = ft.MainAxisAlignment.CENTER
     page.horizontal_alignment      = ft.CrossAxisAlignment.CENTER
     #:  COLOR
     page.theme_mode                = ft.ThemeMode.DARK         #ft.ThemeMode.LIGHT
     page.window_bgcolor            = ft.colors.RED_100

     #: POSITION OF SC
     page.window_left               = 3
     page.window_top                = 3

     #: SIZE
     page.window_height             = 768
     page.window_width              = 1360
     page.padding                   = 0
     page.spacing                   = 0

     #: GLOBAL_VAR PAGE
     GLOBAL_VAR(set_global_var={'PAGE':page})
     #: GLOBAL_VAR PAGE

     drag_container_to_phone = Build_Drag_Editor()
     phone_testing           = Build_Phone_Editor(page)
     right_config_container  = Build_Editor(widget=phone_testing.build())

     space_widget_1 = ft.Container( expand = True)
     space_widget_2 = ft.Container( expand = True)

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
                                                                                              content = ft.Row(
                                                                                                              spacing     = 0,
                                                                                                              run_spacing = 0,
                                                                                                             controls = [
                                                                                                                        space_widget_1,
                                                                                                                        TreeView(),
                                                                                                                        phone_testing,
                                                                                                                        space_widget_1,
                                                                                                                        LiteMenuUpContainer(
                                                                                                                                 menu_left_container    = drag_container_to_phone,
                                                                                                                                 phone_widget_container = phone_testing,
                                                                                                                                 menu_right_container   = right_config_container,
                                                                                                                                 main_page              = page,
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
                         ]
          )

     #: only use in production
     print(page.views)
     page.add(data_stack)
     page.update()

if __name__ == '__main__':
     ft.app(
               target         = main,
          )
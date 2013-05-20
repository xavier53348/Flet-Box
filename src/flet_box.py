################################################################################## LEFT DRAGG CONTAINER
from extra_utils.config_container.widget_editor                  import Build_Editor
from extra_utils.drag_container.widget_drag_editor               import Build_Drag_Editor
from extra_utils.drag_container.drag_handler_container           import HandlerDraggBox
################################################################################## TREEVIEW CONTAINER
from extra_utils.tree_view.tree_view                             import TreeView
from extra_utils.tree_view.tree_view_text_editor                 import TreeViewTextEditor
################################################################################## PHONE CONTAINER
from extra_utils.phone_container.widget_phone_editor             import Build_Phone_Editor
################################################################################## TAB MENU CONTAINER
from extra_utils.menu_tab_up_phone.widget_menu_tab_editor        import MenuUpContainer
from extra_utils.menu_tab_left_phone.widget_menu_left_editor     import MenuLeftContainer
################################################################################### LITE MENU RIGHT PHONE AND DOWN
from extra_utils.lite_menu_bar_up_phone.head_bar_menu_phone      import LiteMenuUpContainer
from extra_utils.lite_menu_bar_down_phone.footer_bar_menu_phone  import LiteMenuDownContainer
from extra_utils.lite_menu_bar_down_phone.selected_widget        import SelectedWidget
################################################################################### ICON AND COLOR BROWSER CONTAINER
from extra_utils.icon_browser.icon_browser                       import IconBrowser
from extra_utils.color_browser.color_browser                     import ColorBrowser
from extra_utils.chat_gpt_browser.gpt_browser                    import GptBrowser
################################################################################### ABOUT CONTAINER
from extra_utils.about.about                                     import AboutPage
###################### CALL GLOBAL VAR ############################################ GLOBAL VARS
from extra_utils.settings_var.settings_widget                    import GLOBAL_VAR
###################################################################################

# import logging
import flet as ft

def main(page: ft.Page):
     ###################### CONFIGURATION
     # page.title                   = "Containers - clickable and not"
     page.window_title_bar_hidden         = True
     page.window_title_bar_buttons_hidden = True
     page.window_focused                  = True
     # page.window_skip_task_bar    = True
     # page.window_frameless
     # print(dir(page))
     # page.window_frameless        = True
     # page.auto_scroll             = True #scroll_to()
     # page.fonts                   = {"RobotoSlab": "https://github.com/google/fonts/raw/main/apache/robotoslab/RobotoSlab%5Bwght%5D.ttf"}
     # page.splash                  = ft.Image(src=f"/home/mjay/Pictures/3d_neon_pink-2560x1440.jpg")
     # page.splash                    = True
     page.scroll                    = "HIDDEN" #AUTO ADAPTIVE ALWAYS HIDDEN
     page.vertical_alignment        = ft.MainAxisAlignment.CENTER
     page.horizontal_alignment      = ft.CrossAxisAlignment.CENTER
     ######################  COLOR
     page.theme_mode                = ft.ThemeMode.DARK         #ft.ThemeMode.LIGHT
     page.window_bgcolor            = ft.colors.RED_100
     # page.bgcolor                 = ft.colors.BLACK
     # page.window_bgcolor          =  ft.colors.RED
     # page.window_bgcolor          =  ft.colors.TRANSPARENT
     ###################### POSITION OF SC
     page.window_left               = 3
     page.window_top                = 3
     # page.window_center()
     ###################### SIZE
     page.window_height             = 768
     page.window_width              = 1360
     ######################
     # page.window_width            = 800
     # page.window_height           = 400
     ######################
     page.padding                   = 0
     page.spacing                   = 0
     # page.expand                    = True

     ###################### GLOBAL_VAR PAGE
     GLOBAL_VAR(set_global_var={'PAGE':page})
     ###################### GLOBAL_VAR PAGE

     drag_container_to_phone = Build_Drag_Editor()
     phone_testing           = Build_Phone_Editor(page)
     right_config_container  = Build_Editor(widget=phone_testing.build())

     space_widget_1 = ft.Container( expand = True)
     space_widget_2 = ft.Container( expand = True)

     ############################################ ICON BROWSER
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
     ############################################ COLOR BROWSER
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

     ############################################ GPT BROWSER
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

     ############################################ ABOUT
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

     ############################################ TEXT EDITOR
     TextEditor = TreeViewTextEditor()

     TextEditorContainer = ft.Container(
               visible= False,
               expand=True,
               right  = 0,
               left   = 0,
               top    = 0,
               bottom = 0,
               # bgcolor='red',
               # blur = (12,12),

          content=TextEditor,
          )
     GLOBAL_VAR(set_global_var={'TEXT_EDITOR_CONTAINER':TextEditorContainer})

     ############################################
     right_config_container = ft.Container( ###################### RIGHT CONFIG CONTAINER
               ##################### PROPERTY COLUMN
               ##################### [rotate,offset] , [scale,aspect_ratio] , [visible,disabled]
               # expand        = True,
               # visible=False, #<========== UNCOMMENT #####################
               ink             = False,                                                          # click effect ripple
               bgcolor         = ft.colors.BLACK38,                                              # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
               # bgcolor       = 'RED',                                                          # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
               padding         = ft.padding.all(0),    # inside box                              # padding.only(left=8, top=8, right=8, bottom=8),
               margin          = ft.margin.all(0),    # outside box                              # margin.only (left=8, top=8, right=8, bottom=8),
               alignment       = ft.alignment.center,                                            # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right.    posicionamiento adentro widget
               border_radius   = ft.border_radius.all(30),                                       # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
               # border        = ft.border.all(2, ft.colors.BLACK),                              # ft.border.only(Left=8, top=8, right=8, bottom=8),
               #####################
               # image_src     = f"/home/mjay/Pictures/3d_neon_pink-2560x1440.jpg",
               # image_opacity = 0.1,
               # image_fit     = 'COVER',                                            # CONTAIN, COVER, FILL, FIT_HEIGHT, FIT_WIDTH, SCALE_DOWN
               #####################
               width           = 368,
               # height        = 150,
               # tooltip       = 'Container',
               ##################### EFFECTS
               # gradient      = ft.LinearGradient( begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=[ft.colors.BLUE, ft.colors.YELLOW],),
               # gradient      = ft.RadialGradient( colors=[ft.colors.YELLOW, ft.colors.BLUE],),
               ##################### WIDGETS
          content=ft.Column(
                         ##################### PROPERTY BOX
                         # expand               = True,
                         # alignment            = ft.MainAxisAlignment.SPACE_AROUND,              # horizontal <=> START,CENTER,END SPACE_BETWEEN SPACE_AROUND SPACE_EVENLY
                         # horizontal_alignment = ft.CrossAxisAlignment.CENTER,                   # vertical       START,CENTER END
                         ##################### LET MAKE SCROLL IN LONG QUANTITY
                         # scroll               = True,                                           # center widget
                         # tight                = True,
                         ##################### ADAPT TO SCREEN
                         # wrap                 = True,                                           # justify in all screen
                         # spacing              = 8,                                              # space widget left right
                         # run_spacing          = 8,                                              # space widget up down
                         ##################### WIDGETS
                    controls = [
                                 right_config_container,
                              ],
          ),#<=== NOTE COMA [NOTE]                    # for x in range(1,50): widget.content.controls.append(ft.ElevatedButton("press buttom",tooltip='buttom'))
               ##################### EVENTS
               # on_click=lambda _:print(_),       # on_hover=print('on click over'), on_long_press=print('long press'),
     )#<=== NOTE COMA
     screen_1 = ft.Container(
                    ##################### PROPERTY
                    ##################### [rotate,offset] , [scale,aspect_ratio] , [visible,disabled]
                    # expand        = True,
                    ink             = False,                                                # click effect ripple
                    bgcolor         = ft.colors.BLACK54,                                    # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                    padding         = ft.padding.only(left=0, top=0, right=0, bottom=0),    # inside box                # padding.only(left=8, top=8, right=8, bottom=8),
                    margin          = ft.margin.all(0),    #outside box                     # margin.only (left=8, top=8, right=8, bottom=8),
                    alignment       = ft.alignment.center,                                  # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right.    posicionamiento adentro widget
                    # border_radius = ft.border_radius.all(30),                             # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                    border          = ft.border.all(6, ft.colors.BLACK12),                    # ft.border.only(Left=8, top=8, right=8, bottom=8),
                    #####################
                    # image_src     = f"/home/mjay/Pictures/3d_neon_pink-2560x1440.jpg",
                    # image_opacity = 0.1,
                    # image_fit     = 'COVER',                                              # CONTAIN, COVER, FILL, FIT_HEIGHT, FIT_WIDTH, SCALE_DOWN
                    #####################
                    # width         = 150,
                    height          = 768,
                    # height          = 715,
                    # tooltip       = 'Container',
                    ##################### EFFECTS
                    # gradient      = ft.LinearGradient( begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=[ft.colors.BLUE, ft.colors.YELLOW],),
                    # gradient      = ft.RadialGradient( colors=[ft.colors.YELLOW, ft.colors.BLUE],),
                    ##################### WIDGETS
               content=ft.Row(
                              ##################### PROPERTY BOX
                              # alignment          = ft.MainAxisAlignment.SPACE_AROUND,  # horizontal <=> START,CENTER,END SPACE_BETWEEN SPACE_AROUND SPACE_EVENLY
                              # vertical_alignment = ft.CrossAxisAlignment.CENTER,       # vertical       START,CENTER END
                              ##################### LET MAKE SCROLL IN LONG QUANTITY
                              # scroll             = True,                               # center widget
                              # tight              = True,
                              ##################### ADAPT TO SCREEN
                              # wrap               = True,                               # justify in all screen
                              # spacing            = 8,                                  # space widget left right
                              # run_spacing        = 8,                                  # space widget left down
                              ##################### WIDGETS
                         controls=[
                                        MenuLeftContainer(),

                                        ft.Container( ######################
                                                ##################### PROPERTY COLUMN
                                                ##################### [rotate,offset] , [scale,aspect_ratio] , [visible,disabled]
                                                expand          = True,
                                                ink             = False,                                                # click effect ripple
                                                # bgcolor       = "#3f449a",                                            # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                                                padding         = ft.padding.only(left=0, top=4, right=0, bottom=4),    # inside box                        # padding.only(left=8, top=8, right=8, bottom=8),
                                                margin          = ft.margin.all(0),    # outside box                    # margin.only (left=8, top=8, right=8, bottom=8),
                                                alignment       = ft.alignment.center,                                  # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right.    posicionamiento adentro widget
                                                # border_radius   = ft.border_radius.all(24),                             # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                                                # border        = ft.border.all(2, ft.colors.BLACK),                    # ft.border.only(Left=8, top=8, right=8, bottom=8),
                                                #####################
                                                # image_src     = f"/home/mjay/Pictures/3d_neon_pink-2560x1440.jpg",
                                                # image_opacity = 0.1,
                                                # image_fit     = 'COVER',                                              # CONTAIN, COVER, FILL, FIT_HEIGHT, FIT_WIDTH, SCALE_DOWN
                                                #####################
                                                # width         = 1100,
                                                # height        = 150,
                                                # tooltip       = 'Container',
                                                ##################### EFFECTS
                                                # gradient      = ft.LinearGradient( begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=[ft.colors.BLUE, ft.colors.YELLOW],),
                                                # gradient      = ft.RadialGradient( colors=[ft.colors.YELLOW, ft.colors.BLUE],),
                                                ##################### WIDGETS
                                            content=ft.Column(
                                                            ##################### PROPERTY BOX
                                                            expand               = True,
                                                            # alignment            = ft.MainAxisAlignment.SPACE_AROUND, # horizontal <=> START,CENTER,END SPACE_BETWEEN SPACE_AROUND SPACE_EVENLY
                                                            # horizontal_alignment = ft.CrossAxisAlignment.CENTER,      # vertical       START,CENTER END
                                                            ##################### LET MAKE SCROLL IN LONG QUANTITY
                                                            # scroll               = True,                              # center widget
                                                            # tight                = True,
                                                            ##################### ADAPT TO SCREEN
                                                            # wrap                 = True,                              # justify in all screen
                                                            # spacing              = 8,                                 # space widget left right
                                                            # run_spacing          = 8,                                 # space widget up down
                                                            ##################### WIDGETS
                                                        controls=[
                                                                    MenuUpContainer(main_page = page),

                                                                    ft.Container( ###################### CENTER MAIN CONTAINER THAT HAVE ['LEFT DRAG', 'MIDDLE PHONE' ,'RIGHT CONFIG']
                                                                                ##################### PROPERTY
                                                                                ##################### [rotate,offset] , [scale,aspect_ratio] , [visible,disabled]
                                                                                # expand        = True,
                                                                                ink             = False,                                                  # click effect ripple
                                                                                # bgcolor       = "#44CCCC00",                                            # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                                                                                padding         = ft.padding.all(0),    # inside box                      # padding.only(left=8, top=8, right=8, bottom=8),
                                                                                margin          = ft.margin.all(0),    #outside box                       # margin.only (left=8, top=8, right=8, bottom=8),
                                                                                alignment       = ft.alignment.center,                                    # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right.    posicionamiento adentro widget
                                                                                # border_radius = ft.border_radius.all(30),                               # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                                                                                # border        = ft.border.all(2, ft.colors.BLACK),                      # ft.border.only(Left=8, top=8, right=8, bottom=8),
                                                                                #####################
                                                                                # image_src     = f"oriental_dragg.jpg",
                                                                                # image_opacity = 0.1,
                                                                                # image_fit     = 'COVER',                                                # CONTAIN, COVER, FILL, FIT_HEIGHT, FIT_WIDTH, SCALE_DOWN
                                                                                #####################
                                                                                # width         = 900,
                                                                                height          = 680,
                                                                                # tooltip       = 'Container',
                                                                                ##################### EFFECTS
                                                                                # gradient      = ft.LinearGradient( begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=[ft.colors.BLUE, ft.colors.YELLOW],),
                                                                                # gradient      = ft.RadialGradient( colors=[ft.colors.YELLOW, ft.colors.BLUE],),
                                                                                ##################### WIDGETS
                                                                        content = ft.Row(
                                                                                        ##################### PROPERTY BOX
                                                                                        # expand             = True,
                                                                                        # alignment          = ft.MainAxisAlignment.SPACE_AROUND,        # horizontal <=> START,CENTER,END SPACE_BETWEEN SPACE_AROUND SPACE_EVENLY
                                                                                        # vertical_alignment = ft.CrossAxisAlignment.CENTER,             # vertical       START,CENTER END
                                                                                        ##################### LET MAKE SCROLL IN LONG QUANTITY
                                                                                        # scroll             = True,                                     # center widget
                                                                                        # tight              = True,
                                                                                        ##################### ADAPT TO SCREEN
                                                                                        # wrap               = True,                                     # justify in all screen
                                                                                        # spacing            = 8,                                        # space widget left right
                                                                                        # run_spacing        = 8,                                        # space widget up down
                                                                                        ##################### WIDGETS
                                                                                    controls=[
                                                                                                drag_container_to_phone,

                                                                                                ft.Container( ###################### MIDDLE CONTAINER
                                                                                                            ##################### PROPERTY COLUMN
                                                                                                            ##################### [rotate,offset] , [scale,aspect_ratio] , [visible,disabled]
                                                                                                            expand          = True,
                                                                                                            ink             = False,                                              # click effect ripple
                                                                                                            # bgcolor       = "red",                                              # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                                                                                                            padding         = ft.padding.all(0),    # inside box                  # padding.only(left=8, top=8, right=8, bottom=8),
                                                                                                            margin          = ft.margin.all(0),    # outside box                  # margin.only (left=8, top=8, right=8, bottom=8),
                                                                                                            alignment       = ft.alignment.center,                                # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right.    posicionamiento adentro widget
                                                                                                            # border_radius = ft.border_radius.all(30),                           # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                                                                                                            # border        = ft.border.all(2, ft.colors.BLACK12),                  # ft.border.only(Left=8, top=8, right=8, bottom=8),
                                                                                                            #####################
                                                                                                            # image_src     = f"/home/mjay/Pictures/3d_neon_pink-2560x1440.jpg",
                                                                                                            # image_opacity = 0.1,
                                                                                                            # image_fit     = 'COVER',                                            # CONTAIN, COVER, FILL, FIT_HEIGHT, FIT_WIDTH, SCALE_DOWN
                                                                                                            #####################
                                                                                                            # width         = 520,
                                                                                                            height        = 675,
                                                                                                            # tooltip       = 'Container',
                                                                                                            ##################### EFFECTS
                                                                                                            # gradient      = ft.LinearGradient( begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=[ft.colors.GREY_900, ft.colors.BLACK87],),
                                                                                                            # gradient      = ft.RadialGradient( colors=[ft.colors.YELLOW, ft.colors.BLUE],),
                                                                                                            ##################### WIDGETS
                                                                                                    content=ft.Column(
                                                                                                                    # expand=True,
                                                                                                                    horizontal_alignment   = ft.CrossAxisAlignment.CENTER,
                                                                                                                    # content              = ft.Row(
                                                                                                                    # vertical_alignment   = ft.CrossAxisAlignment.CENTER,        # vertical       START,CENTER END
                                                                                                                    ##################### PROPERTY BOX
                                                                                                                    # expand               = True,
                                                                                                                    # alignment            = ft.MainAxisAlignment.SPACE_AROUND,   # horizontal <=> START,CENTER,END SPACE_BETWEEN SPACE_AROUND SPACE_EVENLY
                                                                                                                    # horizontal_alignment = ft.CrossAxisAlignment.CENTER,        # vertical       START,CENTER END
                                                                                                                    ##################### LET MAKE SCROLL IN LONG QUANTITY
                                                                                                                    # scroll               = True,                                # center widget
                                                                                                                    # tight                = True,
                                                                                                                    ##################### ADAPT TO SCREEN
                                                                                                                    # wrap                 = True,                                # justify in all screen

                                                                                                                    spacing              = 2,                                   # space widget left right
                                                                                                                    run_spacing          = 2,                                   # space widget up down
                                                                                                                ##################### WIDGETS
                                                                                                                controls=[
                                                                                                                            # lite menu up phone,
                                                                                                                            # HandlerDraggBox(),

                                                                                                                            ft.Container(
                                                                                                                                       padding=ft.padding.all(0),
                                                                                                                                       margin=ft.margin.all(0),
                                                                                                                                       height=620,
                                                                                                                                       # width=1200,
                                                                                                                                       # gradient      = ft.LinearGradient( begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=[ft.colors.BLUE, ft.colors.YELLOW],),

                                                                                                                                 content = ft.Row(

                                                                                                                                                 spacing=0,
                                                                                                                                                 run_spacing=0,
                                                                                                                                                controls = [
                                                                                                                                                           space_widget_1,
                                                                                                                                                           TreeView(),
                                                                                                                                                           phone_testing,
                                                                                                                                                           # TreeViewTextEditor(),

                                                                                                                                                           space_widget_1,

                                                                                                                                                           LiteMenuUpContainer(
                                                                                                                                                                    menu_left_container    = drag_container_to_phone,
                                                                                                                                                                    phone_widget_container = phone_testing,
                                                                                                                                                                    menu_right_container   = right_config_container,
                                                                                                                                                                    main_page              = page,
                                                                                                                                                                    space_widget           = [space_widget_1,space_widget_2],
                                                                                                                                                                    ),

                                                                                                                                                          # phone_screen,
                                                                                                                                                          # space_widget_1,
                                                                                                                                                          # space_widget_2,
                                                                                                                                                          # lite menu Down phone
                                                                                                                                                          ],),
                                                                                                                                                ),

                                                                                                                            LiteMenuDownContainer(),

                                                                                                                         ],
                                                                                                            ),#<=== NOTE COMA [NOTE]                     for x in range(1,50): widget.content.controls.append(ft.ElevatedButton("press buttom",tooltip='buttom'))
                                                                                                            ##################### EVENTS
                                                                                                            # on_click=lambda _:print(_),                            # on_hover=print('on click over'), on_long_press=print('long press'),
                                                                                                ),#<=== NOTE COMA


                                                                                               # UNCOMMENT THIS <<<<<<>>>>>>>>
                                                                                               right_config_container, #  <======== UNCOMENT
                                                                                             ],),
                                                                        ##################### EVENTS
                                                                        # on_click=lambda _:print(_),                            # on_hover=print('on click over'), on_long_press=print('long press'),
                                                                    ),#<=== NOTE COMA
                                                                 ],
                                                        ),#<=== NOTE COMA [NOTE]                     # for x in range(1,50): widget.content.controls.append(ft.ElevatedButton("press buttom",tooltip='buttom'))
                                                        ##################### EVENTS
                                            # on_click=lambda _:print(_),                            # on_hover=print('on click over'), on_long_press=print('long press'),
                                            ),#<=== NOTE COMA
                                     ],),
            ##################### EVENTS
                # on_click=lambda _:print(_),                                                        # on_hover=print('on click over'), on_long_press=print('long press'),
     )#<=== NOTE COMA
     # right  = 350,
     # left   = 350,
     # bottom = 100,
     # top    = 100,
     # Icon_Browser = IconBrowser(blur_effect=True)
     # IconBrowserContainer = ft.Container(
     #           visible= False,
     #           right  = 340,
     #           left   = 340,
     #           top    = 100,
     #           bottom = 100,
     #      content=Icon_Browser,
     #      )
     # GLOBAL_VAR(set_global_var={'Icon_Browser':IconBrowserContainer})

     data_stack = ft.Stack(

                    controls=[
                         screen_1,                 #  <=== main page
                         IconBrowserContainer,   #  <======== UNCOMENT
                         ColorBrowserContainer,  #  <======== UNCOMENT
                         GptBrowserContainer,
                         AboutContainer,         #  <======== UNCOMENT
                         TextEditorContainer,
                         ]
          )

     # page.add(screen_1)

     # def window_event(e):
     #      if e.data == "close":
     #           page.dialog = confirm_dialog
     #           confirm_dialog.open = True
     #           page.update()

     # page.window_prevent_close = True
     # page.on_window_event = window_event

     # def yes_click(e):
     #      ft.page.window_destroy()

     # def no_click(e):
     #      confirm_dialog.open = False
     #      page.update()

     # confirm_dialog = ft.AlertDialog(
     #      modal=True,
     #      title=ft.Text("Please confirm"),
     #      content=ft.Text("Do you really want to exit this app?"),
     #      actions=[
     #        ft.ElevatedButton("Yes", on_click=yes_click),
     #        ft.OutlinedButton("No", on_click=no_click),
     #      ],
     #      actions_alignment="end",
     #      )


     print(page.views)
     page.add(data_stack)
     page.update()

if __name__ == '__main__':
     #####################
     # python3 ./.venv/bin/flet run 'main.py' -w #< run as web
     # python3 ./.venv/bin/flet run 'main.py' -r #< run as normal
     ###################### video
     # pip install flet_ivid --upgrade # <===== video
     # from flet_ivid import VideoContainer # import the package
     # vc            = VideoContainer("yourvideo.mp4", border_radius=18, expand=True) #lambda _:vc.play() #lambda _:vc.pause()
     ###################### audio
     # ft.Audio( src ="https://luan.xyz/files/audio/ambient_c_motion.mp3", autoplay=True) #lambda _: audio1.pause() #audio1.resume()) audio1.release()) audio1.seek(2000))
     # audio1.volume -= 0.1 #
     # audio1.update()
     # logging.basicConfig(level=logging.DEBUG,
     #                     format='%(asctime)s.%(msecs)03d %(message)s', datefmt='%H:%M:%S')

     ft.app(
               # assets_dir   = "assets",
               target         = main,
               # port         = 8082,
               # port         = 8080,
               # view         = ft.AppView.WEB_BROWSER, #view=ft.WEB_BROWSER,
               # web_renderer = ft.WebRenderer.HTML
          )
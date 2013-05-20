###################### CALL GLOBAL VAR #############
from ..settings_var.settings_widget import GLOBAL_VAR
####################################################
import flet as ft
####################################################

class LiteMenuUpContainer(ft.UserControl):
    # globalVar='Erase this test'

     def __init__(self,main_page= None , phone_widget_container= None,menu_left_container= None , menu_right_container= None, space_widget = None):
          super().__init__()
          self.main_page = main_page
          self.menu_left_container    = menu_left_container
          self.phone_widget_container = phone_widget_container
          self.menu_right_container   = menu_right_container
          self.space_widget_1 , self.space_widget_2  = space_widget
          # print(self.space_widget_1)
     def build(self):

          self.Drop_LiteMenuUpContainer = ft.Container(
                                        ##################### PROPERTY
                                        ##################### [rotate,offset] , [scale,aspect_ratio] , [visible,disabled]
                                        # expand=True,
                                        offset=(0.1,0),
                                        ink             = False,                                         # click effect ripple
                                        # bgcolor         = ft.colors.BLACK26,                           # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                                        padding         = ft.padding.all(2),    # inside box             # padding.only(left=8, top=8, right=8, bottom=8),
                                        margin          = ft.margin.only (left=2, top=0, right=0, bottom=0),     # outside box            # margin.only (left=8, top=8, right=8, bottom=8),
                                        alignment       = ft.alignment.center,                           # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right.    posicionamiento adentro widget
                                        border_radius   = ft.border_radius.all(30),                      # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                                        # border        = ft.border.all(2, ft.colors.BLACK),             # ft.border.only(Left=8, top=8, right=8, bottom=8),
                                        #               ===================
                                        # image_src     = f"/home/mjay/Pictures/3d_neon_pink-2560x1440.jpg",
                                        # image_opacity = 0.1,
                                        # image_fit     = 'COVER',                                       # CONTAIN, COVER, FILL, FIT_HEIGHT, FIT_WIDTH, SCALE_DOWN
                                        #               ===================
                                        # width         = 150,
                                        height        = 410,
                                        # tooltip       = 'Container',
                                        ##################### EFFECTS
                                        gradient      = ft.LinearGradient( begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=[ft.colors.TEAL, ft.colors.BLACK12],),
                                        # gradient      = ft.RadialGradient( colors=[ft.colors.YELLOW, ft.colors.BLUE],),
                                        ##################### WIDGETS
                                   content=ft.Column(
                                                  ##################### PROPERTY BOX
                                                  # expand             = True,
                                                  # alignment          = ft.MainAxisAlignment.SPACE_BETWEEN,            # horizontal <=> START,CENTER,END SPACE_BETWEEN SPACE_AROUND SPACE_EVENLY
                                                  # vertical_alignment = ft.CrossAxisAlignment.CENTER,                  # vertical       START,CENTER END
                                                  ##################### LET MAKE SCROLL IN LONG QUANTITY
                                                  # scroll           = True,                                            # center widget
                                                  # tight            = True,
                                                  ##################### ADAPT TO SCREEN
                                                  # wrap             = True,                                            # justify in all screen
                                                  # spacing          = 8,                                               # space widget left right
                                                  # run_spacing      = 8,                                               # space widget up down
                                                  ##################### WIDGETS
                                             controls=[
                                                       ft.Container( ##################### DEVICES
                                                                 ##################### PROPERTY
                                                                 ##################### [rotate,offset] , [scale,aspect_ratio] , [visible,disabled]
                                                                 # expand=True,
                                                                 ink           = False,                                                # click effect ripple
                                                                 bgcolor       = ft.colors.BLACK26,                                    # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                                                                 padding       = ft.padding.only(left=0, top=8, right=0, bottom=8),    # inside box                # padding.only(left=8, top=8, right=8, bottom=8),
                                                                 # margin      = ft.margin.all(8),    #outside box                     # margin.only (left=8, top=8, right=8, bottom=8),
                                                                 alignment     = ft.alignment.center,                                  # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right.    posicionamiento adentro widget
                                                                 border_radius = ft.border_radius.all(30),                             # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                                                                 border        = ft.border.all(2, ft.colors.BLACK12),                  # ft.border.only(Left=8, top=8, right=8, bottom=8),
                                                                 #####################
                                                                 # image_src     = f"/home/mjay/Pictures/3d_neon_pink-2560x1440.jpg",
                                                                 # image_opacity = 0.1,
                                                                 # image_fit     = 'COVER',                                            # CONTAIN, COVER, FILL, FIT_HEIGHT, FIT_WIDTH, SCALE_DOWN
                                                                 #####################
                                                                 # width         = 150,
                                                                 # height        = 150,
                                                                 # tooltip       = 'Container',
                                                                 ##################### EFFECTS
                                                                 # gradient      = ft.LinearGradient( begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=[ft.colors.BLUE, ft.colors.YELLOW],),
                                                                 # gradient      = ft.RadialGradient( colors=[ft.colors.YELLOW, ft.colors.BLUE],),
                                                                 ##################### WIDGETS
                                                            content=ft.Column(
                                                                           ##################### PROPERTY BOX
                                                                           # expand             = True,
                                                                           # alignment          = ft.MainAxisAlignment.SPACE_BETWEEN,    # horizontal <=> START,CENTER,END SPACE_BETWEEN SPACE_AROUND SPACE_EVENLY
                                                                           # vertical_alignment = ft.CrossAxisAlignment.CENTER,          # vertical       START,CENTER END
                                                                           ##################### LET MAKE SCROLL IN LONG QUANTITY
                                                                           # scroll             = True,                                  # center widget
                                                                           # tight              = True,
                                                                           ##################### ADAPT TO SCREEN
                                                                           # wrap               = True,                                  # justify in all screen
                                                                           spacing              = 8,                                     # space widget left right
                                                                           # run_spacing        = 8,                                     # space widget up down
                                                                           ##################### WIDGETS
                                                                      controls=[
                                                                           ft.IconButton(icon = ft.icons.EDIT_SQUARE,                tooltip='EDIT WIDGET',on_click=lambda _:self.modify_widget_in_phone_container(),bgcolor='Blue',icon_color='White'),
                                                                           ft.IconButton(icon = ft.icons.SMARTPHONE,                 tooltip='SMARTPHONE', on_click=lambda _:self.action_button( action = 'SMARTPHONE')),
                                                                           ft.IconButton(icon = ft.icons.TABLET_ANDROID,             tooltip='TABLET',     on_click=lambda _:self.action_button( action = 'TABLET')),
                                                                           ft.IconButton(icon = ft.icons.TV_OUTLINED,                tooltip='PC',         on_click=lambda _:self.action_button( action = 'PC')),
                                                                           ft.IconButton(icon = ft.icons.FEATURED_PLAY_LIST_OUTLINED,tooltip='SHOW PC',    on_click=lambda _:self.action_button( action = 'SHOW PC')),
                                                                           # ft.Container( ##################### NAME DEVICE
                                                                           #                ##################### PROPERTY
                                                                           #                ink       = False,                                                # click effect ripple
                                                                           #                # bgcolor = "#44CCCC00",                                          # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                                                                           #                padding   = ft.padding.all(8), # inside box                       # padding.only(left=8, top=8, right=8, bottom=8),
                                                                           #                margin    = ft.margin.all(0),  # outside box                      # margin.only (left=8, top=8, right=8, bottom=8),
                                                                           #                alignment = ft.alignment.center,                                  # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right. posicionamiento adentro widget
                                                                           #                ##################### WIDGETS
                                                                           #           content=ft.Text(
                                                                           #                          ##################### PROPERTY
                                                                           #                          value           = "Device IPhone\n",                    # content = ft.Text(value="Compound button", size=12,),
                                                                           #                          text_align      = ft.TextAlign.LEFT,                    # LEFT (default),RIGHT,CENTER,JUSTIFY,START,END
                                                                           #                          weight          = ft.FontWeight.BOLD,                   # NORMAL (default), BOLD, W_100, W_200,  W_300, W_400, W_500, W_600, W_700, W_800,W_900
                                                                           #                          font_family     = "Consolas", #"Consolas ,RobotoSlab
                                                                           #                          ##################### COLOR
                                                                           #                          height          = 25,
                                                                           #                          overflow="ellipsis",                                     # FADE,ELLIPSIS,CLIP,VISIBLE
                                                                           #                          #####################
                                                                           #                          spans=[ft.TextSpan( "375(px) x 812(px)", ft.TextStyle( size=8, color=ft.colors.BLUE),),],
                                                                           #           ),),#<=== NOTE COMA <==> ERASE COMA IF MAKE 1 ERROR
                                                                        ],),
                                                                   ##################### EVENTS
                                                                   # on_click=lambda _:print(_),                            # on_hover=print('on click over'), on_long_press=print('long press'),
                                                       ),#<=== NOTE COMA
                                                       ft.Container( ##################### ROTATION
                                                                      ##################### [rotate,offset] , [scale,aspect_ratio] , [visible,disabled]
                                                                      # expand=True,
                                                                      padding= ft.padding.only(left=0, top=2, right=0, bottom=2),    # inside box                # padding.only(left=8, top=8, right=8, bottom=8),
                                                                      bgcolor=ft.colors.BLACK26,
                                                                      ink=False,                                                # click effect ripple
                                                                      # bgcolor="#44CCCC00",                                    # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                                                                      # padding= ft.padding.all(8),    # inside box             # padding.only(left=8, top=8, right=8, bottom=8),
                                                                      # margin = ft.margin.all(8),     # outside box            # margin.only (left=8, top=8, right=8, bottom=8),
                                                                      alignment=ft.alignment.center,                            # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right.    posicionamiento adentro widget
                                                                      border_radius= ft.border_radius.all(30),                  # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                                                                      border=ft.border.all(2, ft.colors.BLACK12),               # ft.border.only(Left=8, top=8, right=8, bottom=8),
                                                                      # ===================
                                                                      # image_src = f"/home/mjay/Pictures/3d_neon_pink-2560x1440.jpg",
                                                                      # image_opacity=0.1,
                                                                      # image_fit='COVER',                                            # CONTAIN, COVER, FILL, FIT_HEIGHT, FIT_WIDTH, SCALE_DOWN
                                                                      # ===================
                                                                      # width=150,
                                                                      # height=150,
                                                                      # tooltip='Container',
                                                                      ##################### EFFECTS
                                                                      # gradient=ft.LinearGradient( begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=[ft.colors.BLUE, ft.colors.YELLOW],),
                                                                      # gradient=ft.RadialGradient( colors=[ft.colors.YELLOW, ft.colors.BLUE],),
                                                                      ##################### WIDGETS
                                                                 content=ft.Column(
                                                                                ##################### PROPERTY BOX
                                                                                expand=True,
                                                                                # alignment=ft.MainAxisAlignment.SPACE_AROUND,              # horizontal <=> START,CENTER,END SPACE_BETWEEN SPACE_AROUND SPACE_EVENLY
                                                                                # vertical_alignment=ft.CrossAxisAlignment.CENTER,          # vertical       START,CENTER END
                                                                                ##################### LET MAKE SCROLL IN LONG QUANTITY
                                                                                # scroll=True,                                              # center widget
                                                                                # tight=True,
                                                                                ##################### ADAPT TO SCREEN
                                                                                # wrap=True,                                                  # justify in all screen
                                                                                spacing=8,                                                # space widget left right
                                                                                # run_spacing=8,                                            # space widget up down
                                                                                ##################### WIDGETS
                                                                           controls=[
                                                                                     ft.IconButton(icon=ft.icons.DELETE_SWEEP_OUTLINED,tooltip='DELETE_',     on_click=lambda _:self.action_button(action='delete')),
                                                                                     ft.IconButton(icon=ft.icons.SCREEN_ROTATION,      tooltip='ROTATE',      on_click=lambda _:self.action_button(action='rotation')),
                                                                                     ft.IconButton(icon=ft.icons.DEBLUR,               tooltip='LIGHT / DARK',on_click=lambda _:self.action_button(action='LIGHT / DARK')),
                                                                                     ft.IconButton(icon=ft.icons.SCHEMA,               tooltip='TREE',        on_click=lambda _:self.action_button(action='TREE')),
                                                                                  ],),
                                                                   ##################### EVENTS
                                                                   # on_click=lambda _:print(_),                            # on_hover=print('on click over'), on_long_press=print('long press'),
                                                                 ),#<===
                                                       # ft.ElevatedButton("rotate",tooltip='buttom',on_click=lambda _:self.action_windows(_)),
                                                       # ft.ElevatedButton("press row",tooltip='buttom'),
                                                       # ft.ElevatedButton("press row",tooltip='buttom'),
                                                       # ft.Container( ##################### NAME DEVICE
                                                                                               #                ##################### PROPERTY
                                                                                               #                ink       = False,                                                # click effect ripple
                                                                                               #                # bgcolor = "#44CCCC00",                                          # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                                                                                               #                padding   = ft.padding.all(8), # inside box                       # padding.only(left=8, top=8, right=8, bottom=8),
                                                                                               #                margin    = ft.margin.all(0),  # outside box                      # margin.only (left=8, top=8, right=8, bottom=8),
                                                                                               #                alignment = ft.alignment.center,                                  # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right. posicionamiento adentro widget
                                                                                               #                ##################### WIDGETS
                                                                                               #           content=ft.Text(
                                                                                               #                          ##################### PROPERTY
                                                                                               #                          value           = "Device IPhone\n",                    # content = ft.Text(value="Compound button", size=12,),
                                                                                               #                          text_align      = ft.TextAlign.LEFT,                    # LEFT (default),RIGHT,CENTER,JUSTIFY,START,END
                                                                                               #                          weight          = ft.FontWeight.BOLD,                   # NORMAL (default), BOLD, W_100, W_200,  W_300, W_400, W_500, W_600, W_700, W_800,W_900
                                                                                               #                          font_family     = "Consolas", #"Consolas ,RobotoSlab
                                                                                               #                          ##################### COLOR
                                                                                               #                          height          = 25,
                                                                                               #                          overflow="ellipsis",                                     # FADE,ELLIPSIS,CLIP,VISIBLE
                                                                                               #                          #####################
                                                                                               #                          spans=[ft.TextSpan( "375(px) x 812(px)", ft.TextStyle( size=8, color=ft.colors.BLUE),),],
                                                                                               #           ),),#
                                                    ],

                                                  ),

                                ##################### EVENTS
                                # on_click=lambda _:print(_),                                           # on_hover=print('on click over'), on_long_press=print('long press'),
                            )#<=== NOTE COMA
          return self.Drop_LiteMenuUpContainer

     def modify_widget_in_phone_container(self):
          print('Im modificating....')

          """
          GLOBAL VARS:
                         CONFIG_TABS_CONTAINERS
                         CONFIG_TABS_CONTAINERS_CONTENT

          NOTE:
               IS NECESSARY ADD THIS 2 GLOVAL VAR TO CALL TAB MENU AND MAKE CHANGES IN STRAMING

          GLOBAL VARS:
                         SELECT_DROPP_WIDGET_CONTAINER
                         SELECT_DROPP_WIDGET_CONTAINER_CONTENT

          NOTE:
               EVERY TIME THAT IS SELECTED WIDGET INSIDE THE PHONE.
               THIS 2 VAR ARE CHANGE EVERY TIME THAT DETECT ONE CLICK
               AND AFTER PERES BUTTON EDIT WILL CALL THIS METOD TO
               CHANGE PROPERTY

          """
          BOOL_SHOW_SELECTED = GLOBAL_VAR(get_global_var='BOOL_SHOW_SELECTED')
          ############################
          LIST_KEYS_DICT_USED = GLOBAL_VAR(get_global_var='LIST_KEYS_DICT_USED')
          ############################
          CONFIG_TABS_CONTAINERS                = GLOBAL_VAR(get_global_var='CONFIG_TABS_CONTAINERS')
          CONFIG_TABS_CONTAINERS_CONTENT        = GLOBAL_VAR(get_global_var='CONFIG_TABS_CONTAINERS_CONTENT')
          ############################
          SELECT_DROPP_WIDGET_CONTAINER         = GLOBAL_VAR(get_global_var='SELECT_DROPP_WIDGET_CONTAINER')
          SELECT_DROPP_WIDGET_CONTAINER_CONTENT = GLOBAL_VAR(get_global_var='SELECT_DROPP_WIDGET_CONTAINER_CONTENT')

          ###################################### 'Position','Modification','Color','Image',
          control_tab_2 = CONFIG_TABS_CONTAINERS.content.controls
          ######################################
          control_tab_3 = CONFIG_TABS_CONTAINERS_CONTENT.content.controls
          ######################################
          # control_2_inside = control_tab_2[0]                                   ## <==== MAIN_CONTROLS IN EACH TAB
          # control_2_inside.controls[0].content.controls[0]                    ## <==== MAIN_CONTROLS / NAME_OF_BOX
          # control_2_inside.controls[0].content.controls[1]                    ## <==== MAIN_CONTROLS / BLACK BOX  <=  with the input inside
          # control_2_inside.controls[0].content.controls[1].content.controls   ## <==== all controls inside BLACK BOX
          ############################ main black box
          # control_2_inside.controls[0].content.controls[1].visible = False
          # control_2_inside.controls[0].content.controls[1].update()
          ############################ widgets in main black box
          # control_2_inside.controls[0].content.controls[1].content.controls[0].visible = False
          # control_2_inside.controls[0].content.controls[1].content.controls[1].visible = False
          # control_2_inside.controls[0].content.controls[1].update()
          ############################ VALUES CHANGE IN EXEMPLE
          # tmp_value = control_2_inside.controls[0].content.controls[1].content.controls[0].widget = SELECT_DROPP_WIDGET_CONTAINER
          # tmp_value = control_2_inside.controls[0].content.controls[1].content.controls[1].widget = SELECT_DROPP_WIDGET_CONTAINER
          ############################ VALUES in main black box
          # control_tab_2                                                       <===== LIST OF ALL BOXES IN TAB2
          # control_2_inside.controls[0].content.controls[1].content.controls   <===== LIST OF ALL BOXES IN TAB2 WITH controls[0] INDEX 0 SELECTED
          ############################ TAB 2


          def insert_data_in_box_container(column_tab):
               """
               THIS METOD WALK IN TABS number #2 EACH COLUMN WITH WIDGETS INSIDE 4 COLUMNS

               """
               ############################ TAB 2 ############################
               if column_tab == '2_0':
                    control_2_inside = control_tab_2[0]  ## <==== MAIN_CONTROLS IN EACH TAB
                    tmp_value = control_2_inside.controls[0].content.controls[1].content.controls

               if column_tab == '2_1':
                    control_2_inside = control_tab_2[1]  ## <==== MAIN_CONTROLS IN EACH TAB
                    tmp_value = control_2_inside.controls[0].content.controls[1].content.controls

               if column_tab == '2_2':
                    control_2_inside = control_tab_2[2]  ## <==== MAIN_CONTROLS IN EACH TAB
                    tmp_value = control_2_inside.controls[0].content.controls[1].content.controls

               if column_tab == '2_3':
                    control_2_inside = control_tab_2[3]  ## <==== MAIN_CONTROLS IN EACH TAB
                    tmp_value = control_2_inside.controls[0].content.controls[1].content.controls
               ############################ FINISH ############################
               for _ in tmp_value:
                    # WALK ALL TABS TO INSERT THE VALUE THAT WE
                    _.controls[0].visible = True
                    _.widget  = SELECT_DROPP_WIDGET_CONTAINER

          def insert_data_in_box_container_content(column_tab):
               """
               THIS METOD WALK IN TABS number #3 EACH COLUMN WITH WIDGETS INSIDE 4 COLUMNS

               """
               ############################ TAB 3 ############################
               if column_tab == '3_0':
                    control_3_inside = control_tab_3[0]  ## <==== MAIN_CONTROLS IN EACH TAB
                    tmp_value_tab_widget = control_3_inside.controls[0].content.controls[1].content.controls

               if column_tab == '3_1':
                    control_3_inside = control_tab_3[1]  ## <==== MAIN_CONTROLS IN EACH TAB
                    tmp_value_tab_widget = control_3_inside.controls[0].content.controls[1].content.controls

               if column_tab == '3_2':
                    control_3_inside = control_tab_3[2]  ## <==== MAIN_CONTROLS IN EACH TAB
                    tmp_value_tab_widget = control_3_inside.controls[0].content.controls[1].content.controls

               if column_tab == '3_3':
                    control_3_inside = control_tab_3[3]  ## <==== MAIN_CONTROLS IN EACH TAB
                    tmp_value_tab_widget = control_3_inside.controls[0].content.controls[1].content.controls

               if column_tab == '3_4':
                    control_3_inside = control_tab_3[4]  ## <==== MAIN_CONTROLS IN EACH TAB
                    tmp_value_tab_widget = control_3_inside.controls[0].content.controls[1].content.controls

               if column_tab == '3_5':
                    control_3_inside = control_tab_3[5]  ## <==== MAIN_CONTROLS IN EACH TAB
                    tmp_value_tab_widget = control_3_inside.controls[0].content.controls[1].content.controls

               if column_tab == '3_6':
                    control_3_inside = control_tab_3[6]  ## <==== MAIN_CONTROLS IN EACH TAB
                    tmp_value_tab_widget = control_3_inside.controls[0].content.controls[1].content.controls

               if column_tab == '3_7':
                    control_3_inside = control_tab_3[7]  ## <==== MAIN_CONTROLS IN EACH TAB
                    tmp_value_tab_widget = control_3_inside.controls[0].content.controls[1].content.controls
               ############################ FINISH ############################
               # NEED CHECK IF THE WIDGET IT'S IN LIST_KEYS_DICT_USED
               # IF IS TRUE THE CONTAINER CONFIG
               #
               # WILL PUT          VISIBLE TRUE
               # IF NOT WILL PUT   VISIBLE OFF
               # print(LIST_KEYS_DICT_USED)

               for _ in tmp_value_tab_widget:
                    # WALK ALL TABS TO INSERT THE VALUE THAT WE

                    # if _.id_name_widget_dict in LIST_KEYS_DICT_USED:
                    if _.id_name_widget_dict in SELECT_DROPP_WIDGET_CONTAINER_CONTENT.__dir__():
                         data = _.id_name_widget_dict in SELECT_DROPP_WIDGET_CONTAINER_CONTENT.__dir__()

                         # print(_.id_name_widget_dict,data)

                         # print(SELECT_DROPP_WIDGET_CONTAINER_CONTENT._wrap_attr_dict('name')  )
                         # print(SELECT_DROPP_WIDGET_CONTAINER_CONTENT._Control__attrs  )


                         # FILTER THAT IS USE TO COMPARE WIDGET SELECTED
                         # if _.id_name_widget_dict in LIST_KEYS_DICT_USED or dict of all widget inside widget_editor.py

                         _.controls[0].visible = True
                         _.widget  = SELECT_DROPP_WIDGET_CONTAINER_CONTENT
                         _.update()  #<==== update exactly widget
                         # print(_.id_name_widget_dict,'<======== widget')
                    else:
                         _.controls[0].visible = False
                         _.widget  = SELECT_DROPP_WIDGET_CONTAINER_CONTENT
                         _.update()  #<==== update exactly widget

               # control_3_inside = control_tab_3[0]  ## <==== MAIN_CONTROLS IN EACH TAB
               # tmp_value_tab_widget = control_3_inside.controls[0].content.controls[1].content.controls[0].update()

          if BOOL_SHOW_SELECTED:
               ############################ TAB 2

               CONFIG_TABS_CONTAINERS.visible = True
               CONFIG_TABS_CONTAINERS.update()

               insert_data_in_box_container(column_tab='2_0')
               insert_data_in_box_container(column_tab='2_1')
               insert_data_in_box_container(column_tab='2_2')
               insert_data_in_box_container(column_tab='2_3')

               ############################ TAB 3
               CONFIG_TABS_CONTAINERS_CONTENT.visible = True
               CONFIG_TABS_CONTAINERS_CONTENT.update()

               insert_data_in_box_container_content(column_tab='3_0')
               insert_data_in_box_container_content(column_tab='3_1')
               insert_data_in_box_container_content(column_tab='3_2')
               insert_data_in_box_container_content(column_tab='3_3')
               insert_data_in_box_container_content(column_tab='3_4')
               insert_data_in_box_container_content(column_tab='3_5')
               insert_data_in_box_container_content(column_tab='3_6')
               insert_data_in_box_container_content(column_tab='3_7')

          else:
               # tmp_value = control_2_inside.controls[0].content.controls[1].content.controls
               ############################ TAB 2
               CONFIG_TABS_CONTAINERS.visible = False
               CONFIG_TABS_CONTAINERS.update()
               ############################ TAB 3
               CONFIG_TABS_CONTAINERS_CONTENT.visible = False
               CONFIG_TABS_CONTAINERS_CONTENT.update()





          # control_2_inside.controls[0].content.controls[1].content.update()
          # control_2_inside.controls[0].content.controls[1].update()
          # control_2_inside.controls[0].content.update()


          # print(control_tab_2)
          # for index_main , value in enumerate(control_tab_2):
          #      # WALK TROUGHT TAB2 CONTAINERS
          #      all_cantainers = control_tab_2[index_main].controls[0]
          #      # tmp_value = control_2_inside.controls[ index_main ].content.controls[1].content.controls
          #      # for _ in tmp_value:
          #           # _.widget = SELECT_DROPP_WIDGET_CONTAINER
          #      # print(value.controls[index_main])
          #      print(all_cantainers)


          # print(tmp_value)
          # CONFIG_TABS_CONTAINERS.update()

     def action_button(self,action):

          ###############################################################

          if action == 'delete':
               touch_widget_in_phone = GLOBAL_VAR(get_global_var='LIST_SELECTED_WIDGETS')

               # get the corret way to delete widget <===
               if touch_widget_in_phone:
                   page           = GLOBAL_VAR(get_global_var='PAGE')
                   id_widget      = page.get_control(touch_widget_in_phone.uid)
                   get_control_id = f"_{int(id_widget.uid.replace('_','')) - 2}" # <===== Stack()
                   page_control   = page.get_control(get_control_id)
                   page_control.clean()
                   del page_control._Control__previous_children
                   del page_control
                   GLOBAL_VAR(set_global_var={'LIST_SELECTED_WIDGETS':[]})

          if action == 'rotation':
               self.phone_widget_container.controls[0].width , self.phone_widget_container.controls[0].height = self.phone_widget_container.controls[0].height , self.phone_widget_container.controls[0].width
               self.phone_widget_container.controls[0].update()

               if self.phone_widget_container.controls[0].width >= 600:
                    self.menu_right_container.visible = False if self.menu_right_container.visible else True
                    self.menu_left_container.visible  = False if self.menu_right_container.visible else True
                    self.menu_left_container.update()
                    self.menu_right_container.update()

               else:
                    self.Drop_LiteMenuUpContainer.update()

          if action == 'LIGHT / DARK':
               self.phone_widget_container.controls[0].bgcolor = ft.colors.WHITE  if self.phone_widget_container.controls[0].bgcolor == '#070707' else '#070707'
               self.phone_widget_container.controls[0].update()


          ###############################################################
          if action == 'SMARTPHONE':
               self.phone_widget_container.controls[0].width  = 295
               self.phone_widget_container.controls[0].height = 566
               self.phone_widget_container.controls[0].update()


               self.menu_left_container.visible  = True
               self.menu_right_container.visible = True
               self.menu_left_container.update()
               self.menu_right_container.update()

          if action == 'TABLET':

               #################### Phone Container offset
               self.phone_widget_container.controls[0].width  = 460
               self.phone_widget_container.controls[0].height = 625
               self.phone_widget_container.controls[0].update()

               self.menu_left_container.visible  = True
               self.menu_right_container.visible = True
               self.menu_left_container.update()
               self.menu_right_container.update()

          if action == 'PC':
               self.phone_widget_container.controls[0].width  = 780
               self.phone_widget_container.controls[0].height = 525
               self.phone_widget_container.controls[0].update()

               self.menu_right_container.visible = False if self.menu_right_container.visible else True
               self.menu_left_container.visible  = False if self.menu_right_container.visible else True
               self.menu_left_container.update()
               self.menu_right_container.update()

          if action == 'SHOW PC':
               self.width_  = 780

               if self.menu_left_container.visible and self.menu_right_container.visible:
                    self.menu_left_container.visible  = False
                    self.menu_right_container.visible = False

               elif not self.menu_left_container.visible and not self.menu_right_container.visible:
                    if self.phone_widget_container.controls[0].width >= 500:
                         self.phone_widget_container.controls[0].width  = 460
                         self.phone_widget_container.controls[0].height = 625
                         self.phone_widget_container.controls[0].update()

                    self.menu_left_container.visible  = True
                    self.menu_right_container.visible = True

               elif not self.menu_left_container.visible and self.menu_right_container.visible:
                    self.menu_left_container.visible  = False
                    self.menu_right_container.visible = False

               elif self.menu_left_container.visible and not self.menu_right_container.visible:
                    self.menu_left_container.visible  = False
                    self.menu_right_container.visible = False

               self.menu_left_container.update()
               self.menu_right_container.update()

     def action_windows(self,action):
          self.phone_widget_container.controls[0].width , self.phone_widget_container.controls[0].height = self.phone_widget_container.controls[0].height , self.phone_widget_container.controls[0].width
          self.phone_widget_container.controls[0].update()


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

     def main(page: ft.Page):
          ###################### CONFIGURATION
          # page.title                   = "Containers - clickable and not"
          # page.window_title_bar_hidden   = True
          # page.window_title_bar_buttons_hidden = True
          # page.window_focused            = True
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
          page.window_left               = 20
          page.window_top                = 20
          # page.window_center()
          ###################### SIZE
          page.window_height           = 400
          # page.window_height             = 800
          # page.window_height             = 715
          page.window_width            = 600
          # page.window_width            = 1200
          page.padding                   = 0
          page.spacing                   = 0
          page.expand                    = True
          Lite_MenuUpContainer = LiteMenuUpContainer()
          page.add(Lite_MenuUpContainer)
          page.update()
     ft.app(
            # assets_dir   = "assets",
            target         = main,
            # port         = 8080,
            # view         = ft.AppView.WEB_BROWSER, #view=ft.WEB_BROWSER,
            # web_renderer = ft.WebRenderer.HTML
            )
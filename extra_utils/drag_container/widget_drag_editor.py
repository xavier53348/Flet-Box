from extra_utils.drag_container.dragg_widget import DraggWidget
from extra_utils.settings_var.settings_widget import global_var, get_global_var

import flet as ft

class Build_Drag_Editor(ft.UserControl):
     """
    Center Box that contain the phone to add Widget

    Note:
        How build Dragging Widget.

    1.  Make a Dragg Box.

        - We need crate the Dragg
            * widget = Widget Name
            * color  = Color of the box Dragg
            * icons  = icons of the box Dragg

            self.RowDragg  = DraggWidget( widget='Row' ,color='BLUE' ,icons= ft.icons.BURST_MODE_ROUNDED)

        - After we need add manual in [ drag_container_to_phone ]

           ft.Container(
                    content=ft.GridView(
                                        ##################### PROPERTY GRIDVIEW
                                        runs_count=3,                                             # column's number
                                        run_spacing=8,                                            # space between widget
                                        padding=4,
                                        spacing=8,                                                # space widget left right
                                        expand=1,
                                        ##################### WIDGETS
                                        controls=[  ##################### CONTROLS
                                                    self.RowDragg,
                                                 ],

    2.  Go to infinity_box_layer_one.py and add Manually.

        - 'extra_utils/drag_container/infinity_box_layer_one.py'

        - we need build the Container that will have the drop Widget inside

        Exemple how will be build

           "Row": [    ft.Container(bgcolor='blue',alignment=ft.alignment.center,padding=ft.padding.all(4),border=ft.border.all(0.8, ft.colors.BLACK),tooltip='Row',
                   on_hover=lambda _:self.resetClick(),
                   on_click=lambda _:self.touchWidgetIndex(self.infinityDropWidget),
                   content=ft.Row( scroll="ALWAYS",
                        controls= [
                                       ],),),
              ],

     """

     def __init__(self,data='Erase this test'):
          super().__init__()
          # self.title='data'
          self.title=data
          # self.dropDragg= DropDragg()

     def build(self):
        ####################### CONTROLS
        # VIEW_COLUMN_ROUNDED
        # TABLE_ROWS_ROUNDED
        # WIDGETS_ROUNDED
        # WEB_STORIES_ROUNDED
        # icons.FORMAT_SIZE_ROUNDED <=== texto
        # icons.FORMAT_COLOR_FILL_ROUNDED <== color

        ####################### CONTAINERS LAYOUTS
        self.RowDragg  = DraggWidget( widget='Row'            ,color='BLUE'   ,icons= ft.icons.BURST_MODE_ROUNDED)
        self.ColDragg  = DraggWidget( widget='Column'         ,color='RED'    ,icons= ft.icons.WRAP_TEXT_ROUNDED)
        self.GriDragg  = DraggWidget( widget='GridView'       ,color='PURPLE' ,icons= ft.icons.WIDGETS_ROUNDED )
        self.StaDragg  = DraggWidget( widget='Stack'          ,color='YELLOW' ,icons= ft.icons.JOIN_RIGHT_SHARP)

        ####################### SPACE LAYOUTS
        self.DivDragg  = DraggWidget( widget='Divider'        ,color='CYAN'   ,icons= ft.icons.HORIZONTAL_RULE)
        self.VerDragg  = DraggWidget( widget='Vertical'       ,color='CYAN'   ,icons= ft.icons.SAFETY_DIVIDER_ROUNDED)

        ####################### IMAGE WIDGET
        self.ImagDragg = DraggWidget( widget='Image'          ,color='CYAN'   ,icons= ft.icons.IMAGE)
        self.CircDragg = DraggWidget( widget='Avatar'         ,color='CYAN'   ,icons= ft.icons.ACCOUNT_CIRCLE_ROUNDED)
        self.Ico_Dragg = DraggWidget( widget='Icon'           ,color='CYAN'   ,icons= ft.icons.ADD_REACTION_OUTLINED)

        ####################### TEXT  WIDGET
        self.TexsDragg = DraggWidget( widget='Text'           ,color='CYAN'   ,icons= ft.icons.TEXT_FIELDS)
        self.TexfDragg = DraggWidget( widget='Text Field'     ,color='CYAN'   ,icons= ft.icons.INPUT)

        ####################### BUTTONS WIDGET
        self.ElevDragg = DraggWidget( widget='Elevated Button',color='CYAN'   ,icons= ft.icons.EDIT_ATTRIBUTES_ROUNDED)
        self.TextDragg = DraggWidget( widget='Text Button'    ,color='CYAN'   ,icons= ft.icons.ABC_ROUNDED)
        self.IconDragg = DraggWidget( widget='Icon Button'    ,color='CYAN'   ,icons= ft.icons.ADD_LINK_SHARP)
        self.FillDragg = DraggWidget( widget='Filled'         ,color='CYAN'   ,icons= ft.icons.EDIT_ATTRIBUTES_ROUNDED)
        self.TonaDragg = DraggWidget( widget='Tonal'          ,color='CYAN'   ,icons= ft.icons.EDIT_ATTRIBUTES_ROUNDED)
        self.OutlDragg = DraggWidget( widget='Outline'        ,color='CYAN'   ,icons= ft.icons.EDIT_ATTRIBUTES_OUTLINED)

        ####################### SELECTIONS WIDGET
        self.ChecDragg = DraggWidget( widget='Checkbox'       ,color='CYAN'   ,icons= ft.icons.CHECK_ROUNDED)
        self.CupeDragg = DraggWidget( widget='Cupertino'      ,color='CYAN'   ,icons= ft.icons.CHECK_BOX_ROUNDED)
        self.ChiSDragg = DraggWidget( widget='Slider'         ,color='CYAN'   ,icons= ft.icons.COMMIT_OUTLINED)
        self.CupSDragg = DraggWidget( widget='Switch'         ,color='CYAN'   ,icons= ft.icons.SWIPE_RIGHT_ALT_ROUNDED)
        self.ChipDragg = DraggWidget( widget='Chip'           ,color='CYAN'   ,icons= ft.icons.CLEAR_ALL)

        self.RadiDragg = DraggWidget( widget='Radio'          ,color='CYAN'   ,icons= ft.icons.RADIO_BUTTON_OFF)
        self.CupRDragg = DraggWidget( widget='Cup Radio'      ,color='CYAN'   ,icons= ft.icons.RADIO_BUTTON_ON)

        ####################### ALERTS STATUS

        ####################### WIDGETS STATUS

        ####################### ESPECIAL WIDGET

        ####################### CHARTS LAYOUTS


        drag_container_to_phone =ft.Container( ###################### LEFT DROP CONTAINER
                                    ##################### PROPERTY COLUMN
                                    ##################### [rotate,offset] , [scale,aspect_ratio] , [visible,disabled]
                                    # expand=True,
                                    ink           = False,                                                          # click effect ripple
                                    # bgcolor     = ft.colors.BLACK12,                                              # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                                    bgcolor       = ft.colors.BLACK38,                                              # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                                    padding       = ft.padding.all(8),    # inside box                              # padding.only(left=8, top=8, right=8, bottom=8),
                                    margin        = ft.margin.all(0),     # outside box                             # margin.only (left=8, top=8, right=8, bottom=8),
                                    alignment     = ft.alignment.center,                                            # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right.    posicionamiento adentro widget
                                    border_radius = ft.border_radius.all(30),                                       # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                                    # border      = ft.border.all(2, ft.colors.BLACK),                              # ft.border.only(Left=8, top=8, right=8, bottom=8),
                                    ######################
                                    # image_src   = f"dragg_container3.jpg",
                                    image_src     = f"dragg_container.jpg",
                                    image_opacity = 0.03,
                                    image_fit     = 'FILL',                                            # CONTAIN, FILL, FILL, FIT_HEIGHT, FIT_WIDTH, SCALE_DOWN
                                    ######################
                                    width         = 280,
                                    # height      = 150,
                                    # tooltip     = 'Container',
                                    ##################### EFFECTS
                                    # gradient    = ft.LinearGradient( begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=[ft.colors.BLUE, ft.colors.YELLOW],),
                                    # gradient    = ft.RadialGradient( colors=[ft.colors.BLACK12, ft.colors.BLACK45],),
                                    ##################### WIDGETS
                                    content=ft.Column(
                                        ##################### PROPERTY BOX
                                        # expand               = True,
                                        # alignment            = ft.MainAxisAlignment.SPACE_AROUND,                       # horizontal <=> START,CENTER,END SPACE_BETWEEN SPACE_AROUND SPACE_EVENLY
                                        # horizontal_alignment = ft.CrossAxisAlignment.CENTER,                            # vertical       START,CENTER END
                                        ##################### LET MAKE SCROLL IN LONG QUANTITY
                                        scroll                 = 'HIDDEN',                                                # center widget
                                        # tight                = True,
                                        ##################### ADAPT TO SCREEN
                                        # wrap                 = True,                                                    # justify in all screen
                                        # spacing              = 8,                                                       # space widget left right
                                        # run_spacing          = 8,                                                       # space widget up down
                                        ##################### WIDGETS
                                        controls=[
                                                    ft.Container( ##################### CONTAINERS LAYOUTS
                                                                ##################### [rotate,offset] , [scale,aspect_ratio] , [visible,disabled]
                                                                # expand        = True,
                                                                ink             = False,                                  # click effect ripple
                                                                bgcolor         = ft.colors.BLACK26,                      # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                                                                # padding       = ft.padding.only(left=12), # inside box  # padding.only(left=8, top=8, right=8, bottom=8),
                                                                margin          = ft.margin.all(0),  # outside box        # margin.only (left=8, top=8, right=8, bottom=8),
                                                                alignment       = ft.alignment.center,                    # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right. posicionamiento adentro widget
                                                                border_radius   = ft.border_radius.all(30),               # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                                                                #####################
                                                                # image_src     = f"/home/mjay/Pictures/3d_neon_pink-2560x1440.jpg",
                                                                # image_opacity = 0.1,
                                                                # image_fit     = 'COVER',                                # CONTAIN, COVER, FILL, FIT_HEIGHT, FIT_WIDTH, SCALE_DOWN
                                                                #####################
                                                                width           = 150,
                                                                # height        = 150,
                                                                ##################### WIDGETS
                                                        content = ft.Text(
                                                                    value       = "Containers Layouts",
                                                                    text_align  = ft.TextAlign.CENTER,                   # LEFT (default),RIGHT,CENTER,JUSTIFY,START,END
                                                                    weight      = ft.FontWeight.BOLD,                    # NORMAL (default), BOLD, W_100, W_200,  W_300, W_400, W_500, W_600, W_700, W_800,W_900
                                                                    font_family = "Consolas", #"Consolas ,RobotoSlab
                                                                    color       = ft.colors.BLUE,
                                                                ),),#<=== NOTE COMA <==> ERASE COMA IF MAKE 1 ERROR
                                                    ft.Container( ##################### CONTAINERS LAYOUTS
                                                                ##################### [rotate,offset] , [scale,aspect_ratio] , [visible,disabled]
                                                                # expand = True,
                                                                ink       = False,                                       # click effect ripple
                                                                bgcolor   = ft.colors.BLACK26,                           # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                                                                padding   = ft.padding.all(2),    # inside box           # padding.only(left=8, top=8, right=8, bottom=8),
                                                                margin    = ft.margin.all(2),     # outside box          # margin.only (left=8, top=8, right=8, bottom=8),
                                                                alignment = ft.alignment.center,                         # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right.    posicionamiento adentro widget
                                                                border_radius= ft.border_radius.all(16),                 # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                                                                # border        = ft.border.all(2, ft.colors.BLACK),     # ft.border.only(Left=8, top=8, right=8, bottom=8),
                                                                ######################
                                                                # image_src     = f"/home/mjay/Pictures/3d_neon_pink-2560x1440.jpg",
                                                                # image_opacity = 0.1,
                                                                # image_fit     = 'COVER',                                            # CONTAIN, COVER, FILL, FIT_HEIGHT, FIT_WIDTH, SCALE_DOWN
                                                                ######################
                                                                # scroll        = True,
                                                                # width         = 150,
                                                                # height        = 150,
                                                                # tooltip       = 'Container',
                                                                ##################### EFFECTS
                                                                # gradient      = ft.LinearGradient( begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=[ft.colors.BLUE, ft.colors.YELLOW],),
                                                                # gradient      = ft.RadialGradient( colors=[ft.colors.YELLOW, ft.colors.BLUE],),
                                                                ##################### WIDGETS
                                                                content = ft.GridView(
                                                                                    ##################### PROPERTY GRIDVIEW
                                                                                    runs_count           = 3,           # column's number
                                                                                    run_spacing          = 8,           # space between widget
                                                                                    padding              = 4,
                                                                                    spacing              = 8,           # space widget left right
                                                                                    expand               = 1,
                                                                                    # child_aspect_ratio = 4,           # scale of widget
                                                                                    # horizontal         = False,
                                                                                    # max_extent         = 150,         # lateral_size max
                                                                                    ##################### WIDGETS
                                                                                    controls=[  ##################### CONTROLS
                                                                                                self.RowDragg,
                                                                                                self.ColDragg,
                                                                                                self.GriDragg,
                                                                                                self.StaDragg,
                                                                                             ],
                                                                ),#<=== NOTE COMA [NOTE]                     for x in range(1,50): widget.content.controls.append(ft.ElevatedButton("press buttom",tooltip='buttom'))
                                                                ##################### EVENTS
                                                                # on_click=lambda _:print(_),                            # on_hover=print('on click over'), on_long_press=print('long press'),
                                                    ),#<=== CONTAINERS

                                                    ft.Container( ##################### SPACE LAYOUTS
                                                                ##################### [rotate,offset] , [scale,aspect_ratio] , [visible,disabled]
                                                                # expand        = True,
                                                                ink             = False,                                                      # click effect ripple
                                                                bgcolor         = ft.colors.BLACK26,                                          # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                                                                # padding       = ft.padding.only(left=12), # inside box                      # padding.only(left=8, top=8, right=8, bottom=8),
                                                                margin          = ft.margin.all(0),  # outside box                            # margin.only (left=8, top=8, right=8, bottom=8),
                                                                alignment       = ft.alignment.center,                                        # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right. posicionamiento adentro widget
                                                                border_radius   = ft.border_radius.all(30),                                   # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                                                                ######################
                                                                # image_src     = f"/home/mjay/Pictures/3d_neon_pink-2560x1440.jpg",
                                                                # image_opacity = 0.1,
                                                                # image_fit     = 'COVER',                                                    # CONTAIN, COVER, FILL, FIT_HEIGHT, FIT_WIDTH, SCALE_DOWN
                                                                ######################
                                                                width           = 150,
                                                                # height        = 150,
                                                                ##################### WIDGETS
                                                                content=ft.Text(
                                                                            value       = "Space Layouts",
                                                                            text_align  = ft.TextAlign.CENTER,                                # LEFT (default),RIGHT,CENTER,JUSTIFY,START,END
                                                                            weight      = ft.FontWeight.BOLD,                                 # NORMAL (default), BOLD, W_100, W_200,  W_300, W_400, W_500, W_600, W_700, W_800,W_900
                                                                            font_family = "Consolas", #"Consolas ,RobotoSlab
                                                                            color       = ft.colors.BLUE,
                                                                ),),#<=== NOTE COMA <==> ERASE COMA IF MAKE 1 ERROR
                                                    ft.Container( ##################### SPACE LAYOUTS
                                                                ##################### [rotate,offset] , [scale,aspect_ratio] , [visible,disabled]
                                                                # expand=True,
                                                                ink=False,                                                                   # click effect ripple
                                                                bgcolor         = ft.colors.BLACK26,                                         # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                                                                padding         = ft.padding.all(2),    # inside box                         # padding.only(left=8, top=8, right=8, bottom=8),
                                                                margin          = ft.margin.all(2),     # outside box                        # margin.only (left=8, top=8, right=8, bottom=8),
                                                                alignment       = ft.alignment.center,                                       # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right.    posicionamiento adentro widget
                                                                border_radius   = ft.border_radius.all(16),                                  # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                                                                # border        = ft.border.all(2, ft.colors.BLACK),                         # ft.border.only(Left=8, top=8, right=8, bottom=8),
                                                                #####################
                                                                # image_src     = f"/home/mjay/Pictures/3d_neon_pink-2560x1440.jpg",
                                                                # image_opacity = 0.1,
                                                                # image_fit     = 'COVER',                                            # CONTAIN, COVER, FILL, FIT_HEIGHT, FIT_WIDTH, SCALE_DOWN
                                                                #####################
                                                                # scroll        = True,
                                                                # width         = 150,
                                                                # height        = 150,
                                                                # tooltip       = 'Container',
                                                                ##################### EFFECTS
                                                                # gradient      = ft.LinearGradient( begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=[ft.colors.BLUE, ft.colors.YELLOW],),
                                                                # gradient      = ft.RadialGradient( colors=[ft.colors.YELLOW, ft.colors.BLUE],),
                                                                ##################### WIDGETS
                                                                content=ft.GridView(
                                                                                    ##################### PROPERTY GRIDVIEW
                                                                                    runs_count           = 3,                               # column's number
                                                                                    run_spacing          = 8,                               # space between widget
                                                                                    padding              = 4,
                                                                                    spacing              = 8,                               # space widget left right
                                                                                    expand               = 1,
                                                                                    # child_aspect_ratio = 4,                               # scale of widget
                                                                                    # horizontal         = False,
                                                                                    # max_extent         = 150,                             # lateral_size max
                                                                                    ##################### WIDGETS
                                                                            controls=[  ##################### CONTROLS
                                                                                        self.DivDragg,
                                                                                        self.VerDragg,
                                                                                        # self.RowDragg,
                                                                                        # self.ColDragg,
                                                                                        # self.GriDragg,
                                                                                        # self.StaDragg,
                                                                                     ],
                                                                ),#<=== NOTE COMA [NOTE]                     for x in range(1,50): widget.content.controls.append(ft.ElevatedButton("press buttom",tooltip='buttom'))
                                                                ##################### EVENTS
                                                                # on_click=lambda _:print(_),                            # on_hover=print('on click over'), on_long_press=print('long press'),
                                                    ),#<=== SPACE

                                                    ft.Container( ##################### IMAGE WIDGET
                                                                ##################### [rotate,offset] , [scale,aspect_ratio] , [visible,disabled]
                                                                # expand        = True,
                                                                ink             = False,                                                # click effect ripple
                                                                bgcolor         = ft.colors.BLACK26,                                    # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                                                                # padding       = ft.padding.only(left=12), # inside box                # padding.only(left=8, top=8, right=8, bottom=8),
                                                                margin          = ft.margin.all(0),  # outside box                      # margin.only (left=8, top=8, right=8, bottom=8),
                                                                alignment       = ft.alignment.center,                                  # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right. posicionamiento adentro widget
                                                                border_radius   = ft.border_radius.all(30),                             # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                                                                #####################
                                                                # image_src     = f"/home/mjay/Pictures/3d_neon_pink-2560x1440.jpg",
                                                                # image_opacity = 0.1,
                                                                # image_fit     ='COVER',                                            # CONTAIN, COVER, FILL, FIT_HEIGHT, FIT_WIDTH, SCALE_DOWN
                                                                #####################
                                                                width           = 150,
                                                                # height        = 150,
                                                                ##################### WIDGETS
                                                            content=ft.Text(
                                                                        value       = "Images Widgets",
                                                                        text_align  = ft.TextAlign.CENTER,                              # LEFT (default),RIGHT,CENTER,JUSTIFY,START,END
                                                                        weight      = ft.FontWeight.BOLD,                               # NORMAL (default), BOLD, W_100, W_200,  W_300, W_400, W_500, W_600, W_700, W_800,W_900
                                                                        font_family = "Consolas", #"Consolas ,RobotoSlab
                                                                        color=ft.colors.BLUE,
                                                            ),),#<=== NOTE COMA <==> ERASE COMA IF MAKE 1 ERROR
                                                    ft.Container( ##################### IMAGE WIDGET
                                                                ##################### [rotate,offset] , [scale,aspect_ratio] , [visible,disabled]
                                                                # expand=True,
                                                                ink=False,                                                              # click effect ripple
                                                                bgcolor         = ft.colors.BLACK26,                                    # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                                                                padding         = ft.padding.all(2),    # inside box                    # padding.only(left=8, top=8, right=8, bottom=8),
                                                                margin          = ft.margin.all(2),     # outside box                   # margin.only (left=8, top=8, right=8, bottom=8),
                                                                alignment       = ft.alignment.center,                                  # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right.    posicionamiento adentro widget
                                                                border_radius   = ft.border_radius.all(16),                             # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                                                                # border        = ft.border.all(2, ft.colors.BLACK),                    # ft.border.only(Left=8, top=8, right=8, bottom=8),
                                                                #####################
                                                                # image_src     = f"/home/mjay/Pictures/3d_neon_pink-2560x1440.jpg",
                                                                # image_opacity = 0.1,
                                                                # image_fit     = 'COVER',                                              # CONTAIN, COVER, FILL, FIT_HEIGHT, FIT_WIDTH, SCALE_DOWN
                                                                #####################
                                                                # scroll        = True,
                                                                # width         = 150,
                                                                # height        = 150,
                                                                # tooltip       = 'Container',
                                                                ##################### EFFECTS
                                                                # gradient      = ft.LinearGradient( begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=[ft.colors.BLUE, ft.colors.YELLOW],),
                                                                # gradient      = ft.RadialGradient( colors=[ft.colors.YELLOW, ft.colors.BLUE],),
                                                                ##################### WIDGETS
                                                            content=ft.GridView(
                                                                                ##################### PROPERTY GRIDVIEW
                                                                                runs_count           = 3,                                   # column's number
                                                                                run_spacing          = 8,                                   # space between widget
                                                                                padding              = 4,
                                                                                spacing              = 8,                                   # space widget left right
                                                                                expand               = 1,
                                                                                # child_aspect_ratio = 4,                                   # scale of widget
                                                                                # horizontal         = False,
                                                                                # max_extent         = 150,                                 # lateral_size max
                                                                                ##################### WIDGETS
                                                                        controls=[  ##################### CONTROLS
                                                                                    # self.RowDragg,
                                                                                    self.ImagDragg,
                                                                                    self.CircDragg,
                                                                                    self.Ico_Dragg,
                                                                                    # self.ColDragg,
                                                                                    # self.GriDragg,
                                                                                    # self.StaDragg,
                                                                                 ],
                                                            ),#<=== NOTE COMA [NOTE]                     for x in range(1,50): widget.content.controls.append(ft.ElevatedButton("press buttom",tooltip='buttom'))
                                                                ##################### EVENTS
                                                                # on_click=lambda _:print(_),                            # on_hover=print('on click over'), on_long_press=print('long press'),
                                                    ),#<=== IMAGE WIDGET

                                                    ft.Container( ##################### TEXT WIDGET
                                                                ##################### [rotate,offset] , [scale,aspect_ratio] , [visible,disabled]
                                                                # expand        = True,
                                                                ink             = False,                                                      # click effect ripple
                                                                bgcolor         = ft.colors.BLACK26,                                          # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                                                                # padding       = ft.padding.only(left=12), # inside box                      # padding.only(left=8, top=8, right=8, bottom=8),
                                                                margin          = ft.margin.all(0),  # outside box                            # margin.only (left=8, top=8, right=8, bottom=8),
                                                                alignment       = ft.alignment.center,                                        # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right. posicionamiento adentro widget
                                                                border_radius   = ft.border_radius.all(30),                                   # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                                                                #####################
                                                                # image_src     = f"/home/mjay/Pictures/3d_neon_pink-2560x1440.jpg",
                                                                # image_opacity = 0.1,
                                                                # image_fit     = 'COVER',                                                    # CONTAIN, COVER, FILL, FIT_HEIGHT, FIT_WIDTH, SCALE_DOWN
                                                                #####################
                                                                width           = 150,
                                                                # height        = 150,
                                                                ##################### WIDGETS
                                                                content = ft.Text(
                                                                            value       = "Texts Widgets",
                                                                            text_align  = ft.TextAlign.CENTER,                                # LEFT (default),RIGHT,CENTER,JUSTIFY,START,END
                                                                            weight      = ft.FontWeight.BOLD,                                 # NORMAL (default), BOLD, W_100, W_200,  W_300, W_400, W_500, W_600, W_700, W_800,W_900
                                                                            font_family = "Consolas", #"Consolas ,RobotoSlab
                                                                            color       = ft.colors.BLUE,
                                                                ),),#<=== NOTE COMA <==> ERASE COMA IF MAKE 1 ERROR
                                                    ft.Container( ##################### TEXT WIDGET
                                                                ##################### [rotate,offset] , [scale,aspect_ratio] , [visible,disabled]
                                                                # expand=True,
                                                                ink             = False,                                                # click effect ripple
                                                                bgcolor         = ft.colors.BLACK26,                                    # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                                                                padding         = ft.padding.all(2),    # inside box                    # padding.only(left=8, top=8, right=8, bottom=8),
                                                                margin          = ft.margin.all(2),     # outside box                   # margin.only (left=8, top=8, right=8, bottom=8),
                                                                alignment       = ft.alignment.center,                                  # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right.    posicionamiento adentro widget
                                                                border_radius   = ft.border_radius.all(16),                             # ft.border.only(Left=8, top=8, right=8, bottom=8),
                                                                #####################
                                                                # image_src     = f"/home/mjay/Pictures/3d_neon_pink-2560x1440.jpg",
                                                                # image_opacity = 0.1,
                                                                # image_fit     = 'COVER',                                              # CONTAIN, COVER, FILL, FIT_HEIGHT, FIT_WIDTH, SCALE_DOWN
                                                                #####################
                                                                # scroll        = True,
                                                                # width         = 150,
                                                                # height        = 150,
                                                                # tooltip       = 'Container',
                                                                ##################### EFFECTS
                                                                # gradient      = ft.LinearGradient( begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=[ft.colors.BLUE, ft.colors.YELLOW],),
                                                                # gradient      = ft.RadialGradient( colors=[ft.colors.YELLOW, ft.colors.BLUE],),
                                                                ##################### WIDGETS
                                                        content=ft.GridView(
                                                                            ##################### PROPERTY GRIDVIEW
                                                                            runs_count           = 3,                                   # column's number
                                                                            run_spacing          = 8,                                   # space between widget
                                                                            padding              = 4,
                                                                            spacing              = 8,                                   # space widget left right
                                                                            expand               = 1,
                                                                            # child_aspect_ratio = 4,                                   # scale of widget
                                                                            # horizontal         = False,
                                                                            # max_extent         = 150,                                 # lateral_size max
                                                                            ##################### WIDGETS
                                                                    controls=[  ##################### CONTENT
                                                                                self.TexsDragg,
                                                                                self.TexfDragg,
                                                                             ],
                                                                ),#<=== NOTE COMA [NOTE]
                                                    ),#<=== TEXT

                                                    ft.Container( ##################### BUTTONS WIDGETS
                                                                ##################### [rotate,offset] , [scale,aspect_ratio] , [visible,disabled]
                                                                # expand        = True,
                                                                ink             = False,                                                # click effect ripple
                                                                bgcolor         = ft.colors.BLACK26,                                    # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                                                                # padding       = ft.padding.only(left=12), # inside box                # padding.only(left=8, top=8, right=8, bottom=8),
                                                                margin          = ft.margin.all(0),  # outside box                      # margin.only (left=8, top=8, right=8, bottom=8),
                                                                alignment       = ft.alignment.center,                                  # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right. posicionamiento adentro widget
                                                                border_radius   = ft.border_radius.all(30),                             # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                                                                #####################
                                                                # image_src     = f"/home/mjay/Pictures/3d_neon_pink-2560x1440.jpg",
                                                                # image_opacity = 0.1,
                                                                # image_fit     = 'COVER',                                              # CONTAIN, COVER, FILL, FIT_HEIGHT, FIT_WIDTH, SCALE_DOWN
                                                                #####################
                                                                width           = 150,
                                                                # height        = 150,
                                                                ##################### WIDGETS
                                                            content = ft.Text(
                                                                        value       = "Buttons Widgets",
                                                                        text_align  = ft.TextAlign.CENTER,                                    # LEFT (default),RIGHT,CENTER,JUSTIFY,START,END
                                                                        weight      = ft.FontWeight.BOLD,                                    # NORMAL (default), BOLD, W_100, W_200,  W_300, W_400, W_500, W_600, W_700, W_800,W_900
                                                                        font_family = "Consolas", #"Consolas ,RobotoSlab
                                                                        color       = ft.colors.BLUE,
                                                            ),),#<=== NOTE COMA <==> ERASE COMA IF MAKE 1 ERROR
                                                    ft.Container( ##################### BUTTONS WIDGETS
                                                                ##################### [rotate,offset] , [scale,aspect_ratio] , [visible,disabled]
                                                                # expand        = True,
                                                                ink             = False,                                                # click effect ripple
                                                                bgcolor         = ft.colors.BLACK26,                                    # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                                                                padding         = ft.padding.all(2),    # inside box                    # padding.only(left=8, top=8, right=8, bottom=8),
                                                                margin          = ft.margin.all(2),     # outside box                   # margin.only (left=8, top=8, right=8, bottom=8),
                                                                alignment       = ft.alignment.center,                                  # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right.    posicionamiento adentro widget
                                                                border_radius   = ft.border_radius.all(16),                             # ft.border.only(Left=8, top=8, right=8, bottom=8),
                                                                #####################
                                                                # image_src     = f"/home/mjay/Pictures/3d_neon_pink-2560x1440.jpg",
                                                                # image_opacity = 0.1,
                                                                # image_fit     = 'COVER',                                              # CONTAIN, COVER, FILL, FIT_HEIGHT, FIT_WIDTH, SCALE_DOWN
                                                                #####################
                                                                # scroll        = True,
                                                                # width         = 150,
                                                                # height        = 150,
                                                                # tooltip       = 'Container',
                                                                ##################### EFFECTS
                                                                # gradient      = ft.LinearGradient( begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=[ft.colors.BLUE, ft.colors.YELLOW],),
                                                                # gradient      = ft.RadialGradient( colors=[ft.colors.YELLOW, ft.colors.BLUE],),
                                                                ##################### WIDGETS
                                                        content = ft.GridView(
                                                                            ##################### PROPERTY GRIDVIEW
                                                                            runs_count           = 3,                                   # column's number
                                                                            run_spacing          = 8,                                   # space between widget
                                                                            padding              = 4,
                                                                            spacing              = 8,                                   # space widget left right
                                                                            expand               = 1,
                                                                            # child_aspect_ratio = 4,                                   # scale of widget
                                                                            # horizontal         = False,
                                                                            # max_extent         = 150,                                 # lateral_size max
                                                                            ##################### WIDGETS
                                                                    controls=[  ##################### CONTENT
                                                                                self.ElevDragg,
                                                                                self.TextDragg,
                                                                                self.IconDragg,
                                                                                self.FillDragg,
                                                                                self.TonaDragg,
                                                                                self.OutlDragg,
                                                                             ],
                                                        ),#<=== NOTE COMA [NOTE]                     for x in range(1,50): widget.content.controls.append(ft.ElevatedButton("press buttom",tooltip='buttom'))
                                                                ##################### EVENTS
                                                                # on_click=lambda _:print(_),                                          # on_hover=print('on click over'), on_long_press=print('long press'),
                                                    ),#<=== BUTTONS

                                                    ft.Container( ##################### SELECTION WIDGET
                                                                ##################### [rotate,offset] , [scale,aspect_ratio] , [visible,disabled]
                                                                # expand        = True,
                                                                ink             = False,                                               # click effect ripple
                                                                bgcolor         = ft.colors.BLACK26,                                   # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                                                                # padding       = ft.padding.only(left=12), # inside box               # padding.only(left=8, top=8, right=8, bottom=8),
                                                                margin          = ft.margin.all(0),  # outside box                     # margin.only (left=8, top=8, right=8, bottom=8),
                                                                alignment       = ft.alignment.center,                                 # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right. posicionamiento adentro widget
                                                                border_radius   = ft.border_radius.all(30),                            # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                                                                #####################
                                                                # image_src     = f"/home/mjay/Pictures/3d_neon_pink-2560x1440.jpg",
                                                                # image_opacity = 0.1,
                                                                # image_fit     = 'COVER',                                             # CONTAIN, COVER, FILL, FIT_HEIGHT, FIT_WIDTH, SCALE_DOWN
                                                                #####################
                                                                width           = 150,
                                                                # height        = 150,
                                                                ##################### WIDGETS
                                                        content=ft.Text(
                                                                    value       = "Selections Widgets",
                                                                    text_align  = ft.TextAlign.CENTER,                                 # LEFT (default),RIGHT,CENTER,JUSTIFY,START,END
                                                                    weight      = ft.FontWeight.BOLD,                                  # NORMAL (default), BOLD, W_100, W_200,  W_300, W_400, W_500, W_600, W_700, W_800,W_900
                                                                    font_family = "Consolas", #"Consolas ,RobotoSlab
                                                                    color       = ft.colors.BLUE,
                                                        ),),#<=== NOTE COMA <==> ERASE COMA IF MAKE 1 ERROR
                                                    ft.Container( ##################### SELECTION WIDGET
                                                                ##################### [rotate,offset] , [scale,aspect_ratio] , [visible,disabled]
                                                                # expand        = True,
                                                                ink             = False,                                               # click effect ripple
                                                                bgcolor         = ft.colors.BLACK26,                                   # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                                                                padding         = ft.padding.all(2),    # inside box                   # padding.only(left=8, top=8, right=8, bottom=8),
                                                                margin          = ft.margin.all(2),     # outside box                  # margin.only (left=8, top=8, right=8, bottom=8),
                                                                alignment       = ft.alignment.center,                                 # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right.    posicionamiento adentro widget
                                                                border_radius   = ft.border_radius.all(16),                            # ft.border.only(Left=8, top=8, right=8, bottom=8),
                                                                #####################
                                                                # image_src     = f"/home/mjay/Pictures/3d_neon_pink-2560x1440.jpg",
                                                                # image_opacity = 0.1,
                                                                # image_fit     = 'COVER',                                             # CONTAIN, COVER, FILL, FIT_HEIGHT, FIT_WIDTH, SCALE_DOWN
                                                                #####################
                                                                # scroll        = True,
                                                                # width         = 150,
                                                                # height        = 150,
                                                                # tooltip       = 'Container',
                                                                ##################### EFFECTS
                                                                # gradient      = ft.LinearGradient( begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=[ft.colors.BLUE, ft.colors.YELLOW],),
                                                                # gradient      = ft.RadialGradient( colors=[ft.colors.YELLOW, ft.colors.BLUE],),
                                                                ##################### WIDGETS
                                                        content=ft.GridView(
                                                                            ##################### PROPERTY GRIDVIEW
                                                                            runs_count           = 3,                                   # column's number
                                                                            run_spacing          = 8,                                   # space between widget
                                                                            padding              = 4,
                                                                            spacing              = 8,                                   # space widget left right
                                                                            expand               = 1,
                                                                            # child_aspect_ratio = 4,                                   # scale of widget
                                                                            # horizontal         = False,
                                                                            # max_extent         = 150,                                 # lateral_size max
                                                                            ##################### WIDGETS
                                                                    controls=[  ##################### CONTENT
                                                                                self.ChecDragg,
                                                                                self.CupeDragg,
                                                                                self.CupRDragg,
                                                                                self.CupSDragg,
                                                                                self.ChiSDragg,
                                                                                self.ChipDragg,
                                                                                self.RadiDragg,
                                                                             ],
                                                                ),#<=== NOTE COMA [NOTE]                     for x in range(1,50): widget.content.controls.append(ft.ElevatedButton("press buttom",tooltip='buttom'))
                                                                ##################### EVENTS
                                                                # on_click=lambda _:print(_),                                          # on_hover=print('on click over'), on_long_press=print('long press'),
                                                    ),#<=== SELECTION
                                                 ],
                                    ),#<=== NOTE COMA [NOTE]                     for x in range(1,50): widget.content.controls.append(ft.ElevatedButton("press buttom",tooltip='buttom'))
                                    ##################### EVENTS
                                    # on_click=lambda _:print(_),                                                                      # on_hover=print('on click over'), on_long_press=print('long press'),
                        )#<=== NOTE COMA
        return drag_container_to_phone
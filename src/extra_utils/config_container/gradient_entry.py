####################################################
import flet as ft
####################################################

class GradientEntry(ft.UserControl): ##################### PROPERTY
    """
    box_layout = ft.Container(content=ft.Text())

    Double_Widget = GradientEntry
    Double_Widget(config_widget='value',widget = box_layout),

    """
    color_1        = 'Black'
    color_2        = 'Teal'
    color_3        = None
    color_4        = None

    main_gradient  = None
    start_gradient = ' center_left '
    end_gradient   = ' top_right '
    data_color = list()
    effects_gradients = {
                            # " Linear ": ft.LinearGradient,
                            # " Radial ": ft.RadialGradient,
                            " top_left": ft.alignment.top_left,
                            " top_center": ft.alignment.top_center,
                            " top_right": ft.alignment.top_right,
                            " center_left": ft.alignment.center_left,
                            " center": ft.alignment.center,
                            " center_right": ft.alignment.center_right,
                            " bottom_left": ft.alignment.bottom_left,
                            " bottom_center": ft.alignment.bottom_center,
                            " bottom_right": ft.alignment.bottom_right,
                            " top_left ": ft.alignment.top_left,
                            " top_center ": ft.alignment.top_center,
                            " top_right ": ft.alignment.top_right,
                            " center_left ": ft.alignment.center_left,
                            " center ": ft.alignment.center,
                            " center_right ": ft.alignment.center_right,
                            " bottom_left ": ft.alignment.bottom_left,
                            " bottom_center ": ft.alignment.bottom_center,
                            " bottom_right ": ft.alignment.bottom_right,
                                }
    def __init__(self,config_widget='exemple [value,bgcolor,width,height] ....',widget=''):
        super().__init__()
        self.widget           = widget        # <=== widget
        self.attribute_widget = config_widget # <=== widget attribute

        ################# CONTAINER STR
        if self.attribute_widget == "gradient ":
            """top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right"""
            # gradient=ft.LinearGradient( begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=[ft.colors.BLUE, ft.colors.YELLOW],),

            self.options_tmp = [
                                    ft.dropdown.Option(" None "),
                                    ft.dropdown.Option(" Linear "),
                                    ft.dropdown.Option(" Radial "),
                                    ]
            self.options_tmp_1 = [
                                    ft.dropdown.Option(" top_left "),
                                    ft.dropdown.Option(" top_center "),
                                    ft.dropdown.Option(" top_right "),
                                    ft.dropdown.Option(" center_left "),
                                    ft.dropdown.Option(" center "),
                                    ft.dropdown.Option(" center_right "),
                                    ft.dropdown.Option(" bottom_left "),
                                    ft.dropdown.Option(" bottom_center "),
                                    ft.dropdown.Option(" bottom_right "),
                                    ]
            self.options_tmp_2 = [
                                    ft.dropdown.Option(" top_left"),
                                    ft.dropdown.Option(" top_center"),
                                    ft.dropdown.Option(" top_right"),
                                    ft.dropdown.Option(" center_left"),
                                    ft.dropdown.Option(" center"),
                                    ft.dropdown.Option(" center_right"),
                                    ft.dropdown.Option(" bottom_left"),
                                    ft.dropdown.Option(" bottom_center"),
                                    ft.dropdown.Option(" bottom_right"),
                                    ]
            self.attribute_widget_name_1 = 'Black'
            self.attribute_widget_name_2 = 'Teal'
            self.attribute_widget_name_3 = 'Color'
            self.attribute_widget_name_4 = 'Color'

    def build(self):
        self.main_gradient_widget = ft.Container(
                                        ##################### PROPERTY
                                        ink           = False,                                   # click effect ripple
                                        bgcolor       = "#3e4046",                               # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                                        padding       = ft.padding.all(0),    # inside box       # padding.only(left=8, top=8, right=8, bottom=8),
                                        alignment     = ft.alignment.center,                     # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right.    posicionamiento adentro widget
                                        border_radius = ft.border_radius.all(30),                # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                                        border        = ft.border.all(2, '#646871'),             # ft.border.only(Left=8, top=8, right=8, bottom=8),
                                        width         = 150,
                                        height        = 35,
                                        ##################### WIDGETS
                                        content=ft.Dropdown(
                                                            hint_text       = " None ",
                                                            width           = 140,
                                                            content_padding = ft.padding.only(left=0, top=0, right=8, bottom=14),
                                                            alignment       = ft.alignment.center_left,                            # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right.    posicionamiento adentro widget
                                                            border_radius   = ft.border_radius.all(15),                            # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                                                            border          = ft.InputBorder.NONE,
                                                            options         = self.options_tmp,
                                                            ##################### EVENTS
                                                    # on_change = lambda _: _.__dict__.get('value') if _.__dict__.get('data') == "green" else  _.__dict__.get('data'),
                                                    on_change   = lambda _:self.modify_widget_attributes(config_widget=_.__dict__.get('data'),value='form_gradient',widget=Drop_GradientEntry),
                                                    # on_change = lambda _:print(_.__dict__.get('data')),
                                                    # on_click  = lambda _:print(_),   # on_hover=print('on click over'), on_long_press=print('long press'),
                                                ),#<=== NOTE COMA <==> ERASE COMA IF MAKE 1 ERROR,

                                        ##################### EVENTS
                                        # on_click=lambda _:print(_),                            # on_hover=print('on click over'), on_long_press=print('long press'),
                                )#<=== NOTE COMA,
        Drop_GradientEntry = ft.Container(
                            ##################### PROPERTY COLUMN
                            ink           = False,                                                # click effect ripple
                            bgcolor       = ft.colors.BLACK45,                                    # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                            padding       = ft.padding.all(4),    # inside box                    # padding.only(left=8, top=8, right=8, bottom=8),
                            margin        = ft.margin.all(0),    # outside box                    # margin.only (left=8, top=8, right=8, bottom=8),
                            alignment     = ft.alignment.center,                                  # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right.    posicionamiento adentro widget
                            border_radius = ft.border_radius.all(16),                             # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                            border        = ft.border.all(2, ft.colors.BLACK),                    # ft.border.only(Left=8, top=8, right=8, bottom=8),
                            width         = 360,
                            height        = 150,
                            ##################### WIDGETS
                            content=ft.Column(
                                        ##################### PROPERTY BOX
                                        alignment = ft.MainAxisAlignment.SPACE_AROUND,            # horizontal <=> START,CENTER,END SPACE_BETWEEN SPACE_AROUND SPACE_EVENLY
                                        ##################### WIDGETS
                                        controls=[
                                                ft.Container(
                                                            ##################### PROPERTY
                                                            ink           = False,                               # click effect ripple
                                                            bgcolor       = ft.colors.BLACK38,                   # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                                                            padding       = ft.padding.all(4),    # inside box   # padding.only(left=8, top=8, right=8, bottom=8),
                                                            margin        = ft.margin.all(0),     # outside box  # margin.only (left=8, top=8, right=8, bottom=8),
                                                            alignment     = ft.alignment.center,                 # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right.    posicionamiento adentro widget
                                                            border_radius = ft.border_radius.all(30),            # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                                                            height        = 38,
                                                            ##################### WIDGETS
                                                            content=ft.Row(
                                                                            ##################### PROPERTY BOX
                                                                            alignment = ft.MainAxisAlignment.SPACE_BETWEEN,              # horizontal <=> START,CENTER,END SPACE_BETWEEN SPACE_AROUND SPACE_EVENLY
                                                                            ##################### WIDGETS
                                                                            controls  = [
                                                                                        self.main_gradient_widget,
                                                                                        ft.Container(
                                                                                                    ##################### PROPERTY
                                                                                                    ink       =False,                   # click effect ripple
                                                                                                    alignment = ft.alignment.center,    # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right. posicionamiento adentro widget
                                                                                                    disabled  = True,
                                                                                                    content = ft.ElevatedButton(
                                                                                                                    ##################### PROPERTY
                                                                                                                    text            = f"Apply {self.attribute_widget.capitalize()}".replace('_',' '), # content = ft.Text(value="Compound button", size=12,),
                                                                                                                    ##################### EVENTS
                                                                                                                    # on_click      = lambda _:print(screen_1.content.data),     #FloatingActionButton
                                                                                                                    # on_hover      = lambda _:print(screen_1.content.data),
                                                                                                                    # on_long_press = lambda _:print(screen_1.content.data),
                                                                                                                    #####################
                                                                                                                    # on_blur       = lambda _:print(screen_1.content.data),
                                                                                                                    # on_focus      = lambda _:print(screen_1.content.data),
                                                                                                    ##################### EVENTS
                                                                                                    on_click = lambda _:self.apply_gradient(),   # on_hover=print('on click over'), on_long_press=print('long press'),
                                                                                        ),),#<=== NOTE COMA <==> ERASE COMA IF MAKE 1 ERROR
                                                                                     ],),
                                                            ##################### EVENTS
                                                            # on_click=lambda _:print(_),                            # on_hover=print('on click over'), on_long_press=print('long press'),
                                                ),#<=== NOTE COMA

                                                ft.Container( ##################### First Dual Entry
                                                    ##################### PROPERTY
                                                    ink           = False,                                        # click effect ripple
                                                    bgcolor       = "#0e0f11",                                    # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                                                    padding       = ft.padding.all(2),    # inside box            # padding.only(left=8, top=8, right=8, bottom=8),
                                                    alignment     = ft.alignment.center,                          # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right.    posicionamiento adentro widget
                                                    border_radius = ft.border_radius.all(30),                     # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                                                    border        = ft.border.all(1, ft.colors.BLACK38),          # ft.border.only(Left=8, top=8, right=8, bottom=8),
                                                    height        = 36,
                                                    disabled      = True,
                                                    ##################### WIDGETS
                                                    content=ft.Row(
                                                                    ##################### PROPERTY BOX
                                                                    spacing=8.7,                                  # space widget left right
                                                                    ##################### WIDGETS
                                                                    controls=[
                                                                                ft.Container(
                                                                                            ##################### PROPERTY
                                                                                            ink           = False,                                              # click effect ripple
                                                                                            width         = 68,
                                                                                            height        = 35,
                                                                                            border_radius = ft.border_radius.all(30),                           # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                                                                                            content = ft.TextField(
                                                                                                            hint_text = self.attribute_widget_name_1,
                                                                                                            border    = ft.InputBorder.NONE,                    # border=ft.InputBorder.[NONE ,OUTLINE ,UNDERLINE]
                                                                                                            bgcolor   = 'dark',                                 # inside box
                                                                                                            color     = 'YELLOW',
                                                                                                            text_size = 15,
                                                                                                            #======================= EVENTS ===========================
                                                                                                    on_change   = lambda x:self.modify_widget_attributes(config_widget =self.attribute_widget ,value = 'color_1',widget=Drop_GradientEntry),
                                                                                                    # on_change = lambda x:print('Pressed [< Write inside > ]'),
                                                                                                    # on_submit = lambda x:print('Pressed [< Enter > ]'),
                                                                                                    # on_focus  = lambda x:print('Pressed [< Click inside > ]'),
                                                                                                    # on_blur   = lambda x:print('Pressed [< click click and outside > ]'),
                                                                                                            ),
                                                                                            ##################### EVENTS
                                                                                            # on_click=lambda _:print(_),   # on_hover=print('on click over'), on_long_press=print('long press'),
                                                                                ),#<=== NOTE COMA <==> ERASE COMA IF MAKE 1 ERROR,
                                                                                ft.Container(
                                                                                            ##################### PROPERTY
                                                                                            ink           = False,                                          # click effect ripple
                                                                                            width         = 68,
                                                                                            height        = 35,
                                                                                            border_radius = ft.border_radius.all(30),                       # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                                                                                            content = ft.TextField(
                                                                                                            hint_text = self.attribute_widget_name_2,
                                                                                                            border    = ft.InputBorder.NONE,                # border=ft.InputBorder.[NONE ,OUTLINE ,UNDERLINE]
                                                                                                            bgcolor   = 'dark',                             # inside box
                                                                                                            color     = 'YELLOW',
                                                                                                            text_size = 15,
                                                                                                            #======================= EVENTS ===========================
                                                                                                    on_change   = lambda x:self.modify_widget_attributes(config_widget =self.attribute_widget ,value = 'color_2',widget=Drop_GradientEntry),
                                                                                                    # on_change = lambda x:print('Pressed [< Write inside > ]'),
                                                                                                    # on_submit = lambda x:print('Pressed [< Enter > ]'),
                                                                                                    # on_focus  = lambda x:print('Pressed [< Click inside > ]'),
                                                                                                    # on_blur   = lambda x:print('Pressed [< click click and outside > ]'),
                                                                                                            ),
                                                                                            ##################### EVENTS
                                                                                            # on_click=lambda _:print(_),   # on_hover=print('on click over'), on_long_press=print('long press'),
                                                                                ),#<=== NOTE COMA <==> ERASE COMA IF MAKE 1 ERROR
                                                                                ft.Container(width=18),

                                                                                ft.Container(
                                                                                            ##################### PROPERTY
                                                                                            ink           = False,                                        # click effect ripple
                                                                                            bgcolor       = "#3e4046",                                    # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                                                                                            padding       = ft.padding.all(0),    # inside box            # padding.only(left=8, top=8, right=8, bottom=8),
                                                                                            alignment     = ft.alignment.center,                          # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right.    posicionamiento adentro widget
                                                                                            border_radius = ft.border_radius.all(30),                     # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                                                                                            border        = ft.border.all(2, '#646871'),                  # ft.border.only(Left=8, top=8, right=8, bottom=8),
                                                                                            width         = 150,
                                                                                            height        = 35,
                                                                                            ##################### WIDGETS
                                                                                            content=ft.Dropdown(
                                                                                                                hint_text       = " center_left ",
                                                                                                                width           = 140,
                                                                                                                content_padding = ft.padding.only(left=0, top=0, right=8, bottom=14),
                                                                                                                alignment       = ft.alignment.center_left,            # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right.    posicionamiento adentro widget
                                                                                                                border_radius   = ft.border_radius.all(15),            # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                                                                                                                border          = ft.InputBorder.NONE,
                                                                                                                options         = self.options_tmp_1,
                                                                                                                ##################### EVENTS
                                                                                                        # on_change = lambda _: _.__dict__.get('value') if _.__dict__.get('data') == "green" else  _.__dict__.get('data'),
                                                                                                        on_change   = lambda _:self.modify_widget_attributes(config_widget=_.__dict__.get('data'),value="begin gradient",widget=Drop_GradientEntry),
                                                                                                        # on_change = lambda _:print(_.__dict__.get('data')),
                                                                                                        # on_click  = lambda _:print(_),   # on_hover=print('on click over'), on_long_press=print('long press'),
                                                                                                    ),#<=== NOTE COMA <==> ERASE COMA IF MAKE 1 ERROR,

                                                                                            ##################### EVENTS
                                                                                            # on_click=lambda _:print(_),                            # on_hover=print('on click over'), on_long_press=print('long press'),
                                                                                ),#<=== NOTE COMA,
                                                                             ],),
                                                                        ##################### EVENTS
                                                                        # on_click=lambda _:print(_),                            # on_hover=print('on click over'), on_long_press=print('long press'),
                                                                        ),#<=== NOTE COMA,
                                                ft.Container( ##################### Secon Dual Entry
                                                    ink           = False,                               # click effect ripple
                                                    bgcolor       = "#0e0f11",                           # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                                                    padding       = ft.padding.all(2),    # inside box   # padding.only(left=8, top=8, right=8, bottom=8),
                                                    alignment     = ft.alignment.center,                 # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right.    posicionamiento adentro widget
                                                    border_radius = ft.border_radius.all(30),            # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                                                    border        = ft.border.all(1, ft.colors.BLACK38), # ft.border.only(Left=8, top=8, right=8, bottom=8),
                                                    height        = 36,
                                                    disabled      = True,
                                                    ##################### WIDGETS
                                                    content=ft.Row(
                                                                    ##################### PROPERTY BOX
                                                                    spacing  = 8.7,                      # space widget left right
                                                                    ##################### WIDGETS
                                                                    controls = [
                                                                                ft.Container(
                                                                                            ##################### PROPERTY
                                                                                            ink           = False,                                              # click effect ripple
                                                                                            width         = 68,
                                                                                            height        = 30,
                                                                                            border_radius = ft.border_radius.all(30),                           # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                                                                                        content = ft.TextField(
                                                                                                            hint_text = self.attribute_widget_name_3,
                                                                                                            border    = ft.InputBorder.NONE,                    # border=ft.InputBorder.[NONE ,OUTLINE ,UNDERLINE]
                                                                                                            bgcolor   = 'dark',                                 # inside box
                                                                                                            color     = 'YELLOW',
                                                                                                            text_size = 15,
                                                                                                            #======================= EVENTS ===========================
                                                                                                    on_change   = lambda x:self.modify_widget_attributes(config_widget =self.attribute_widget ,value = 'color_3',widget=Drop_GradientEntry),
                                                                                                    # on_change = lambda x:print('Pressed [< Write inside > ]'),
                                                                                                    # on_submit = lambda x:print('Pressed [< Enter > ]'),
                                                                                                    # on_focus  = lambda x:print('Pressed [< Click inside > ]'),
                                                                                                    # on_blur   = lambda x:print('Pressed [< click click and outside > ]'),
                                                                                                            ),
                                                                                            ##################### EVENTS
                                                                                            # on_click=lambda _:print(_),   # on_hover=print('on click over'), on_long_press=print('long press'),
                                                                                ),#<=== NOTE COMA <==> ERASE COMA IF MAKE 1 ERROR,
                                                                                ft.Container(
                                                                                            ##################### PROPERTY
                                                                                            ink           = False,                                           # click effect ripple
                                                                                            width         = 68,
                                                                                            height        = 30,
                                                                                            border_radius = ft.border_radius.all(30),                        # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                                                                                        content = ft.TextField(
                                                                                                        hint_text = self.attribute_widget_name_4,
                                                                                                        border    = ft.InputBorder.NONE,                     # border=ft.InputBorder.[NONE ,OUTLINE ,UNDERLINE]
                                                                                                        bgcolor   = 'dark',                                  # inside box
                                                                                                        color     = 'YELLOW',
                                                                                                        text_size = 15,
                                                                                                        #======================= EVENTS ===========================
                                                                                                on_change   = lambda x:self.modify_widget_attributes(config_widget =self.attribute_widget ,value = 'color_4',widget=Drop_GradientEntry),
                                                                                                # on_change = lambda x:print('Pressed [< Write inside > ]'),
                                                                                                # on_submit = lambda x:print('Pressed [< Enter > ]'),
                                                                                                # on_focus  = lambda x:print('Pressed [< Click inside > ]'),
                                                                                                # on_blur   = lambda x:print('Pressed [< click click and outside > ]'),
                                                                                                            ),
                                                                                ),#<=== NOTE COMA <==> ERASE COMA IF MAKE 1 ERROR
                                                                                ft.Container(width=18),
                                                                                ft.Container(
                                                                                            ##################### PROPERTY
                                                                                            ink           = False,                                          # click effect ripple
                                                                                            bgcolor       = "#3e4046",                                      # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                                                                                            padding       = ft.padding.all(0),    # inside box              # padding.only(left=8, top=8, right=8, bottom=8),
                                                                                            alignment     = ft.alignment.center,                            # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right.    posicionamiento adentro widget
                                                                                            border_radius = ft.border_radius.all(30),                       # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                                                                                            border        = ft.border.all(2, '#646871'),                    # ft.border.only(Left=8, top=8, right=8, bottom=8),
                                                                                            width         = 150,
                                                                                            height        = 35,
                                                                                            ##################### WIDGETS
                                                                                            content=ft.Dropdown(
                                                                                                                hint_text       = " top_right ",
                                                                                                                width           = 140,
                                                                                                                content_padding = ft.padding.only(left=0, top=0, right=8, bottom=14),
                                                                                                                alignment       = ft.alignment.center_left,            # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right.    posicionamiento adentro widget
                                                                                                                border_radius   = ft.border_radius.all(15),            # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                                                                                                                border          = ft.InputBorder.NONE,
                                                                                                                options         = self.options_tmp_2,
                                                                                                                ##################### EVENTS
                                                                                                        # on_change = lambda _: _.__dict__.get('value') if _.__dict__.get('data') == "green" else  _.__dict__.get('data'),
                                                                                                        on_change   = lambda _:self.modify_widget_attributes(config_widget=_.__dict__.get('data'),value="end gradient",widget=Drop_GradientEntry),
                                                                                                        # on_change = lambda _:print(_.__dict__.get('data')),
                                                                                                        # on_click  = lambda _:print(_),   # on_hover=print('on click over'), on_long_press=print('long press'),
                                                                                                    ),#<=== NOTE COMA <==> ERASE COMA IF MAKE 1 ERROR,

                                                                                            ##################### EVENTS
                                                                                            # on_click=lambda _:print(_),                            # on_hover=print('on click over'), on_long_press=print('long press'),
                                                                                ),#<=== NOTE COMA,
                                                                             ],),
                                                                    ),#<=== NOTE COMA,
                                                ],
                                    ),#<=== NOTE COMA [NOTE]                     # for x in range(1,50): widget.content.controls.append(ft.ElevatedButton("press buttom",tooltip='buttom'))
                            )#<=== NOTE COMA
        return Drop_GradientEntry
    def apply_gradient(self):

        # all_data = f"""
        #                 color 1:        {self.color_1}
        #                 color 2:        {self.color_2}
        #                 color 3:        {self.color_3}
        #                 color 4:        {self.color_4}

        #                 main gradient:  {self.main_gradient}
        #                 begin gradient: {self.start_gradient}
        #                 end gradient:   {self.end_gradient}
        #                         """
        # all_x = [self.color_1]
        # self.

        if self.main_gradient == ' Linear ':
            if self.color_1 and self.color_2:

                if self.color_1 and self.color_2 and self.color_3 and self.color_4:
                    self.data_color = [self.color_1, self.color_2, self.color_3,self.color_4]
                elif self.color_1 and self.color_2 and self.color_3:
                    self.data_color = [self.color_1, self.color_2, self.color_3]
                else:
                    self.data_color = [self.color_1, self.color_2]

                self.widget.gradient = ft.LinearGradient(
                                                            begin  = self.effects_gradients.get(self.start_gradient),
                                                            end    = self.effects_gradients.get(self.end_gradient),
                                                            colors = self.data_color,
                                                        )
        elif self.main_gradient == ' Radial ':
            if self.color_1 and self.color_2:
                if self.color_1 and self.color_2 and self.color_3 and self.color_4:
                    self.data_color = [self.color_1, self.color_2, self.color_3,self.color_4]
                elif self.color_1 and self.color_2 and self.color_3:
                    self.data_color = [self.color_1, self.color_2, self.color_3]
                else:
                    self.data_color = [self.color_1, self.color_2]

                self.widget.gradient = ft.RadialGradient(
                                                            # colors = ['yellow','blue','green','red'],
                                                            colors = self.data_color,
                                                        )
        elif self.main_gradient == ' None ':
            self.widget.gradient = None,

        # if self.color_1 and self.color_2

        self.widget.update()
    def modify_widget_attributes(self,config_widget,value,widget):
        """
    NOTE:

        Will modify all attrib inside the widget that we selected

        on_change= lambda x:self.modify_widget_attributes(config_widget =self.attribute_widget ,value = Drop_GradientEntry),

    EXEMPLE:

        width:      value
        height:     value
        bgcolor:    value
        value:      value
        """
        # print(config_widget)
        # print(value)

        # self.widget.content.value = value if config_widget  == "value" else None
        # will modify attributes of the widget class in real time
        ################################# ONLY FOR CONTAINER
        # print(self.main_gradient_widget.content.value,'asdasd')
        # widget.content.controls[1].disabled = False
        # widget.content.controls[1].content.update()
        if config_widget == ' None ':
            widget.content.controls[1].disabled = True
            widget.content.controls[2].disabled = True
            widget.content.controls[0].content.controls[1].disabled = True
            self.widget.gradient=None

        elif config_widget == ' Linear ':
            widget.content.controls[1].disabled = False
            widget.content.controls[2].disabled = False
            widget.content.controls[0].content.controls[1].disabled = False
            widget.content.controls[1].content.controls[3].content.disabled = False
            widget.content.controls[2].content.controls[3].content.disabled = False
            widget.content.update()
        elif config_widget == ' Radial ':
            widget.content.controls[1].disabled = False
            widget.content.controls[2].disabled = False
            widget.content.controls[0].content.controls[1].disabled = False
            widget.content.controls[1].content.controls[3].content.disabled = True
            widget.content.controls[2].content.controls[3].content.disabled = True
            widget.content.update()

        if self.attribute_widget == 'gradient ':
            if value == "color_1" :
                self.color_1 = widget.content.controls[1].content.controls[0].content.value
            if value == "color_2" :
                self.color_2 = widget.content.controls[1].content.controls[1].content.value
            if value == "color_3":
                self.color_3 = widget.content.controls[2].content.controls[0].content.value
            if value == "color_4":
                self.color_4 = widget.content.controls[2].content.controls[1].content.value

            if config_widget == ' Linear ':
                self.main_gradient = config_widget
            if config_widget == ' Radial ':
                self.main_gradient = config_widget

            if value == 'begin gradient':
                self.start_gradient = config_widget
            if value == 'end gradient':
                self.end_gradient = config_widget

        ################################# ONLY FOR CONTAINER content
        self.widget.update()

######## Double_Widget = GradientEntry(),# <======= Comma
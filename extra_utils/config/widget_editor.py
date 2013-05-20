######################
from extra_utils.config.double_entry import DoubleEntry
from extra_utils.config.color_entry  import ColorEntry
from extra_utils.config.bool_entry import BoolEntry
from extra_utils.config.four_entry import FourEntry
from extra_utils.config.single_entry import SingleEntry
from extra_utils.config.selection_entry import SelectionEntry
from extra_utils.config.gradient_entry import GradientEntry


######################
import flet as ft
######################

class Build_Editor(ft.UserControl):
    """
    Builder editor is a Row Container that will content all widgets editors inside

    Tabs:
        Container:
                edit_Container: value
        Widget:
                edit_Widget: value

    NOTE:
        Is necessary put class widget of the widget to edit Attributes
    """

    def __init__(self,widget='Erase this test'):
        super().__init__()
        self.widget = widget

    def build(self):
        Drop_Build_Editor=ft.Container(
                                ##################### PROPERTY ROW
                                ##################### [rotate,offset] , [scale,aspect_ratio] , [visible,disabled]
                                # scroll=True,
                                # expand=True,
                                # ink=True,                                                      # click effect ripple
                                # bgcolor=ft.colors.BLACK12,                                              # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                                padding= ft.padding.all(0),    # inside box                     # padding.only(left=8, top=8, right=8, bottom=8),
                                margin = ft.margin.all(0),     # outside box                    # margin.only (left=8, top=8, right=8, bottom=8),
                                # alignment=ft.alignment.center,                                  # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right.    posicionamiento adentro widget
                                border_radius= ft.border_radius.all(28),                      # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                                # border=ft.border.all(2, ft.colors.BLACK38),                       # ft.border.only(Left=8, top=8, right=8, bottom=8),
                                # ===================
                                # image_src = f"/home/mjay/Pictures/3d_neon_pink-2560x1440.jpg",
                                # image_opacity=0.1,
                                # image_fit='COVER',                                            # CONTAIN, COVER, FILL, FIT_HEIGHT, FIT_WIDTH, SCALE_DOWN
                                # ===================
                                # blur=18,
                                width=370,
                                height=580,
                                # tooltip='Container',
                                ############################
                            content=ft.Tabs(
                                            label_color='BLUE',
                                            indicator_border_radius=ft.border_radius.all(20),
                                            tabs=[
                                                    ft.Tab( text="Container",
                                                            # icon='',
                                                            content=ft.Container(
                                                                        ##################### PROPERTY COLUMN
                                                                        ##################### [rotate,offset] , [scale,aspect_ratio] , [visible,disabled]
                                                                        # expand=True,
                                                                        # ink=False,                                                      # click effect ripple
                                                                        # bgcolor= ft.colors.BLACK12,                                              # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                                                                        padding= ft.padding.all(4),    # inside box                        # padding.only(left=8, top=8, right=8, bottom=8),
                                                                        margin = ft.margin.all(0),    # outside box                       # margin.only (left=8, top=8, right=8, bottom=8),
                                                                        # alignment=ft.alignment.center,                                  # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right.    posicionamiento adentro widget
                                                                        # border_radius= ft.border_radius.all(30),                      # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                                                                        # border=ft.border.all(2, ft.colors.BLACK),                     # ft.border.only(Left=8, top=8, right=8, bottom=8),
                                                                        # ===================
                                                                        # image_src = f"/home/mjay/Pictures/3d_neon_pink-2560x1440.jpg",
                                                                        # image_opacity=0.1,
                                                                        # image_fit='COVER',                                            # CONTAIN, COVER, FILL, FIT_HEIGHT, FIT_WIDTH, SCALE_DOWN
                                                                        # ===================
                                                                        # width=150,
                                                                        # height=1200,
                                                                        # tooltip='Container',
                                                                        ##################### EFFECTS
                                                                        # gradient=ft.LinearGradient( begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=[ft.colors.BLACK12, ft.colors.BLACK45],),
                                                                        # gradient=ft.RadialGradient( colors=[ft.colors.YELLOW, ft.colors.BLUE],),
                                                                        ##################### WIDGETS
                                                                        content=ft.Row(
                                                                                ##################### PROPERTY BOX
                                                                                # expand=True,
                                                                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,              # horizontal <=> START,CENTER,END SPACE_BETWEEN SPACE_AROUND SPACE_EVENLY
                                                                                # horizontal_alignment=ft.CrossAxisAlignment.CENTER,        # vertical       START,CENTER END
                                                                                ##################### LET MAKE SCROLL IN LONG QUANTITY
                                                                                scroll='HIDDEN',                                              # center widget
                                                                                tight=True,
                                                                                ##################### ADAPT TO SCREEN
                                                                                wrap=True,                                                  # justify in all screen
                                                                                spacing=0,                                                # space widget left right
                                                                                run_spacing=8,                                            # space widget up down
                                                                                ##################### WIDGETS

                                                                            ),#<=== NOTE COMA [NOTE]                     for x in range(1,50): widget.content.controls.append(ft.ElevatedButton("press buttom",tooltip='buttom'))
                                                                            ##################### EVENTS
                                                                            # on_click=lambda _:print(_),                            # on_hover=print('on click over'), on_long_press=print('long press'),
                                                                            # controls=[],
                                                            ),#<=== NOTE COMA
                                                    ),
                                                    ft.Tab(text="Widget",
                                                            content=ft.Container(
                                                                        ##################### PROPERTY COLUMN
                                                                        ##################### [rotate,offset] , [scale,aspect_ratio] , [visible,disabled]
                                                                        # expand=True,
                                                                        # ink=False,                                                      # click effect ripple
                                                                        # bgcolor= ft.colors.BLACK12,                                              # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                                                                        padding= ft.padding.all(4),    # inside box                        # padding.only(left=8, top=8, right=8, bottom=8),
                                                                        margin = ft.margin.all(0),    # outside box                       # margin.only (left=8, top=8, right=8, bottom=8),
                                                                        # alignment=ft.alignment.center,                                  # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right.    posicionamiento adentro widget
                                                                        # border_radius= ft.border_radius.all(30),                      # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                                                                        # border=ft.border.all(2, ft.colors.BLACK),                     # ft.border.only(Left=8, top=8, right=8, bottom=8),
                                                                        # ===================
                                                                        # image_src = f"/home/mjay/Pictures/3d_neon_pink-2560x1440.jpg",
                                                                        # image_opacity=0.1,
                                                                        # image_fit='COVER',                                            # CONTAIN, COVER, FILL, FIT_HEIGHT, FIT_WIDTH, SCALE_DOWN
                                                                        # ===================
                                                                        # width=150,
                                                                        # height=1200,
                                                                        # tooltip='Container',
                                                                        ##################### EFFECTS
                                                                        # gradient=ft.LinearGradient( begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=[ft.colors.BLACK12, ft.colors.BLACK45],),
                                                                        # gradient=ft.RadialGradient( colors=[ft.colors.YELLOW, ft.colors.BLUE],),
                                                                        ##################### WIDGETS
                                                                        content=ft.Row(
                                                                                ##################### PROPERTY BOX
                                                                                # expand=True,
                                                                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,              # horizontal <=> START,CENTER,END SPACE_BETWEEN SPACE_AROUND SPACE_EVENLY
                                                                                # horizontal_alignment=ft.CrossAxisAlignment.CENTER,        # vertical       START,CENTER END
                                                                                ##################### LET MAKE SCROLL IN LONG QUANTITY
                                                                                scroll='HIDDEN',                                              # center widget
                                                                                tight=True,
                                                                                ##################### ADAPT TO SCREEN
                                                                                wrap=True,                                                  # justify in all screen
                                                                                spacing=0,                                                # space widget left right
                                                                                run_spacing=8,                                            # space widget up down
                                                                                ##################### WIDGETS

                                                                            ),#<=== NOTE COMA [NOTE]                     for x in range(1,50): widget.content.controls.append(ft.ElevatedButton("press buttom",tooltip='buttom'))
                                                                            ##################### EVENTS
                                                                            # on_click=lambda _:print(_),                            # on_hover=print('on click over'), on_long_press=print('long press'),
                                                                            # controls=[],
                                                            ),#<=== NOTE COMA

                                                            ),
                                                    ]

                                            ),
                        )
        ########################################################################################
        """
        We call the widget specific made in /extra_utils/config/

                  name_widget  attributes              widget_to_modify_attrib
        ==================================================================
        'height' :DoubleEntry(config_widget = 'height',widget=self.widget),
        ==================================================================

                                tab[0]=Container               add_to_tab[0]                     add_specific_widget
        ==============================================================================================================
        Drop_Build_Editor.content.tabs[0].content.content.controls.append(self.widgets_dict.get('width'))
        ==============================================================================================================

        Note:

        1. we need have builder attribute widget
        2. we need get all attribute from selected widget
        3. we need compara to get similitudes betwen [ builder attribute widget ] and [ self.attribute_widget ]
        4. add to Tab 1 ==>> Container attributes
        4. add to Tab 2 ==>> Selected widget attributes

        self.widgets_dict     <=== Contain all builder attribute widget
        self.attribute_widget <=== Contain all attributes from selected widget  == ft.Container().__dir__()


        """
        self.widgets_dict = {
                                ######################### ESPECIAL WIDGETS ONLY FOR CONTAINERS
                                # SINGLE SELECTION ENTRY
                                'image_opacity ':SingleEntry(config_widget = 'image_opacity ',widget = self.widget),  # <=== this take width and hight in same time
                                'image_src '    :SingleEntry(config_widget = 'image_src '    ,widget = self.widget),  # <=== this take width and hight in same time
                                'tooltip '      :SingleEntry(config_widget = 'tooltip '      ,widget = self.widget),  # <=== this take width and hight in same time
                                'rotate '       :SingleEntry(config_widget = 'rotate '       ,widget = self.widget),  # <=== this take width and hight in same time
                                'scale '        :SingleEntry(config_widget = 'scale '        ,widget = self.widget),  # <=== this take width and hight in same time
                                # DOUBLE SELECTION ENTRY
                                'border '       :DoubleEntry(config_widget = 'border '       ,widget = self.widget),  # <=== this take width and hight in same time
                                'offset '       :DoubleEntry(config_widget = 'offset '       ,widget = self.widget),  # <=== this take width and hight in same time
                                'width '        :DoubleEntry(config_widget = 'width '        ,widget = self.widget),  # <=== this take width and hight in same time
                                'blur '         :DoubleEntry(config_widget = 'blur '         ,widget = self.widget),  # <=== this take width and hight in same time
                                # 4 SELECTION ENTRIES
                                'padding '      :FourEntry(config_widget   = 'padding '      ,widget = self.widget),
                                'margin '       :FourEntry(config_widget   = 'margin '       ,widget = self.widget),
                                'border_radius ':FourEntry(config_widget   = 'border_radius ',widget = self.widget),
                                # COLOR ENTRY ['RED' ...]
                                'bgcolor '      :ColorEntry(config_widget  = 'bgcolor '      ,widget = self.widget),
                                # BOOL ENTRY [TRUE FALSE]
                                'visible '      :BoolEntry(config_widget   = 'visible '      ,widget = self.widget),
                                'expand '       :BoolEntry(config_widget   = 'expand '       ,widget = self.widget),
                                'ink '          :BoolEntry(config_widget   = 'ink '          ,widget = self.widget),
                                # SELECTION ENTRY
                                'image_fit '    :SelectionEntry(config_widget = 'image_fit ' ,widget = self.widget),
                                'alignment '    :SelectionEntry(config_widget = 'alignment ' ,widget = self.widget),
                                # SELECTION GRADIENT
                                'gradient '     :GradientEntry(config_widget  = 'gradient '  ,widget = self.widget),
                                ##################################################################################################
                                ######################### SINGLE SELECTION ENTRY
                                'label'               :SingleEntry(config_widget = 'label'            ,widget = self.widget),  # <=== this take width and hight in same time
                                'value'               :SingleEntry(config_widget = 'value'            ,widget = self.widget),  # <=== this take width and hight in same time
                                'key'                 :SingleEntry(config_widget = 'key'              ,widget = self.widget),  # <=== this take width and hight in same time
                                'hint_text'           :SingleEntry(config_widget = 'hint_text'        ,widget = self.widget),  # <=== this take width and hight in same time
                                'counter_text'        :SingleEntry(config_widget = 'counter_text'     ,widget = self.widget),  # <=== this take width and hight in same time
                                'suffix_text'         :SingleEntry(config_widget = 'suffix_text'      ,widget = self.widget),  # <=== this take width and hight in same time
                                'url'                 :SingleEntry(config_widget = 'url'              ,widget = self.widget),  # <=== this take width and hight in same time
                                'url_target'          :SingleEntry(config_widget = 'url_target'       ,widget = self.widget),  # <=== this take width and hight in same time
                                'icon'                :SingleEntry(config_widget = 'icon'             ,widget = self.widget),  # <=== this take width and hight in same time
                                'tooltip'             :SingleEntry(config_widget = 'tooltip'          ,widget = self.widget),  # <=== this take width and hight in same time
                                'src'                 :SingleEntry(config_widget = 'src'              ,widget = self.widget),  # <=== this take width and hight in same time
                                'data'                :SingleEntry(config_widget = 'data'             ,widget = self.widget),  # <=== this take width and hight in same time
                                'semantics_label'     :SingleEntry(config_widget = 'semantics_label'  ,widget = self.widget),  # <=== this take width and hight in same time
                                'src_base64'          :SingleEntry(config_widget = 'src_base64'       ,widget = self.widget),  # <=== this take width and hight in same time
                                'image_src'           :SingleEntry(config_widget = 'image_src'        ,widget = self.widget),  # <=== this take width and hight in same time
                                'blur_radius'         :SingleEntry(config_widget = 'blur_radius'      ,widget = self.widget),  # <=== this take width and hight in same time
                                'spread_radius'       :SingleEntry(config_widget = 'spread_radius'    ,widget = self.widget),  # <=== this take width and hight in same time
                                'elevation'           :SingleEntry(config_widget = 'elevation'        ,widget = self.widget),  # <=== this take width and hight in same time
                                'rotate'              :SingleEntry(config_widget = 'rotate'           ,widget = self.widget),  # <=== this take width and hight in same time
                                'scale'               :SingleEntry(config_widget = 'scale'            ,widget = self.widget),  # <=== this take width and hight in same time
                                'aspect_ratio'        :SingleEntry(config_widget = 'aspect_ratio'     ,widget = self.widget),  # <=== this take width and hight in same time
                                'runs_count'          :SingleEntry(config_widget = 'runs_count'       ,widget = self.widget),  # <=== this take width and hight in same time
                                'run_spacing'         :SingleEntry(config_widget = 'run_spacing'      ,widget = self.widget),  # <=== this take width and hight in same time
                                'spacing'             :SingleEntry(config_widget = 'spacing'          ,widget = self.widget),  # <=== this take width and hight in same time
                                'child_aspect_ratio'  :SingleEntry(config_widget = 'child_aspect_ratio',widget = self.widget), # <=== this take width and hight in same time
                                'max_extent'          :SingleEntry(config_widget = 'max_extent'       ,widget = self.widget),  # <=== this take width and hight in same time
                                'min_lines'           :SingleEntry(config_widget = 'min_lines'        ,widget = self.widget),  # <=== this take width and hight in same time
                                'max_lines'           :SingleEntry(config_widget = 'max_lines'        ,widget = self.widget),  # <=== this take width and hight in same time
                                'border_width'        :SingleEntry(config_widget = 'border_width'     ,widget = self.widget),  # <=== this take width and hight in same time
                                'text_size'           :SingleEntry(config_widget = 'text_size'        ,widget = self.widget),  # <=== this take width and hight in same time
                                'image_opacity'       :SingleEntry(config_widget = 'image_opacity'    ,widget = self.widget),  # <=== this take width and hight in same time
                                'opacity'             :SingleEntry(config_widget = 'opacity'          ,widget = self.widget),  # <=== this take width and hight in same time
                                ######################### DOUBLE SELECTION ENTRY
                                'width'               :DoubleEntry(config_widget = 'width'            ,widget = self.widget),  # <=== this take width and hight in same time
                                'border'              :DoubleEntry(config_widget = 'border'           ,widget = self.widget),
                                'offset'              :DoubleEntry(config_widget = 'offset'           ,widget = self.widget),
                                'blur'                :DoubleEntry(config_widget = 'blur'             ,widget = self.widget),
                                ######################### 4 SELECTION ENTRIE S
                                'padding'             :FourEntry(config_widget = 'padding'            ,widget = self.widget),
                                'margin'              :FourEntry(config_widget = 'margin'             ,widget = self.widget),
                                'border_radius'       :FourEntry(config_widget = 'border_radius'      ,widget = self.widget),
                                ######################### COLOR ENTRY ['RED' ...]
                                'bgcolor'             :ColorEntry(config_widget= 'bgcolor'            ,widget = self.widget),
                                'color'               :ColorEntry(config_widget= 'color'              ,widget = self.widget),
                                'shadow_color'        :ColorEntry(config_widget= 'shadow_color'       ,widget = self.widget),
                                'icon_color'          :ColorEntry(config_widget= 'icon_color'         ,widget = self.widget),
                                'check_color'         :ColorEntry(config_widget= 'check_color'        ,widget = self.widget),
                                'fill_color'          :ColorEntry(config_widget= 'fill_color'         ,widget = self.widget),
                                'border_color'        :ColorEntry(config_widget= 'border_color'       ,widget = self.widget),
                                'focused_bgcolor'     :ColorEntry(config_widget= 'focused_bgcolor'    ,widget = self.widget),
                                'focused_border_color':ColorEntry(config_widget= 'focused_border_color',widget= self.widget),
                                ######################### BOOL ENTRY [TRUE FALSE]
                                'expand':             BoolEntry(config_widget = 'expand'              ,widget = self.widget),
                                'ink':                BoolEntry(config_widget = 'ink'                 ,widget = self.widget),
                                'scroll':             BoolEntry(config_widget = 'scroll'              ,widget = self.widget),
                                'wrap':               BoolEntry(config_widget = 'wrap'                ,widget = self.widget),
                                'tight':              BoolEntry(config_widget = 'tight'               ,widget = self.widget),
                                'visible':            BoolEntry(config_widget = 'visible'             ,widget = self.widget),
                                'multiline':          BoolEntry(config_widget = 'multiline'           ,widget = self.widget),
                                'disabled':           BoolEntry(config_widget = 'disabled'            ,widget = self.widget),
                                'read_only':          BoolEntry(config_widget = 'read_only'           ,widget = self.widget),
                                'password':           BoolEntry(config_widget = 'password'            ,widget = self.widget),
                                'filled':             BoolEntry(config_widget = 'filled'              ,widget = self.widget),
                                'adaptive':           BoolEntry(config_widget = 'adaptive'            ,widget = self.widget),
                                'tristate':           BoolEntry(config_widget = 'tristate'            ,widget = self.widget),
                                'autofocus':          BoolEntry(config_widget = 'autofocus'           ,widget = self.widget),
                                'horizontal':         BoolEntry(config_widget = 'horizontal'          ,widget = self.widget),
                                'can_reveal_password':BoolEntry(config_widget = 'can_reveal_password' ,widget = self.widget),
                                'capitalization':     BoolEntry(config_widget = 'capitalization'      ,widget = self.widget),
                                'gapless_playback':   BoolEntry(config_widget = 'gapless_playback'    ,widget = self.widget),
                                ######################### SELECTION ENTRY
                                'image_fit':          SelectionEntry(config_widget = 'image_fit'      ,widget = self.widget),
                                'weight':             SelectionEntry(config_widget = 'weight'         ,widget = self.widget),
                                'keyboard_type':      SelectionEntry(config_widget = 'keyboard_type'  ,widget = self.widget),
                                'text_align':         SelectionEntry(config_widget = 'text_align'     ,widget = self.widget),
                                'alignment':          SelectionEntry(config_widget = 'alignment'      ,widget = self.widget),
                                'content_alignment':  SelectionEntry(config_widget = 'content_alignment' ,widget = self.widget),
                                'vertical_alignment' :SelectionEntry(config_widget = 'vertical_alignment',widget = self.widget),
                               'horizontal_alignment':SelectionEntry(config_widget = 'horizontal_alignment',widget = self.widget),
                                ######################### GRADIEN ENTRY
                               'gradient':            GradientEntry(config_widget   = 'gradient',widget = self.widget),


                                #############################################################################################
                            }
        """
        will add first tab Drop_Build_Editor.content.tabs[0].content.content.controls.append the defaulds WIDGET

        data = [SingleEntry(config_widget = 'label'            ,widget = self.widget),
                SingleEntry(config_widget = 'value'            ,widget = self.widget),
                SingleEntry(config_widget = 'rotate'            ,widget = self.widget),
        ]
        Drop_Build_Editor.content.tabs[0].content.content.controls=data
        """
        ######################### ONLY FOR CONTAINERS
        # SINGLE SELECTION ENTRY
        # Drop_Build_Editor.content.tabs[0].content.content.controls.append(self.widgets_dict.get("image_opacity "))
        # Drop_Build_Editor.content.tabs[0].content.content.controls.append(self.widgets_dict.get("image_src "))
        # Drop_Build_Editor.content.tabs[0].content.content.controls.append(self.widgets_dict.get("tooltip "))
        # Drop_Build_Editor.content.tabs[0].content.content.controls.append(self.widgets_dict.get("rotate "))
        # Drop_Build_Editor.content.tabs[0].content.content.controls.append(self.widgets_dict.get("scale "))
        # DOUBLE SELECTION ENTRY
        # Drop_Build_Editor.content.tabs[0].content.content.controls.append(self.widgets_dict.get("blur "))
        # Drop_Build_Editor.content.tabs[0].content.content.controls.append(self.widgets_dict.get("border "))
        # Drop_Build_Editor.content.tabs[0].content.content.controls.append(self.widgets_dict.get("offset "))
        # Drop_Build_Editor.content.tabs[0].content.content.controls.append(self.widgets_dict.get("width "))
        # 4 SELECTION ENTRIES
        # Drop_Build_Editor.content.tabs[0].content.content.controls.append(self.widgets_dict.get("padding "))
        # Drop_Build_Editor.content.tabs[0].content.content.controls.append(self.widgets_dict.get("margin "))
        # Drop_Build_Editor.content.tabs[0].content.content.controls.append(self.widgets_dict.get("border_radius "))
        # COLOR ENTRY ['RED' ...]
        # Drop_Build_Editor.content.tabs[0].content.content.controls.append(self.widgets_dict.get("bgcolor "))
        # BOOL ENTRY [TRUE FALSE]
        # Drop_Build_Editor.content.tabs[0].content.content.controls.append(self.widgets_dict.get("visible "))
        # Drop_Build_Editor.content.tabs[0].content.content.controls.append(self.widgets_dict.get("expand "))
        # Drop_Build_Editor.content.tabs[0].content.content.controls.append(self.widgets_dict.get("ink "))
        # SELECTION ENTRY
        # Drop_Build_Editor.content.tabs[0].content.content.controls.append(self.widgets_dict.get("image_fit "))
        # Drop_Build_Editor.content.tabs[0].content.content.controls.append(self.widgets_dict.get("alignment "))
        ######################### SINGLE SELECTION ENTRY CONTAINER
        # Drop_Build_Editor.content.tabs[0].content.content.controls.append(self.widgets_dict.get('label'))
        # Drop_Build_Editor.content.tabs[0].content.content.controls.append(self.widgets_dict.get('value'))
        # Drop_Build_Editor.content.tabs[0].content.content.controls.append(self.widgets_dict.get('rotate'))
        # Drop_Build_Editor.content.tabs[0].content.content.controls.append(self.widgets_dict.get('scale'))
        # Drop_Build_Editor.content.tabs[0].content.content.controls.append(self.widgets_dict.get('opacity'))
        # Drop_Build_Editor.content.tabs[0].content.content.controls.append(self.widgets_dict.get('tooltip'))
        ###########################################################################
        # Drop_Build_Editor.content.tabs[0].content.content.controls.append(self.widgets_dict.get('key'))
        # Drop_Build_Editor.content.tabs[0].content.content.controls.append(self.widgets_dict.get('hint_text'))
        # Drop_Build_Editor.content.tabs[0].content.content.controls.append(self.widgets_dict.get('counter_text'))
        # Drop_Build_Editor.content.tabs[0].content.content.controls.append(self.widgets_dict.get('suffix_text'))
        # Drop_Build_Editor.content.tabs[0].content.content.controls.append(self.widgets_dict.get('url'))
        # Drop_Build_Editor.content.tabs[0].content.content.controls.append(self.widgets_dict.get('url_target'))
        # Drop_Build_Editor.content.tabs[0].content.content.controls.append(self.widgets_dict.get('icon'))
        # Drop_Build_Editor.content.tabs[0].content.content.controls.append(self.widgets_dict.get('src'))
        # Drop_Build_Editor.content.tabs[0].content.content.controls.append(self.widgets_dict.get('data'))
        # Drop_Build_Editor.content.tabs[0].content.content.controls.append(self.widgets_dict.get('semantics_label'))
        # Drop_Build_Editor.content.tabs[0].content.content.controls.append(self.widgets_dict.get('src_base64'))
        # Drop_Build_Editor.content.tabs[0].content.content.controls.append(self.widgets_dict.get('image_src'))
        # Drop_Build_Editor.content.tabs[0].content.content.controls.append(self.widgets_dict.get('blur_radius'))
        # Drop_Build_Editor.content.tabs[0].content.content.controls.append(self.widgets_dict.get('spread_radius'))
        # Drop_Build_Editor.content.tabs[0].content.content.controls.append(self.widgets_dict.get('elevation'))
        # Drop_Build_Editor.content.tabs[0].content.content.controls.append(self.widgets_dict.get('aspect_ratio'))
        # Drop_Build_Editor.content.tabs[0].content.content.controls.append(self.widgets_dict.get('runs_count'))
        # Drop_Build_Editor.content.tabs[0].content.content.controls.append(self.widgets_dict.get('run_spacing'))
        # Drop_Build_Editor.content.tabs[0].content.content.controls.append(self.widgets_dict.get('spacing'))
        # Drop_Build_Editor.content.tabs[0].content.content.controls.append(self.widgets_dict.get('child_aspect_ratio'))
        # Drop_Build_Editor.content.tabs[0].content.content.controls.append(self.widgets_dict.get('max_extent'))
        # Drop_Build_Editor.content.tabs[0].content.content.controls.append(self.widgets_dict.get('min_lines'))
        # Drop_Build_Editor.content.tabs[0].content.content.controls.append(self.widgets_dict.get('max_lines'))
        # Drop_Build_Editor.content.tabs[0].content.content.controls.append(self.widgets_dict.get('border_width'))
        # Drop_Build_Editor.content.tabs[0].content.content.controls.append(self.widgets_dict.get('text_size'))
        # Drop_Build_Editor.content.tabs[0].content.content.controls.append(self.widgets_dict.get('image_opacity'))
        ######################### DOUBLE SELECTION ENTRY #########################
        # Drop_Build_Editor.content.tabs[0].content.content.controls.append(self.widgets_dict.get('width'))
        # Drop_Build_Editor.content.tabs[0].content.content.controls.append(self.widgets_dict.get('border'))
        # Drop_Build_Editor.content.tabs[0].content.content.controls.append(self.widgets_dict.get('offset'))
        # ######################### 4 SELECTION ENTRIES  #########################
        Drop_Build_Editor.content.tabs[0].content.content.controls.append(self.widgets_dict.get('padding'))
        # Drop_Build_Editor.content.tabs[0].content.content.controls.append(self.widgets_dict.get('margin'))
        # Drop_Build_Editor.content.tabs[0].content.content.controls.append(self.widgets_dict.get('border_radius'))
        # # ######################### COLOR ENTRY ['RED' ...] #########################
        # Drop_Build_Editor.content.tabs[0].content.content.controls.append(self.widgets_dict.get('bgcolor'))
        # Drop_Build_Editor.content.tabs[0].content.content.controls.append(self.widgets_dict.get('focused_bgcolor'))
        # Drop_Build_Editor.content.tabs[0].content.content.controls.append(self.widgets_dict.get('border_color'))
        # Drop_Build_Editor.content.tabs[0].content.content.controls.append(self.widgets_dict.get('focused_border_color'))
        # Drop_Build_Editor.content.tabs[0].content.content.controls.append(self.widgets_dict.get('color'))
        # Drop_Build_Editor.content.tabs[0].content.content.controls.append(self.widgets_dict.get('shadow_color'))
        # Drop_Build_Editor.content.tabs[0].content.content.controls.append(self.widgets_dict.get('icon_color'))
        # Drop_Build_Editor.content.tabs[0].content.content.controls.append(self.widgets_dict.get('check_color'))
        # Drop_Build_Editor.content.tabs[0].content.content.controls.append(self.widgets_dict.get('fill_color'))
        # # ######################### BOOL ENTRY [TRUE FALSE] #########################
        # Drop_Build_Editor.content.tabs[0].content.content.controls.append(self.widgets_dict.get('expand'))
        # Drop_Build_Editor.content.tabs[0].content.content.controls.append(self.widgets_dict.get('ink'))
        # Drop_Build_Editor.content.tabs[0].content.content.controls.append(self.widgets_dict.get('scroll'))
        # Drop_Build_Editor.content.tabs[0].content.content.controls.append(self.widgets_dict.get('wrap'))
        # Drop_Build_Editor.content.tabs[0].content.content.controls.append(self.widgets_dict.get('tight'))
        # Drop_Build_Editor.content.tabs[0].content.content.controls.append(self.widgets_dict.get('multiline'))
        # Drop_Build_Editor.content.tabs[0].content.content.controls.append(self.widgets_dict.get('disabled'))
        # Drop_Build_Editor.content.tabs[0].content.content.controls.append(self.widgets_dict.get('read_only'))
        # Drop_Build_Editor.content.tabs[0].content.content.controls.append(self.widgets_dict.get('password'))
        # Drop_Build_Editor.content.tabs[0].content.content.controls.append(self.widgets_dict.get('filled'))
        # Drop_Build_Editor.content.tabs[0].content.content.controls.append(self.widgets_dict.get('adaptive'))
        # Drop_Build_Editor.content.tabs[0].content.content.controls.append(self.widgets_dict.get('tristate'))
        # Drop_Build_Editor.content.tabs[0].content.content.controls.append(self.widgets_dict.get('autofocus'))
        # Drop_Build_Editor.content.tabs[0].content.content.controls.append(self.widgets_dict.get('horizontal'))
        # Drop_Build_Editor.content.tabs[0].content.content.controls.append(self.widgets_dict.get('can_reveal_password'))
        # Drop_Build_Editor.content.tabs[0].content.content.controls.append(self.widgets_dict.get('capitalization'))
        # Drop_Build_Editor.content.tabs[0].content.content.controls.append(self.widgets_dict.get('gapless_playback'))
        # # ######################### SELECTION ENTRY #########################
        # Drop_Build_Editor.content.tabs[0].content.content.controls.append(self.widgets_dict.get('content_alignment'))
        # Drop_Build_Editor.content.tabs[0].content.content.controls.append(self.widgets_dict.get('alignment'))
        # Drop_Build_Editor.content.tabs[0].content.content.controls.append(self.widgets_dict.get('text_align'))
        # Drop_Build_Editor.content.tabs[0].content.content.controls.append(self.widgets_dict.get('vertical_alignment'))
        # Drop_Build_Editor.content.tabs[0].content.content.controls.append(self.widgets_dict.get('horizontal_alignment'))
        # Drop_Build_Editor.content.tabs[0].content.content.controls.append(self.widgets_dict.get('keyboard_type'))
        # Drop_Build_Editor.content.tabs[0].content.content.controls.append(self.widgets_dict.get('image_fit'))
        # Drop_Build_Editor.content.tabs[0].content.content.controls.append(self.widgets_dict.get('weight'))
        # # ######################### GRADIEN ENTRY #########################
        Drop_Build_Editor.content.tabs[0].content.content.controls.append(self.widgets_dict.get('gradient'))

        ########################################################################################
        # """
        # ######Drop_Build_Editor.content.tabs[1].content.content.controls.append(self.widgets_dict.get('margin'))
        # """
        # Drop_Build_Editor.content.tabs[0].content.content.controls.append(self.widgets_dict.get('border'))
        # Drop_Build_Editor.content.tabs[0].content.content.controls.append(self.widgets_dict.get("image_opacity "))
        # Drop_Build_Editor.content.tabs[0].content.content.controls.append(self.widgets_dict.get("image_src "))
        # Drop_Build_Editor.content.tabs[0].content.content.controls.append(self.widgets_dict.get("tooltip "))
        # Drop_Build_Editor.content.tabs[0].content.content.controls.append(self.widgets_dict.get("rotate "))
        # Drop_Build_Editor.content.tabs[0].content.content.controls.append(self.widgets_dict.get("scale "))
        # DOUBLE SELECTION ENTRY
        # Drop_Build_Editor.content.tabs[0].content.content.controls.append(self.widgets_dict.get("blur "))
        # Drop_Build_Editor.content.tabs[0].content.content.controls.append(self.widgets_dict.get("border "))
        # Drop_Build_Editor.content.tabs[0].content.content.controls.append(self.widgets_dict.get("offset "))
        # Drop_Build_Editor.content.tabs[0].content.content.controls.append(self.widgets_dict.get("width "))
        # 4 SELECTION ENTRIES
        # Drop_Build_Editor.content.tabs[0].content.content.controls.append(self.widgets_dict.get("padding "))
        # Drop_Build_Editor.content.tabs[0].content.content.controls.append(self.widgets_dict.get("margin "))
        # Drop_Build_Editor.content.tabs[0].content.content.controls.append(self.widgets_dict.get("border_radius "))
        # COLOR ENTRY ['RED' ...]
        # Drop_Build_Editor.content.tabs[0].content.content.controls.append(self.widgets_dict.get("bgcolor "))
        # BOOL ENTRY [TRUE FALSE]
        # Drop_Build_Editor.content.tabs[0].content.content.controls.append(self.widgets_dict.get("visible "))
        # Drop_Build_Editor.content.tabs[0].content.content.controls.append(self.widgets_dict.get("expand "))
        # Drop_Build_Editor.content.tabs[0].content.content.controls.append(self.widgets_dict.get("ink "))
        # SELECTION ENTRY
        # Drop_Build_Editor.content.tabs[0].content.content.controls.append(self.widgets_dict.get("image_fit "))
        # Drop_Build_Editor.content.tabs[0].content.content.controls.append(self.widgets_dict.get("alignment "))
        self.get_attributes = {
                                'Container':{
                                            'width ',  # <==== Height is implicited
                                            'scale ',
                                            'rotate ',
                                            'offset ',
                                            'bgcolor ',
                                            'visible ',
                                            'padding ',
                                            'blur ',
                                            'margin ',
                                            'border ',
                                            'tooltip ',
                                            'border_radius ',
                                            'ink ',
                                            'image_fit ',
                                            'image_src ',
                                            'image_opacity ',
                                            'expand ',
                                            'alignment ',

                                            # 'animate ',
                                            # 'url_target ',
                                            # 'url ',
                                            # 'clip_behavior ',
                                            # 'content ',
                                            # 'gradient ',
                                            # 'image_repeat ',
                                            # 'image_src_base64 ',
                                            # 'blend_mode ',
                                            # 'rtl ',
                                            # 'shadow ',
                                            # 'shape ',
                                            # 'theme_mode ',
                                            # 'theme ',
                                            }
        }

        # ######################## 1.0 -  WE GET NAME OF THE WIDGET
        # self.widget_name       = 'Container'
        # # self.widget_name     = self.widget.content._get_control_name()    # <<<==== widget name
        # ######################### 2.0 -  WE MAKE widgets_dict A SET TO GET INTERSECTION BETWEEN [widget_name] AND [widgets_dict.KEYS]
        # self.my_builder_widget = set(self.widgets_dict.keys())
        # ######################### 3.0 -  GET ATTRIBUTES AVIABLES INTERSECTION
        # # self.get_attributes_from_my_builder_widget       = set(self.widget.__dir__())                #  <=== DEFAULD dict attrib CONTAINER
        # self.get_attributes_from_my_builder_widget         = self.get_attributes.get(self.widget_name) #  <=== personal dict attrib CONTAINER

        # self.get_attributes_from_my_builder_widget_content = set(self.widget.content.__dir__())        #  <=== personal dict attrib CONTAINER CONTENT
        # ######################### 4.0 -  GET ONLY INTERSECTION TO GET SPECIFIC BUILDER ATRRIBUTES
        # self.compare_intersection         = self.get_attributes_from_my_builder_widget.intersection(self.my_builder_widget)           #  <=== personal CONTAINER || WIDGET_SELECTED coindences point
        # self.compare_intersection_content = self.get_attributes_from_my_builder_widget_content.intersection(self.my_builder_widget)   #  <=== personal WIDGET_SELECTED coindences point

        # # self.compare_intersection_content = self.compare_intersection_content.difference(self.get_attributes.get('Container'))        #  <=== personal get diference CONTAINER and WIDGET_SELECTED to use only Container attib and no repeat in WIDGET_SELECTED attributes
        # ######################### 4.0 - GET LIS OF BUILDER ATTRIBUTES
        # self.get_widgets         = [self.widgets_dict.get(_) for _ in self.compare_intersection]
        # self.get_widgets_content = [self.widgets_dict.get(_) for _ in self.compare_intersection_content]
        # ######################### 5.0 - ADD TO TAB CONTAINER
        # Drop_Build_Editor.content.tabs[0].content.content.controls = self.get_widgets
        # ######################### 5.0 - ADD TO TAB WIDGET
        # Drop_Build_Editor.content.tabs[1].content.content.controls = self.get_widgets_content
        # # ##########################################################################


        # print(self.widget_name)
        # print(self.my_builder_widget)
        # print(self.get_attributes_from_my_builder_widget)
        # print( self.compare_intersection)
        # print(self.get_widgets)
        return Drop_Build_Editor
######## BuildEditor = Build_Editor(),# <======= Comma

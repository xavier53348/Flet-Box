######################
from extra_utils.config_container.double_entry import DoubleEntry
from extra_utils.config_container.color_entry  import ColorEntry
from extra_utils.config_container.bool_entry   import BoolEntry
from extra_utils.config_container.four_entry   import FourEntry
from extra_utils.config_container.single_entry import SingleEntry
from extra_utils.config_container.selection_entry import SelectionEntry
from extra_utils.config_container.gradient_entry  import GradientEntry

from extra_utils.settings_var.settings_widget import global_var, get_global_var
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
        global Drop_Build_Editor

        Drop_Build_Editor=ft.Container(
                                ##################### PROPERTY ROW
                                padding       = ft.padding.all(0),    # inside box                     # padding.only(left=8, top=8, right=8, bottom=8),
                                margin        = ft.margin.all(0),     # outside box                    # margin.only (left=8, top=8, right=8, bottom=8),
                                border_radius = ft.border_radius.all(28),                              # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                                image_src     = f"dragg_container3.jpg",
                                image_opacity = 0.03,
                                image_fit     ='COVER',                                                # CONTAIN, COVER, FILL, FIT_HEIGHT, FIT_WIDTH, SCALE_DOWN
                                # blur        = 18,
                                width         = 370,
                                # height        = 580,
                                height        = 670,
                                # expand=True,
                                ############################
                            on_hover = lambda _:print(f'ID of the Config Container: {Drop_Build_Editor._Control__uid}'),

                            content = ft.Tabs(
                                            label_color             = 'BLUE',
                                            indicator_border_radius = ft.border_radius.all(20),
                                            tabs = [
                                                    ft.Tab( text = "Container",
                                                            # icon='',
                                                            content = ft.Container(
                                                                        ##################### PROPERTY COLUMN
                                                                        padding = ft.padding.all(4),    # inside box                        # padding.only(left=8, top=8, right=8, bottom=8),
                                                                        margin  = ft.margin.all(0),     # outside box                       # margin.only (left=8, top=8, right=8, bottom=8),
                                                                        ##################### WIDGETS
                                                                        content = ft.Row(
                                                                                ##################### PROPERTY BOX
                                                                                alignment   = ft.MainAxisAlignment.SPACE_BETWEEN,           # horizontal <=> START,CENTER,END SPACE_BETWEEN SPACE_AROUND SPACE_EVENLY
                                                                                scroll      = 'HIDDEN',                                     # center widget
                                                                                tight       = True,
                                                                                wrap        = True,                                         # justify in all screen
                                                                                spacing     = 0,                                            # space widget left right
                                                                                run_spacing = 8,                                            # space widget up down
                                                                                ##################### WIDGETS
                                                                            ),#<=== NOTE COMA [NOTE]                                        # for x in range(1,50): widget.content.controls.append(ft.ElevatedButton("press buttom",tooltip='buttom'))
                                                                            ##################### EVENTS
                                                                            # on_click=lambda _:print(_),                                   # on_hover=print('on click over'), on_long_press=print('long press'),
                                                                            # controls=[],
                                                            ),#<=== NOTE COMA
                                                    ),
                                                    ft.Tab(text="Widget",
                                                            content=ft.Container(
                                                                        ##################### PROPERTY COLUMN
                                                                        padding = ft.padding.all(4),    # inside box                        # padding.only(left=8, top=8, right=8, bottom=8),
                                                                        margin  = ft.margin.all(0),     # outside box                       # margin.only (left=8, top=8, right=8, bottom=8),
                                                                        ##################### WIDGETS
                                                                    content = ft.Row(
                                                                                ##################### PROPERTY BOX
                                                                                # expand = True,
                                                                                alignment = ft.MainAxisAlignment.SPACE_BETWEEN,              # horizontal <=> START,CENTER,END SPACE_BETWEEN SPACE_AROUND SPACE_EVENLY
                                                                                # horizontal_alignment =ft.CrossAxisAlignment.CENTER,        # vertical       START,CENTER END
                                                                                ##################### LET MAKE SCROLL IN LONG QUANTITY
                                                                                scroll      = 'HIDDEN',                                      # center widget
                                                                                tight       = True,
                                                                                ##################### ADAPT TO SCREEN
                                                                                wrap        = True,                                          # justify in all screen
                                                                                spacing     = 0,                                             # space widget left right
                                                                                run_spacing = 8,                                             # space widget up down
                                                                                ##################### WIDGETS
                                                                            ),#<=== NOTE COMA [NOTE]                                         # for x in range(1,50): widget.content.controls.append(ft.ElevatedButton("press buttom",tooltip='buttom'))
                                                                            ##################### EVENTS
                                                                            # on_click = lambda _:print(_),                                  # on_hover=print('on click over'), on_long_press=print('long press'),
                                                                            # controls = [ ],
                                                            ),#<=== NOTE COMA
                                                            ),
                                                    ]
                                            ),
                        )

        Drop_Build_Editor.content.tabs[0].content.content.controls = None

        return Drop_Build_Editor

    def update_widget_attributes(widget_cliked):
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
        widgets_dict = {
            ######################### ESPECIAL WIDGETS ONLY FOR CONTAINERS
            # SINGLE SELECTION ENTRY
            'image_opacity ':SingleEntry(config_widget = 'image_opacity ',widget = widget_cliked),  # <=== this take width and hight in same time
            'image_src '    :SingleEntry(config_widget = 'image_src '    ,widget = widget_cliked),  # <=== this take width and hight in same time
            'tooltip '      :SingleEntry(config_widget = 'tooltip '      ,widget = widget_cliked),  # <=== this take width and hight in same time
            'rotate '       :SingleEntry(config_widget = 'rotate '       ,widget = widget_cliked),  # <=== this take width and hight in same time
            'scale '        :SingleEntry(config_widget = 'scale '        ,widget = widget_cliked),  # <=== this take width and hight in same time
            # DOUBLE SELECTION ENTRY
            'border '       :DoubleEntry(config_widget = 'border '       ,widget = widget_cliked),  # <=== this take width and hight in same time
            'offset '       :DoubleEntry(config_widget = 'offset '       ,widget = widget_cliked),  # <=== this take width and hight in same time
            'width '        :DoubleEntry(config_widget = 'width '        ,widget = widget_cliked),  # <=== this take width and hight in same time
            'blur '         :DoubleEntry(config_widget = 'blur '         ,widget = widget_cliked),  # <=== this take width and hight in same time
            # 4 SELECTION ENTRIES
            'padding '      :FourEntry(config_widget   = 'padding '      ,widget = widget_cliked),
            'margin '       :FourEntry(config_widget   = 'margin '       ,widget = widget_cliked),
            'border_radius ':FourEntry(config_widget   = 'border_radius ',widget = widget_cliked),
            # COLOR ENTRY ['RED' ...]
            'bgcolor '      :ColorEntry(config_widget  = 'bgcolor '      ,widget = widget_cliked),
            # BOOL ENTRY [TRUE FALSE]
            'visible '      :BoolEntry(config_widget   = 'visible '      ,widget = widget_cliked),
            'expand '       :BoolEntry(config_widget   = 'expand '       ,widget = widget_cliked),
            'ink '          :BoolEntry(config_widget   = 'ink '          ,widget = widget_cliked),
            # SELECTION ENTRY
            'image_fit '    :SelectionEntry(config_widget = 'image_fit ' ,widget = widget_cliked),
            'alignment '    :SelectionEntry(config_widget = 'alignment ' ,widget = widget_cliked),
            # SELECTION GRADIENT
            'gradient '     :GradientEntry(config_widget  = 'gradient '  ,widget = widget_cliked),
            ##################################################################################################
            ######################### SINGLE SELECTION ENTRY
            'text'                :SingleEntry(config_widget = 'text'             ,widget = widget_cliked),  # <=== this take width and hight in same time
            'size'                :SingleEntry(config_widget = 'size'             ,widget = widget_cliked),  # <=== this take width and hight in same time
            'label'               :SingleEntry(config_widget = 'label'            ,widget = widget_cliked),  # <=== this take width and hight in same time
            'value'               :SingleEntry(config_widget = 'value'            ,widget = widget_cliked),  # <=== this take width and hight in same time
            'key'                 :SingleEntry(config_widget = 'key'              ,widget = widget_cliked),  # <=== this take width and hight in same time
            'hint_text'           :SingleEntry(config_widget = 'hint_text'        ,widget = widget_cliked),  # <=== this take width and hight in same time
            'counter_text'        :SingleEntry(config_widget = 'counter_text'     ,widget = widget_cliked),  # <=== this take width and hight in same time
            'suffix_text'         :SingleEntry(config_widget = 'suffix_text'      ,widget = widget_cliked),  # <=== this take width and hight in same time
            'url'                 :SingleEntry(config_widget = 'url'              ,widget = widget_cliked),  # <=== this take width and hight in same time
            'url_target'          :SingleEntry(config_widget = 'url_target'       ,widget = widget_cliked),  # <=== this take width and hight in same time
            'icon'                :SingleEntry(config_widget = 'icon'             ,widget = widget_cliked),  # <=== this take width and hight in same time
            'tooltip'             :SingleEntry(config_widget = 'tooltip'          ,widget = widget_cliked),  # <=== this take width and hight in same time
            'src'                 :SingleEntry(config_widget = 'src'              ,widget = widget_cliked),  # <=== this take width and hight in same time
            'data'                :SingleEntry(config_widget = 'data'             ,widget = widget_cliked),  # <=== this take width and hight in same time
            'semantics_label'     :SingleEntry(config_widget = 'semantics_label'  ,widget = widget_cliked),  # <=== this take width and hight in same time
            'src_base64'          :SingleEntry(config_widget = 'src_base64'       ,widget = widget_cliked),  # <=== this take width and hight in same time
            'image_src'           :SingleEntry(config_widget = 'image_src'        ,widget = widget_cliked),  # <=== this take width and hight in same time
            'blur_radius'         :SingleEntry(config_widget = 'blur_radius'      ,widget = widget_cliked),  # <=== this take width and hight in same time
            'spread_radius'       :SingleEntry(config_widget = 'spread_radius'    ,widget = widget_cliked),  # <=== this take width and hight in same time
            'elevation'           :SingleEntry(config_widget = 'elevation'        ,widget = widget_cliked),  # <=== this take width and hight in same time
            'rotate'              :SingleEntry(config_widget = 'rotate'           ,widget = widget_cliked),  # <=== this take width and hight in same time
            'scale'               :SingleEntry(config_widget = 'scale'            ,widget = widget_cliked),  # <=== this take width and hight in same time
            'aspect_ratio'        :SingleEntry(config_widget = 'aspect_ratio'     ,widget = widget_cliked),  # <=== this take width and hight in same time
            'runs_count'          :SingleEntry(config_widget = 'runs_count'       ,widget = widget_cliked),  # <=== this take width and hight in same time
            'run_spacing'         :SingleEntry(config_widget = 'run_spacing'      ,widget = widget_cliked),  # <=== this take width and hight in same time
            'spacing'             :SingleEntry(config_widget = 'spacing'          ,widget = widget_cliked),  # <=== this take width and hight in same time
            'child_aspect_ratio'  :SingleEntry(config_widget = 'child_aspect_ratio',widget = widget_cliked), # <=== this take width and hight in same time
            'max_extent'          :SingleEntry(config_widget = 'max_extent'       ,widget = widget_cliked),  # <=== this take width and hight in same time
            'min_lines'           :SingleEntry(config_widget = 'min_lines'        ,widget = widget_cliked),  # <=== this take width and hight in same time
            'max_lines'           :SingleEntry(config_widget = 'max_lines'        ,widget = widget_cliked),  # <=== this take width and hight in same time
            'border_width'        :SingleEntry(config_widget = 'border_width'     ,widget = widget_cliked),  # <=== this take width and hight in same time
            'text_size'           :SingleEntry(config_widget = 'text_size'        ,widget = widget_cliked),  # <=== this take width and hight in same time
            'image_opacity'       :SingleEntry(config_widget = 'image_opacity'    ,widget = widget_cliked),  # <=== this take width and hight in same time
            'opacity'             :SingleEntry(config_widget = 'opacity'          ,widget = widget_cliked),  # <=== this take width and hight in same time
            ######################### DOUBLE SELECTION ENTRY
            'width'               :DoubleEntry(config_widget = 'width'            ,widget = widget_cliked),  # <=== this take width and hight in same time
            'border'              :DoubleEntry(config_widget = 'border'           ,widget = widget_cliked),
            'offset'              :DoubleEntry(config_widget = 'offset'           ,widget = widget_cliked),
            'blur'                :DoubleEntry(config_widget = 'blur'             ,widget = widget_cliked),
            ######################### 4 SELECTION ENTRIE S
            'padding'             :FourEntry(config_widget = 'padding'            ,widget = widget_cliked),
            'margin'              :FourEntry(config_widget = 'margin'             ,widget = widget_cliked),
            'border_radius'       :FourEntry(config_widget = 'border_radius'      ,widget = widget_cliked),
            ######################### COLOR ENTRY ['RED' ...]
            'bgcolor'             :ColorEntry(config_widget= 'bgcolor'            ,widget = widget_cliked),
            'color'               :ColorEntry(config_widget= 'color'              ,widget = widget_cliked),
            'shadow_color'        :ColorEntry(config_widget= 'shadow_color'       ,widget = widget_cliked),
            'icon_color'          :ColorEntry(config_widget= 'icon_color'         ,widget = widget_cliked),
            'check_color'         :ColorEntry(config_widget= 'check_color'        ,widget = widget_cliked),
            'fill_color'          :ColorEntry(config_widget= 'fill_color'         ,widget = widget_cliked),
            'border_color'        :ColorEntry(config_widget= 'border_color'       ,widget = widget_cliked),
            'focused_bgcolor'     :ColorEntry(config_widget= 'focused_bgcolor'    ,widget = widget_cliked),
            'focused_border_color':ColorEntry(config_widget= 'focused_border_color',widget= widget_cliked),
            ######################### BOOL ENTRY [TRUE FALSE]
            'expand':             BoolEntry(config_widget = 'expand'              ,widget = widget_cliked),
            'ink':                BoolEntry(config_widget = 'ink'                 ,widget = widget_cliked),
            'scroll':             BoolEntry(config_widget = 'scroll'              ,widget = widget_cliked),
            'wrap':               BoolEntry(config_widget = 'wrap'                ,widget = widget_cliked),
            'tight':              BoolEntry(config_widget = 'tight'               ,widget = widget_cliked),
            'visible':            BoolEntry(config_widget = 'visible'             ,widget = widget_cliked),
            'multiline':          BoolEntry(config_widget = 'multiline'           ,widget = widget_cliked),
            'disabled':           BoolEntry(config_widget = 'disabled'            ,widget = widget_cliked),
            'read_only':          BoolEntry(config_widget = 'read_only'           ,widget = widget_cliked),
            'password':           BoolEntry(config_widget = 'password'            ,widget = widget_cliked),
            'filled':             BoolEntry(config_widget = 'filled'              ,widget = widget_cliked),
            'adaptive':           BoolEntry(config_widget = 'adaptive'            ,widget = widget_cliked),
            'tristate':           BoolEntry(config_widget = 'tristate'            ,widget = widget_cliked),
            'autofocus':          BoolEntry(config_widget = 'autofocus'           ,widget = widget_cliked),
            'horizontal':         BoolEntry(config_widget = 'horizontal'          ,widget = widget_cliked),
            'can_reveal_password':BoolEntry(config_widget = 'can_reveal_password' ,widget = widget_cliked),
            'capitalization':     BoolEntry(config_widget = 'capitalization'      ,widget = widget_cliked),
            'gapless_playback':   BoolEntry(config_widget = 'gapless_playback'    ,widget = widget_cliked),
            ######################### SELECTION ENTRY
            'image_fit':          SelectionEntry(config_widget = 'image_fit'      ,widget = widget_cliked),
            'weight':             SelectionEntry(config_widget = 'weight'         ,widget = widget_cliked),
            'keyboard_type':      SelectionEntry(config_widget = 'keyboard_type'  ,widget = widget_cliked),
            'text_align':         SelectionEntry(config_widget = 'text_align'     ,widget = widget_cliked),
            'alignment':          SelectionEntry(config_widget = 'alignment'      ,widget = widget_cliked),
            'content_alignment':  SelectionEntry(config_widget = 'content_alignment' ,widget = widget_cliked),
            'vertical_alignment' :SelectionEntry(config_widget = 'vertical_alignment',widget = widget_cliked),
           'horizontal_alignment':SelectionEntry(config_widget = 'horizontal_alignment',widget = widget_cliked),
            ######################### GRADIEN ENTRY
           'gradient':            GradientEntry(config_widget   = 'gradient',widget = widget_cliked),
            #############################################################################################

        }

        get_attributes = {
                        'container':{
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
                                    'gradient ',

                                    # 'animate ',
                                    # 'url_target ',
                                    # 'url ',
                                    # 'clip_behavior ',
                                    # 'content ',
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

        ##################################################
        ######################### TAKE NAME IN STR OF THE WIDGET DRAGG AND CONTENT NAME
        tmp_clicked_widget                   = widget_cliked._get_control_name()            # NAME 'Container'
        ######################### 2.0 -SET ALL KEYS INSIDE widgets_dict TO COMPARE WITH tmp_widget_clicked TO GET INTERSECTION BETWEEN [tmp_widget_clicked] AND [widgets_dict.KEYS]
        # check_clicked_widget               = set(widget_cliked.__dir__())                 # ATTRIBUTES TO COMPARE 'Widget Container'
        check_clicked_widget_content         = set(widget_cliked.content.__dir__())         # ATTRIBUTES TO COMPARE 'Widget Container.content'
        # our dictionaries
        attrib_compare_container_dict        = set(get_attributes.get(tmp_clicked_widget))  # ATTRIBUTES TO COMPARE 'Container'
        attrib_compare_container_widget_dict = set(widgets_dict.keys())                     # ATTRIBUTES TO COMPARE 'Container.content'
        # ALL DOWN WORK
        ########################

        get_widgets         = {widgets_dict.get(_) for _ in attrib_compare_container_dict}
        ########################

        ######################### set making error in intersection solved with personal set
        # print(check_clicked_widget_content.intersection(attrib_compare_container_widget_dict))
        # if container_property not in widget_cliked.content take and if in widgets_dict.keys() take only intersection
        # data_ = widget_cliked.content._Control__attrs.keys()
        # data_ =  [ _ for _ in attrib_compare_container_widget_dict if _ in data_ ]
        print(widget_cliked.content)
        ######################### set making error in intersection solved with personal set
        intersection_filter_data = { widgets_dict.get(_) for _ in check_clicked_widget_content if not _ in attrib_compare_container_dict if _ in attrib_compare_container_widget_dict }
        # ##########################################################################
        main_page_to_update = get_global_var(get_var='page')
        tmp_                = main_page_to_update.get_control('_330')
        ######################## 4.0 - GET LIS OF BUILDER ATTRIBUTES get_attributes
        # print(tmp_,'<<<<<<<')
        tmp_.content.tabs[0].content.content.controls = get_widgets # #<<<<<<<<<<
        # ######################### 5.0 - ADD TO TAB WIDGET
        tmp_.content.tabs[1].content.content.controls = intersection_filter_data
        # ##########################################################################
        tmp_.content.update()

        ######## BuildEditor = Build_Editor(),# <======= Comma

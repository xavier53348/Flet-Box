import flet as ft

from .double_entry     import DoubleEntry
from .color_entry      import ColorEntry
from .bool_entry       import BoolEntry
from .four_entry       import FourEntry
from .single_entry     import SingleEntry
from .selection_entry  import SelectionEntry
from .gradient_entry   import GradientEntry
from .blur_color_entry import BlurColorEntry

from ..settings_var.settings_widget import GLOBAL_VAR


class BoxConfigContainer(ft.Stack):
    """
    RIGHT BOX THAT CONTENT ALL WIDGET TO MODY ATTRIBUTES WILL SHOW OR NOT DEPENDING PREES CONFIGURATION ACTION BUTTON
    """
    def __init__(self,
                 title: str="",
                 controls: list=[]
                 ):
        super().__init__()
        self.title    = title
        self.controls = controls

    def build(self):
        Drop_BoxConfigContainer = ft.Container(
                              padding = ft.padding.only(left=4, top=4, right=4, bottom=4),
                         content = ft.Column(
                                   controls = [

                                             ft.Container(
                                                       border_radius = ft.border_radius.all(20),
                                                       bgcolor       = ft.colors.BLACK26,
                                                       padding       = ft.padding.only(left=8, top=2, right=8, bottom=2),
                                                       margin        = ft.margin.only( left=8, top=2, right=20, bottom=2),
                                                       gradient      = ft.LinearGradient(
                                                                                          begin = ft.alignment.top_center,
                                                                                          end   = ft.alignment.bottom_center,
                                                                                          colors= [ft.colors.TEAL, ft.colors.BLACK38],),
                                                  content=ft.Text(
                                                                 value       = self.title,
                                                                 text_align  = ft.TextAlign.CENTER,

                                                                 font_family = "Consolas", #"Consolas ,RobotoSlab
                                                                 color       = ft.colors.WHITE,
                                                       ),
                                                  ),
                                             ft.Container(
                                                       bgcolor       = ft.colors.BLACK38,
                                                       width         = 425,
                                                       padding       = ft.padding.only(left=6, top=6, right=6, bottom=6),
                                                       border_radius = ft.border_radius.all(20),
                                                  content=ft.Row(
                                                                 wrap= True,
                                                            controls = self.controls
                                                       ,),),
                                                  ], #: <<<< controls
                                             ),      #: <<<< column
                                        )            #: <<<< container
        return Drop_BoxConfigContainer

class Build_Editor(ft.Stack):
     """
     MAIN BUILDER EDITOR: IT'S A ROW CONTAINER THAT WILL CONTENT ALL WIDGET INSIDE WILL CALL BoxConfigContainer
     FUNCTION THAT HAVE THE BOX TO SHOW ASACTLY THE WIDGET ATTRIBUTES TO MODIFY

     Tabs:
        Container:
                edit_Container: value
        Widget:
                edit_Widget: value

     NOTE:
        Is necessary put class widget of the widget to edit Attributes
     """

     def __init__(self,widget=""):
          super().__init__()
          #: VERY IMPORTANT
          #: WIDGET PHONE SELECTED TO MODIFY ATTRIBUTES
          # if not widget == "":
          #      self.widget = widget
          # else:
          #      print('hello world')
          # self.widget = GLOBAL_VAR(get_global_var='main_screen').build()
          # self.widget = ""
          # print(self.widget.uid ,'<<<<<<< WIDGER')
          # self.build()
          self.widget = ''

     def build(self):
          """
          ALL IN THIS APP IS A MODULE THAT'S WAY YOU MAY TAKE THE PART THAT YOU WANT REBUILD

          widgets_dict <= IS A DICT THAT CONTAIN ALL WIDGET THAT ARE WATING TO SHOW BECOUS BY DEFAULD ARE VISIBLE = OFF
          """
          global Drop_Build_Editor
          # self.selected_screen           = GLOBAL_VAR(get_global_var='SELECT_SCREEN')

          # self.main_phone                 = self.widget
          # self.main_phone                 = GLOBAL_VAR(get_global_var='SELECTED_SCREEN')

          # self.main_phone                 = GLOBAL_VAR(get_global_var='PHONE_MAIN')
          # self.main_phone                 = GLOBAL_VAR(get_global_var='PHONE_MAIN')
          # self.main_phone_conainer        = GLOBAL_VAR(get_global_var='PHONE_CONTAINER')
          # self.main_phone_conainer_conent = GLOBAL_VAR(get_global_var='PHONE_CONTAINER_CONTENT')


          # print(self.main_phone,'main_phone')
          self.main_phone                 = GLOBAL_VAR(get_global_var='SELECTED_SCREEN')            # main_phone
          self.main_phone_conainer        =  self.main_phone.content.content.content                # main_phone_conainer
          self.main_phone_conainer_conent =  self.main_phone.content.content.content.content        # main_phone_conainer_conent

          self.container_widget           = GLOBAL_VAR(get_global_var='SELECT_DROPP_WIDGET_CONTAINER')
          self.container_widget_content   = GLOBAL_VAR(get_global_var='SELECT_DROPP_WIDGET_CONTAINER_CONTENT')

          widgets_dict = {

               #: ESPECIAL WIDGETS ONLY FOR PHONE

               'phone_margin'       :FourEntry(      config_widget='padding'               ,widget=self.main_phone_conainer        ,id_name_widget_dict="main_phone_conainer"),

               'phone_image_src'    :SingleEntry(    config_widget='image_src'             ,widget=self.main_phone                 ,id_name_widget_dict='main_phone'),
               'phone_image_opacity':SingleEntry(    config_widget='image_opacity'         ,widget=self.main_phone                 ,id_name_widget_dict='main_phone'),
              'column_phone_spacing':SingleEntry(    config_widget='spacing'               ,widget=self.main_phone_conainer_conent ,id_name_widget_dict="main_phone_conainer_conent"),

               'phone_bgcolor'      :ColorEntry(     config_widget='bgcolor'               ,widget=self.main_phone_conainer        ,id_name_widget_dict="main_phone_conainer"),

               'column_phone_wrap'  :BoolEntry(      config_widget='wrap'                  ,widget=self.main_phone_conainer_conent ,id_name_widget_dict="main_phone_conainer_conent"),
               'column_phone_tight' :BoolEntry(      config_widget='tight'                 ,widget=self.main_phone_conainer_conent ,id_name_widget_dict="main_phone_conainer_conent"),
               'column_phone_scroll':BoolEntry(      config_widget='scroll'                ,widget=self.main_phone_conainer_conent ,id_name_widget_dict="main_phone_conainer_conent"),

               'phone_image_fit'    :SelectionEntry( config_widget='image_fit'             ,widget=self.main_phone                 ,id_name_widget_dict='main_phone'),
           'column_phone_alignment' :SelectionEntry( config_widget='alignment'             ,widget=self.main_phone_conainer_conent ,id_name_widget_dict="main_phone_conainer_conent"),
'column_phone_horizontal_alignment' :SelectionEntry( config_widget='horizontal_alignment'  ,widget=self.main_phone_conainer_conent ,id_name_widget_dict="main_phone_conainer_conent"),

               'phone_gradient'     :GradientEntry(  config_widget='gradient'              ,widget=self.main_phone                 ,id_name_widget_dict='main_phone'),
               'phone_blur'         :DoubleEntry(    config_widget='blur'                  ,widget=self.main_phone_conainer        ,id_name_widget_dict="main_phone_conainer"),

               #: ESPECIAL WIDGETS ONLY FOR CONTAINERS

               'container_rotate'   :SingleEntry(    config_widget='rotate'                ,widget=self.container_widget),
               'container_scale'    :SingleEntry(    config_widget='scale'                 ,widget=self.container_widget),
               'container_padding'  :FourEntry(      config_widget='padding'               ,widget=self.container_widget),
               'container_margin'   :FourEntry(      config_widget='margin'                ,widget=self.container_widget),
               'container_offset'   :DoubleEntry(    config_widget='offset'                ,widget=self.container_widget),
               'container_alignment':SelectionEntry( config_widget='alignment '            ,widget=self.container_widget),

               'container_width'    :DoubleEntry(    config_widget='width'                 ,widget=self.container_widget),
               'container_scale'    :SingleEntry(    config_widget='scale'                 ,widget=self.container_widget),
               'container_border'   :DoubleEntry(    config_widget='border'                ,widget=self.container_widget),
               'container_expand'   :BoolEntry(      config_widget='expand'                ,widget=self.container_widget),
               'container_ink'      :BoolEntry(      config_widget='ink'                   ,widget=self.container_widget),
               'container_visible'  :BoolEntry(      config_widget='visible'               ,widget=self.container_widget),
           'container_border_radius':FourEntry(      config_widget='border_radius'         ,widget=self.container_widget),

               # 'container_blur'     :DoubleEntry(    config_widget='blur'                  ,widget=self.container_widget),
               'container_bgcolor'  :ColorEntry(     config_widget='bgcolor'               ,widget=self.container_widget),
               'BlurColorEntry'     :BlurColorEntry( config_widget='blur'                  ,widget=self.container_widget),

               'shadow_color'       :ColorEntry(     config_widget='shadow_color'          ,widget=self.container_widget),
               'container_gradient' :GradientEntry(  config_widget='gradient'              ,widget=self.container_widget),

           'container_image_src'    :SingleEntry(    config_widget='image_src'             ,widget=self.container_widget),
           'container_image_opacity':SingleEntry(    config_widget='image_opacity'         ,widget=self.container_widget),
           'container_image_fit'    :SelectionEntry( config_widget='image_fit'             ,widget=self.container_widget),

               #: ESPECIAL WIDGETS ONLY FOR WIDGET

               'text'                :SingleEntry(config_widget='text'             ,widget=self.container_widget_content , id_name_widget_dict='text'),
               'name'                :SingleEntry(config_widget='name'             ,widget=self.container_widget_content , id_name_widget_dict='name'),
               'size'                :SingleEntry(config_widget='size'             ,widget=self.container_widget_content , id_name_widget_dict='size'),
               'label'               :SingleEntry(config_widget='label'            ,widget=self.container_widget_content , id_name_widget_dict='label'),
               'value'               :SingleEntry(config_widget='value'            ,widget=self.container_widget_content , id_name_widget_dict='value'),

               'hint_text'           :SingleEntry(config_widget='hint_text'        ,widget=self.container_widget_content , id_name_widget_dict='hint_text'),
               'counter_text'        :SingleEntry(config_widget='counter_text'     ,widget=self.container_widget_content , id_name_widget_dict='counter_text'),
               'suffix_text'         :SingleEntry(config_widget='suffix_text'      ,widget=self.container_widget_content , id_name_widget_dict='suffix_text'),
               'url'                 :SingleEntry(config_widget='url'              ,widget=self.container_widget_content , id_name_widget_dict='url'),
               'url_target'          :SingleEntry(config_widget='url_target'       ,widget=self.container_widget_content , id_name_widget_dict='url_target'),
               'icon'                :SingleEntry(config_widget='icon'             ,widget=self.container_widget_content , id_name_widget_dict='icon'),
               'tooltip'             :SingleEntry(config_widget='tooltip'          ,widget=self.container_widget_content , id_name_widget_dict='tooltip'),
               'src'                 :SingleEntry(config_widget='src'              ,widget=self.container_widget_content , id_name_widget_dict='src'),
               'data'                :SingleEntry(config_widget='data'             ,widget=self.container_widget_content , id_name_widget_dict='data'),
               'semantics_label'     :SingleEntry(config_widget='semantics_label'  ,widget=self.container_widget_content , id_name_widget_dict='semantics_label'),
               'src_base64'          :SingleEntry(config_widget='src_base64'       ,widget=self.container_widget_content , id_name_widget_dict='src_base64'),
               'image_src'           :SingleEntry(config_widget='image_src'        ,widget=self.container_widget_content , id_name_widget_dict='image_src'),
               'blur_radius'         :SingleEntry(config_widget='blur_radius'      ,widget=self.container_widget_content , id_name_widget_dict='blur_radius'),
               'spread_radius'       :SingleEntry(config_widget='spread_radius'    ,widget=self.container_widget_content , id_name_widget_dict='spread_radius'),
               'elevation'           :SingleEntry(config_widget='elevation'        ,widget=self.container_widget_content , id_name_widget_dict='elevation'),
               'rotate'              :SingleEntry(config_widget='rotate'           ,widget=self.container_widget_content , id_name_widget_dict='rotate'),
               'scale'               :SingleEntry(config_widget='scale'            ,widget=self.container_widget_content , id_name_widget_dict='scale'),
               'aspect_ratio'        :SingleEntry(config_widget='aspect_ratio'     ,widget=self.container_widget_content , id_name_widget_dict='aspect_ratio'),
               'runs_count'          :SingleEntry(config_widget='runs_count'       ,widget=self.container_widget_content , id_name_widget_dict='runs_count'),
               'run_spacing'         :SingleEntry(config_widget='run_spacing'      ,widget=self.container_widget_content , id_name_widget_dict='run_spacing'),
               'spacing'             :SingleEntry(config_widget='spacing'          ,widget=self.container_widget_content , id_name_widget_dict='spacing'),
               'child_aspect_ratio'  :SingleEntry(config_widget ='child_aspect_ratio',widget=self.container_widget_content , id_name_widget_dict='child_aspect_ratio'),
               'max_extent'          :SingleEntry(config_widget='max_extent'       ,widget=self.container_widget_content , id_name_widget_dict='max_extent'),
               'min_lines'           :SingleEntry(config_widget='min_lines'        ,widget=self.container_widget_content , id_name_widget_dict='min_lines'),
               'max_lines'           :SingleEntry(config_widget='max_lines'        ,widget=self.container_widget_content , id_name_widget_dict='max_lines'),
               'border_width'        :SingleEntry(config_widget='border_width'     ,widget=self.container_widget_content , id_name_widget_dict='border_width'),
               'text_size'           :SingleEntry(config_widget='text_size'        ,widget=self.container_widget_content , id_name_widget_dict='text_size'),
               'image_opacity'       :SingleEntry(config_widget='image_opacity'    ,widget=self.container_widget_content , id_name_widget_dict='image_opacity'),
               'opacity'             :SingleEntry(config_widget='opacity'          ,widget=self.container_widget_content , id_name_widget_dict='opacity'),

               #: DOUBLE SELECTION ENTRY

               'width'               :DoubleEntry(config_widget='width'            ,widget=self.container_widget_content , id_name_widget_dict='width'),
               'border'              :DoubleEntry(config_widget='border'           ,widget=self.container_widget_content , id_name_widget_dict='border'),
               'offset'              :DoubleEntry(config_widget='offset'           ,widget=self.container_widget_content , id_name_widget_dict='offset'),
               'blur'                :DoubleEntry(config_widget='blur'             ,widget=self.container_widget_content , id_name_widget_dict='blur'),

               #: 4 SELECTION ENTRIE S

               'padding'             :FourEntry(config_widget='padding'            ,widget=self.container_widget_content , id_name_widget_dict='padding'),
               'margin'              :FourEntry(config_widget='margin'             ,widget=self.container_widget_content , id_name_widget_dict='margin'),
               'border_radius'       :FourEntry(config_widget='border_radius'      ,widget=self.container_widget_content , id_name_widget_dict='border_radius'),

               #: COLOR ENTRY ['RED' ...]

               'bgcolor'             :ColorEntry(config_widget= 'bgcolor'            ,widget=self.container_widget_content , id_name_widget_dict='bgcolor'),
               'color'               :ColorEntry(config_widget= 'color'              ,widget=self.container_widget_content , id_name_widget_dict='color'),
               'icon_color'          :ColorEntry(config_widget= 'icon_color'         ,widget=self.container_widget_content , id_name_widget_dict='icon_color'),
               'check_color'         :ColorEntry(config_widget= 'check_color'        ,widget=self.container_widget_content , id_name_widget_dict='check_color'),
               'fill_color'          :ColorEntry(config_widget= 'fill_color'         ,widget=self.container_widget_content , id_name_widget_dict='fill_color'),
               'border_color'        :ColorEntry(config_widget= 'border_color'       ,widget=self.container_widget_content , id_name_widget_dict='border_color'),
               'focused_bgcolor'     :ColorEntry(config_widget= 'focused_bgcolor'    ,widget=self.container_widget_content , id_name_widget_dict='focused_bgcolor'),
               'focused_border_color':ColorEntry(config_widget= 'focused_border_color',widget=self.container_widget_content, id_name_widget_dict='focused_border_color'),
               'box_shadow'          :ColorEntry(config_widget= 'box_shadow',         widget=self.container_widget_content , id_name_widget_dict='box_shadow'),

               #: BOOL ENTRY [TRUE FALSE]

               'expand':             BoolEntry(config_widget='expand'              ,widget=self.container_widget_content , id_name_widget_dict='expand'),
               'ink':                BoolEntry(config_widget='ink'                 ,widget=self.container_widget_content , id_name_widget_dict='ink'),
               'scroll':             BoolEntry(config_widget='scroll'              ,widget=self.container_widget_content , id_name_widget_dict='scroll'),
               'wrap':               BoolEntry(config_widget='wrap'                ,widget=self.container_widget_content , id_name_widget_dict='wrap'),
               'tight':              BoolEntry(config_widget='tight'               ,widget=self.container_widget_content , id_name_widget_dict='tight'),
               'visible':            BoolEntry(config_widget='visible'             ,widget=self.container_widget_content , id_name_widget_dict='visible'),
               'multiline':          BoolEntry(config_widget='multiline'           ,widget=self.container_widget_content , id_name_widget_dict='multiline'),
               'disabled':           BoolEntry(config_widget='disabled'            ,widget=self.container_widget_content , id_name_widget_dict='disabled'),
               'read_only':          BoolEntry(config_widget='read_only'           ,widget=self.container_widget_content , id_name_widget_dict='read_only'),
               'password':           BoolEntry(config_widget='password'            ,widget=self.container_widget_content , id_name_widget_dict='password'),
               'filled':             BoolEntry(config_widget='filled'              ,widget=self.container_widget_content , id_name_widget_dict='filled'),
               'adaptive':           BoolEntry(config_widget='adaptive'            ,widget=self.container_widget_content , id_name_widget_dict='adaptive'),
               'tristate':           BoolEntry(config_widget='tristate'            ,widget=self.container_widget_content , id_name_widget_dict='tristate'),
               'autofocus':          BoolEntry(config_widget='autofocus'           ,widget=self.container_widget_content , id_name_widget_dict='read_only'),
               'horizontal':         BoolEntry(config_widget='horizontal'          ,widget=self.container_widget_content , id_name_widget_dict='horizontal'),
               'can_reveal_password':BoolEntry(config_widget='can_reveal_password' ,widget=self.container_widget_content , id_name_widget_dict='can_reveal_password'),
               'capitalization':     BoolEntry(config_widget='capitalization'      ,widget=self.container_widget_content , id_name_widget_dict='capitalization'),
               'gapless_playback':   BoolEntry(config_widget='gapless_playback'    ,widget=self.container_widget_content , id_name_widget_dict='gapless_playback'),

               #: SELECTION ENTRY

               'image_fit':          SelectionEntry(config_widget='image_fit'           ,widget=self.container_widget_content , id_name_widget_dict='image_fit'),
               'weight':             SelectionEntry(config_widget='weight'              ,widget=self.container_widget_content , id_name_widget_dict='weight'),
               'keyboard_type':      SelectionEntry(config_widget='keyboard_type'       ,widget=self.container_widget_content , id_name_widget_dict='keyboard_type'),
               'text_align':         SelectionEntry(config_widget='text_align'          ,widget=self.container_widget_content , id_name_widget_dict='text_align'),
               'alignment':          SelectionEntry(config_widget='alignment'           ,widget=self.container_widget_content , id_name_widget_dict='alignment'),
               'content_alignment':  SelectionEntry(config_widget='content_alignment'   ,widget=self.container_widget_content , id_name_widget_dict='content_alignment'),
               'vertical_alignment' :SelectionEntry(config_widget='vertical_alignment'  ,widget=self.container_widget_content , id_name_widget_dict='vertical_alignment'),
              'horizontal_alignment':SelectionEntry(config_widget='horizontal_alignment',widget=self.container_widget_content , id_name_widget_dict='horizontal_alignment'),

               #: GRADIEN ENTRY

               'gradient':           GradientEntry(config_widget ='gradient'            ,widget=self.container_widget_content , id_name_widget_dict='gradient'),
          }

          self.main_phone_tab_1 =ft.Container(
                                   padding = ft.padding.only(left=4, top=4, right=4, bottom=4),
                              content = ft.Column(
                                             scroll="HIDDEN",
                                             controls = [
                                                       BoxConfigContainer(
                                                                 title='Color Phone Container',
                                                            controls=[
                                                                      widgets_dict.get('phone_blur'),
                                                                      widgets_dict.get('phone_bgcolor'),
                                                                      widgets_dict.get('phone_gradient'),
                                                                 ],),

                                                       BoxConfigContainer(
                                                                 title='Image Phone Container',
                                                            controls=[
                                                                      widgets_dict.get('phone_image_src'),
                                                                      widgets_dict.get('phone_image_fit'),
                                                                      widgets_dict.get('phone_image_opacity'),
                                                                 ],),

                                                       BoxConfigContainer(
                                                                 title='Column Phone Property',
                                                            controls=[
                                                                      widgets_dict.get('phone_margin'),
                                                                      widgets_dict.get('column_phone_tight'),
                                                                      widgets_dict.get('column_phone_wrap'),
                                                                      widgets_dict.get('column_phone_scroll'),
                                                                      widgets_dict.get('column_phone_spacing'),
                                                                      widgets_dict.get('column_phone_alignment'),
                                                                      widgets_dict.get('column_phone_horizontal_alignment'),
                                                                 ],),
                                                       ],
                                                  ),
                                             )
          self.widget_container = ft.Container(
                                   padding = ft.padding.only(left=4, top=4, right=4, bottom=4),
                                   visible=False,
                              content = ft.Column(
                                             scroll="HIDDEN",
                                             controls = [
                                                       BoxConfigContainer(
                                                                 title='Color Container',
                                                            controls=[
                                                                      widgets_dict.get('BlurColorEntry'),
                                                                      widgets_dict.get('container_gradient'),
                                                                      widgets_dict.get('container_ink'),
                                                                      widgets_dict.get('container_bgcolor'),
                                                                      widgets_dict.get('shadow_color'),
                                                                 ],),

                                                       BoxConfigContainer(
                                                                 title='Image Container',
                                                            controls=[
                                                                      widgets_dict.get('container_image_fit'),
                                                                      widgets_dict.get('container_image_src'),
                                                                      widgets_dict.get('container_image_opacity'),
                                                                 ],),

                                                       BoxConfigContainer(
                                                                 title='Position Container',
                                                            controls=[
                                                                      widgets_dict.get('container_padding'),
                                                                      widgets_dict.get('container_margin'),
                                                                      widgets_dict.get('container_border_radius'),
                                                                      widgets_dict.get('container_border'),
                                                                      widgets_dict.get('container_rotate'),
                                                                      widgets_dict.get('container_scale'),
                                                                      widgets_dict.get('container_offset'),
                                                                      widgets_dict.get('container_alignment'),
                                                                 ],),

                                                       BoxConfigContainer(
                                                                 title='Modification Container',
                                                            controls=[
                                                                      widgets_dict.get('container_width'),
                                                                      widgets_dict.get('container_expand'),
                                                                      widgets_dict.get('container_visible'),
                                                                 ],),

                                                       ],
                                                  ),
                                             )

          self.widget_container_content  =ft.Container(
                                   padding = ft.padding.only(left=4, top=4, right=4, bottom=4),
                                   visible = False,
                              content = ft.Column(
                                             scroll="HIDDEN",
                                             controls = [

                                                       BoxConfigContainer(
                                                                 title='Modification Widget',
                                                            controls=[
                                                                      widgets_dict.get('visible'),
                                                                      widgets_dict.get('disabled'),
                                                                      widgets_dict.get('read_only'),
                                                                      widgets_dict.get('autofocus'),
                                                                      widgets_dict.get('ink'),
                                                                      widgets_dict.get('scroll'),
                                                                      widgets_dict.get('tristate'),
                                                                      widgets_dict.get('gapless_playback'),
                                                                 ],),

                                                       BoxConfigContainer(
                                                                 title='Input Text Data',
                                                            controls=[
                                                                      widgets_dict.get('text'),
                                                                      widgets_dict.get('name'),
                                                                      widgets_dict.get('label'),
                                                                      widgets_dict.get('data'),
                                                                      widgets_dict.get('value'),
                                                                      widgets_dict.get('url'),
                                                                      widgets_dict.get('url_target'),
                                                                 ],),

                                                       BoxConfigContainer(
                                                                 title='Modification Text Data',
                                                            controls=[
                                                                      widgets_dict.get('text_size'),
                                                                      widgets_dict.get('hint_text'),
                                                                      widgets_dict.get('min_lines'),
                                                                      widgets_dict.get('max_lines'),
                                                                      widgets_dict.get('counter_text'),
                                                                      widgets_dict.get('semantics_label'),
                                                                      widgets_dict.get('suffix_text'),
                                                                      widgets_dict.get('text_align'),
                                                                      widgets_dict.get('weight'),
                                                                      widgets_dict.get('multiline'),
                                                                      widgets_dict.get('capitalization'),
                                                                      widgets_dict.get('password'),
                                                                      widgets_dict.get('can_reveal_password'),
                                                                 ],),

                                                       BoxConfigContainer(
                                                                 title='Position Widget in Box',
                                                            controls=[
                                                                      widgets_dict.get('padding'),
                                                                      widgets_dict.get('margin'),
                                                                      widgets_dict.get('border_radius'),
                                                                      widgets_dict.get('spacing'),
                                                                      widgets_dict.get('offset'),
                                                                      widgets_dict.get('rotate'),
                                                                      widgets_dict.get('runs_count'),
                                                                      widgets_dict.get('run_spacing'),
                                                                      widgets_dict.get('elevation'),
                                                                      widgets_dict.get('keyboard_type'),
                                                                      widgets_dict.get('alignment'),
                                                                      widgets_dict.get('vertical_alignment'),
                                                                      widgets_dict.get('horizontal_alignment'),
                                                                      widgets_dict.get('horizontal'),
                                                                      widgets_dict.get('filled'),
                                                                 ],),

                                                       BoxConfigContainer(
                                                                 title='Modification Size Widget',
                                                            controls=[
                                                                      widgets_dict.get('width'),
                                                                      widgets_dict.get('size'),
                                                                      widgets_dict.get('scale'),
                                                                      widgets_dict.get('aspect_ratio'),
                                                                      widgets_dict.get('child_aspect_ratio'),
                                                                      widgets_dict.get('max_extent'),
                                                                      widgets_dict.get('wrap'),
                                                                      widgets_dict.get('adaptive'),
                                                                      widgets_dict.get('expand'),
                                                                      widgets_dict.get('tight'),
                                                                 ],),

                                                       BoxConfigContainer(
                                                                 title='Modification Border Widget Box',
                                                            controls=[
                                                                      widgets_dict.get('border'),
                                                                      widgets_dict.get('spread_radius'),
                                                                      widgets_dict.get('border_width'),
                                                                 ],),

                                                       BoxConfigContainer(
                                                                 title='Colors Widget in Box',
                                                            controls=[
                                                                      widgets_dict.get('color'),
                                                                      widgets_dict.get('bgcolor'),
                                                                      widgets_dict.get('icon_color'),
                                                                      widgets_dict.get('check_color'),
                                                                      widgets_dict.get('fill_color'),
                                                                      # widgets_dict.get('shadow_color'),
                                                                      widgets_dict.get('focused_bgcolor'),
                                                                      widgets_dict.get('border_color'),
                                                                      widgets_dict.get('focused_border_color'),
                                                                 ],),

                                                       BoxConfigContainer(
                                                                 title='Icon or Image in Box',
                                                            controls=[
                                                                      widgets_dict.get('icon'),
                                                                      widgets_dict.get('src'),
                                                                      widgets_dict.get('image_src'),
                                                                      widgets_dict.get('src_base64'),
                                                                      widgets_dict.get('blur'),
                                                                      widgets_dict.get('blur_radius'),
                                                                      widgets_dict.get('image_fit'),
                                                                      widgets_dict.get('opacity'),
                                                                      widgets_dict.get('image_opacity'),
                                                                 ],),
                                                       ],
                                                  ),
                                             )
          Drop_Build_Editor=ft.Container(
                                   padding       = ft.padding.all(0),
                                   margin        = ft.margin.all(0),
                                   border_radius = ft.border_radius.all(28),
                                   width         = 372,
                                   height        = 670,
                              content  = ft.Tabs(
                                             label_color             = 'BLUE',
                                             indicator_border_radius = ft.border_radius.all(20),
                                        tabs = [
                                                       ft.Tab(
                                                                 text    = "Box Phone",

                                                            content = self.main_phone_tab_1
                                                       ),
                                                       ft.Tab(
                                                                 text    = "Box Container",
                                                            content = self.widget_container
                                                       ),
                                                       ft.Tab(
                                                                 text    = "Box Widget",
                                                            content = self.widget_container_content,
                                                         ),
                                             ],
                                            ),
                              )

          GLOBAL_VAR(set_global_var={
                                        'CONFIG_TABS_PHONE':self.main_phone_tab_1,
                                   'CONFIG_TABS_CONTAINERS':self.widget_container,
                           'CONFIG_TABS_CONTAINERS_CONTENT':self.widget_container_content,
                                      'LIST_KEYS_DICT_USED':widgets_dict.keys(),
                                   } )

          return Drop_Build_Editor

if __name__ == '__main__':
    def main(page: ft.Page):

        page.scroll                    = "HIDDEN" #AUTO ADAPTIVE ALWAYS HIDDEN
        page.vertical_alignment        = ft.MainAxisAlignment.CENTER
        page.horizontal_alignment      = ft.CrossAxisAlignment.CENTER
        page.theme_mode                = ft.ThemeMode.DARK         #ft.ThemeMode.LIGHT
        page.window_bgcolor            = ft.colors.RED_100
        page.window_left               = 3
        page.window_top                = 3
        page.window_height             = 680
        page.window_width              = 370
        page.padding                   = 0
        page.spacing                   = 0
        page.add(Build_Editor(widget=ft.Container()))

    ft.app(target=main)
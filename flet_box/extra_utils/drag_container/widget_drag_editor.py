import flet as ft

from .dragg_widget import DraggWidget
# from ..settings_var.settings_widget import GLOBAL_VAR


class Build_Drag_Editor(ft.Stack):
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

                                        runs_count  = 3,
                                        run_spacing = 8,
                                        padding     = 4,
                                        spacing     = 8,
                                        expand      = 1,

                                        controls=[
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
          self.title=data

     def build(self):

          #: CONTROLS

          #: VIEW_COLUMN_ROUNDED
          #: TABLE_ROWS_ROUNDED
          #: WIDGETS_ROUNDED
          #: WEB_STORIES_ROUNDED
          #: icons.FORMAT_SIZE_ROUNDED <=== texto
          #: icons.FORMAT_COLOR_FILL_ROUNDED <== color

          #: CONTAINERS LAYOUTS
          self.RowDragg  = DraggWidget( widget= 'Row'            ,color= 'BLUE'   ,icons= ft.icons.BURST_MODE_ROUNDED)
          self.ColDragg  = DraggWidget( widget= 'Column'         ,color= 'RED'    ,icons= ft.icons.WRAP_TEXT_ROUNDED)
          self.GriDragg  = DraggWidget( widget= 'GridView'       ,color= 'PURPLE' ,icons= ft.icons.WIDGETS_ROUNDED )
          self.StaDragg  = DraggWidget( widget= 'Stack'          ,color= 'YELLOW' ,icons= ft.icons.JOIN_RIGHT_SHARP)

          #: SPACE LAYOUTS
          self.SpaceWid  = DraggWidget( widget= 'Space'          ,color= 'CYAN'   ,icons= ft.icons.FORMAT_LINE_SPACING_ROUNDED)
          self.DivDragg  = DraggWidget( widget= 'Divider'        ,color= 'CYAN'   ,icons= ft.icons.HORIZONTAL_RULE)
          self.VerDragg  = DraggWidget( widget= 'Vertical'       ,color= 'CYAN'   ,icons= ft.icons.SAFETY_DIVIDER_ROUNDED)

          #: IMAGE WIDGET
          self.ImagDragg = DraggWidget( widget= 'Image'          ,color= 'CYAN'   ,icons= ft.icons.IMAGE)
          self.CircDragg = DraggWidget( widget= 'Avatar'         ,color= 'CYAN'   ,icons= ft.icons.ACCOUNT_CIRCLE_ROUNDED)
          self.Ico_Dragg = DraggWidget( widget= 'Icon'           ,color= 'CYAN'   ,icons= ft.icons.ADD_REACTION_OUTLINED)

          #: TEXT  WIDGET
          self.TexsDragg = DraggWidget( widget= 'Text'           ,color= 'CYAN'   ,icons= ft.icons.TEXT_FIELDS)
          self.TexfDragg = DraggWidget( widget= 'Text Field'     ,color= 'CYAN'   ,icons= ft.icons.INPUT)

          #: BUTTONS WIDGET
          self.ElevDragg = DraggWidget( widget= 'Elevated Button',color= 'CYAN'   ,icons= ft.icons.EDIT_ATTRIBUTES_ROUNDED)
          self.TextDragg = DraggWidget( widget= 'Text Button'    ,color= 'CYAN'   ,icons= ft.icons.ABC_ROUNDED)
          self.IconDragg = DraggWidget( widget= 'Icon Button'    ,color= 'CYAN'   ,icons= ft.icons.ADD_LINK_SHARP)
          self.FillDragg = DraggWidget( widget= 'Filled'         ,color= 'CYAN'   ,icons= ft.icons.EDIT_ATTRIBUTES_ROUNDED)
          self.TonaDragg = DraggWidget( widget= 'Tonal'          ,color= 'CYAN'   ,icons= ft.icons.EDIT_ATTRIBUTES_ROUNDED)
          self.OutlDragg = DraggWidget( widget= 'Outline'        ,color= 'CYAN'   ,icons= ft.icons.EDIT_ATTRIBUTES_OUTLINED)
          self.ChipDragg = DraggWidget( widget= 'Chip'           ,color= 'CYAN'   ,icons= ft.icons.LINK)

          #: SELECTIONS WIDGET
          self.ChecDragg = DraggWidget( widget= 'Checkbox'       ,color= 'CYAN'   ,icons= ft.icons.CHECK_ROUNDED)
          self.CupeDragg = DraggWidget( widget= 'Cupertino'      ,color= 'CYAN'   ,icons= ft.icons.CHECK_BOX_ROUNDED)
          self.ChiSDragg = DraggWidget( widget= 'Slider'         ,color= 'CYAN'   ,icons= ft.icons.COMMIT_OUTLINED)
          self.CupSDragg = DraggWidget( widget= 'Switch'         ,color= 'CYAN'   ,icons= ft.icons.SWIPE_RIGHT_ALT_ROUNDED)

          self.RadiDragg = DraggWidget( widget= 'Radio'          ,color= 'CYAN'   ,icons= ft.icons.RADIO_BUTTON_OFF)
          self.CupRDragg = DraggWidget( widget= 'Cup Radio'      ,color= 'CYAN'   ,icons= ft.icons.RADIO_BUTTON_ON)

          #: ALERTS STATUS
          #: WIDGETS STATUS
          #: ESPECIAL WIDGET
          self.DateTable = DraggWidget( widget= 'Table',       color= 'CYAN'   ,icons= ft.icons.TABLE_CHART)
          self.Dismisble = DraggWidget( widget= 'Dismissible' ,color= 'CYAN'   ,icons= ft.icons.CLEAR_ALL_OUTLINED)
          self.ExpaPList = DraggWidget( widget= 'ExpPanelList',color= 'CYAN'   ,icons= ft.icons.BATCH_PREDICTION_OUTLINED)
          self.ExpaPTile = DraggWidget( widget= 'ExpPanelTile',color= 'CYAN'   ,icons= ft.icons.BATCH_PREDICTION_OUTLINED)
          self.ListView  = DraggWidget( widget= 'ListView'    ,color= 'CYAN'   ,icons= ft.icons.FORMAT_LIST_BULLETED_ROUNDED)
          self.PlaceHold = DraggWidget( widget= 'Placeholder' ,color= 'CYAN'   ,icons= ft.icons.BROWSER_NOT_SUPPORTED)
          self.Web_Views = DraggWidget( widget= 'WebView'     ,color= 'CYAN'   ,icons= ft.icons.WEBHOOK)
          self.Progressr = DraggWidget( widget= 'Ring'        ,color= 'CYAN'   ,icons= ft.icons.REPLAY_OUTLINED)
          self.Progressb = DraggWidget( widget= 'ProgressBar' ,color= 'CYAN'   ,icons= ft.icons.LINEAR_SCALE_ROUNDED)
          self.CAIndicat = DraggWidget( widget= 'CupAcIndicator' ,color= 'CYAN'   ,icons= ft.icons.LOOP_SHARP)
          self.Markdown  = DraggWidget( widget= 'Markdown'    ,color= 'CYAN'   ,icons= ft.icons.LINE_STYLE)

          #
          self.BadgeWidg  = DraggWidget( widget= 'Badge'    ,color= 'CYAN'   ,icons= ft.icons.CAR_CRASH_ROUNDED)
          self.PieChart  = DraggWidget( widget= 'PieChart'    ,color= 'CYAN'   ,icons= ft.icons.PIE_CHART)

          #: CHARTS LAYOUTS

          drag_container_to_phone =ft.Container( #: LEFT DROP CONTAINER
                                        ink           = False,
                                        bgcolor       = ft.colors.BLACK38,
                                        padding       = ft.padding.all(8),
                                        margin        = ft.margin.all(0),
                                        alignment     = ft.alignment.center,
                                        border_radius = ft.border_radius.all(30),
                                        width         = 280,

                                        border =ft.border.all(0.6, ft.colors.WHITE12),
                                        shadow = ft.BoxShadow(
                                             spread_radius=1,
                                             blur_radius=16,
                                             color=ft.colors.with_opacity(0.8,ft.colors.BLACK26),
                                             offset=ft.Offset(0, 0),
                                             blur_style=ft.ShadowBlurStyle.OUTER,
                                        ),
                                   content = ft.Column(
                                        scroll                 = 'HIDDEN',
                                        controls = [

                                                  ft.Container( #: CONTAINERS LAYOUTS
                                                            ink             = False,
                                                            bgcolor         = ft.colors.BLACK26,
                                                            margin          = ft.margin.all(0),
                                                            alignment       = ft.alignment.center,
                                                            border_radius   = ft.border_radius.all(30),
                                                            width           = 150,
                                                       content = ft.Text(
                                                               value       = "Containers Layouts",
                                                               text_align  = ft.TextAlign.CENTER,
                                                               weight      = ft.FontWeight.BOLD,
                                                               font_family = "Consolas", #"Consolas ,RobotoSlab
                                                               color       = ft.colors.BLUE,
                                                           ),),
                                                  ft.Container( #: CONTAINERS LAYOUTS
                                                           ink             = False,
                                                           bgcolor         = ft.colors.BLACK26,
                                                           padding         = ft.padding.all(2),
                                                           margin          = ft.margin.all(2),
                                                           alignment       = ft.alignment.center,
                                                           border_radius   = ft.border_radius.all(16),
                                                           content = ft.GridView(
                                                                               runs_count           = 3,
                                                                               run_spacing          = 8,
                                                                               padding              = 4,
                                                                               spacing              = 8,
                                                                               expand               = 1,
                                                                               controls=[
                                                                                           self.RowDragg,
                                                                                           self.ColDragg,
                                                                                           self.GriDragg,
                                                                                           self.StaDragg,
                                                                                        ],
                                                           ),
                                                  ),
                                                  ft.Container( #: SPACE LAYOUTS
                                                           ink             = False,
                                                           bgcolor         = ft.colors.BLACK26,
                                                           margin          = ft.margin.all(0),
                                                           alignment       = ft.alignment.center,
                                                           border_radius   = ft.border_radius.all(30),
                                                           width           = 150,
                                                           content=ft.Text(
                                                                       value       = "Space Layouts",
                                                                       text_align  = ft.TextAlign.CENTER,
                                                                       weight      = ft.FontWeight.BOLD,
                                                                       font_family = "Consolas", #"Consolas ,RobotoSlab
                                                                       color       = ft.colors.BLUE,
                                                           ),),
                                                  ft.Container( #: SPACE LAYOUTS
                                                           ink=False,
                                                           bgcolor         = ft.colors.BLACK26,
                                                           padding         = ft.padding.all(2),
                                                           margin          = ft.margin.all(2),
                                                           alignment       = ft.alignment.center,
                                                           border_radius   = ft.border_radius.all(16),
                                                           content=ft.GridView(
                                                                               runs_count           = 3,
                                                                               run_spacing          = 8,
                                                                               padding              = 4,
                                                                               spacing              = 8,
                                                                               expand               = 1,
                                                                       controls=[
                                                                                   self.SpaceWid,
                                                                                   self.DivDragg,
                                                                                   self.VerDragg,
                                                                                ],
                                                           ),
                                                  ),
                                                  ft.Container( #: IMAGE WIDGET
                                                           ink             = False,
                                                           bgcolor         = ft.colors.BLACK26,
                                                           margin          = ft.margin.all(0),
                                                           alignment       = ft.alignment.center,
                                                           border_radius   = ft.border_radius.all(30),
                                                           width           = 150,
                                                       content=ft.Text(
                                                                   value       = "Images Widgets",
                                                                   text_align  = ft.TextAlign.CENTER,
                                                                   weight      = ft.FontWeight.BOLD,
                                                                   font_family = "Consolas", #"Consolas ,RobotoSlab
                                                                   color=ft.colors.BLUE,
                                                       ),),
                                                  ft.Container( #: IMAGE WIDGET
                                                           ink=False,
                                                           bgcolor         = ft.colors.BLACK26,
                                                           padding         = ft.padding.all(2),
                                                           margin          = ft.margin.all(2),
                                                           alignment       = ft.alignment.center,
                                                           border_radius   = ft.border_radius.all(16),
                                                       content=ft.GridView(
                                                                           runs_count           = 3,
                                                                           run_spacing          = 8,
                                                                           padding              = 4,
                                                                           spacing              = 8,
                                                                           expand               = 1,
                                                                   controls=[
                                                                               self.ImagDragg,
                                                                               self.CircDragg,
                                                                               self.Ico_Dragg,
                                                                            ],
                                                       ),
                                                  ),
                                                  ft.Container( #: TEXT WIDGET
                                                           ink             = False,
                                                           bgcolor         = ft.colors.BLACK26,
                                                           margin          = ft.margin.all(0),
                                                           alignment       = ft.alignment.center,
                                                           border_radius   = ft.border_radius.all(30),
                                                           width           = 150,
                                                           content = ft.Text(
                                                                       value       = "Texts Widgets",
                                                                       text_align  = ft.TextAlign.CENTER,
                                                                       weight      = ft.FontWeight.BOLD,
                                                                       font_family = "Consolas", #"Consolas ,RobotoSlab
                                                                       color       = ft.colors.BLUE,
                                                           ),),
                                                  ft.Container( #: TEXT WIDGET
                                                           ink             = False,
                                                           bgcolor         = ft.colors.BLACK26,
                                                           padding         = ft.padding.all(2),
                                                           margin          = ft.margin.all(2),
                                                           alignment       = ft.alignment.center,
                                                           border_radius   = ft.border_radius.all(16),
                                                       content = ft.GridView(
                                                                       runs_count           = 3,
                                                                       run_spacing          = 8,
                                                                       padding              = 4,
                                                                       spacing              = 8,
                                                                       expand               = 1,
                                                               controls=[
                                                                           self.TexsDragg,
                                                                           self.TexfDragg,
                                                                        ],
                                                           ),
                                                  ),
                                                  ft.Container( #: BUTTONS WIDGETS
                                                           ink             = False,
                                                           bgcolor         = ft.colors.BLACK26,
                                                           margin          = ft.margin.all(0),
                                                           alignment       = ft.alignment.center,
                                                           border_radius   = ft.border_radius.all(30),
                                                           width           = 150,
                                                       content = ft.Text(
                                                                   value       = "Buttons Widgets",
                                                                   text_align  = ft.TextAlign.CENTER,
                                                                   weight      = ft.FontWeight.BOLD,
                                                                   font_family = "Consolas", #"Consolas ,RobotoSlab
                                                                   color       = ft.colors.BLUE,
                                                       ),),
                                                  ft.Container( #: BUTTONS WIDGETS
                                                           ink             = False,
                                                           bgcolor         = ft.colors.BLACK26,
                                                           padding         = ft.padding.all(2),
                                                           margin          = ft.margin.all(2),
                                                           alignment       = ft.alignment.center,
                                                           border_radius   = ft.border_radius.all(16),
                                                       content = ft.GridView(
                                                                       runs_count           = 3,
                                                                       run_spacing          = 8,
                                                                       padding              = 4,
                                                                       spacing              = 8,
                                                                       expand               = 1,
                                                               controls=[
                                                                           self.ElevDragg,
                                                                           self.TextDragg,
                                                                           self.IconDragg,
                                                                           self.FillDragg,
                                                                           self.TonaDragg,
                                                                           self.OutlDragg,
                                                                           self.ChipDragg,
                                                                        ],
                                                   ),
                                                  ),
                                                  ft.Container( #: SELECTION WIDGET
                                                           ink             = False,
                                                           bgcolor         = ft.colors.BLACK26,
                                                           margin          = ft.margin.all(0),
                                                           alignment       = ft.alignment.center,
                                                           border_radius   = ft.border_radius.all(30),
                                                           width           = 150,
                                                       content = ft.Text(
                                                               value       = "Selections Widgets",
                                                               text_align  = ft.TextAlign.CENTER,
                                                               weight      = ft.FontWeight.BOLD,
                                                               font_family = "Consolas", #"Consolas ,RobotoSlab
                                                               color       = ft.colors.BLUE,
                                                   ),),
                                                  ft.Container( #: SELECTION WIDGET
                                                           ink             = False,
                                                           bgcolor         = ft.colors.BLACK26,
                                                           padding         = ft.padding.all(2),
                                                           margin          = ft.margin.all(2),
                                                           alignment       = ft.alignment.center,
                                                           border_radius   = ft.border_radius.all(16),
                                                       content = ft.GridView(
                                                                       runs_count           = 3,
                                                                       run_spacing          = 8,
                                                                       padding              = 4,
                                                                       spacing              = 8,
                                                                       expand               = 1,
                                                               controls=[
                                                                           self.ChecDragg,
                                                                           self.CupeDragg,
                                                                           self.CupRDragg,
                                                                           self.CupSDragg,
                                                                           self.ChiSDragg,
                                                                           # self.RadiDragg, #: <=== NEED WORK ON CONTROLS INSIDE THIS WIDGET
                                                                        ],
                                                           ),
                                                  ),
                                                  ft.Container( #: SELECTION WIDGET
                                                           ink             = False,
                                                           bgcolor         = ft.colors.BLACK26,
                                                           margin          = ft.margin.all(0),
                                                           alignment       = ft.alignment.center,
                                                           border_radius   = ft.border_radius.all(30),
                                                           width           = 150,
                                                       content = ft.Text(
                                                               value       = "No Implementet",
                                                               text_align  = ft.TextAlign.CENTER,
                                                               weight      = ft.FontWeight.BOLD,
                                                               font_family = "Consolas", #"Consolas ,RobotoSlab
                                                               color       = ft.colors.BLUE,
                                                   ),),
                                                  ft.Container( #: SELECTION WIDGET
                                                           ink             = False,
                                                           bgcolor         = ft.colors.BLACK26,
                                                           padding         = ft.padding.all(2),
                                                           margin          = ft.margin.all(2),
                                                           alignment       = ft.alignment.center,
                                                           border_radius   = ft.border_radius.all(16),
                                                       content = ft.GridView(
                                                                       runs_count           = 3,
                                                                       run_spacing          = 8,
                                                                       padding              = 4,
                                                                       spacing              = 8,
                                                                       expand               = 1,
                                                               controls=[
                                                                           self.DateTable,
                                                                           self.Dismisble,
                                                                           self.ExpaPList,
                                                                           self.ExpaPTile,
                                                                           self.ListView,
                                                                           self.PlaceHold,
                                                                           self.Web_Views,
                                                                           self.Progressr,
                                                                           self.Progressb,
                                                                           self.CAIndicat,
                                                                           self.Markdown,
                                                                           self.BadgeWidg,
                                                                           self.PieChart,

                                                                           # self.RadiDragg, #: <=== NEED WORK ON CONTROLS INSIDE THIS WIDGET
                                                                        ],
                                                           ),
                                                  ),
                                                 ],
                                    ),
                        )

          return drag_container_to_phone
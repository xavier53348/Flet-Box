import flet as ft

from .dragg_widget import DraggWidget


class Build_Drag_Editor(ft.Container):
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

       - After we need add manual in [ self.drag_container_to_phone ]

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
    drag_container_color = ft.colors('black12')
    drag_container_border_color = ft.colors('background')
    drag_container_shadow_color = ft.colors('black54')
    drag_text_container_color = ft.colors('black26')
    drag_text_color = ft.colors('cyan')

    def __init__(self, page: object = None,):
        super().__init__()
        self.drag_box = self
        self.page = page
        self.ink = False
        # self.bgcolor       = self.drag_container_color
        self.padding = ft.padding.all(0)
        self.margin = ft.margin.all(6)
        self.alignment = ft.alignment.center
        self.border_radius = ft.border_radius.all(45)
        self.width = 268

        self.gradient = ft.LinearGradient(begin=ft.alignment.top_center, end=ft.alignment.bottom_center, colors=[
                                          ft.colors('black38'), ft.Colors.with_opacity(0.2, 'cyan'), ft.colors('black38')],)
        self.blur = (4, 8)

        self.border = ft.border.all(0.2, self.drag_container_border_color)
        self.shadow = ft.BoxShadow(
            spread_radius=1,
            blur_radius=16,
            color=ft.Colors.with_opacity(0.8, self.drag_container_shadow_color),
            offset=ft.Offset(0, 0),
            blur_style=ft.ShadowBlurStyle.OUTER,
        )

    def build(self):

        #: CONTROLS

        #: VIEW_COLUMN_ROUNDED
        #: TABLE_ROWS_ROUNDED
        #: WIDGETS_ROUNDED
        #: WEB_STORIES_ROUNDED
        #: icons.FORMAT_SIZE_ROUNDED <=== texto
        #: icons.FORMAT_COLOR_FILL_ROUNDED <== color

        #: CONTAINERS LAYOUTS
        self.RespDragg = DraggWidget(page=self.page, drag_box=self.drag_box, widget= 'ResponsiveRow'  ,color= 'PURPLE' ,icons= ft.icons('burst_mode_rounded'))
        self.RowDragg  = DraggWidget(page=self.page, drag_box=self.drag_box, widget= 'Row'            ,color= 'BLUE'   ,icons= ft.icons('burst_mode_rounded'))
        self.ColDragg  = DraggWidget(page=self.page, drag_box=self.drag_box, widget= 'Column'         ,color= 'RED'    ,icons= ft.icons('wrap_text_rounded'))
        self.GriDragg  = DraggWidget(page=self.page, drag_box=self.drag_box, widget= 'GridView'       ,color= 'PURPLE' ,icons= ft.icons('widgets_rounded') )
        self.StaDragg  = DraggWidget(page=self.page, drag_box=self.drag_box, widget= 'Stack'          ,color= 'YELLOW' ,icons= ft.icons('join_right_sharp'))

        #: SPACE LAYOUTS
        self.SpaceWid  = DraggWidget(page=self.page, drag_box=self.drag_box, widget= 'Space'          ,color= 'CYAN'   ,icons= ft.icons('format_line_spacing_rounded'))
        self.DivDragg  = DraggWidget(page=self.page, drag_box=self.drag_box, widget= 'Divider'        ,color= 'CYAN'   ,icons= ft.icons('horizontal_rule'))
        self.VerDragg  = DraggWidget(page=self.page, drag_box=self.drag_box, widget= 'Vertical'       ,color= 'CYAN'   ,icons= ft.icons('safety_divider_rounded'))

        #: IMAGE WIDGET
        self.ImagDragg = DraggWidget(page=self.page, drag_box=self.drag_box, widget= 'Image'          ,color= 'CYAN'   ,icons= ft.icons('image'))
        self.CircDragg = DraggWidget(page=self.page, drag_box=self.drag_box, widget= 'Avatar'         ,color= 'CYAN'   ,icons= ft.icons('account_circle_rounded'))
        self.Ico_Dragg = DraggWidget(page=self.page, drag_box=self.drag_box, widget= 'Icon'           ,color= 'CYAN'   ,icons= ft.icons('add_reaction_outlined'))

        #: TEXT  WIDGET
        self.TexsDragg = DraggWidget(page=self.page, drag_box=self.drag_box, widget= 'Text'           ,color= 'CYAN'   ,icons= ft.icons('text_fields'))
        self.TexfDragg = DraggWidget(page=self.page, drag_box=self.drag_box, widget= 'Text Field'     ,color= 'CYAN'   ,icons= ft.icons('input'))

        #: BUTTONS WIDGET
        self.ElevDragg = DraggWidget(page=self.page, drag_box=self.drag_box, widget= 'Elevated Button',color= 'CYAN'   ,icons= ft.icons('edit_attributes_rounded'))
        self.TextDragg = DraggWidget(page=self.page, drag_box=self.drag_box, widget= 'Text Button'    ,color= 'CYAN'   ,icons= ft.icons('abc_rounded'))
        self.IconDragg = DraggWidget(page=self.page, drag_box=self.drag_box, widget= 'Icon Button'    ,color= 'CYAN'   ,icons= ft.icons('add_link_sharp'))
        self.FillDragg = DraggWidget(page=self.page, drag_box=self.drag_box, widget= 'Filled'         ,color= 'CYAN'   ,icons= ft.icons('edit_attributes_rounded'))
        self.TonaDragg = DraggWidget(page=self.page, drag_box=self.drag_box, widget= 'Tonal'          ,color= 'CYAN'   ,icons= ft.icons('edit_attributes_rounded'))
        self.OutlDragg = DraggWidget(page=self.page, drag_box=self.drag_box, widget= 'Outline'        ,color= 'CYAN'   ,icons= ft.icons('edit_attributes_outlined'))
        self.ChipDragg = DraggWidget(page=self.page, drag_box=self.drag_box, widget= 'Chip'           ,color= 'CYAN'   ,icons= ft.icons('link'))

        #: SELECTIONS WIDGET
        self.ChecDragg = DraggWidget(page=self.page, drag_box=self.drag_box, widget= 'Checkbox'       ,color= 'CYAN'   ,icons= ft.icons('check_rounded'))
        self.CupeDragg = DraggWidget(page=self.page, drag_box=self.drag_box, widget= 'Cupertino'      ,color= 'CYAN'   ,icons= ft.icons('check_box_rounded'))
        self.ChiSDragg = DraggWidget(page=self.page, drag_box=self.drag_box, widget= 'Slider'         ,color= 'CYAN'   ,icons= ft.icons('commit_outlined'))
        self.CupSDragg = DraggWidget(page=self.page, drag_box=self.drag_box, widget= 'Switch'         ,color= 'CYAN'   ,icons= ft.icons('swipe_right_alt_rounded'))

        self.RadiDragg = DraggWidget(page=self.page, drag_box=self.drag_box, widget= 'Radio'          ,color= 'CYAN'   ,icons= ft.icons('radio_button_off'))
        self.CupRDragg = DraggWidget(page=self.page, drag_box=self.drag_box, widget= 'Cup Radio'      ,color= 'CYAN'   ,icons= ft.icons('radio_button_on'))

        #: ALERTS STATUS
        #: WIDGETS STATUS
        #: ESPECIAL WIDGET
        self.DateTable = DraggWidget(page=self.page, drag_box=self.drag_box, widget= 'Table',       color= 'CYAN'   ,icons= ft.icons('table_chart'))
        self.ExpaPList = DraggWidget(page=self.page, drag_box=self.drag_box, widget= 'ExpPanelList',color= 'CYAN'   ,icons= ft.icons('batch_prediction_outlined'))
        self.ExpaPTile = DraggWidget(page=self.page, drag_box=self.drag_box, widget= 'ExpPanelTile',color= 'CYAN'   ,icons= ft.icons('batch_prediction_outlined'))
        self.ListView  = DraggWidget(page=self.page, drag_box=self.drag_box, widget= 'ListView'    ,color= 'CYAN'   ,icons= ft.icons('format_list_bulleted_rounded'))
        self.PlaceHold = DraggWidget(page=self.page, drag_box=self.drag_box, widget= 'Placeholder' ,color= 'CYAN'   ,icons= ft.icons('browser_not_supported'))
        self.Web_Views = DraggWidget(page=self.page, drag_box=self.drag_box, widget= 'WebView'     ,color= 'CYAN'   ,icons= ft.icons('webhook'))
        self.Progressr = DraggWidget(page=self.page, drag_box=self.drag_box, widget= 'Ring'        ,color= 'CYAN'   ,icons= ft.icons('replay_outlined'))
        self.Progressb = DraggWidget(page=self.page, drag_box=self.drag_box, widget= 'ProgressBar' ,color= 'CYAN'   ,icons= ft.icons('linear_scale_outlined'))
        self.CAIndicat = DraggWidget(page=self.page, drag_box=self.drag_box, widget= 'CupAcIndicator' ,color= 'CYAN'   ,icons= ft.icons('loop_sharp'))
        self.Markdown  = DraggWidget(page=self.page, drag_box=self.drag_box, widget= 'Markdown'    ,color= 'CYAN'   ,icons= ft.icons('line_style'))

        #
        # self.BadgeWidg  = DraggWidget(page=self.page, drag_box=self.drag_box, widget= 'Badge'    ,color= 'CYAN'   ,icons= ft.icons('car_crash_rounded'))
        self.PieChart  = DraggWidget(page=self.page, drag_box=self.drag_box, widget= 'PieChart'    ,color= 'CYAN'   ,icons= ft.icons('pie_chart'))

        #: CHARTS LAYOUTS

        self.content = ft.Column(
            scroll='HIDDEN',
            controls=[

                ft.Container(  # : CONTAINERS LAYOUTS
                    ink=False,
                    bgcolor=self.drag_text_container_color,
                    margin=ft.margin.all(0),
                    alignment=ft.alignment.center,
                    border_radius=ft.border_radius.all(45),
                    width=150,
                    content=ft.Text(
                        value="Containers Layouts",
                        text_align=ft.TextAlign.CENTER,
                        weight=ft.FontWeight.BOLD,
                        font_family="Consolas",  # "Consolas ,RobotoSlab
                        color=self.drag_text_color,
                    ),),
                ft.Container(  # : CONTAINERS LAYOUTS
                    ink=False,
                    bgcolor=self.drag_text_container_color,
                    padding=ft.padding.all(2),
                    margin=ft.margin.all(2),
                    alignment=ft.alignment.center,
                    border_radius=ft.border_radius.all(28),
                    border=ft.border.all(
                        0.2, self.drag_container_border_color),
                    content=ft.GridView(
                        runs_count=3,
                        run_spacing=8,
                        padding=4,
                        spacing=8,
                        expand=1,
                        controls=[
                            self.RespDragg,
                            self.RowDragg,
                            self.ColDragg,
                            self.ListView,
                            self.GriDragg,
                            self.StaDragg,
                        ],
                    ),
                ),
                ft.Container(  # : SPACE LAYOUTS
                    ink=False,
                    bgcolor=self.drag_text_container_color,
                    margin=ft.margin.all(0),
                    alignment=ft.alignment.center,
                    border_radius=ft.border_radius.all(45),
                    width=150,
                    content=ft.Text(
                        value="Space Layouts",
                        text_align=ft.TextAlign.CENTER,
                        weight=ft.FontWeight.BOLD,
                        font_family="Consolas",  # "Consolas ,RobotoSlab
                        color=self.drag_text_color,
                    ),),
                ft.Container(  # : SPACE LAYOUTS
                    ink=False,
                    bgcolor=self.drag_text_container_color,
                    padding=ft.padding.all(2),
                    margin=ft.margin.all(2),
                    alignment=ft.alignment.center,
                    border_radius=ft.border_radius.all(28),
                    border=ft.border.all(
                        0.2, self.drag_container_border_color),
                    content=ft.GridView(
                        runs_count=3,
                        run_spacing=8,
                        padding=4,
                        spacing=8,
                        expand=1,
                        controls=[
                            self.SpaceWid,
                            self.DivDragg,
                            self.VerDragg,
                        ],
                    ),
                ),
                ft.Container(  # : IMAGE WIDGET
                    ink=False,
                    bgcolor=self.drag_text_container_color,
                    margin=ft.margin.all(0),
                    alignment=ft.alignment.center,
                    border_radius=ft.border_radius.all(45),
                    width=150,
                    content=ft.Text(
                        value="Images Widgets",
                        text_align=ft.TextAlign.CENTER,
                        weight=ft.FontWeight.BOLD,
                        font_family="Consolas",  # "Consolas ,RobotoSlab
                        color=self.drag_text_color,
                    ),),
                ft.Container(  # : IMAGE WIDGET
                    ink=False,
                    bgcolor=self.drag_text_container_color,
                    padding=ft.padding.all(2),
                    margin=ft.margin.all(2),
                    alignment=ft.alignment.center,
                    border_radius=ft.border_radius.all(28),
                    border=ft.border.all(
                        0.2, self.drag_container_border_color),
                    content=ft.GridView(
                        runs_count=3,
                        run_spacing=8,
                        padding=4,
                        spacing=8,
                        expand=1,
                        controls=[
                            self.ImagDragg,
                            self.CircDragg,
                            self.Ico_Dragg,
                        ],
                    ),
                ),
                ft.Container(  # : TEXT WIDGET
                    ink=False,
                    bgcolor=self.drag_text_container_color,
                    margin=ft.margin.all(0),
                    alignment=ft.alignment.center,
                    border_radius=ft.border_radius.all(45),
                    width=150,
                    content=ft.Text(
                        value="Texts Widgets",
                        text_align=ft.TextAlign.CENTER,
                        weight=ft.FontWeight.BOLD,
                        font_family="Consolas",  # "Consolas ,RobotoSlab
                        color=self.drag_text_color,
                    ),),
                ft.Container(  # : TEXT WIDGET
                    ink=False,
                    bgcolor=self.drag_text_container_color,
                    padding=ft.padding.all(2),
                    margin=ft.margin.all(2),
                    alignment=ft.alignment.center,
                    border_radius=ft.border_radius.all(28),
                    border=ft.border.all(
                        0.2, self.drag_container_border_color),
                    content=ft.GridView(
                        runs_count=3,
                        run_spacing=8,
                        padding=4,
                        spacing=8,
                        expand=1,
                        controls=[
                            self.TexsDragg,
                            self.TexfDragg,
                        ],
                    ),
                ),
                ft.Container(  # : BUTTONS WIDGETS
                    ink=False,
                    bgcolor=self.drag_text_container_color,
                    margin=ft.margin.all(0),
                    alignment=ft.alignment.center,
                    border_radius=ft.border_radius.all(45),
                    width=150,
                    content=ft.Text(
                        value="Buttons Widgets",
                        text_align=ft.TextAlign.CENTER,
                        weight=ft.FontWeight.BOLD,
                        font_family="Consolas",  # "Consolas ,RobotoSlab
                        color=self.drag_text_color,
                    ),),
                ft.Container(  # : BUTTONS WIDGETS
                    ink=False,
                    bgcolor=self.drag_text_container_color,
                    padding=ft.padding.all(2),
                    margin=ft.margin.all(2),
                    alignment=ft.alignment.center,
                    border_radius=ft.border_radius.all(28),
                    border=ft.border.all(
                        0.2, self.drag_container_border_color),
                    content=ft.GridView(
                        runs_count=3,
                        run_spacing=8,
                        padding=4,
                        spacing=8,
                        expand=1,
                        controls=[
                            self.ElevDragg,
                            self.TextDragg,
                            self.IconDragg,
                            self.FillDragg,
                            self.TonaDragg,
                            self.OutlDragg,
                            # self.ChipDragg,
                        ],
                    ),
                ),
                ft.Container(  # : SELECTION WIDGET
                    ink=False,
                    bgcolor=self.drag_text_container_color,
                    margin=ft.margin.all(0),
                    alignment=ft.alignment.center,
                    border_radius=ft.border_radius.all(45),
                    width=150,
                    content=ft.Text(
                        value="Selections Widgets",
                        text_align=ft.TextAlign.CENTER,
                        weight=ft.FontWeight.BOLD,
                        font_family="Consolas",  # "Consolas ,RobotoSlab
                        color=self.drag_text_color,
                    ),),
                ft.Container(  # : SELECTION WIDGET
                    ink=False,
                    bgcolor=self.drag_text_container_color,
                    padding=ft.padding.all(2),
                    margin=ft.margin.all(2),
                    alignment=ft.alignment.center,
                    border_radius=ft.border_radius.all(28),
                    border=ft.border.all(
                        0.2, self.drag_container_border_color),
                    content=ft.GridView(
                        runs_count=3,
                        run_spacing=8,
                        padding=4,
                        spacing=8,
                        expand=1,
                        controls=[
                            self.ChecDragg,
                            self.CupeDragg,
                            # self.CupRDragg,
                            self.CupSDragg,
                            self.ChiSDragg,
                            # self.RadiDragg, #: <=== NEED WORK ON CONTROLS INSIDE THIS WIDGET
                        ],
                    ),
                ),
                ft.Container(  # : SELECTION WIDGET
                    ink=False,
                    bgcolor=self.drag_text_container_color,
                    margin=ft.margin.all(0),
                    alignment=ft.alignment.center,
                    border_radius=ft.border_radius.all(45),
                    width=150,
                    content=ft.Text(
                        value="No Implementet",
                        text_align=ft.TextAlign.CENTER,
                        weight=ft.FontWeight.BOLD,
                        font_family="Consolas",  # "Consolas ,RobotoSlab
                        color=self.drag_text_color,
                    ),),
                ft.Container(  # : SELECTION WIDGET
                    ink=False,
                    bgcolor=self.drag_text_container_color,
                    padding=ft.padding.all(2),
                    margin=ft.margin.all(2),
                    alignment=ft.alignment.center,
                    border_radius=ft.border_radius.all(28),
                    border=ft.border.all(
                        0.2, self.drag_container_border_color),
                    content=ft.GridView(
                        runs_count=3,
                        run_spacing=8,
                        padding=4,
                        spacing=8,
                        expand=1,
                        controls=[
                            # self.DateTable,
                            # self.ExpaPList,
                            # self.ExpaPTile,
                            self.PlaceHold,
                            self.Web_Views,
                            self.Progressr,
                            self.Progressb,
                            self.CAIndicat,
                            self.Markdown,
                            # self.BadgeWidg,
                            # self.PieChart,

                            # self.RadiDragg, #: <=== NEED WORK ON CONTROLS INSIDE THIS WIDGET
                        ],
                    ),
                ),
            ],
        )

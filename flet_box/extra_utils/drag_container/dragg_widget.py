import flet as ft


class DraggWidget(ft.Stack):
    """
    NOTE:

    1. ONLY FUNCTION IS TAKE DRAGGABLE WIDGET AND TRASLATE TO DRAGGABLE_PHONE
    2. SET IN VARIABLE GLOBAL THE SELECTED DRAGGABLE WIDGET
    3. CLEAN THE LIST listWidgetUpdate
    """
    dragg_border_color = ft.Colors.with_opacity(0.4, 'white')
    dragg_shadow_color = ft.Colors.with_opacity(0.3, 'white')
    dragg_text_color = ft.Colors.with_opacity(0.6, 'white')
    dragg_icon_color = ft.Colors.with_opacity(0.6, 'white')

    take_dragg_border_color = ft.Colors.with_opacity(0.04, 'white')
    take_dragg_bground_color = ft.Colors.with_opacity(0.01, 'cyan')
    take_icon_border_color = ft.Colors.with_opacity(0.4, 'white')
    take_text_border_color = ft.Colors.with_opacity(0.4, 'white')

    color_minimum: float = 0.02
    color_medium: float = 0.04
    color_hight: float = 0.06

    def __init__(
        self,
        drag_box: object = None,
        page: object = None,
        widget="type widget selected",
        color="BLACK", icons="/icons/icon-512.png"
    ):
        super().__init__()
        self.page = page
        self.drag_box_container = drag_box
        self.widget = widget
        self.takeClick = False
        self.myColor = color
        self.icons = icons
        self.padding = 0
        self.margin = 0

    def build(self):
        self.DropTakeDragg = ft.Draggable(
            group="GroupDragg",
            on_drag_start=lambda _: self.SelectedWidget(
                selected_widget=self.widget),
            # on_drag_complete = lambda _: self.ShowWidget(), # WILL SHOW VISIBLE AFTER DROP
            content=ft.Container(
                width=90,
                height=90,
                border_radius=23,
                padding=ft.padding.all(4),
                alignment=ft.alignment.center,
                border=ft.border.all(1, self.dragg_border_color),
                # on_click=lambda _: self.SelectedWidget(selected_widget=self.widget),
                # on_long_press = lambda _: self.SelectedWidget(selected_widget=self.widget),
                gradient=ft.LinearGradient(
                    begin=ft.alignment.top_center,
                    end=ft.alignment.bottom_center,
                    colors=[
                        ft.Colors.with_opacity(self.color_minimum, 'white'),
                        ft.Colors.with_opacity(self.color_medium, 'black'),
                        ft.Colors.with_opacity(self.color_minimum, 'black'),
                    ],
                ),
                # blur=(16, 16),
                content=ft.Column(
                    alignment=ft.MainAxisAlignment.SPACE_AROUND,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Icon(
                            name=self.icons,
                            color=self.dragg_icon_color,
                            size=50,
                        ),
                        ft.Text(
                            value=self.widget,
                            text_align=ft.TextAlign.CENTER,
                            weight=ft.FontWeight.BOLD,
                            size=12,
                            color=self.dragg_text_color,
                        ),
                    ],
                ),
            ),
            content_when_dragging=ft.Container(
                padding=2,
                width=80,
                height=80,
                border_radius=13,
            ),
            content_feedback=ft.Container(
                alignment=ft.alignment.bottom_center,
                width=80,
                height=80,
                border=ft.border.all(
                    0.5, self.take_dragg_border_color),
                border_radius=23,
                blur=(8, 8),
                gradient=ft.LinearGradient(
                    begin=ft.alignment.top_center,
                    end=ft.alignment.bottom_center,
                    colors=[
                        self.take_dragg_bground_color,
                        self.dragg_shadow_color
                    ],
                ),
                content=ft.Column(
                    spacing=0,
                    controls=[
                        ft.Container(
                            alignment=ft.alignment.center,
                            padding=ft.padding.only(left=0,
                                                    top=16,
                                                    right=0,
                                                    bottom=0),
                            content=ft.Icon(
                                name=self.icons,
                                color=self.take_icon_border_color,
                                size=50
                            ),
                        ),
                        ft.Container(
                            alignment=ft.alignment.center,
                            padding=ft.padding.all(0),
                            margin=ft.margin.all(0),
                            content=ft.Text(
                                color=self.take_text_border_color,
                                size=16,
                                weight=ft.FontWeight.BOLD,
                                spans=[
                                    ft.TextSpan(
                                        # self.widget,
                                        # ft.TextStyle(size=16, color=ft.colors.TRANSPARENT),
                                    ),
                                ],
                            ),
                        ),
                    ],
                ),
            ),
        )

        return self.DropTakeDragg

    def ShowWidget(self):
        self.drag_box_container.visible = True
        self.drag_box_container.update()
        # print(self.drag_box_container,'<<<<<<<<<<<<<<<,,')
        self.reset_show_text_dragg_selected()

    def check_size_page(self) -> float:
        # set visble off if is phone or movile les than 690 pixel
        page_width = self.page.width
        # page_width = self.page.window.width

        if page_width < 690.0:
            self.drag_box_container.visible = False
            self.drag_box_container.update()

    def reset_border_select_widget(self) -> None:
        self.widget_selected = self.page.session.get("SELECTED_CONTAINER")

        if not self.widget_selected == None:
            self.widget_selected.border = ft.border.all(
                2, ft.colors('transparent'))

        self.page.session.set("SELECTED_CONTAINER", None)

    def reset_show_text_dragg_selected(self):
        self.draggs_selected = self.page.session.get(
            "SHOW_TEXT_SELECTED_DRAGG_WIDGET")
        self.draggs_selected.content.controls[1].content.spans[0].text = "None"
        self.draggs_selected.bgcolor = ft.colors('black12')
        self.draggs_selected.update()

    def show_text_dragg_selected(self) -> None:
        session_id = self.page._session_id
        self.name_selected = self.page.session.get(session_id)

        self.widget_selected = self.page.session.get(
            "SHOW_TEXT_SELECTED_PHONE_WIDGET")
        self.widget_selected.content.controls[1].content.spans[0].text = "None"
        self.widget_selected.bgcolor = ft.colors('black12')
        self.widget_selected.update()

        self.draggs_selected = self.page.session.get(
            "SHOW_TEXT_SELECTED_DRAGG_WIDGET")
        self.draggs_selected.content.controls[1].content.spans[0].text = self.name_selected
        self.draggs_selected.bgcolor = "cyan,0.1"
        self.draggs_selected.update()

    def SelectedWidget(self, selected_widget) -> None:
        """
        NOTE:

        1. SET IN GLOBAL VAR THE SELECTED WIDGET
        2. RESET THE LIST listWidgetUpdate

        """
        session_id = self.page._session_id
        self.page.session.set(session_id, selected_widget)

        # print(selected_widget)
        print(f"{self.page.session.get(session_id)} ID: <<< SELECTED: [drag_widget.py] : selected: >>> {selected_widget}")
        # CHECK SIZE OF PAGE IF LESS VISIBLE OFF
        self.check_size_page()
        self.reset_border_select_widget()
        self.show_text_dragg_selected()

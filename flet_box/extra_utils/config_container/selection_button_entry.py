import flet as ft


class SelectionButtonEntry(ft.Stack):
    """
    box_layout = ft.Container(content = ft.Text())

    Double_Widget = SelectionButtonEntry
    Double_Widget(config_widget='value',widget = box_layout),

    """

    def __init__(
        self,
        id_name_widget_dict=None,
        config_widget: str="exemple [value,bgcolor,width,height] ....",
        page: object = None,
        screen_phone: object = None,
    ):
        super().__init__()
        self.page = page
        self.widget = screen_phone

        self.tooltip="SelectionButtonEntry"
        self.widget_name = config_widget
        self.id_name_widget_dict = id_name_widget_dict

        #: will change name of entry points
        #: ONLY FOR CONTAINER
        if self.widget_name == "image_src" or self.widget_name == "src":
            self.tmp_widget_name = " Open Image "

    def build(self):
        Drop_SelectionButtonEntry = ft.Container(
            ink=False,
            bgcolor="#0c0d0e",
            padding=ft.padding.only(left=4, top=4, right=4, bottom=4),
            margin=ft.margin.all(0),
            alignment=ft.alignment.center,
            border_radius=ft.border_radius.all(16),
            border=ft.border.all(2, ft.colors('black')),
            width=165,
            height=80,
            content=ft.Column(
                wrap=True,
                controls=[
                    ft.Container(
                        ink=False,
                        bgcolor="#0e0f11",
                        padding=ft.padding.only(left=12, top=0, right=12, bottom=0),
                        alignment=ft.alignment.center,
                        border_radius=ft.border_radius.all(30),
                        height=20,
                        content=ft.Text(
                            value=self.widget_name.capitalize().replace("_", " "),
                            font_family="Consolas",  # "Consolas ,RobotoSlab
                        ),
                    ),
                    ft.Container(
                        ink=False,
                        padding=ft.padding.all(2),
                        alignment=ft.alignment.center,
                        border_radius=ft.border_radius.all(30),
                        border=ft.border.all(0.1, "#0e0f11"),
                        width=152,
                        height=36,
                        gradient=ft.LinearGradient(
                            begin=ft.alignment.top_center,
                            end=ft.alignment.bottom_center,
                            colors=[ft.colors('cyan600'), ft.colors('black38')],
                        ),
                        content=ft.Row(
                            controls=[
                                ft.Container(
                                    ink=False,
                                    # bgcolor       =ft.colors.TEAL_900,
                                    padding=ft.padding.all(0),
                                    margin=ft.margin.all(0),
                                    alignment=ft.alignment.center,
                                    border_radius=ft.border_radius.all(30),
                                    width=147,
                                    height=35,
                                    gradient=ft.LinearGradient(
                                        begin=ft.alignment.top_center,
                                        end=ft.alignment.center_right,
                                        colors=[
                                            ft.colors('black12'),
                                            ft.colors('cyan900'),
                                            ft.colors('black38'),
                                        ],
                                    ),
                                    content=ft.ElevatedButton(
                                        text=self.tmp_widget_name,
                                        width=147,
                                        bgcolor=ft.colors('transparent'),
                                        on_click=lambda _: self.modify_widget_attributes(
                                            widget_name=self.widget_name,
                                            attribute_to_change=self.widget,
                                        ),
                                    ),
                                ),
                            ],
                        ),
                    ),
                ],
            ),
        )

        return Drop_SelectionButtonEntry

    def modify_widget_attributes(self, widget_name: str= str(), attribute_to_change: object = None):
        print("[+] change content tab [ selection_button_entry.py ]")
        self.tab_container = self.page.session.get('PHOTO_SELECTION')
        # self.tab_container.update()

        self.tab_container.controls[0].visible=False
        self.tab_container.controls[1].visible=True
        self.tab_container.controls[2].visible=False
        self.tab_container.update()

        self.page.session.set('set_attribute_image',widget_name) # <== SET (BGCOLOR, ...)
        self.page.session.set('set_edit_widget_image',attribute_to_change)  # <== SET (ft.Container, Image)

        # print(widget_name)
        # print(attribute_to_change)

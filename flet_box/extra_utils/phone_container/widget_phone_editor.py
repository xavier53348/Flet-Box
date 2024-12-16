import flet as ft
from ..drag_container.infinity_box_layer_one import InfinityBoxLayerOne
from ..external_library.sqlite_db import sqlite_db

# from .app_manager.app_screen_manager import screens


class Build_Phone_Editor(ft.Stack):
    """
    NOTE:

    ONLY FUNCTION OF THIS MODULE
    - ADD TO PHONE_SCREEN A DRAGABLE WIDGET THAT WILL BE A DRAGABLE_LOOP
    """
    color_minimum: float = 0.04
    color_medium: float = 0.08
    color_hight: float = 0.16

    def __init__(self,
                 color_data=ft.colors("transparent"),
                 screen_name_id: str = "",
                 page: object = None,
                 ):
        super().__init__()
        self.page = page
        self.colored_widget = color_data
        self.screen_name_id = screen_name_id
        self.page.session.set('infinity_box', InfinityBoxLayerOne)

    def build(self):
        # self.user_name = self.page.session.get('user_name').get('user_name')
        # self.password = self.page.session.get('user_name').get('password')

        sqlite_obj = sqlite_db()
        data_returned = sqlite_obj.find_name(
            table_name='user_screen',
            column='user_name',
            name='user_demo'
            # name='kuko53348'
            # name=self.user_name
        )
        self.data_selected = data_returned[0][1]
        # self.data_selected = screens.get('main_screen')(page=self.page)

        self.Build_Phone_Editor = ft.Container(
            border_radius=ft.border_radius.all(42),
            alignment=ft.alignment.center,

            # content=self.data_selected,
            content=self.load_module_from_string(
                page=self.page,
                string_code=self.data_selected
            )
        )

        self.phone = ft.Container(
            alignment=ft.alignment.center,
            bgcolor=ft.Colors.with_opacity(0.60, 'black'),

            # gradient=ft.LinearGradient(
            #     begin=ft.alignment.top_center,
            #     end=ft.alignment.bottom_center,
            #     colors=[
            #         ft.Colors.with_opacity(self.color_minimum, 'cyan'),
            #         ft.Colors.with_opacity(self.color_medium, 'yellow'),
            #         ft.Colors.with_opacity(self.color_hight, 'teal'),
            #         ft.Colors.with_opacity(self.color_minimum, 'black'),
            #     ],
            # ),
            # blur=(16, 16),
            border=ft.border.all(2.5, ft.colors("white")),
            border_radius=ft.border_radius.all(42),
            height=567,
            blur=(24, 24),
            ink=False,
            margin=ft.margin.all(0),
            padding=ft.padding.only(left=0, top=0, right=0, bottom=0),
            width=320,
            content=self.Build_Phone_Editor,
        )

        self.page.session.set('user_name_phone', self.Build_Phone_Editor)

        return self.phone

    def load_module_from_string(self, page, string_code: str = str()) -> object:
        import importlib.util
        # import sys

        spec = importlib.util.spec_from_loader('dynamic_module', loader=None)
        module = importlib.util.module_from_spec(spec)
        exec(string_code, module.__dict__)
        # sys.modules['dynamic_module'] = module
        globals()['dynamic_module'] = module

        return dynamic_module.load_module_str()

    def drag_accept(self, widgetDropBox):
        #: IF SELECT_DRAGG WIDGET IS FAKE SELECTED WILL BE SET IN GLOVAL VAR NONE
        #: RETURNING NONE
        #: WITH THIS CONDITION WE EVOID ADD FAKE WIDGETS EMPY
        #: IS NECESARRY RESET SELECT_DRAGG TO NONE EVERY TIME THAT WE ADD ONE WIDGET NEW
        self.InfinityBox = InfinityBoxLayerOne

        session_id = self.page._session_id
        selectWidgetBox = self.page.session.get(session_id)

        print(f"{selectWidgetBox} ID: <<< drag_accept: [widget_phone_editor.py]")

        if not selectWidgetBox == None:

            ADD_WIDGET_SELECTED = self.InfinityBox(
                dataPassed=selectWidgetBox, page=self.page)

            if not load_file == True:
                # add in normal phone if not loading file
                self.Build_Phone_Editor.content.content.content.controls.append(
                    ADD_WIDGET_SELECTED)
            else:
                self.data_selected.content.content.controls.append(
                    ADD_WIDGET_SELECTED)

            widgetDropBox.control.content.border = True
            widgetDropBox.control.content.border = ft.border.all(
                3, ft.colors("black"))
            widgetDropBox.control.update()

    def drag_will_accept(self, widgetDropBox):
        #: IF IT'S OVER WIDGET DROPED INSIDE PHONE BOX MARK BORDER COLOR RED
        widgetDropBox.control.content.border = None
        widgetDropBox.control.content.border = ft.border.all(
            3, ft.colors("red"))

        widgetDropBox.control.update()

        print(f"===== here ===== {self.page.session.get('cover_widget')}")

        self.page.session.set('dict_widget', widgetDropBox)

    def drag_leave(self, widgetDropBox):
        #: IF LEAVE OF THE WIDGET DROPED INSIDE PHONE BOX BORDER COLOR WILL RESET
        widgetDropBox.control.content.border = True
        widgetDropBox.control.content.border = ft.border.all(
            3, ft.colors('black'))
        widgetDropBox.control.update()

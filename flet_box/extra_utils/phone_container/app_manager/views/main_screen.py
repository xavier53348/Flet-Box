
#: MAIN WIDGET SCREEN CLASS
import flet as ft

# from .main_screen_styles import styles
# from .main_screen_events import *

#: STYLE TO MAIN SCREEN WIDGET
phone_style_widget: dict = {
    "main_container":  {
        "image":  {"src": "designer_5.jpeg", "fit": "cover"},
        "gradient":  {"colors": ["cyan,0.04", "yellow,0.08", "teal,0.16", "black,0.04"], "tile_mode": "clamp", "begin": {"x": 0, "y": -1},
                    "end": {"x": 0, "y": 1},
                    "type": "linear"}
    },
    "second_container":  {
        "padding":  {"l": 8, "t": 8, "r": 8, "b": 8},
        "blur":  {"sigma_x": 8, "sigma_y": 8, "tile_mode": "mirror"},
        "bgcolor":  None
    },
    "column_attributes":  {
        "scroll":  None,
        "spacing":  None,
        "tight":  None,
        "wrap":  None,
        "alignment":  "center",
        "horizontal_alignment":  "center"
    }
}

#: STYLES IN SCREEN_STYLE
styles = {
    "Container_2886":  {
        "alignment":  {"x": 0, "y": 0},
        "bgcolor":  "black54",
        "blur":  [8, 8],
        "border":  {"l": {"w": 0, "c": "transparent", "sa": None},
                    "t": {"w": 0, "c": "transparent", "sa": None},
                    "r": {"w": 0, "c": "transparent", "sa": None},
                    "b": {"w": 0, "c": "transparent", "sa": None}
                    },
        "ink":  True,
        "padding":  {"l": 8, "t": 8, "r": 8, "b": 8},
        "border_radius":  {"bl": 12, "br": 12, "tl": 12, "tr": 12},
        "ink_color":  "yellow"
    },
    "Column_2887":  {
        "scroll":  "ALWAYS",
        "horizontal_alignment":  "center"
    },
    "Container_2892":  {
        "alignment":  {"x": 0, "y": 0},
        "bgcolor":  "transparent",
        "border":  {"l": {"w": 0, "c": "transparent", "sa": None},
                    "t": {"w": 0, "c": "transparent", "sa": None},
                    "r": {"w": 0, "c": "transparent", "sa": None},
                    "b": {"w": 0, "c": "transparent", "sa": None}
                    },
        "ink":  True,
        "margin":  {"l": 0, "t": 0, "r": 0, "b": 0},
        "padding":  {"l": 6, "t": 6, "r": 6, "b": 6},
        "ink_color":  "red"
    },
    "Text_2897":  {
        "size":  10,
        "value":  "Ready to make your first app!!"
    },
    "Container_2895":  {
        "alignment":  {"x": 0, "y": 0},
        "bgcolor":  "transparent",
        "border":  {"l": {"w": 0, "c": "transparent", "sa": None},
                    "t": {"w": 0, "c": "transparent", "sa": None},
                    "r": {"w": 0, "c": "transparent", "sa": None},
                    "b": {"w": 0, "c": "transparent", "sa": None}
                    },
        "ink":  True,
        "margin":  {"l": 0, "t": 0, "r": 0, "b": 0},
        "padding":  {"l": 6, "t": 6, "r": 6, "b": 6},
        "ink_color":  "red"
    },
    "TextField_2898":  {
        "height":  32,
        "label":  "Tell me something ?",
        "width":  240,
        "border_color":  "white",
        "border_radius":  {"bl": 30, "br": 30, "tl": 30, "tr": 30},
        "content_padding":  {"l": 16, "t": 16, "r": 16, "b": 16},
        "cursor_height":  20,
        "text_size":  12,
        "focused_border_color":  "red"
    },
    "Container_2900":  {
        "alignment":  {"x": 0, "y": 0},
        "bgcolor":  "transparent",
        "border":  {"l": {"w": 0, "c": "transparent", "sa": None},
                    "t": {"w": 0, "c": "transparent", "sa": None},
                    "r": {"w": 0, "c": "transparent", "sa": None},
                    "b": {"w": 0, "c": "transparent", "sa": None}
                    },
        "ink":  True,
        "margin":  {"l": 0, "t": 0, "r": 0, "b": 0},
        "padding":  {"l": 6, "t": 6, "r": 6, "b": 6},
        "ink_color":  "red"
    },
    "ElevatedButton_2901":  {
        "text":  "Accept"
    }
}


class main_screen(ft.DragTarget):
    #: NECCESARY HAVE INSTANCE OF ACTUALLY PAGE
    # main_page: dict = dict()
    def __init__(self, page: object = None):
        super().__init__(content=None)
        self.group="GroupDragg"

        # ERASE IN PRODUCTION
        self.drag_width = 320

        #: NECCESARY HAVE INSTANCE OF ACTUALLY PAGE
        self.page = page

        #: ERASE IN PRODUCTION OR COMMENT THIS 2 LINES
        self.expand = True
        self.border_radius=ft.border_radius.all(32)

    def build(self,):
        #: DRAGG_CONTROLS
        list_controls: list = [
            
            #: DRAG-BOX-CONTROLS [ID: 2885]
            self.draggin_framework(
                content=ft.Container(
                    **self.dict_style("Container_2886"),
                    on_click=lambda dragg_item: self.dragg_event(
                                     selected_widget=dragg_item ),

                    content=ft.Column(
                        **self.dict_style("Column_2887"),
                        controls=[
                        #: DRAG-BOX-CONTENT [ID: 2891]
                        self.draggin_framework(
                            content=ft.Container(
                                **self.dict_style("Container_2892"),
                                on_click=lambda dragg_item: self.dragg_event(
                                                 selected_widget=dragg_item,),

                                content=ft.Text(
                                    **self.dict_style("Text_2897"),
                                    # on_click= lambda tmp_widget: event_2897(
                                    #        payload="Text_2897",
                                    #        page= self.page ),
                                ),
                            ),),
                        #: DRAG-BOX-CONTENT [ID: 2894]
                        self.draggin_framework(
                            content=ft.Container(
                                **self.dict_style("Container_2895"),
                                on_click=lambda dragg_item: self.dragg_event(
                                                 selected_widget=dragg_item,),

                                content=ft.TextField(
                                    **self.dict_style("TextField_2898"),
                                    # on_click= lambda tmp_widget: event_2898(
                                    #        payload="TextField_2898",
                                    #        page= self.page ),
                                ),
                            ),),
                        #: DRAG-BOX-CONTENT [ID: 2899]
                        self.draggin_framework(
                            content=ft.Container(
                                **self.dict_style("Container_2900"),
                                on_click=lambda dragg_item: self.dragg_event(
                                                 selected_widget=dragg_item,),

                                content=ft.ElevatedButton(
                                    **self.dict_style("ElevatedButton_2901"),
                                    # on_click= lambda tmp_widget: event_2901(
                                    #        payload="ElevatedButton_2901",
                                    #        page= self.page ),
                                ),
                            ),),]
                    ),
                ),),
        ]

        #: DRAGGIN CONTENT WIDGETS
        self.content = ft.Container(
            width=self.drag_width,
            **self.main_screen_style(code='main_container'),
            content=ft.Container(
                **self.main_screen_style(code='second_container'),
                content=self.draggin_framework(
                    content=ft.Container(
                        content=ft.Column(
                            **self.main_screen_style(code='column_attributes'),
                            controls=list_controls
                        ),
                        on_click=lambda dragg_item: self.dragg_event(
                            selected_widget=dragg_item,),
                    ),
                ),)
        )
        self.on_will_accept    = lambda dragg_item : self.dragg_on_will_accept(DragTargetEvent=dragg_item) # Traslate Drop
        self.on_leave          = lambda dragg_item : self.dragg_on_leave(DragTargetEvent=dragg_item) # Leafing Drop Line Border
        self.on_accept         = lambda dragg_item : self.dragg_on_accept(DragTargetEvent=dragg_item) # Leafing Drop Line Border

    def main_screen_style(self, code: str = ''):
        #: SET MAIN STYLE WIDGET
        return phone_style_widget.get(code)

    def dict_style(self, code: str = ''):
        #: SET CONTENT STYLE WIDGET
        return styles.get(code)

    def show_text_dragg_selected(self, name_selected: str = "") -> None:
        # session_id = self.page._session_id
        # self.name_selected = self.page.session.get(session_id)
        self.name_selected = name_selected
        self.widget_selected = self.page.session.get("SHOW_TEXT_SELECTED_DRAGG_WIDGET")
        self.draggs_selected = self.page.session.get("SHOW_TEXT_SELECTED_PHONE_WIDGET")

        self.widget_selected.content.controls[1].content.spans[0].text = "None"
        self.draggs_selected.content.controls[1].content.spans[0].text = self.name_selected
        self.widget_selected.bgcolor = ft.colors('black12')
        self.draggs_selected.bgcolor = ft.Colors.with_opacity(0.1,ft.colors('cyan'))
        self.widget_selected.update()
        self.draggs_selected.update()

    def dragg_on_will_accept(self, DragTargetEvent: object = None):
        DragTargetEvent.control.content.border = None
        DragTargetEvent.control.content.border = ft.border.all(4, ft.colors('cyan900'))
        DragTargetEvent.control.update()
        self.page.update()

    def dragg_on_accept(self, DragTargetEvent: object = None):
        # print(DragTargetEvent.control.content.content)
        self.widgetFilter = self.page.session.get("ONLY_CONTROLS_ADDING_IN_APP")

        session_id = self.page._session_id
        selectWidgetBox = self.page.session.get(session_id)

        self.InfinityBox = self.page.session.get('infinity_box')
        self.InstanceNewWidget = self.InfinityBox(
                                        dataPassed=selectWidgetBox,
                                        page=self.page
                                    )

        self.right_widget = DragTargetEvent.control.content.content
        self.right_control = self.right_widget._get_control_name()

        if self.right_control in self.widgetFilter:
            DragTargetEvent.control.content.content.controls.append(self.InstanceNewWidget)

        else:
            if self.right_control in self.widgetFilter:
                DragTargetEvent.control.content.content.controls.append(self.InstanceNewWidget)

            else:
                # GET FROM INFINITY DRAGG BOX CONTENT OF MAIN CONTAINER
                DragTargetEvent.control.content.content = self.InstanceNewWidget.widgets.get(selectWidgetBox)[0].content

        #: UPDATE COLOR WIDGET
        DragTargetEvent.control.content.border = True
        DragTargetEvent.control.content.border = ft.border.all(0, ft.colors('transparent'))
        DragTargetEvent.control.update()

        self.page.update()

    def draggin_framework(self, content: object =None) -> object():
        return ft.DragTarget(
            group="GroupDragg",
            on_will_accept    = lambda dragg_item : self.dragg_on_will_accept(DragTargetEvent=dragg_item), # Traslate Drop
            on_leave          = lambda dragg_item : self.dragg_on_leave(DragTargetEvent=dragg_item), # Leafing Drop Line Border
            on_accept         = lambda dragg_item : self.dragg_on_accept(DragTargetEvent=dragg_item), # Leafing Drop Line Border
            content=content
        )

    def dragg_on_leave(self, DragTargetEvent: object = None):
        DragTargetEvent.control.content.border = True
        DragTargetEvent.control.content.border = ft.border.all(0, ft.colors('transparent'))

        DragTargetEvent.control.update()
        self.page.update()

        # return ft.DragTarget(group="GroupDragg",on_will_accept=lambda dragg_item: self.dragg_on_will_accept(DragTargetEvent=dragg_item),  # Traslate Drop
        #     on_leave=lambda dragg_item: self.dragg_on_leave(DragTargetEvent=dragg_item),  # Leafing Drop Line Border
        #     on_accept=lambda dragg_item: self.dragg_on_accept(DragTargetEvent=dragg_item),  # Leafing Drop Line Border
        #     content=content
        # )

    def switch_border_selected(self, selected: object =None):
        selected_widget = self.page.session.get("SELECTED_CONTAINER")

        # print(selected_widget)
        if not selected_widget == None:
            selected_widget.border = ft.border.all(2, ft.colors('transparent'))
            selected_widget.update()

        selected.border = ft.border.all(2, ft.colors('yellow900'))
        selected.update()

        self.show_text_dragg_selected(
            name_selected=selected.content._get_control_name())

    def set_selected_widget(self, selected):
        self.page.session.set("SELECTED_CONTAINER", selected)

    def set_selected_widget_id(self, selected):
        self.page.session.set("SELECTED_CONTAINER_ID", selected.uid)

    def dragg_event(self, selected_widget: object =None):
        # def dragg_event(self,listWidget,e: ft.ContainerTapEvent):
        '''
        NOTE:

        WE CAPTURE THE CLICK SELECTION_WIDGET SHOWING BORDER COLOR YELLOW

        IF PRESS IN OTHER WIDGET WE COMPARE tmp_list listWidgetUpdate
        IF IS DIFERENT SHOW BLACK COLOR THE PREVIEW SELECT_WIDGET

        NOTE:

        WE PASS TO Build_Editor => self.infinityDropWidget[0] THAT IS CLICKED SELECTION
        Build_Editor.update_widget_attributes(widget_cliked=ft.Container(content=ft.Text()))

        '''

        # print(selected_widget.control)
        # SWITCH BORDER COLOR IN SELECTED CONTAINER PHONE
        self.selected = selected_widget.control
        # self.selected = selected_widget[0]
        self.page.session.set("cover_widget", self.selected.parent.parent)

        self.switch_border_selected(selected=selected_widget.control)
        self.set_selected_widget(selected=self.selected)
        self.set_selected_widget_id(selected=self.selected)

        # print(f"[-] {self.selected.tooltip} ID: <<< dragg_event: [infinity_box_layer_one.py]")


# MAKE CLASS A DYNAMIC MODULE
load_module_str = main_screen

import json
import re

from ..external_library.sqlite_db import sqlite_db

FRAME_WIDGET: dict = {

    "dragg_content": """
[+]#: DRAG-BOX-CONTENT [ID: NUMBER_DRAGG]
[+]self.draggin_framework(
[+]    content=ft.Container(
[+]        **self.dict_style("ContainerCONTAINER_ID"),
[+]        on_click=lambda dragg_item: self.dragg_event(
[+]                         selected_widget=dragg_item,),

[+]        content=ft.CHANGE_CONTENT_WIDGET(
[+]            **self.dict_style("CHANGE_CONTENT_WIDGETCONTEN_ID"),
[+]            # on_click= lambda tmp_widget: eventCONTEN_ID(
[+]            #        payload="CHANGE_CONTENT_WIDGETCONTEN_ID",
[+]            #        page= self.page ),
[+]        ),
[+]    ),),""",

    "dragg_controls": """
[+]#: DRAG-BOX-CONTROLS [ID: NUMBER_DRAGG]
[+]self.draggin_framework(
[+]    content=ft.Container(
[+]        **self.dict_style("ContainerCONTAINER_ID"),
[+]        on_click=lambda dragg_item: self.dragg_event(
[+]                         selected_widget=dragg_item ),

[+]        content=ft.CHANGE_CONTENT_WIDGET(
[+]            **self.dict_style("CHANGE_CONTENT_WIDGETCONTEN_ID"),
[+]            controls=CHANGE_CONTROLS,
[+]        ),
[+]    ),),""",

    "event_dragg_target": "on_click= lambda dragg_item: self.dragg_event(selected_widget= dragg_item),",

    "frame_content": """
CHANGE_NAME(
    content= CHANGE_WIDGET
            ),""",

    "frame_controls": """
CHANGE_NAME(
    controls=[
        CHANGE_WIDGET
            ],),""",

    "screen_event": """
'''
EVENT MANAGER WILL CONTENT ALL APP EVENT IN ONE PLACE TO MAKE A EASY USABILITY
'''

# from builder.app_manager import got_to_screen


def CONTEN_ID(payload: str = str(), page: object = None):  # ID: CONTEN_ID
    # EASY WAY GO TROUGHT DIFERENT SCREENS NO LAG BETWEEN THEM
    # got_to_screen(
    #                 to_screen= 'first_screen' ,
    #                 style='burble' ,
    #                 time_style=0.8,
    #                 rotation=True,
    #                 page=page
    #                 )
    print(f"Demo App: {payload} CONTEN_ID")""",

    "widget_reference": """
self.widget_reference: dict() line 248

exemple:

    self.widget_reference: {

        'text':'Text',
        'container':'Container'

}""",

    "screen_class": """
#: MAIN WIDGET SCREEN CLASS
import flet as ft

from .main_screen_styles import styles
from .main_screen_events import *

#: STYLE TO MAIN SCREEN WIDGET
phone_style_widget: dict = CONTAINER_STYLE

#: STYLES IN SCREEN_STYLE
# styles = CHANGE_STYLE


class SCREEN_NAME(ft.DragTarget):
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
            REPLACE_WIDGET
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
load_module_str = SCREEN_NAME
""",
}


class refactory_flet_box:
    """
    code_returned = refactory_flet_box(page=page)
    code_returned.get_widget_attributes(widget= widget_name, screen_name='main_screens')

    # refactory code
    clean_code = code_returned.refactory_code(string_widget=widget)

    # name of class widget
    widget_name = code_returned.get_widget_name(widget_name=widget)

    # get list of controls
    list_controls = code_returned.get_list_controls(widget_name=widget_name, widget=widget)

    # id calss widget
    widget_id = code_returned.get_widget_id(widget_id=widget)

    # get style coded
    widget_style = code_returned.get_style_function(widget_id=widget_id.get('id'))

    # get funtion coded
    widget_function = code_returned.get_function_in_app(widget_id=widget_id.get('id'),string_widget=widget)


    return

    [control_type]   >>> {'parent_controls': 'column'}
    [controls_child] >>> {'child_controls': []}
    [control_style]  >>> {'alignment': 'center', 'horizontal_alignment': 'center', 'scroll': 'auto'}
    [control_id]     >>> {'id': '_2'}
    [control_style]  >>> **self.dict_style('_2'),
    [control_event]  >>> # on_click= lambda tmp_widget: event_2(data='_2'),

    """

    def __init__(self, page: object = None):
        self.page = page
        # STRING THAT CONTENT ALL MAIN SCREEN
        self.refactory_string: str = str()

        # LIST WITH CONTRLS WIDGET
        self.controls_widget: list = []
        self.all_controls_in_widget: list = []

        # SCREEN STYLE AND SCREEN EVENT
        self.all_events_widget: list = []
        self.all_events_id: list = []
        self.screen_styles: dict = dict()
        self.all_widget_in_row: list = []

        self.code_to_refactory: dict = {
            "aspectratio": "aspect_ratio",
            "backgroundimage_src": "background_image_src",
            "blurradius": "blur_radius",
            "bordercolor": "border_color",
            "borderradius": "border_radius",
            "borderwidth": "border_width",
            "childaspect_ratio": "child_aspect_ratio",
            "colspacing": "col_spacing",
            "contentpadding": "content_padding",
            "countertext": "counter_text",
            "cursorheight": "cursor_height",
            "focusedborder_color": "focused_border_color",
            "hinttext": "hint_text",
            "horizontalalignment": "horizontal_alignment",
            "imagefit": "image_fit",
            "imageopacity": "image_opacity",
            "imagesrc": "image_src",
            "inkcolor": "ink_color",
            "maxextent": "max_extent",
            "maxlines": "max_lines",
            "minlines": "min_lines",
            "onclick": "on_click",
            "runscount": "runs_count",
            "runspacing": "run_spacing",
            "semanticslabel": "semantics_label",
            "spaceAround": "space_around",
            "spaceBetween": "space_between",
            "spaceEvenly": "space_evenly",
            "spreadradius": "spread_radius",
            "srcbase64": "src_base64",
            "suffixtext": "suffix_text",
            "textalign": "text_align",
            "textsize": "text_size",
            "urltarget": "url_target",
            "verticalalignment": "vertical_alignment",
            "centerspaceradius": "center_space_radius",
            "sectionsspace": "sections_space",
            "extensionset": "extension_set",
            "autoscroll": "auto_scroll",
            "focusedbordercolor": "focused_border_color",
            "backgroundimagesrc": "background_image_src",
            "dismissdirection": "dismiss_direction",
            "dismissthresholds": "dismiss_thresholds",

            "crossaxisalignment": "cross_axis_alignment",
            "maintainstate": "maintain_state",
            "collapsedtextcolor": "collapsed_text_color",
            "textcolor": "text_color",
        }

        # SEPARATE BY TYPE CONTENT AND CONTROLS
        # WILL DELIMITATE TO ADD NEW WIDGET OR NOT
        self.content_attributes: dict = {
            "container": "content",
            "dragtarget": "content",
            "dismissible": "content",
            "radiogroup": "content",

            "piechart": "sections",

            "row": "controls",
            "column": "controls",
            "stack": "controls",
            "gridview": "controls",
            "responsiverow": "controls",
            "listview": "controls",
        }

        # ONLY THIS TYPE CONTENT WILL HAVE FUNCTION IN APP
        # on_click= lambda tmp_widget: event_3634(data='_3634'),
        self.function_attributes: dict = {
            # "container": True,
            "dragtarget": True,
        }

        self.del_attributes: list = [
            'n',
            'tooltip',
            'onclick',
            'style',
            'round'
        ]

        self.widget_reference: dict = {
            "container": "Container",
            "dragtarget": "DragTarget",
            "row": "Row",
            "column": "Column",
            "stack": "Stack",
            "gridview": "GridView",
            "responsiverow": "ResponsiveRow",
            'listview': 'ListView',

            'space': 'Space',
            'divider': 'Divider',
            'verticaldivider': 'VerticalDivider',
            'image': 'Image',
            'circleavatar': 'CircleAvatar',
            'icon': 'Icon',

            'text': 'Text',
            'textfield': 'TextField',

            'elevatedbutton': 'ElevatedButton',
            'textbutton': 'TextButton',
            'iconbutton': 'IconButton',
            'filledbutton': 'FilledButton',
            'filledtonalbutton': 'FilledTonalButton',
            'outlinedbutton': 'OutlinedButton',
            'chip': 'Chip',

            'checkbox': 'Checkbox',
            'cupertinocheckbox': 'CupertinoCheckbox',
            'cupertinoradio': 'CupertinoRadio',
            'radio': 'Radio',
            'cupertinoslider': 'CupertinoSlider',
            'switch': 'Switch',
            'badge': 'Badge',
            'radiogroup': 'RadioGroup',

            'datatable': 'DataTable',
            'dismissible': 'Dismissible',
            'expansionpanelist': 'ExpansionPanelList',
            'expansiontile': 'ExpansionTile',
            'placeholder': 'Placeholder',
            'webview': 'WebView',
            'progressring': 'ProgressRing',
            'progressbar': 'ProgressBar',
            'cupertinoactivityindicator': 'CupertinoActivityIndicator',
            'markdown': 'Markdown',
            'piechart': 'PieChart',
        }

        self.attributes: dict = dict()

    def refactory_code(self, string_widget: object = object()) -> str:
        """
        :param      string_widget:  flet object example ft.Container()
        :type       string_widget:  object

        TAKE OBJECT EXAMPLE CONTAINER AND TAKE IT ATTRIBUTES AND REFACTORY
        TO CLEAN CODE:

        >>> FROM: 'borderradius':  '{"bl":30,"br":30,"tl":30,"tr":30}'
        >>> TO:   'border_radius': '{"bl":30,"br":30,"tl":30,"tr":30}'

        :rtype:     str

        """
        self.attributes= {}
        string_widget.copy_attrs(dest=self.attributes)

        # print(string_widget,"<<<<")
        # DELETING ATTRIBUTES EXEMPLE 'n','tooltip'
        for _ in self.del_attributes:
            if self.attributes.get(_, False):
                del self.attributes[_]

        for _ in self.code_to_refactory:
            if self.attributes.get(_):
                self.attributes[self.code_to_refactory[_]] = self.attributes.pop(_)

        # WILL RETURNED CLEAN CODE
        return self.attributes

    def get_widget_name(self, widget_name: object = object()) -> dict:
        """
        Gets the widget name.

        :param      widget_name:  The widget name
        :type       widget_name: get name of class widget

        :returns:   {'controls': 'column'}
        :rtype:     str
        """
        value: str = ""
        self.widget_name: str = widget_name._get_control_name()
        self.check_data = self.content_attributes.get(self.widget_name, "No content | No controls")

        if self.check_data == "No content | No controls":
            value = self.widget_name

        elif self.check_data == "controls":
            value = self.widget_name

        elif self.check_data == "content":
            # print(self.check_data,"<<<<<")
            value = self.widget_name

        return value

    def get_list_controls(self, widget_name: dict = dict(), widget: object = object()) -> dict:
        """
        Gets the list controls.

        :param      widget_name:  The widget name
        :type       widget_name:  dict
        :param      widget:       The widget
        :type       widget:       object

        :returns:   The list controls.
        :rtype:     dict
        """
        # self.is_true = widget_name.get('parent_controls',None)

        # if self.is_true:
        #     return {'child_controls': widget.controls}

        # else:
        #     self.is_true = widget_name.get('no_content_controls',False)

        #     if self.is_true:
        #         return {'child_content': None}

        #     else:
        #         return {'child_content': widget.content}
        ##
        is_content = self.content_attributes.get(str(widget_name), None)
        print('[+]',is_content, widget_name)

        if is_content == 'content':
            return {'content': widget.uid}

        elif is_content == 'controls':
            return {'controls': [_.uid for _ in widget.controls]}

        else:
            # if not have content will return other content
            return {'content': widget.uid}

        # print(is_content)

    def get_widget_id(self, widget_id: object = object()) -> str:
        """
        Gets the widget identifier ID

        :param      widget_id:  The widget identifier
        :returns:   The widget identifier {'id': '_2'}
        :rtype:     str
        """

        return widget_id.__dict__['_Control__uid']

    def get_style_function(self, widget_id: str = str()) -> str:
        """
        retunr the style function ID.

        :param      widget_id:  The widget identifier
        :returns:   >>> **self.dict_style('_125'),
        :rtype:     str
        """
        return f"**self.dict_style('{widget_id}'),"

    def get_function_in_app(self, widget_id: str = str(), string_widget: object = object()) -> str:
        """
        Gets the function in application.

        :param      widget_id:  The widget identifier
        :returns:   >>> on_click= lambda tmp_widget: event_3634(data='_3634'),
        :rtype:     str
        """

        # print(string_widget._get_control_name())

        # IF _GET_CONTROL_NAME IN function_attributes DICT WILL HAVE ON_CLICK
        self.check_data = self.function_attributes.get(
            string_widget._get_control_name(), False)

        # if is container will have on_click
        if self.check_data:
            # return f"on_click= lambda dragg_item: self.dragg_event(selected_widget=dragg_item),"

            return FRAME_WIDGET.get('event_dragg_target')

        else:
            return f"# on_click= lambda btn_event: event{widget_id}(data=\'{widget_id}\'),"

    def get_draggable_app(self, widget_name: dict = dict())-> dict:
        """
        Gets the draggable application.

        :param      widget_name:  The widget name
        :returns:   The draggable application.
        :rtype:     dict
        """
        is_container = widget_name.get('parent_content', False)

        if is_container:
            return {"dragg_editor": FRAME_WIDGET.get('frame_content')}

        return {"dragg_editor": None}

    def create_framework(self,
                         tab: str = '\t',
                         widget_id: dict = dict(),
                         clean_code: dict = dict(),
                         widget_name: dict = dict(),
                         dragg_controls: dict = dict(),
                         )-> dict:

        self.tab = tab
        self.dragg_id = widget_id.get('dragg_id')
        self.container_id = widget_id.get('container_id')
        self.content_id = widget_id.get('content_id')

        self.check_controls = self.content_attributes.get(widget_name.get('content_name'))
        self.change_content = self.widget_reference.get(widget_name.get('content_name'))

        if self.change_content == None:
            """
            if widget not in dict return
            """
            self.open_dialog = self.page.session.get('on_dev')
            self.open_dialog(name_seccion='dev most add widget:',body_string=f"Sorry is not aviable yet it's neccesary be added in [ {widget_name.get('content_name')} ]\n{FRAME_WIDGET.get('widget_reference')}")
            return

        if self.check_controls == 'controls':
            # SKELETON WIDGET WILL RETURN
            # EVENT , STYLE AND CLASS

            self.controls_widget = dragg_controls.get('content_controls').get('controls')

            for _ in self.controls_widget:
                if not f"{_}" in self.all_controls_in_widget:
                    self.all_controls_in_widget.append(_)

            self.skeleton = FRAME_WIDGET.get('dragg_controls')
            self.skeleton = self.skeleton.replace('NUMBER_DRAGG', self.dragg_id.strip('_'))
            self.skeleton = self.skeleton.replace('CONTAINER_ID', self.container_id)
            self.skeleton = self.skeleton.replace('CONTEN_ID', self.content_id)
            self.skeleton = self.skeleton.replace('CHANGE_CONTENT_WIDGET', self.change_content)
            self.skeleton = self.skeleton.replace('CHANGE_CONTROLS', str(self.controls_widget))
            self.skeleton = self.skeleton.replace('[+]', self.tab)

            self.refactory_string = self.skeleton

            self.screen_styles[f"Container{self.container_id}"] = clean_code.get('clean_container')
            self.screen_styles[f"{self.change_content}{self.content_id}"] = clean_code.get('clean_content')

            self.event_btn = FRAME_WIDGET.get("screen_event")
            self.event_btn = self.event_btn.replace('CONTEN_ID', f"event{self.content_id}")

            self.all_events_widget.append(self.event_btn)
            self.all_events_id.append(self.content_id)
            # RUN IN PRODUCTION
            # print(self.event_btn)

        else:
            # SKELETON WIDGET WILL RETURN
            # EVENT , STYLE AND CLASS
            #
            self.skeleton = FRAME_WIDGET.get('dragg_content')
            self.skeleton = self.skeleton.replace('NUMBER_DRAGG', self.dragg_id.strip('_'))
            self.skeleton = self.skeleton.replace('CONTAINER_ID', self.container_id)
            self.skeleton = self.skeleton.replace('CONTEN_ID', self.content_id)
            self.skeleton = self.skeleton.replace('CHANGE_CONTENT_WIDGET', self.change_content)
            self.skeleton = self.skeleton.replace('[+]', self.tab)

            self.refactory_string = self.skeleton

            self.screen_styles[f"Container{self.container_id}"] = clean_code.get('clean_container')
            self.screen_styles[f"{self.change_content}{self.content_id}"] = clean_code.get('clean_content')

            self.event_btn = FRAME_WIDGET.get("screen_event")
            self.event_btn = self.event_btn.replace('CONTEN_ID', f"event{self.content_id}")

            self.all_events_widget.append(self.event_btn)
            self.all_events_id.append(self.content_id)

            # RUN IN PRODUCTION
            # print(self.event_btn)

        return self.refactory_string

    def return_code(self, widget: object = None, tab: int = 3) -> dict:

        dragg = widget
        container = dragg.content
        container_content = container.content

        # # WIDGET ID
        dragg_id = self.get_widget_id(widget_id=dragg)
        container_id = self.get_widget_id(widget_id=container)
        content_id = self.get_widget_id(widget_id=container_content)

        # # CLEAN CODE
        clean_dragg = self.refactory_code(string_widget=dragg)
        clean_conta = self.refactory_code(string_widget=container)
        clean_content = self.refactory_code(string_widget=container_content)

        # #  WIDGET NAME
        dragg_name = self.get_widget_name(widget_name=dragg)
        container_name = self.get_widget_name(widget_name=container)
        content_name = self.get_widget_name(widget_name=container_content)

        content_controls = self.get_list_controls(widget_name=content_name, widget=container_content)

        widget_data: dict = {

            dragg_id: {
                "widget_id": {"dragg_id": dragg_id, "container_id": container_id, "content_id": content_id},
                "clean_code": {"clean_dragg": clean_dragg, "clean_container": clean_conta, "clean_content": clean_content},
                "widget_name": {"dragg_name": dragg_name, "container_name": container_name, "content_name": content_name},
                "dragg_controls": {"content_controls": content_controls},
            }}

        self.tab = '    ' * tab

        self.refactorized = self.create_framework(
            tab=self.tab,
            widget_id=widget_data.get(dragg_id).get('widget_id'),
            clean_code=widget_data.get(dragg_id).get('clean_code'),
            widget_name=widget_data.get(dragg_id).get('widget_name'),
            dragg_controls=widget_data.get(dragg_id).get('dragg_controls'),
        )

        # print(clean_conta)
        # print(widget_data.get(dragg_id).get('widget_id'))
        # print(widget_data.get(dragg_id).get('clean_code'))
        # print(widget_data.get(dragg_id).get('widget_name'))
        # print(widget_data.get(dragg_id).get('dragg_controls'))
        # print(self.page._index['_2245'])

        return self.refactorized

    def recursive_nested(self, tab: int = int()):
        """
        recursion neste function
        """
        for _ in self.controls_widget:
            self.tmp = self.return_code(widget=self.page._index[_], tab=tab)
            if _ in self.edit_data:
                # self.edit_data= self.edit_data.replace(_, 'self.tmp')
                self.edit_data = self.edit_data.replace(_, self.tmp)

        # IF SCAPE WIDGETS IN MIDDLE CALL AGAIN IN LIST
        for _ in self.all_controls_in_widget:
            self.tmp = self.return_code(widget=self.page._index[_], tab=tab+2)
            if _ in self.edit_data:
                # print(self.tmp,'==========================')
                self.edit_data = self.edit_data.replace(_, self.tmp)

        # print(self.all_controls_in_widget)

    def get_widget_attributes(self, widget: object = ""):
        """
        Gets the widget attributes.

        code_returned = refactory_flet_box(page=page)
        code_returned.get_widget_attributes(widget=widget1,screen_name='main_screens')

        """
        tab = 3

        # WILLRETURN A LIST WITH ALL WIDGET TO MAKE A NESTED RECURSION
        self.refactorized = self.return_code(widget=widget, tab=tab)
        self.edit_data = self.refactorized

        while "'_" in self.edit_data:
            tab += 3
            self.recursive_nested(tab=tab)

        self.edit_data = self.edit_data.replace("'],", ']').replace("['", "[").replace("', '", '')
        #  REMOVE COMA [ , ]
        # self.edit_data = self.edit_data[:-1]

        self.all_widget_in_row.append(self.edit_data)

    def save_all_data(  self,
                        screen_name: str = str(),
                        one_file: bool = False,

                        container_attributes: dict = dict(),
                      ):
        """
        save data in app
        """
        widgets_events: str = str()
        widgets_class:  str = str()
        widgets_styles: str = str()

        # ALL WIDGETS DRAGGIN CLASS
        for widgets in self.all_widget_in_row:
            widgets_class+=widgets

        # ALL WOIDGETS STYLES
        widgets_styles = self.refactory_wring_attributes(dict_string=self.screen_styles)

        # ONLY GET NUMBERS
        for _ in re.findall('"[0-9(.)]+"', widgets_styles):
            widgets_styles = widgets_styles.replace(_, _.strip('"'))

        # ALL WIDGETS EVENTS
        tmp_list = set(self.all_events_widget)
        # tmp_list_id = set(self.all_eventsid)

        for events in tmp_list:
            widgets_events += events

        self.class_bone = FRAME_WIDGET.get('screen_class')
        self.class_bone = self.class_bone.replace('SCREEN_NAME', screen_name)
        self.class_bone = self.class_bone.replace('REPLACE_WIDGET', widgets_class)

        # ========================================
        # print(self.class_bone)
        # print(widgets_styles)
        # print(widgets_events)
        # ========================================
        # print(">>>>>> END <<<<<<")

        # IF ONE FILE WILL BE SAVED IN DATABASE
        if one_file:
            self.container_attributes = self.refactory_code(string_widget=container_attributes.get('container'))
            self.effect_container_attributes = self.refactory_code(string_widget=container_attributes.get('effect_container'))
            self.column_attributes = self.refactory_code(string_widget=container_attributes.get('column_attributes'))

            self.container_widget = {
                    'main_container': {
                                    'image':self.container_attributes.get('image'),
                                    'gradient':self.container_attributes.get('gradient'),
                        },
                    'second_container': {
                                    'padding':self.effect_container_attributes.get('padding'),
                                    'blur':self.effect_container_attributes.get('blur'),
                                    'bgcolor':self.effect_container_attributes.get('bgcolor'),

                    },
                    'column_attributes': {
                                    'scroll':self.column_attributes.get('scroll'),
                                    'spacing':self.column_attributes.get('spacing'),
                                    'tight':self.column_attributes.get('tight'),
                                    'wrap':self.column_attributes.get('wrap'),
                                    'alignment':self.column_attributes.get('alignment'),
                                    'horizontal_alignment':self.column_attributes.get('horizontal_alignment'),
                    },

            }
            self.clean_code_container = self.refactory_wring_attributes(dict_string=self.container_widget)
            self.class_bone = self.class_bone.replace('CONTAINER_STYLE',self.clean_code_container)

            print('================== onefile ====================')
            self.class_bone = self.class_bone.replace("from .main_screen_styles", "# from .main_screen_styles")
            self.class_bone = self.class_bone.replace("from .main_screen_events", "# from .main_screen_events")

            self.class_bone = self.class_bone.replace('# styles','styles').replace('CHANGE_STYLE',widgets_styles)
            self.class_bone = self.class_bone.replace('CONTAINER_STYLE',self.clean_code_container)

            # print(self.class_bone)
            # print(self.clean_code_container)
            #
            # WRITE IN DATABAS
            self.user_name  = self.page.session.get('user_name').get('user_name') if self.page.session.get('user_name') else 'user_demo'
            print( self.user_name,"<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
            sqlite_obj = sqlite_db()
            data_returned = sqlite_obj.update_data(table_name='user_screen',
                                          change_data=('user_name', self.user_name),
                                          by_data=('main_screen', self.class_bone.replace("'",'"'))
                                         )
            # print(f'>>>> {self.user_name}')

            # SAVE DATA TO CONTROL ERRORS
            self.write_files_in_project(
                                    screen_name=f"{screen_name}",
                                    data_to_write=self.class_bone,
                )
        else:

            self.container_attributes = self.refactory_code(string_widget=container_attributes.get('container'))
            self.effect_container_attributes = self.refactory_code(string_widget=container_attributes.get('effect_container'))
            self.column_attributes = self.refactory_code(string_widget=container_attributes.get('column_attributes'))

            self.container_widget = {
                    'main_container':{
                                    'image':self.container_attributes.get('image'),
                                    'gradient':self.container_attributes.get('gradient'),
                        },
                    'second_container':{
                                    'padding':self.effect_container_attributes.get('padding'),
                                    'blur':self.effect_container_attributes.get('blur'),
                                    'bgcolor':self.effect_container_attributes.get('bgcolor'),

                    },
                    'column_attributes':{
                                    'scroll':self.column_attributes.get('scroll'),
                                    'spacing':self.column_attributes.get('spacing'),
                                    'tight':self.column_attributes.get('tight'),
                                    'wrap':self.column_attributes.get('wrap'),
                                    'alignment':self.column_attributes.get('alignment'),
                                    'horizontal_alignment':self.column_attributes.get('horizontal_alignment'),
                    },

            }
            self.clean_code_container = self.refactory_wring_attributes(dict_string=self.container_widget)
            self.class_bone = self.class_bone.replace('CONTAINER_STYLE',self.clean_code_container)
            # print(self.clean_code_container)

            # print()

            # WRITE CLASS WIDGET
            self.write_files_in_project(
                                    screen_name=f"{screen_name}",
                                    data_to_write=self.class_bone,
                )
            # WRITE STYLE WIDGET
            self.write_files_in_project(
                                    screen_name=f"{screen_name}_styles",
                                    data_to_write=f"styles = {widgets_styles}\n",
                )
            # WRITE EVENT WIDGET
            self.write_files_in_project(
                                    screen_name=f"{screen_name}_events",
                                    data_to_write=f"{widgets_events}\n",
                )
        # OPEN ALL DATATA WAS SAVE
        self.open_dialog = self.page.session.get('on_dev')
        self.open_dialog(
                        name_seccion='your project have been saved',
                        body_string=f"Thank your contribution with Flet-Box\nAnd all dev with Flet thanks make posible this App\n\n"
        )

    def write_files_in_project(self,
                               screen_name: str = str(),
                               data_to_write: str = str(),
                               ):

        with open(f"flet_box/extra_utils/phone_container/app_manager/views/{screen_name}.py", 'w') as f:
            f.write(data_to_write)


    def refactory_wring_attributes(self,
                            dict_string: dict=dict()
                            ) -> str:

        widgets_styles = json.dumps(dict_string, indent=4, skipkeys=True )
        widgets_styles = widgets_styles.replace('"{', '{').replace('}"', '}').replace('\\', '').replace(":", ": ").replace('"["', '["').replace('"]"', '"]')
        widgets_styles = widgets_styles.replace('},"', '},\n\t\t\t\t\t"').replace('}},', '}\n\t\t\t\t\t},').replace(',"', ', "')
        widgets_styles = widgets_styles.replace('"on_click"', '# "on_click"').replace('\t', '    ')
        widgets_styles = widgets_styles.replace('"[', '[').replace(']"', ']')
        widgets_styles = widgets_styles.replace('"true"', 'True').replace('true', 'True').replace('"false"', 'False').replace('false', 'False')
        widgets_styles = widgets_styles.replace('null', 'None')
        #
        return widgets_styles
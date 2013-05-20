from ..settings_var.save_export import MakeJasonFile
from extra_utils.settings_var.settings_widget import GLOBAL_VAR

import flet as ft
visible = False

class TextEditorTextStream(ft.Stack):
    def __init__(self,data_stream='Erase this test',height_stream=720,width_stream=None ,header_code='' ,text_size= 12 ,):
        super().__init__()

        self.data_stream   = data_stream
        self.width_stream  = width_stream
        self.header_code   = header_code
        self.text_size     = text_size
        self.height_stream = height_stream

    def build(self):

        global Drop_TextEditorStream

        Drop_TextEditorStream=ft.Container(
                                    expand        = True,
                                    expand_loose  = True,
                                    ink           = False,
                                    bgcolor       = ft.colors.BACKGROUND,
                                    padding       = ft.padding.all(8),
                                    margin        = ft.margin.all(0),
                                    alignment     = ft.alignment.top_left,
                                    border_radius = ft.border_radius.all(12),
                                    border        = ft.border.all(2, ft.colors.BLACK),
                                    width         = self.width_stream,
                                    height        = self.height_stream,
                                content=ft.Column(
                                            expand               = True,
                                            expand_loose         = True,
                                            scroll               = "HIDDEN",
                                            spacing              = 0,
                                            run_spacing          = 0,
                                            alignment            = ft.MainAxisAlignment.CENTER,
                                            horizontal_alignment = ft.CrossAxisAlignment.CENTER,

                                            controls = [
                                                        ft.TextField(
                                                                    label         = self.header_code,
                                                                    multiline     = True,
                                                                    read_only     = True,
                                                                    border        = ft.InputBorder.NONE,
                                                                    border_radius = 8,
                                                                    text_size     = self.text_size,
                                                                    value         = self.data_stream,
                                                                        )
                                                        ]
                        ),)
        return Drop_TextEditorStream
#######
class TreeViewTextEditor(ft.Stack):

    def __init__(self,data='Erase this test'):

        super().__init__()

        self.title  = data
        self.widget = MakeJasonFile()

    def build(self):
        global Drop_TextEditor
        self.data_stream = ''

        self.text_path = ft.Container(
                    expand    = True,
                    ink       = False,
                    bgcolor   = "#44CCCC00",
                    padding   = ft.padding.all(0),
                    margin    = ft.margin.only (left=8, top=0, right=0, bottom=0),
                    alignment = ft.alignment.center,
                content=ft.Text(
                                value       = "simple text",
                                text_align  = ft.TextAlign.CENTER,
                                font_family = "Consolas",
        ),)

        Drop_TextEditor=ft.Container(
                    expand    = True,
                    bgcolor   = ft.colors.BLACK,
                    padding   = ft.padding.only (left=0, top=24, right=0, bottom=24),
                    margin    = ft.margin.only (left=0, top=0, right=0, bottom=0),    #outside box
                    alignment = ft.alignment.center,

                    content=ft.Row(
                                    expand             = True,
                                    alignment          = ft.MainAxisAlignment.CENTER,
                                    vertical_alignment = ft.CrossAxisAlignment.CENTER,
                                    scroll             = True,
                                    spacing            = 0,
                                    run_spacing        = 0,
                                    controls=[
                                                ft.Container(
                                                    content= (ft.Column(
                                                                    alignment            = ft.MainAxisAlignment.CENTER,
                                                                    horizontal_alignment = ft.CrossAxisAlignment.CENTER,
                                                                controls = [
                                                                            ft.Container(
                                                                                        tooltip       = 'UPDATE',
                                                                                        ink           = False,
                                                                                        bgcolor       = ft.colors.GREEN_700,
                                                                                        padding       = ft.padding.all(0),
                                                                                        margin        = ft.margin.all(0),    #outside box
                                                                                        alignment     = ft.alignment.center,
                                                                                        border_radius = ft.border_radius.only(top_left=8, top_right=8, bottom_left=8, bottom_right=8),
                                                                                        width         = 30,
                                                                                        height        = 30,
                                                                                        content       = ft.Icon(name=ft.icons.UPDATE_OUTLINED),

                                                                                    on_click = lambda _:self.update_text_editor(self.widget),
                                                                            ),
                                                                            ft.Container(
                                                                                        tooltip       = 'EXIT',
                                                                                        ink           = False,
                                                                                        bgcolor       = ft.colors.RED_900,
                                                                                        padding       = ft.padding.all(0),
                                                                                        margin        = ft.margin.all(0),    #outside box
                                                                                        alignment     = ft.alignment.center,
                                                                                        border_radius = ft.border_radius.only(top_left=16, top_right=0, bottom_left=16, bottom_right=0),
                                                                                        width         = 30,
                                                                                        height        = 250,
                                                                                        content       = ft.Icon(name=ft.icons.ARROW_LEFT),

                                                                                    on_click = lambda _:self.show_text_editor(),
                                                                            ),
                                                            ])),),
                                                ft.Container(
                                                        bgcolor = ft.colors.BLACK45,
                                                        content = ft.Column(
                                                                controls = [

                                                                        TextEditorTextStream(data_stream=self.data_stream,width_stream=820 , header_code = "\tCode Box",text_size=11),
                                                                            ],
                                                                    ),
                                                        ),
                                                ft.Column(
                                                        scroll      = True,
                                                        spacing     = 0,
                                                        run_spacing = 0,
                                                        controls = [
                                                            ft.Container(
                                                                bgcolor = ft.colors.BLACK45,
                                                                content = ft.Column(
                                                                            controls=[
                                                                                    TextEditorTextStream(
                                                                                                            data_stream   = self.data_stream,
                                                                                                            width_stream  = 500 ,
                                                                                                            height_stream = 360,
                                                                                                            header_code   = "\tStyle Box" ,
                                                                                                            text_size     = 12),
                                                                                    ],
                                                                            ),
                                                                    ),
                                                            ft.Container(
                                                                bgcolor = ft.colors.BLACK45,
                                                                content = ft.Column(
                                                                            controls=[
                                                                                    TextEditorTextStream(
                                                                                                            data_stream   = self.data_stream,
                                                                                                            width_stream  = 500,
                                                                                                            height_stream = 360,
                                                                                                            header_code   = "\tEvents Box",
                                                                                                            text_size     = 11),
                                                                                    ],
                                                                            ),
                                                                    ),],)
                                             ],),
        )

        return Drop_TextEditor

    def show_text_editor(self):
        self.widget_off         = GLOBAL_VAR(get_global_var='TEXT_EDITOR_CONTAINER')
        self.widget_off.visible = False
        self.widget_off.update()

    def update_text_editor(self,widget):

        #: build_json_file
        #: INPUT DATA IN TEXT EDITOR
        build_json_file = widget.build_json_file(widget_show=GLOBAL_VAR(get_global_var='EXPORT_DATA_PHONE'))
        #: print(Drop_TextEditor.content.controls[1].content.controls[0].data_stream)

        #: FIRST
        Drop_TextEditor.content.controls[1].content.controls[0].controls[0].content.controls[0].value=build_json_file.get('main_code')
        Drop_TextEditor.content.controls[1].content.controls[0].controls[0].content.controls[0].update()

        # #: SECOND
        # Drop_TextEditor.content.controls[2].controls[0].content.controls[0].controls[0].content.controls[0].value=build_json_file.get('index_code')
        Drop_TextEditor.content.controls[2].controls[0].content.controls[0].controls[0].content.controls[0].value=build_json_file.get('style_code').replace('styles=', '')
        Drop_TextEditor.content.controls[2].controls[0].content.controls[0].controls[0].content.controls[0].update()

        # #: SECOND
        Drop_TextEditor.content.controls[2].controls[1].content.controls[0].controls[0].content.controls[0].value=build_json_file.get('event_code')
        Drop_TextEditor.content.controls[2].controls[1].content.controls[0].controls[0].content.controls[0].update()


if __name__ == '__main__':

    def main(page: ft.Page):

        page.scroll               = "AUTO"                         # AUTO ADAPTIVE ALWAYS HIDDEN
        page.vertical_alignment   = ft.MainAxisAlignment.CENTER
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        page.theme_mode           = ft.ThemeMode.DARK              # ft.ThemeMode.LIGHT
        page.window_bgcolor       = ft.colors.RED_100
        page.window_left          = 3
        page.window_top           = 3
        page.window_height        = 650
        page.window_width         = 1200
        page.padding              = 0
        page.spacing              = 0
        page.add(TreeViewTextEditor())

    ft.app(target=main)
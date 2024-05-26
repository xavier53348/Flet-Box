
import flet as ft
import os
import pyperclip
import time

from .library_chatgpt import ChatGpt

os.environ["FLET_WS_MAX_MESSAGE_SIZE"] = "8000000"

class Gpt_text(ft.Stack):
    def __init__(self,input_text='Erase this test',color_chat="#0a1618",ask=False):
        super().__init__()

        self.input_text              = input_text
        self.color_chat              = color_chat if ask else ft.colors.BLACK26
        self.position_right_chat_gpt = True if ask else False
        self.position_left_chat_gpt  = True if not ask else False

        self.icon_container =ft.Container(
                                ink           = True,
                                ink_color     = ft.colors.RED_900,
                                bgcolor       = ft.colors.BLUE_900,
                                padding       = ft.padding.only(left=0, top=0, right=0, bottom=0),
                                margin        = ft.margin.all(0),    #outside box
                                alignment     = ft.alignment.center,
                                border_radius = ft.border_radius.all(30),
                                border        = ft.border.all(2, ft.colors.BLUE),
                                width         = 30,
                                height        = 30,
                                offset        = (0.3,0),
                                content= ft.Icon(
                                                    color=ft.colors.WHITE,
                                                    size=18,
                                                    name=ft.icons.COPY
                                                    ),
                            on_click=lambda _:print(_),
                    )#<=== NOTE COMA
        self.widget_to_select = {'gpt':ft.TextField(
                                                value           = self.input_text,
                                                multiline     = True,
                                                read_only     = True,
                                                border        = ft.InputBorder.NONE,
                                                text_size     = 12,
                                                width         = 700,
                                        ),
                                'ask':
                                        ft.Text(
                                                value           = self.input_text,
                                                font_family     = "RobotoSlab", #"Consolas ,RobotoSlab
                                                size=12,
                                                )
                                    }

        self.ask_response =self.widget_to_select.get('gpt')  if not ask else self.widget_to_select.get('ask')
        self.icon_container.visible=True if not ask else False

    def build(self):
        Drop_Gpt_text=ft.Container(
                    ink             = False,
                    bgcolor         = self.color_chat,
                    padding         = ft.padding.only(left=32, top=8, right=32, bottom=8),
                    margin          = ft.margin.all(0),
                    alignment       = ft.alignment.center_left,
                    border_radius   = ft.border_radius.all(32),
                    border        = ft.border.all(2, ft.colors.BLACK12),
                    content = ft.Column(
                                        spacing              = 0,
                                        alignment            = ft.MainAxisAlignment.SPACE_AROUND,
                                        horizontal_alignment = ft.CrossAxisAlignment.END,
                                    controls = [
                                                self.icon_container,
                                                self.ask_response,

                                                ],))#<=== NOTE COMA <==> ERASE COMA IF MAKE 1 ERROR
        self.data = ft.Row(
                        alignment=ft.alignment.center,

                        controls = [
                                    ft.Container(expand=self.position_right_chat_gpt),
                                    Drop_Gpt_text,
                                    ft.Container(expand=self.position_left_chat_gpt),
                                    ]
                                )
        return self.data

class GptBrowser(ft.Stack):
    """
    lite module to find colors by name
    """

    def __init__(self,blur_effect = False, numb_widget_to_show=50):
        super().__init__()
        global alert_dialog
        self.numb_widget_to_show = numb_widget_to_show

        if blur_effect:
            self.blur = 20
        else:
            self.blur = None
        self.Gpt_Text = Gpt_text
        alert_dialog  = ft.Container(
                                        visible       = False,
                                        height        = 40,
                                        width         = 240,
                                        bgcolor       = 'red',
                                        offset        = (0,-1.5),
                                        alignment     = ft.alignment.center,
                                        border_radius = ft.border_radius.all(16),
                                    content = ft.Text(
                                                        value = 'None',
                                                        )
                                        )
        text_test = """
Hello there!

Come and experience the world of knowledge and conversation with ChatGPT.
Let's explore and exchange thoughts on any topic you desire.
Join me and let's embark on a journey of discovery together!...
"""
        self.Search_Gridwiew = ft.Column(
                        scroll               = 'HIDDEN',
                    controls=[
                            self.Gpt_Text(text_test),
                            ],
                        )

        self.text_field_chat_gpt = ft.TextField(
                                label                = "    Hello DEV !!. What do you like talk about ?...",
                                border               = ft.InputBorder.OUTLINE,
                                bgcolor              = ft.colors.BLACK12,
                                focused_bgcolor      = ft.colors.BLACK12,
                                border_color         = ft.colors.TEAL,
                                focused_border_color = ft.colors.TRANSPARENT,
                                border_radius        = 30,
                                text_size            = 15,
                                content_padding      = ft.padding.only(left=16, top=2, right=16, bottom=2),
                                prefix_icon          = ft.icons.LANGUAGE,
                                multiline=True,
                                )

        self.Drop_GptBrowser=ft.Container(
                    ink       = False,
                    padding   = ft.padding.all(8),
                    margin    = ft.margin.all(8),
                    alignment = ft.alignment.center,

                    content   = ft.Column(
                        spacing              = 8,
                        alignment            = ft.MainAxisAlignment.SPACE_AROUND,
                        horizontal_alignment = ft.CrossAxisAlignment.CENTER,
                        scroll=False,
                        controls=[
                                    ft.Container(
                                                ink           = False,
                                                bgcolor       = ft.colors.BLACK38,
                                                padding       = ft.padding.all(8),
                                                margin        = ft.margin.all(0),    #outside box
                                                alignment     = ft.alignment.center,
                                                border_radius = ft.border_radius.all(30),
                                                border        = ft.border.all(0.8, ft.colors.TEAL),
                                                blur          = self.blur,
                                                height        = 500,
                                            content       = self.Search_Gridwiew,
                                    ),#<=== NOTE COMA
                                    ft.Container(
                                                ink=False,
                                                padding= ft.padding.all(0),
                                                margin = ft.margin.all(0),    #outside box
                                                alignment=ft.alignment.center,
                                                content=ft.Row(
                                                    run_spacing=0,
                                                    controls=[
                                                            ft.Container(
                                                                        ink           = False,
                                                                        expand        = True,
                                                                        padding       = ft.padding.only(left=0, top=4, right=0, bottom=4),
                                                                        margin        = ft.margin.all(0),
                                                                        alignment     = ft.alignment.center,
                                                                        border_radius = ft.border_radius.all(30),
                                                                        blur          = self.blur,
                                                                        height        = 50,
                                                                    content=self.text_field_chat_gpt,
                                                            ),#<=== NOTE COMA <==> ERASE COMA IF MAKE 1 ERROR

                                                            ft.Container(
                                                                    bgcolor       = ft.colors.BLUE_900,
                                                                    padding       = ft.padding.all(0),
                                                                    margin        = ft.margin.all(0),
                                                                    alignment     = ft.alignment.center,
                                                                    border_radius = ft.border_radius.all(30),
                                                                    border        = ft.border.all(2, ft.colors.BLUE),
                                                                    ink           = True,
                                                                    ink_color     = 'red',
                                                                    height        = 42,
                                                                    width         = 42,
                                                                on_click      = lambda _: self.search_gpt_question(self.text_field_chat_gpt),     #FloatingActionButton
                                                                    content=ft.Icon(
                                                                                    color =ft.colors.WHITE,
                                                                                    name  = ft.icons.SEND_AND_ARCHIVE,
                                                        ),),#<=== NOTE COMA <==> ERASE COMA IF MAKE 1 ERROR                                                                                ,
                                                             ],
                                                            ),
                                    ),#<=== NOTE COMA
                               alert_dialog,
                                 ],
                    ),#<=== NOTE COMA [NOTE]                     for x in range(1,50): widget.content.controls.append(ft.ElevatedButton("press buttom",tooltip='buttom'))
        )#<=== NOTE COMA

    def build(self):
        return self.Drop_GptBrowser

    def search_gpt_question(self,e):

        search_term = e.value.lower()
        self.user_question_container = Gpt_text(input_text=search_term,ask=True)
        self.Search_Gridwiew.controls.append(self.user_question_container)
        self.Search_Gridwiew.update()
        e.value =''
        e.update()
        message_returned = ChatGpt(question=f"""{search_term}""".rstrip(' '))

        # only run in production
        # print(message_returned)

        if message_returned:
            self.response_question_container = Gpt_text(input_text=message_returned,color_chat=ft.colors.BLACK12,ask=False)
            self.Search_Gridwiew.controls.append(self.response_question_container)
            self.Search_Gridwiew.scroll_to(key=f"{len(self.Search_Gridwiew.controls)}", duration=1000)
            self.Search_Gridwiew.update()

        else:
            self.response_question_container = Gpt_text(input_text=message_returned,color_chat=ft.colors.BLACK12,ask=False)
            self.Search_Gridwiew.controls.append(self.response_question_container)
            self.Search_Gridwiew.scroll_to(key=f"{len(self.Search_Gridwiew.controls)}", duration=1000)
            self.Search_Gridwiew.update()


if __name__ == '__main__':
    def main(page: ft.Page):
        page.scroll                    = "HIDDEN" #AUTO ADAPTIVE ALWAYS HIDDEN
        page.vertical_alignment        = ft.MainAxisAlignment.CENTER
        page.horizontal_alignment      = ft.CrossAxisAlignment.CENTER
        page.theme_mode                = ft.ThemeMode.DARK         #ft.ThemeMode.LIGHT
        page.window_bgcolor            = ft.colors.RED_100
        page.window_left               = 3
        page.window_top                = 3
        page.window_height             = 600
        page.window_width              = 650
        page.padding                   = 0
        page.spacing                   = 0
        page.add(GptBrowser())

    ft.app(target=main)
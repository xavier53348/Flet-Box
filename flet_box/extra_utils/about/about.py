import os
import pyperclip
import flet as ft
import time

os.environ["FLET_WS_MAX_MESSAGE_SIZE"] = "8000000"

from ..settings_var.settings_widget import GLOBAL_VAR


class FlowlowMe(ft.Stack):

    def __init__(self,data='Erase this test'):
        super().__init__()

        self.title=data

    def build(self):
        Drop_FlowlowMe=ft.Container(
                    ink       = False,
                    padding   = ft.padding.all(0),
                    margin    = ft.margin.all(0),
                    alignment = ft.alignment.center,

                content   = ft.Column(
                        controls=[
                                    ft.Container(
                                        ink       = False,
                                        padding   = ft.padding.all(0),
                                        margin    = ft.margin.all(0),
                                        alignment = ft.alignment.center,
                                        content=ft.Text(
                                                    value       = "FOLLOW ME",
                                                    text_align  = ft.TextAlign.CENTER,
                                                    weight      = ft.FontWeight.BOLD,
                                                    font_family = "Consolas",
                                                    size        = 16,
                                    ),),#<=== NOTE COMA <==> ERASE COMA IF MAKE 1 ERROR
                                    ft.Container(
                                        ink       = False,
                                        padding   = ft.padding.all(0),
                                        margin    = ft.margin.all(0),
                                        alignment = ft.alignment.center,
                                        content=ft.Row(
                                                    controls=[
                                                                ft.IconButton(icon=ft.icons.FACEBOOK        ,tooltip='FACEBOOK',                url='https://facebook.com/groups/315046001621078/?mibextid=rS40aB7S9Ucbxw6v',),
                                                                ft.IconButton(icon=ft.icons.DISCORD         ,tooltip='@legend_53348#0000',      ),
                                                                ft.IconButton(icon=ft.icons.CHAT            ,tooltip='WHATSAPP GROUP',          url='https://chat.whatsapp.com/ELFB8fSbdMS2chOjXiYAMo'),
                                                                ft.IconButton(icon=ft.icons.EMAIL_ROUNDED   ,tooltip='xavier53348@gmail.com',   url='mailto:xavier53348@gmail.com'),
                                                                ft.IconButton(icon=ft.icons.PHONE           ,tooltip='(+53) 54448442',          ),
                                                                ft.IconButton(icon=ft.icons.VIDEO_COLLECTION,tooltip='YOUTUBE',                 url='https://www.youtube.com/@flet-box'),
                                                             ],),
                                    ),#<=== NOTE COMA
                                 ],
                    ),#<=== NOTE COMA [NOTE]
        )#<=== NOTE COMA

        return Drop_FlowlowMe

class ABOUT_BOX(ft.Stack):

    INFO_ABOUT = {

                'about_me': """With Flet-Box GUI, you can seamlessly build apps that run smoothly on various platforms, from desktop to mobile. Say goodbye to platform-specific limitations and hello to a unified development experience. Plus, with Python3 as the language of choice, you'll enjoy the simplicity and versatility that comes with one of the most popular programming languages in the world.""",
              'invitation': """So, are you ready to join us on this exciting adventure? Whether you're a developer looking to build your next big project or simply curious about the world of cross-platform app development, Flet-Box GUI welcomes you with open arms. Let's embark on this journey together and unlock the full potential of Flet framework.\nFeel free to reach out for inquiries or collaboration opportunities.""",

    }
    def __init__(self,header='header',body='body',footer='footer',ref_url='reference'):
        super().__init__()

        self.header = header
        self.body   = body
        self.footer = footer
        self.reference = ref_url

    def build(self):
        Drop_ABOUT_BOX = ft.Container(
                    padding   = ft.padding.all(0),
                    margin    = ft.margin.all(0),
                    alignment = ft.alignment.center,
                    content   = ft.Column(
                                    spacing=18,

                                    controls=[
                                            ft.Container(
                                                        padding   = ft.padding.all(0),
                                                        margin    = ft.margin.all(0),
                                                        alignment = ft.alignment.center_left,
                                                    content = ft.Text(

                                                                    value       = self.header,
                                                                    text_align  = ft.TextAlign.LEFT,
                                                                    weight      = ft.FontWeight.BOLD,
                                                                    font_family = "Consolas",           #"Consolas ,RobotoSlab
                                                                    size=18,
                                            ),),#<=== NOTE COMA <==> ERASE COMA IF MAKE 1 ERROR
                                            ft.Container(
                                                        padding   = ft.padding.all(0),
                                                        margin    = ft.margin.all(0),
                                                        alignment = ft.alignment.center_left,
                                                        width     = 400,
                                                    content = ft.Text(

                                                                    value       = self.INFO_ABOUT.get(self.body),
                                                                    text_align  = ft.TextAlign.LEFT,

                                                                    font_family = "Consolas",
                                                                    color       =ft.colors.WHITE38,
                                                                    size        =12,
                                            ),),#<=== NOTE COMA <==> ERASE COMA IF MAKE 1 ERROR
                                            ft.Container(
                                                        padding   = ft.padding.all(0),
                                                        margin    = ft.margin.all(0),
                                                        alignment = ft.alignment.center_left,
                                                    content = ft.Column(
                                                                    spacing=0,
                                                            controls = [
                                                                ft.TextButton(
                                                                    text       = self.footer,
                                                                    url         = self.reference,
                                                                ),
                                                                ft.Container(height=4,width=124,bgcolor=ft.colors.TEAL_800 ),
                                                                ]),
                                            ),#<=== NOTE COMA <==> ERASE COMA IF MAKE 1 ERROR
                                             ],),
        )#<=== NOTE COMA

        return Drop_ABOUT_BOX

class AboutPage(ft.Stack):
    data_dev = {
        'profile':"""Experienced software developer with a passion for creating intuitive graphical user interfaces (GUIs) across multiple platforms. Dedicated to delivering high-quality, user-centric applications tailored to meet specific client needs.
        """
    }
    def __init__(self,data='Erase this test'):
        super().__init__()
        self.title=data

    def build(self):
        self.left_column = ft.Container(
                    ink       = False,
                    padding   = ft.padding.all(4),
                    margin    = ft.margin.all(4),
                    alignment = ft.alignment.center,
                    content=ft.Column(
                        alignment            =ft.MainAxisAlignment.SPACE_AROUND,
                        horizontal_alignment =ft.CrossAxisAlignment.START,

                        controls=[
                                    ft.Container(height=7,width=123,bgcolor=ft.colors.TEAL_800 ),
                                    ft.Container(
                                                ink           = False,
                                                padding       = ft.padding.all(0),
                                                margin        = ft.margin.all(0),
                                                alignment     = ft.alignment.center,
                                                border_radius = ft.border_radius.all(80),
                                                border        = ft.border.all(2, ft.colors.BLACK45),
                                                width         = 150,
                                                height        = 150,
                                                bgcolor       = ft.colors.BLACK45,
                                                content=ft.Image(
                                                            src                = os.path.join('flet_box/assets','my_avatar.png'),
                                                            fit                = ft.ImageFit.COVER,
                                                            repeat             = ft.ImageRepeat.NO_REPEAT,
                                                            border_radius      = ft.border_radius.all(80),
                                                            opacity            = 0.6,
                                                            expand             = True,
                                    ),),#<=== NOTE COMA <==> ERASE COMA IF MAKE 1 ERROR
                                    ft.Container(
                                                ink       = False,
                                                padding   = ft.padding.all(0),
                                                margin    = ft.margin.all(0),
                                                alignment = ft.alignment.center_left,
                                                width     = 350,
                                                content=ft.Text(
                                                            value       = "Hi There!!",
                                                            text_align  = ft.TextAlign.LEFT,
                                                            weight      = ft.FontWeight.BOLD,
                                                            font_family = "Consolas", #"Consolas ,RobotoSlab
                                                            size        = 24,
                                    ),),#<=== NOTE COMA <==> ERASE COMA IF MAKE 1 ERROR
                                    ft.Container(
                                                ink       = False,
                                                padding   = ft.padding.all(0),
                                                margin    = ft.margin.all(0),
                                                alignment = ft.alignment.center_left,
                                                width     = 350,
                                                content=ft.Text(
                                                            value       = "DEV:      Maenys Javier Quesada Reyes\nFrom:    CUBA",
                                                            text_align  = ft.TextAlign.LEFT,
                                                            weight      = ft.FontWeight.BOLD,
                                                            font_family = "Consolas", #"Consolas ,RobotoSlab
                                                            size        = 18,
                                    ),),#<=== NOTE COMA <==> ERASE COMA IF MAKE 1 ERROR
                                    ft.Container(
                                                ink       = False,
                                                padding   = ft.padding.all(0),
                                                margin    = ft.margin.all(0),
                                                alignment = ft.alignment.center_left,
                                                width     = 350,
                                                content=ft.Text(
                                                            value       = self.data_dev.get('profile'),
                                                            text_align  = ft.TextAlign.LEFT,
                                                            font_family = "RobotoSlab", #"Consolas ,RobotoSlab
                                                            color       = ft.colors.WHITE38,
                                                            size        = 12,
                                    ),),#<=== NOTE COMA <==> ERASE COMA IF MAKE 1 ERROR
                                    ft.Container(
                                                ink       = False,
                                                padding   = ft.padding.all(8),
                                                margin    = ft.margin.all(8),
                                                alignment = ft.alignment.center,
                                                content   = ft.ElevatedButton(
                                                                            text      = 'GIT-HUB',
                                                                            bgcolor   = ft.colors.TEAL_800 ,
                                                                            url       = 'https://github.com/xavier53348/Flet-Box',
                                                                            elevation = 16,
                                    ),),#<=== NOTE COMA <==> ERASE COMA IF MAKE 1 ERROR
                                 ],
                    ),#<=== NOTE COMA [NOTE]
        )#<=== NOTE COMA

        self.right_column = ft.Container(
                    ink       = False,
                    padding   = ft.padding.all(8),
                    margin    = ft.margin.all(8),
                    alignment = ft.alignment.center,
                    content=ft.Column(
                                alignment = ft.MainAxisAlignment.SPACE_AROUND,
                                controls  = [
                                            ABOUT_BOX(
                                                        header  = "FLET-BOX",
                                                        body    = 'about_me',
                                                        footer  = "LEARN MORE 🮥",
                                                        ref_url = 'https://github.com/xavier53348/Flet-Box/blob/main/docs/Roadmap.md',
                                                        ),
                                            ABOUT_BOX(
                                                        header  = "WORK TOGETHER",
                                                        body    = 'invitation',
                                                        footer  = "LEARN MORE 🮥",
                                                        ref_url = 'https://github.com/xavier53348/Flet-Box/blob/main/WIDGET.md',
                                                        ),
                                            FlowlowMe(),
                                         ],
                    ),#<=== NOTE COMA [NOTE]
        )#<=== NOTE COMA

        Drop_AboutPage=ft.Container(
                    ink           = False,
                    bgcolor       = ft.colors.BLACK12,
                    padding       = ft.padding.all(32),
                    margin        = ft.margin.all(8),
                    alignment     = ft.alignment.center,
                    border_radius = ft.border_radius.all(30),
                    border        = ft.border.all(1, ft.colors.TEAL_900),
                    height        = 650,
                    width=1200,
                    blur=(20,20),
                    ###################
                on_click  = lambda _:self.show_widgets(show_widget='about_page'),
                content=ft.Row(
                                    alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                    controls=[
                                                self.left_column,
                                                self.right_column,
                                             ],),
        )#<=== NOTE COMA
        return Drop_AboutPage

    def show_widgets(self,show_widget):
        """SHOW PAGES"""
        if show_widget == "about_page":
            self.about_page  = GLOBAL_VAR(get_global_var='ABOUT_CONTAINER')
            self.about_page.visible  = True if not self.about_page.visible else False
            self.about_page.update()

#######
if __name__ == '__main__':
    def main(page: ft.Page):

        page.scroll                    = "HIDDEN" #AUTO ADAPTIVE ALWAYS HIDDEN
        page.vertical_alignment        = ft.MainAxisAlignment.CENTER
        page.horizontal_alignment      = ft.CrossAxisAlignment.CENTER

        page.theme_mode                = ft.ThemeMode.DARK         #ft.ThemeMode.LIGHT
        page.window_bgcolor            = ft.colors.RED_100

        page.window_left               = 3
        page.window_top                = 3
        page.window_height             = 700
        page.window_width              = 800
        page.padding                   = 0
        page.spacing                   = 0
        page.add(AboutPage())

    ft.app(
        target=main,
        assets_dir   = "assets"

        )
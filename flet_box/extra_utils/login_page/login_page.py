import re
import flet as ft
from datetime import datetime
from ..external_library.library_email import send_email
from ..external_library.sqlite_db import sqlite_db

TEXT_PRESENTATION: str = """
Fletbox is an intuitive GUI builder interface designed for creating cross-platform applications with ease.
It features a drag-and-drop functionality, allowing users to visually design user interfaces without extensive coding knowledge
"""

CONGRATULATION: str = """
🎉 Congratulations on signing up for Fletbox! Get ready to unleash your creativity and build stunning GUI interfaces. Happy designing! 🚀
"""


def on_developing(self, name_seccion: str = str(), body_string: str = str(), page: object = None):
    # NEED IMPLEMENT YET
    self.page = page
    if body_string == "":
        self.data = f"""Hello, User!\n\n{name_seccion.upper()}\n{body_string}"""
    else:
        # self.data = body_string
        self.data = f"""Hello, User!\n\n{name_seccion.upper()}\n\n{body_string}"""

    self.dialog_alert = ft.AlertDialog(
        title=ft.Text(value=self.data, size=15),
        on_dismiss=lambda e: print("Dialog dismissed!"),
    )
    # self.page.dialog = self.dialog_alert
    self.page.overlay.append(self.dialog_alert)
    self.page.overlay[0].open = True
    self.page.update()
    self.page.overlay.pop()


class congratulation_menu(ft.Container):

    def __init__(self, page: object = None, middle_box: object = None):
        super().__init__()
        self.page = page
        self.expand = True
        self.ink = False
        self.padding = ft.margin.only(left=8, top=8, right=8, bottom=8)
        self.margin = ft.margin.all(0)
        self.alignment = ft.alignment.top_center
        self.middle_box = middle_box
        self.border = ft.border.all(2, "white,0.01")

    def build(self):
        self.column_data = ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Row(
                    # expand=True,
                    controls=[
                        ft.Container(
                            content=ft.Text(
                                spans=[
                                    ft.TextSpan("Ready to Build",
                                                ft.TextStyle(
                                                    size=40,
                                                    color="WHITE,0.5",
                                                    weight=ft.FontWeight.BOLD
                                                ),),
                                ]
                            ),
                        ),

                    ]),
                ft.Container(
                    # expand=True,
                    width=450,
                    padding=8,
                    content=ft.Text(
                        spans=[
                            ft.TextSpan(CONGRATULATION,
                                        ft.TextStyle(
                                            size=18, color="WHITE,0.2",
                                            weight=ft.FontWeight.BOLD),), ]
                    ),
                ),

                ft.Container(height=16),
                ft.Container(
                    shadow=ft.BoxShadow(
                        spread_radius=1,
                        blur_radius=15,
                        color=ft.colors('black12'),
                        offset=ft.Offset(
                            0, 0),
                        blur_style=ft.ShadowBlurStyle.OUTER,
                    ),
                    ink=False,
                    bgcolor="teal,0.5",
                    width=305,
                    # blur=(8,8),
                    padding=ft.padding.all(12),
                    margin=ft.margin.all(0),
                    alignment=ft.alignment.center,
                    border_radius=ft.border_radius.all(30),
                    on_click=lambda _:self.show_login_menu(),
                    content=ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            ft.Icon(name="sports_handball",),
                            ft.Text(
                                spans=[
                                    ft.TextSpan("START",
                                                ft.TextStyle(
                                                    size=18,
                                                    color="WHITE",
                                                    weight=ft.FontWeight.BOLD
                                                ),), ]
                            ),
                        ])

                ),
            ],
        )
        self.content = ft.Container(
            blur=(8, 8),
            padding=ft.padding.only(left=16, top=16, right=16, bottom=16),
            margin=ft.margin.only(left=4, top=4, right=4, bottom=4),
            border=ft.border.all(2, "white,0.01"),
            width=460,
            content=self.column_data,

        )

    def show_login_menu(self):
        self.middle_box.content.controls.pop()
        self.middle_box.content.controls.append(
            formulary_login(middle_box=self.middle_box))
        self.page.update()


class recover_login(ft.Container):

    payload_textfield = str()

    def __init__(self, page: object = None, middle_box: object = None):
        super().__init__()
        self.page = page
        self.expand = True
        self.ink = False
        self.padding = ft.margin.only(left=8, top=8, right=8, bottom=8)
        self.margin = ft.margin.all(0)
        self.alignment = ft.alignment.top_center
        self.middle_box = middle_box
        self.border = ft.border.all(2, "white,0.01")

    def build(self):
        self.column_data = ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,

            controls=[
                ft.Row(
                    # expand=True,
                    controls=[
                        ft.Container(
                            expand=True,
                            content=ft.Text(
                                spans=[
                                    ft.TextSpan("Recover",
                                                ft.TextStyle(
                                                    size=50, color="WHITE,0.5",
                                                    weight=ft.FontWeight.BOLD),
                                                ),
                                ]
                            ),
                        ),

                        ft.Container(
                            ink=True,
                            ink_color='Cyan',
                            tooltip="REGISTER",

                                    border_radius=ft.border_radius.all(30),
                                    shadow=ft.BoxShadow(
                                        spread_radius=1,
                                        blur_radius=15,
                                        color=ft.colors('black12'),
                                        offset=ft.Offset(0, 0),
                                        blur_style=ft.ShadowBlurStyle.OUTER,
                                    ),
                            height=50,
                            width=50,
                            bgcolor="teal,0.5",
                            on_click=lambda _: self.show_register_menu_email(),
                            content=ft.Icon(
                                        name='supervised_user_circle')
                        ),
                    ]),
                ft.Container(
                    padding=8,
                    alignment=ft.alignment.center_left,
                    on_click=lambda _:self.recover_password(),
                    content=ft.Text(
                        spans=[
                            ft.TextSpan("Recover password by email",
                                        ft.TextStyle(size=18,
                                                     color="WHITE,0.2",
                                                     weight=ft.FontWeight.BOLD
                                                     ),),
                        ]
                    ),
                ),
                ft.Container(
                    # expand=True,
                    ink=False,
                    padding=ft.padding.all(2),
                    margin=ft.margin.all(0),
                    alignment=ft.alignment.center,
                    border_radius=ft.border_radius.all(30),
                    shadow=ft.BoxShadow(
                        spread_radius=1,
                        blur_radius=15,
                        color=ft.colors('white12'),
                        offset=ft.Offset(0, 0),
                        blur_style=ft.ShadowBlurStyle.OUTER,
                    ),
                    content=ft.TextField(
                        label="Write register email",
                        border_color=ft.colors('white12'),
                        border_radius=30,
                        on_change=lambda submit_data:self.update_data(
                            payload=submit_data),
                    ),
                ),
                ft.Container(height=16),
                ft.Container(

                    ink=False,
                    bgcolor="teal,0.5",
                    padding=ft.padding.all(12),
                    margin=ft.margin.all(0),
                    alignment=ft.alignment.center,
                    border_radius=ft.border_radius.all(30),
                    on_click=lambda _:self.recover_email_password(),
                    content=ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            ft.Icon(name="upload",),
                            ft.Text(
                                spans=[
                                    ft.TextSpan("RECOVER", ft.TextStyle(
                                        size=18,
                                        color="WHITE",
                                        weight=ft.FontWeight.BOLD),), ]
                            ),
                        ])
                ),
            ],
        )
        self.content = ft.Container(
            blur=(8, 8),
            padding=ft.padding.only(left=16, top=16, right=16, bottom=16),
            margin=ft.margin.only(left=4, top=4, right=4, bottom=4),
            border=ft.border.all(2, "white,0.01"),
            width=460,
            content=self.column_data,

        )

    def recover_email_password(self):
        # if email exit in database return passord
        sqlite_obj = sqlite_db()
        data_returned = sqlite_obj.find_name(
            table_name='register',
            column='user_email',
            name=self.payload_textfield
        )

        if data_returned:
            try:
                user_name, email, pasword, register_time = data_returned[0]
                email_returned = send_email(
                    user_name=user_name,
                    send_to=self.payload_textfield,
                    title='Flet-Box ',
                    personal_code=pasword,
                )
                if email_returned:
                    self.show_register_menu_email()
                    on_developing(
                        self=self,
                        page=self.page,
                        name_seccion='Email was sent',
                        body_string=f"Mensage was sent sucessfully check your spam email: {email}"
                    )

            except Exception as e:
                on_developing(self=self,
                              page=self.page,
                              name_seccion='Email error',
                              body_string=f"Error: {e}"
                              )

    def update_data(self, payload: str = str()) ->str:
        self.payload_textfield = payload.data

    def show_register_menu_email(self):
        self.middle_box.content.controls.pop()
        self.middle_box.content.controls.append(
            formulary_login(middle_box=self.middle_box))
        self.page.update()


class formulary_login(ft.Container):

    def __init__(self, page: object = None, middle_box: object = None):
        super().__init__()
        self.page = page
        self.expand = True
        self.ink = False
        self.padding = ft.margin.only(left=8, top=8, right=8, bottom=8)
        self.margin = ft.margin.all(0)
        self.alignment = ft.alignment.top_center
        self.middle_box = middle_box
        self.border = ft.border.all(2, "white,0.01")
        self.user_textfield = str()
        self.pasword_textfield = str()

    def build(self):
        self.column_data = ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,

            controls=[
                ft.Row(
                    # expand=True,
                    controls=[
                        ft.Container(
                            expand=True,
                            content=ft.Text(
                                spans=[
                                    ft.TextSpan("Loggin",
                                                ft.TextStyle(
                                                    size=50,
                                                    color="WHITE,0.5",
                                                    weight=ft.FontWeight.BOLD
                                                ),
                                                ), ]
                            ),
                        ),

                        ft.Container(
                            ink=True,
                            ink_color='Cyan',
                            tooltip="REGISTER",

                                    border_radius=ft.border_radius.all(30),
                                    shadow=ft.BoxShadow(
                                        spread_radius=1,
                                        blur_radius=15,
                                        color=ft.colors('black12'),
                                        offset=ft.Offset(0, 0),
                                        blur_style=ft.ShadowBlurStyle.OUTER,
                                    ),
                            height=50,
                            width=50,
                            bgcolor="teal,0.5",
                            on_click=lambda _:self.show_register_menu(),
                            content=ft.Icon(
                                        name='border_color_rounded')
                        ),
                    ]),
                ft.Container(
                    alignment=ft.alignment.center_left,
                    content=ft.Text(
                        spans=[
                            ft.TextSpan("Welcome to flet-box loggin", ft.TextStyle(
                                size=18,
                                color="WHITE,0.2",
                                weight=ft.FontWeight.BOLD),), ]
                    ),
                ),
                ft.Container(
                    ink=False,
                    padding=ft.padding.all(2),
                    margin=ft.margin.all(0),
                    alignment=ft.alignment.center_left,
                    border_radius=ft.border_radius.all(30),
                    shadow=ft.BoxShadow(
                        spread_radius=1,
                        blur_radius=15,
                        color=ft.colors('white12'),
                        offset=ft.Offset(0, 0),
                        blur_style=ft.ShadowBlurStyle.OUTER,
                    ),
                    content=ft.TextField(
                        label="User name",
                        border_color=ft.colors('white12'),
                        border_radius=30,
                        on_change=lambda submit_data:self.user_update_data(
                            payload=submit_data),
                    ),
                ),
                ft.Container(
                    alignment=ft.alignment.center_left,
                    content=ft.Text(
                        spans=[ft.TextSpan("Password",
                                           ft.TextStyle(
                                               size=18,
                                               color="WHITE,0.2",
                                               weight=ft.FontWeight.BOLD),), ]
                    ),
                ),
                ft.Container(
                    ink=False,
                    padding=ft.padding.all(2),
                    margin=ft.margin.all(0),
                    alignment=ft.alignment.center,
                    border_radius=ft.border_radius.all(30),
                    shadow=ft.BoxShadow(
                        spread_radius=1,
                        blur_radius=15,
                        color=ft.colors('white12'),
                        offset=ft.Offset(0, 0),
                        blur_style=ft.ShadowBlurStyle.OUTER,
                    ),
                    content=ft.TextField(
                        label="Password",
                        password=True,
                        border_color=ft.colors('white12'),
                        border_radius=30,
                        on_change=lambda submit_data:self.password_update_data(
                            payload=submit_data),
                    ),
                ),
                ft.Container(
                    padding=ft.padding.all(16),
                    alignment=ft.alignment.center_right,
                    on_click=lambda _:self.go_recover_menu(),
                    content=ft.Text(
                        spans=[
                            ft.TextSpan("Recover Password",
                                        ft.TextStyle(
                                            decoration=ft.TextDecoration.UNDERLINE,
                                            size=18,
                                            color="White,0.8",
                                            weight=ft.FontWeight.BOLD),
                                        ),
                        ]
                    ),

                ),
                ft.Container(height=16),
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,

                    controls=[
                        ft.Container(
                            expand=True,
                            ink=False,
                            bgcolor="teal,0.5",
                            padding=ft.padding.all(12),
                            margin=ft.margin.all(0),
                            alignment=ft.alignment.center,
                            border_radius=ft.border_radius.all(30),
                            on_click=lambda _:self.start_flet_box(),
                            content=ft.Row(
                                alignment=ft.MainAxisAlignment.CENTER,
                                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                controls=[
                                    ft.Text(
                                        spans=[
                                            ft.TextSpan("LOGGIN",
                                                        ft.TextStyle(size=18,
                                                                     color="WHITE",
                                                                     weight=ft.FontWeight.BOLD
                                                                     ),),
                                        ]
                                    ),
                                ])
                        ),
                        ft.Container(

                            expand=True,
                            ink=False,
                            bgcolor=ft.Colors.with_opacity(
                                0.2, ft.colors('white')),
                            padding=ft.padding.all(12),
                            margin=ft.margin.all(0),
                            alignment=ft.alignment.center,
                            border_radius=ft.border_radius.all(30),
                            on_click=lambda _:self.show_register_menu(),
                            content=ft.Row(
                                alignment=ft.MainAxisAlignment.CENTER,
                                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                controls=[
                                    # ft.Icon(name="schedule_send_sharp",),
                                    ft.Text(
                                        spans=[
                                            ft.TextSpan("SIGN UP",
                                                        ft.TextStyle(size=18,
                                                                     color="white",
                                                                     weight=ft.FontWeight.BOLD
                                                                     ),),
                                        ]
                                    ),
                                ])
                        ),

                    ]
                )
            ],
        )
        self.content = ft.Container(
            blur=(8, 8),
            padding=ft.padding.only(left=16, top=16, right=16, bottom=16),
            margin=ft.margin.only(left=4, top=4, right=4, bottom=4),
            border=ft.border.all(2, "white,0.01"),
            width=460,
            content=self.column_data,

        )

    def go_recover_menu(self):
        self.middle_box.content.controls.pop()
        self.middle_box.content.controls.append(
            recover_login(middle_box=self.middle_box))
        self.page.update()

    def show_register_menu(self):
        self.middle_box.content.controls.pop()
        self.middle_box.content.controls.append(
            formulary_register(middle_box=self.middle_box))
        self.page.update()

    def user_update_data(self, payload: str = str()) ->str:
        self.user_textfield = payload.data

    def password_update_data(self, payload: str = str()) ->str:
        self.pasword_textfield = payload.data

    def start_flet_box(self):

        self.user = self.user_textfield
        self.pasword = self.pasword_textfield

        sqlite_obj = sqlite_db()
        data_returned = sqlite_obj.find_name(table_name='register',
                                             column='user_name',
                                             name=self.user,
                                             match=['user_password',
                                                    self.pasword]
                                             )

        if data_returned:
            user_name, email, pasword, register_time = data_returned[0]

            if user_name == self.user and self.pasword == pasword:
                print(f"user_name: {user_name},pasword: {pasword}")
                self.page.session.set(
                    'user_name', {'user_name': user_name, 'pasword': pasword})
                self.page.go('/home')
        else:
            # print('intent 1')
            # self.open_dialog = self.page.session.get('on_dev')
            on_developing(self=self,
                          page=self.page,
                          name_seccion='Wrong validation data',
                          body_string=f"Pleasse insert correct email or password"
                          )


class formulary_register(ft.Container):

    def __init__(self, page: object = None, middle_box: object = None):
        super().__init__()
        self.page = page
        self.expand = True
        self.ink = False
        self.padding = ft.margin.only(left=8, top=8, right=8, bottom=8)
        self.margin = ft.margin.all(0)
        self.alignment = ft.alignment.top_center
        self.middle_box = middle_box
        self.border = ft.border.all(2, "white,0.01")

        self.user_register_str = str()
        self.password_register_str = str()
        self.password_second_register_str = str()
        self.email_register_str = str()

    def build(self):
        self.column_data = ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,

            controls=[
                ft.Row(
                    controls=[
                        ft.Container(
                            expand=True,
                            content=ft.Text(
                                spans=[
                                    ft.TextSpan("Sign Up",
                                                ft.TextStyle(
                                                    size=50,
                                                    color="WHITE,0.5",
                                                    weight=ft.FontWeight.BOLD),
                                                ), ]
                            ),
                        ),

                        ft.Container(
                            tooltip="LOGIN",

                            border_radius=ft.border_radius.all(30),
                            shadow=ft.BoxShadow(
                                spread_radius=1,
                                blur_radius=15,
                                color=ft.colors('black12'),
                                offset=ft.Offset(0, 0),
                                blur_style=ft.ShadowBlurStyle.OUTER,
                            ),
                            ink=True,
                            ink_color="cyan",
                            bgcolor="teal,0.5",
                            on_click=lambda _:self.show_login_menu(),
                            height=50,
                            width=50,
                            content=ft.Icon(
                                name='supervised_user_circle')
                        ),
                    ]),

                ft.Container(
                    padding=8,
                    alignment=ft.alignment.center_left,
                    content=ft.Text(
                        spans=[ft.TextSpan("Welcome to flet-box register",
                                           ft.TextStyle(size=18,
                                                        color="WHITE,0.2",
                                                        weight=ft.FontWeight.BOLD
                                                        ),), ]
                    ),
                ),
                ft.Container(
                    ink=False,
                    padding=ft.padding.all(2),
                    margin=ft.margin.all(0),
                    alignment=ft.alignment.center,
                    border_radius=ft.border_radius.all(30),
                    shadow=ft.BoxShadow(
                        spread_radius=1,
                        blur_radius=15,
                        color=ft.colors('white12'),
                        offset=ft.Offset(0, 0),
                        blur_style=ft.ShadowBlurStyle.OUTER,
                    ),
                    content=ft.TextField(
                        label="User name",
                        border_color=ft.colors('white12'),
                        border_radius=30,
                        on_change=lambda submit_data:self.user_register(
                            payload=submit_data),
                    ),
                ),
                ft.Container(
                    alignment=ft.alignment.center_left,
                    padding=8,
                    content=ft.Text(
                        spans=[ft.TextSpan("Password", ft.TextStyle(
                            size=18, color="WHITE,0.2",
                            weight=ft.FontWeight.BOLD),
                        ), ]
                    ),
                ),
                ft.Container(
                    ink=False,
                    padding=ft.padding.all(2),
                    margin=ft.margin.all(0),
                    alignment=ft.alignment.center,
                    border_radius=ft.border_radius.all(30),
                    shadow=ft.BoxShadow(
                        spread_radius=1,
                        blur_radius=15,
                        color=ft.colors('white12'),
                        offset=ft.Offset(0, 0),
                        blur_style=ft.ShadowBlurStyle.OUTER,
                    ),
                    content=ft.TextField(
                        label="Password",
                        password=True,
                        border_color=ft.colors('white12'),
                        border_radius=30,
                        on_change=lambda submit_data:self.password_register(
                            payload=submit_data),
                    ),
                ),
                ft.Container(
                    alignment=ft.alignment.center_left,
                    content=ft.Text(
                        spans=[
                            ft.TextSpan("Repeat Password",
                                        ft.TextStyle(
                                            size=18,
                                            color="white12",
                                            weight=ft.FontWeight.BOLD
                                        ),), ]
                    ),
                ),
                ft.Container(
                    ink=False,
                    padding=ft.padding.all(2),
                    margin=ft.margin.all(0),
                    alignment=ft.alignment.center_left,
                    border_radius=ft.border_radius.all(30),
                    shadow=ft.BoxShadow(
                        spread_radius=1,
                        blur_radius=15,
                        color=ft.colors('white12'),
                        offset=ft.Offset(0, 0),
                        blur_style=ft.ShadowBlurStyle.OUTER,
                    ),
                    content=ft.TextField(
                        password=True,
                        label="Repeat Password",
                        border_color=ft.colors('white12'),
                        border_radius=30,
                        on_change=lambda submit_data:self.password_second_register(
                            payload=submit_data),
                    ),
                ),

                ft.Container(
                    padding=8,
                    alignment=ft.alignment.center_left,
                    content=ft.Text(
                        spans=[ft.TextSpan("Email",
                                           ft.TextStyle(
                                               size=18,
                                               color="WHITE,0.2",
                                               weight=ft.FontWeight.BOLD
                                           ),),
                               ],
                    ),
                ),
                ft.Container(
                    ink=False,
                    padding=ft.padding.all(2),
                    margin=ft.margin.all(0),
                    alignment=ft.alignment.center,
                    border_radius=ft.border_radius.all(30),
                    shadow=ft.BoxShadow(
                        spread_radius=1,
                        blur_radius=15,
                        color=ft.colors('white12'),
                        offset=ft.Offset(0, 0),
                        blur_style=ft.ShadowBlurStyle.OUTER,
                    ),

                    content=ft.TextField(
                        label="exemple_name@gmail.com",
                        border_color=ft.colors('white12'),
                        border_radius=30,
                        on_change=lambda submit_data:self.email_register(
                            payload=submit_data),
                    ),
                ),

                ft.Container(height=16),
                ft.Container(
                    shadow=ft.BoxShadow(
                        spread_radius=1,
                        blur_radius=15,
                        color=ft.colors('black12'),
                        offset=ft.Offset(
                            0, 0),
                        blur_style=ft.ShadowBlurStyle.OUTER,
                    ),
                    ink=False,
                    bgcolor="teal,0.5",
                    width=305,
                    padding=ft.padding.all(12),
                    margin=ft.margin.all(0),
                    alignment=ft.alignment.center,
                    border_radius=ft.border_radius.all(30),
                    on_click=lambda _:self.open_register_succesfully(),
                    content=ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            ft.Icon(name="how_to_reg_sharp",),
                            ft.Text(
                                spans=[ft.TextSpan("REGISTER", ft.TextStyle(
                                    size=18,
                                    color="WHITE",
                                    weight=ft.FontWeight.BOLD),), ]
                            ),
                        ])
                ),
            ],
        )
        self.content = ft.Container(
            blur=(8, 8),
            padding=ft.padding.only(left=16, top=16, right=16, bottom=16),
            margin=ft.margin.only(left=4, top=4, right=4, bottom=4),
            border=ft.border.all(2, "white,0.01"),
            width=460,
            content=self.column_data,

        )

    def open_register_succesfully(self):
        """
        Opens a register succesfully.
        """
        # verification same password
        if self.password_register_str == self.password_second_register_str\
                and not self.password_register_str == ""\
                and not self.password_second_register_str == ""\
                and not self.user_register_str == ""\
                and not self.email_register_str == "":

            sqlite_obj = sqlite_db()
            is_valid_email = self.check_email(email=self.email_register_str)

            if is_valid_email:
                user_name = sqlite_obj.find_name(
                    table_name='register',
                    column='user_name',
                    name=self.user_register_str
                )
                sqlite_obj = sqlite_db()
                user_email = sqlite_obj.find_name(
                    table_name='register',
                    column='user_email',
                    name=self.email_register_str
                )

                if user_name:
                    on_developing(
                        self=self,
                        page=self.page,
                        name_seccion='Duplicate validation username',
                        body_string="Pleasse username exist in database take another account"
                    )
                elif user_email:
                    on_developing(
                        self=self,
                        page=self.page,
                        name_seccion='Duplicate validation email',
                        body_string="Pleasse email exist in database take another account"
                    )

                elif user_name == False and user_email == False:
                    """
                    write user in database
                    """
                    # WRITE DATA IN REGISTER TABLE
                    sqlite_obj = sqlite_db()
                    sqlite_obj.write_data(
                        table_name='register',
                        column=(
                            self.user_register_str,
                            self.email_register_str,
                            self.password_register_str,
                            str(datetime.now())
                        ))

                    # WITE DATA IN SCREENS TABLE
                    sqlite_obj = sqlite_db()
                    sqlite_obj.write_data(
                        table_name='user_screen',
                        column=(
                            self.user_register_str,  # user_name
                            'None',  # main_screen
                            'None',  # screen_one
                            'None',  # screen_two
                            'None',  # screen_three
                            'None',  # screen_four
                            'None',  # screen_five
                            'None',  # screen_six
                            'None',  # screen_seven
                            'None',  # screen_eigth
                            'None',  # screen_nine
                            'None',  # screen_ten
                            'None',  # screen_eleven
                            'None',  # screen_twelve
                        )
                    )

                    self.middle_box.content.controls.pop()
                    self.middle_box.content.controls.append(
                        congratulation_menu(
                            middle_box=self.middle_box
                        ))
                    self.page.update()
            else:
                on_developing(self=self,
                              page=self.page,
                              name_seccion='Wrong typing email',
                              body_string="Pleasse check email most be real email"
                              )
        else:
            on_developing(self=self,
                          page=self.page,
                          name_seccion='Wrong validation password',
                          body_string="Pleasse both password need be same"
                          )

    def check_email(self, email: str = str()) -> bool:
        valid = re.match(
            r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email)
        return valid

    def user_register(self, payload: str = str()) ->str:
        self.user_register_str = payload.data

    def password_register(self, payload: str = str()) ->str:
        self.password_register_str = payload.data

    def password_second_register(self, payload: str = str()) ->str:
        self.password_second_register_str = payload.data

    def email_register(self, payload: str = str()) ->str:
        self.email_register_str = payload.data

    def show_login_menu(self):
        self.middle_box.content.controls.pop()
        self.middle_box.content.controls.append(
            formulary_login(middle_box=self.middle_box)
        )
        self.page.update()


class about_flet_box(ft.Container):
    def __init__(self, page: object = None, middle_box: object = None):
        super().__init__()
        self.page = page
        self.expand = True
        self.ink = False
        self.padding = ft.margin.only(left=8, top=8, right=8, bottom=8)
        self.margin = ft.margin.all(0)
        self.alignment = ft.alignment.top_center
        self.middle_box = middle_box
        self.border = ft.border.all(2, "white,0.01")

    def build(self):
        self.content = ft.Container(
            ink=False,
            padding=ft.padding.all(16),
            margin=ft.margin.all(8),
            alignment=ft.alignment.center,
            blur=(12, 12),
            width=480,
            border=ft.border.all(2, "white,0.01"),
            content=ft.Column(
                controls=[
                    ft.Container(
                        expand=True,
                        ink=False,
                        padding=ft.padding.all(16),
                        margin=ft.margin.all(0),
                        alignment=ft.alignment.center,
                        content=ft.Text(
                            value="Get your own ",
                            text_align=ft.TextAlign.LEFT,
                            weight=ft.FontWeight.BOLD,
                            font_family="Consolas",
                            size=40,

                            spans=[
                                ft.TextSpan("App\n",
                                            ft.TextStyle(
                                                size=45,
                                                color="cyan,0.5"),),
                                ft.TextSpan("in just one place\n",
                                            ft.TextStyle(
                                                size=30,
                                                color=ft.colors('white')),),
                                ft.TextSpan("FLET", ft.TextStyle(
                                    size=50,
                                    color="teal,0.8",
                                    weight=ft.FontWeight.BOLD)),
                                ft.TextSpan("-BOX\n",
                                            ft.TextStyle(
                                                size=50,
                                                color="teal,0.8",
                                                weight=ft.FontWeight.BOLD),),
                                ft.TextSpan(TEXT_PRESENTATION,
                                            ft.TextStyle(
                                                size=15,
                                                color=ft.colors('white')),),
                            ],
                        ),
                    ),
                    ft.Container(
                        ink=False,
                        bgcolor="teal,0.5",
                        padding=ft.padding.all(16),
                        margin=ft.margin.all(8),
                        alignment=ft.alignment.center,
                        border_radius=ft.border_radius.all(30),
                        on_click=lambda _:self.start_formulary_loggin(),
                        shadow=ft.BoxShadow(
                            spread_radius=1,
                            blur_radius=15,
                            color=ft.colors('black12'),
                            offset=ft.Offset(0, 0),
                            blur_style=ft.ShadowBlurStyle.OUTER,
                        ),
                        content=ft.Text(
                            spans=[
                                ft.TextSpan("Get started", ft.TextStyle(
                                    size=24,
                                    color="WHITE",
                                    weight=ft.FontWeight.BOLD),),
                            ],
                        ),),
                ]),)

    def start_formulary_loggin(self):
        self.middle_box.content.controls.pop()
        self.middle_box.content.controls.append(
            formulary_login(middle_box=self.middle_box))
        self.page.update()


class middle_body(ft.Container):

    def __init__(self, data='Erase this test'):
        super().__init__()
        self.title = data

        self.expand = True
        self.ink = False
        self.padding = ft.padding.all(0)
        self.margin = ft.margin.all(0)
        self.alignment = ft.alignment.center

    def build(self):
        self.content = ft.Row(
            controls=[
                about_flet_box(middle_box=self),
                # formulary_login(middle_box=self),
                # formulary_register(middle_box=self),
                # recover_login(middle_box=self),
                # congratulation_menu(middle_box=self),
            ]
        )


class login_page(ft.Container):
    def __init__(self, page: object = None):
        super().__init__()
        self.page = page
        self.expand = True
        self.ink = False
        self.padding = ft.padding.all(0)
        self.margin = ft.margin.all(0)
        self.alignment = ft.alignment.center
        self.image = ft.DecorationImage(
            src='designer_2.jpeg',
            fit=ft.ImageFit.COVER,
            opacity=0.5 if self.page.window.width <= 620 else 0.5,
        )

    def build(self):
        self.content = ft.Column(
            scroll="ALWAYS",
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                middle_body(),
            ]
        )


if __name__ == "__main__":

    def main(page: ft.Page):

        page.vertical_alignment = ft.MainAxisAlignment.CENTER
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        page.theme_mode = ft.ThemeMode.DARK
        page.window.bgcolor = ft.colors.RED_100
        page.window.left = 3
        page.window.top = 3

        page.padding = 0
        page.spacing = 0
        page.add(login_page())

    ft.app(target=main)

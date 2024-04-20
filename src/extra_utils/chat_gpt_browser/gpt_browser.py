####################################################
import flet as ft
import os
import pyperclip
import time
####################################################
from .library_chatgpt import ChatGpt
####################################################
os.environ["FLET_WS_MAX_MESSAGE_SIZE"] = "8000000"
####################################################

class Gpt_text(ft.Stack):
    # globalVar='Erase this test'

    def __init__(self,input_text='Erase this test',color_chat="#0a1618",ask=False):
        super().__init__()
        self.input_text = input_text
        self.color_chat = color_chat if ask else ft.colors.BLACK26

        self.position_right_chat_gpt = True if ask else False
        self.position_left_chat_gpt  = True if not ask else False

        self.icon_container =ft.Container(
                                ##################### PROPERTY
                                # expand      = True,
                                ink           = True,                                                # click effect ripple
                                ink_color     = ft.colors.RED_900,
                                bgcolor       = ft.colors.BLUE_900,                                    # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                                padding       = ft.padding.only(left=0, top=0, right=0, bottom=0),    # inside box                # padding.only(left=8, top=8, right=8, bottom=8),
                                margin        = ft.margin.all(0),    #outside box                # margin.only (left=8, top=8, right=8, bottom=8),
                                alignment     = ft.alignment.center,                            # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right.    posicionamiento adentro widget
                                border_radius = ft.border_radius.all(30),            # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                                border      = ft.border.all(2, ft.colors.BLUE),             # ft.border.only(Left=8, top=8, right=8, bottom=8),
                                # image_src   = f"/icons/icon-512.png",
                                width         = 30,
                                height        = 30,
                                offset        = (0.3,0),
                                # tooltip     ='Container',
                                ##################### EFFECTS
                                # gradient    = ft.LinearGradient( begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=[ft.colors.BLUE, ft.colors.YELLOW],),
                                # gradient    = ft.RadialGradient( colors=[ft.colors.YELLOW, ft.colors.BLUE],),
                                ##################### WIDGETS
                                content= ft.Icon(
                                                    color=ft.colors.WHITE,
                                                    size=18,
                                                    name=ft.icons.COPY
                                                    ),
                                ##################### EVENTS
                            on_click=lambda _:print(_),                            # on_hover=print('on click over'), on_long_press=print('long press'),
                    )#<=== NOTE COMA
        self.widget_to_select = {'gpt':ft.TextField(
                                                value           = self.input_text, # content = ft.Text(value="Compound button", size=12,),

                                                multiline     = True,
                                                read_only     = True,
                                                border        = ft.InputBorder.NONE,              # border=ft.InputBorder.[NONE ,OUTLINE ,UNDERLINE]
                                                # font_family = "RobotoSlab", #"Consolas ,RobotoSlab
                                                text_size     = 12,
                                                width         = 700,
                                        ),
                                'ask':
                                        ft.Text(
                                                #################### PROPERTY
                                                value           = self.input_text, # content = ft.Text(value="Compound button", size=12,),
                                                font_family     = "RobotoSlab", #"Consolas ,RobotoSlab
                                                size=12,

                                                #################### COLOR
                                                # overflow="FADE",                                      # FADE,ELLIPSIS,CLIP,VISIBLE
                                                #################### STYLES TEXT
                                                #################### EVENTS
                                                # on_click=lambda _:print(_),   # on_hover=print('on click over'), on_long_press=print('long press'),
                                                )
                                    }

        self.ask_response =self.widget_to_select.get('gpt')  if not ask else self.widget_to_select.get('ask')
        self.icon_container.visible=True if not ask else False
    def build(self):



        Drop_Gpt_text=ft.Container(
                    ##################### PROPERTY
                    ##################### [rotate,offset] , [scale,aspect_ratio] , [visible,disabled]
                    # expand=True,
                    ink             = False,                                                      # click effect ripple
                    bgcolor         = self.color_chat,                                            # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                    padding         = ft.padding.only(left=32, top=8, right=32, bottom=8), # inside box                        # padding.only(left=8, top=8, right=8, bottom=8),
                    margin          = ft.margin.all(0),  # outside box                       # margin.only (left=8, top=8, right=8, bottom=8),
                    # alignment     = self.aligment_chat_gpts,                                  # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right. posicionamiento adentro widget
                    alignment       = ft.alignment.center_left,                                  # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right. posicionamiento adentro widget
                    border_radius   = ft.border_radius.all(32),                  # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                    border        = ft.border.all(2, ft.colors.BLACK12),                     # ft.border.only(Left=8, top=8, right=8, bottom=8),
                    #               ===================
                    # image_src     = f"/home/mjay/Pictures/3d_neon_pink-2560x1440.jpg",
                    # image_opacity = 0.1,
                    # image_fit     = 'COVER',                                            # CONTAIN, COVER, FILL, FIT_HEIGHT, FIT_WIDTH, SCALE_DOWN
                    #               ===================
                    # width         = 500,
                    # width         = 700,
                    # height        = 250,
                    # tooltip       = 'Container',
                    # blur          = (12,12),
                    ##################### EFFECTS
                    # gradient      = ft.LinearGradient( begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=[ft.colors.BLACK38, ft.colors.BLACK12],),
                    # gradient      = ft.RadialGradient( colors=[ft.colors.YELLOW, ft.colors.BLUE],),
                    ##################### WIDGETS
                    content = ft.Column(
                                        spacing              = 0,
                                        ##################### PROPERTY BOX
                                        # expand             = True,
                                        alignment            = ft.MainAxisAlignment.SPACE_AROUND,              # horizontal <=> START,CENTER,END SPACE_BETWEEN SPACE_AROUND SPACE_EVENLY
                                        horizontal_alignment = ft.CrossAxisAlignment.END,        # vertical       START,CENTER END
                                        ##################### LET MAKE SCROLL IN LONG QUANTITY
                                        # scroll             = True,                                              # center widget
                                        # tight              = True,
                                        ##################### ADAPT TO SCREEN
                                        # wrap               = True,                                                  # justify in all screen
                                        # spacing            = 8,                                                # space widget left right
                                        # run_spacing        = 8,                                            # space widget up down
                                        ##################### WIDGETS
                                    controls = [
                                                self.icon_container,
                                                self.ask_response,

                                                ],))#<=== NOTE COMA <==> ERASE COMA IF MAKE 1 ERROR
        self.data = ft.Row(
                        alignment=ft.alignment.center,                            # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right.    posicionamiento adentro widget
                        # wrap=True,
                        controls = [
                                    ft.Container(expand=self.position_right_chat_gpt),
                                    Drop_Gpt_text,
                                    ft.Container(expand=self.position_left_chat_gpt),
                                    ]
                                )
        return self.data
        # return Drop_Gpt_text

    # def copy_to_clipboard(self,e):
    #     text_copy = e
    #     ########################## personal scakbar
    #     pyperclip.copy(text_copy)
    #     alert_dialog.visible = True
    #     alert_dialog.content.value = f"Copy: {text_copy} "
    #     alert_dialog.update()
    #     time.sleep(0.5)
    #     alert_dialog.visible = False
    #     alert_dialog.update()
    #     ##########################

######## Gpt_text = Gpt_text(),# <======= Comma
class GptBrowser(ft.Stack):
    """
    lite module to find colors by name
    """

    def __init__(self,blur_effect = False, numb_widget_to_show=50):
        super().__init__()
        global alert_dialog

        # PREPARING THE LIST THAT WILL CONTENT ALL INCON INSIDE
        # self.list_colors = self.preparing_list_colors()
        self.numb_widget_to_show = numb_widget_to_show

        if blur_effect:
            self.blur = 20
        else:
            self.blur = None
        self.Gpt_Text = Gpt_text

        # BARNER THAT WILL SHOW AFTER MAKE CLICK OVER THE WIDGET
        alert_dialog = ft.Container(
                                        visible       = False,
                                        height        = 40,
                                        width         = 240,
                                        bgcolor       = 'red',
                                        offset        = (0,-1.5),
                                        alignment     = ft.alignment.center,                                  # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right. posicionamiento adentro widget
                                        border_radius = ft.border_radius.all(16),
                                    content = ft.Text(
                                                        value = 'None',
                                                        # bold=True,
                                                        )
                                        )

        text_test = """
Hello there!

Come and experience the world of knowledge and conversation with ChatGPT.
Let's explore and exchange thoughts on any topic you desire.
Join me and let's embark on a journey of discovery together!...
"""
        self.Search_Gridwiew = ft.Column(
                        # visible  = False,
                        # wrap                 = True,
                        scroll               = 'HIDDEN',
                        # expand             = True,
                        # wrap               = True,
                        # auto_scroll        = False,
                        # ##################### PROPERTY GRIDVIEW
                        # runs_count         = 10, # column's number
                        # run_spacing        = 5,  # space between widget
                        # padding            = 8,
                        # spacing            = 5,  # space widget left right
                        # expand             = 1,
                        # child_aspect_ratio = 1,  # scale of widget
                        # max_extent         = 150, # lateral_size max
                        ##################### WIDGETS
                    controls=[
                            self.Gpt_Text(text_test),
                            # Gpt_text() for _ in range(self.numb_widget_to_show)
                            ],
                        )
        # MAIN CONTAINER SKELETON OF THE WIDGET OR MAIN LAYOUT
        self.text_field_chat_gpt = ft.TextField(
                                label                = "    Hello DEV !!. What do you like talk about ?...",
                                border               = ft.InputBorder.OUTLINE,                # border=ft.InputBorder.[NONE ,OUTLINE ,UNDERLINE]
                                bgcolor              = ft.colors.BLACK12,                     # inside box
                                focused_bgcolor      = ft.colors.BLACK12,                     # inside box after click
                                border_color         = ft.colors.TEAL,                        # border box
                                focused_border_color = ft.colors.TRANSPARENT,                 # border box after click
                                border_radius        = 30,                                    # corner
                                text_size            = 15,
                                content_padding      = ft.padding.only(left=16, top=2, right=16, bottom=2),
                                prefix_icon          = ft.icons.LANGUAGE,          # Icon left  inside box
                                multiline=True,
                                )
                ##################### EVENTS
                # on_click=lambda _:print(_),   # on_hover=print('on click over'), on_long_press=print('long press'),
        self.Drop_GptBrowser=ft.Container(
                    ##################### PROPERTY COLUMN
                    expand    = True,
                    ink       = False,                                                   # click effect ripple
                    padding   = ft.padding.all(8),    # inside box                       # padding.only(left=8, top=8, right=8, bottom=8),
                    margin    = ft.margin.all(8),    # outside box                       # margin.only (left=8, top=8, right=8, bottom=8),
                    alignment = ft.alignment.center,                                     # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right.    posicionamiento adentro widget

                    content   = ft.Column(
                        spacing              = 8,
                        alignment            = ft.MainAxisAlignment.SPACE_AROUND,        # horizontal <=> START,CENTER,END SPACE_BETWEEN SPACE_AROUND SPACE_EVENLY
                        horizontal_alignment = ft.CrossAxisAlignment.CENTER,             # vertical       START,CENTER END
                        scroll=False,

                        ##################### PROPERTY BOX
                        controls=[

                                    ft.Container( ##################### GRID VIEW
                                                ##################### PROPERTY
                                                ##################### [rotate,offset] , [scale,aspect_ratio] , [visible,disabled]
                                                # expand      = True,
                                                ink           = False,                                          # click effect ripple
                                                bgcolor       = ft.colors.BLACK38,                              # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                                                padding       = ft.padding.all(8),    # inside box              # padding.only(left=8, top=8, right=8, bottom=8),
                                                margin        = ft.margin.all(0),    #outside box               # margin.only (left=8, top=8, right=8, bottom=8),
                                                alignment     = ft.alignment.center,                            # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right.    posicionamiento adentro widget
                                                border_radius = ft.border_radius.all(30),                       # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                                                border        = ft.border.all(0.8, ft.colors.TEAL),             # ft.border.only(Left=8, top=8, right=8, bottom=8),
                                                blur          = self.blur,
                                                height        = 500,
                                                ##################### WIDGETS
                                            content       = self.Search_Gridwiew,
                                                #<=== NOTE COMA [NOTE]                     for x in range(1,50): widget.content.controls.append(ft.ElevatedButton("press buttom",tooltip='buttom'))
                                                ##################### EVENTS
                                                # on_click=lambda _:print(_),                            # on_hover=print('on click over'), on_long_press=print('long press'),
                                    ),#<=== NOTE COMA
                                    ft.Container(
                                                ##################### PROPERTY
                                                ##################### [rotate,offset] , [scale,aspect_ratio] , [visible,disabled]
                                                # expand=True,
                                                ink=False,                                                # click effect ripple
                                                # bgcolor="#44CCCC00",                                    # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                                                padding= ft.padding.all(0),    # inside box                # padding.only(left=8, top=8, right=8, bottom=8),
                                                margin = ft.margin.all(0),    #outside box                # margin.only (left=8, top=8, right=8, bottom=8),
                                                alignment=ft.alignment.center,                            # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right.    posicionamiento adentro widget
                                                content=ft.Row(
                                                                ##################### PROPERTY BOX
                                                                # expand=True,
                                                                # alignment=ft.MainAxisAlignment.SPACE_AROUND,              # horizontal <=> START,CENTER,END SPACE_BETWEEN SPACE_AROUND SPACE_EVENLY
                                                                # vertical_alignment=ft.CrossAxisAlignment.CENTER,          # vertical       START,CENTER END
                                                                ##################### LET MAKE SCROLL IN LONG QUANTITY
                                                                # scroll=True,                                              # center widget
                                                                # tight=True,
                                                                ##################### ADAPT TO SCREEN
                                                                # wrap=True,                                                  # justify in all screen
                                                                # spacing=8,                                                # space widget left right
                                                                run_spacing=0,                                            # space widget up down
                                                                ##################### WIDGETS
                                                                controls=[
                                                                        ft.Container( ##################### TEXT FIELD
                                                                                    ##################### PROPERTY
                                                                                    ink           = False,
                                                                                    expand=True,                                           # click effect ripple
                                                                                    padding       = ft.padding.only(left=0, top=4, right=0, bottom=4),# inside box                       # padding.only(left=8, top=8, right=8, bottom=8),
                                                                                    margin        = ft.margin.all(0),  # outside box                      # margin.only (left=8, top=8, right=8, bottom=8),
                                                                                    alignment     = ft.alignment.center,                                  # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right. posicionamiento adentro widget
                                                                                    border_radius = ft.border_radius.all(30),                             # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                                                                                    blur          = self.blur,
                                                                                    height        = 50,
                                                                                    ##################### WIDGETS
                                                                                content=self.text_field_chat_gpt,
                                                                        ),#<=== NOTE COMA <==> ERASE COMA IF MAKE 1 ERROR

                                                                        ft.Container(
                                                                                ##################### PROPERTY
                                                                                ##################### [rotate,offset] , [scale,aspect_ratio] , [visible,disabled]
                                                                                # expand=True,
                                                                                bgcolor=ft.colors.BLUE_900,                                            # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                                                                                padding= ft.padding.all(0), # inside box                        # padding.only(left=8, top=8, right=8, bottom=8),
                                                                                margin = ft.margin.all(0),  # outside box                       # margin.only (left=8, top=8, right=8, bottom=8),
                                                                                alignment=ft.alignment.center,                                  # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right. posicionamiento adentro widget
                                                                                border_radius= ft.border_radius.all(30),                  # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                                                                                border=ft.border.all(2, ft.colors.BLUE),                     # ft.border.only(Left=8, top=8, right=8, bottom=8),
                                                                                # ===================
                                                                                # image_src = f"/home/mjay/Pictures/3d_neon_pink-2560x1440.jpg",
                                                                                # image_opacity=0.1,
                                                                                # image_fit='COVER',                                            # CONTAIN, COVER, FILL, FIT_HEIGHT, FIT_WIDTH, SCALE_DOWN
                                                                                # ===================
                                                                                # width=150,
                                                                                ink= True,
                                                                                ink_color='red',

                                                                                height=42,
                                                                                width=42,
                                                                                # tooltip='Container',
                                                                                ##################### EFFECTS
                                                                                # gradient=ft.LinearGradient( begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=[ft.colors.BLUE, ft.colors.YELLOW],),
                                                                                # gradient=ft.RadialGradient( colors=[ft.colors.YELLOW, ft.colors.BLUE],),
                                                                                ##################### WIDGETS
                                                                            on_click      = lambda _: self.search_gpt_question(self.text_field_chat_gpt),     #FloatingActionButton
                                                                                content=ft.Icon(
                                                                                                color=ft.colors.WHITE,
                                                                                                name           = ft.icons.SEND_AND_ARCHIVE,
                                                                                ##################### EVENTS
                                                                                # on_click=lambda _:print(_),   # on_hover=print('on click over'), on_long_press=print('long press'),
                                                                    ),),#<=== NOTE COMA <==> ERASE COMA IF MAKE 1 ERROR                                                                                ,
                                                                         ],
                                                            ),
                                                ##################### EVENTS
                                                # on_click=lambda _:print(_),                            # on_hover=print('on click over'), on_long_press=print('long press'),
                                    ),#<=== NOTE COMA
                               alert_dialog,
                                 ],
                    ),#<=== NOTE COMA [NOTE]                     for x in range(1,50): widget.content.controls.append(ft.ElevatedButton("press buttom",tooltip='buttom'))
                    ##################### EVENTS
                    # on_click=lambda _:print(_),                            # on_hover=print('on click over'), on_long_press=print('long press'),
        )#<=== NOTE COMA

    def build(self):
        return self.Drop_GptBrowser

    def search_gpt_question(self,e):
        # ALL DATA THAT WE PASE BY TEXT_INPUT WILL BE IN LOWER CASE
        search_term = e.value.lower()

        self.user_question_container = Gpt_text(input_text=search_term,ask=True)
        self.Search_Gridwiew.controls.append(self.user_question_container)
        self.Search_Gridwiew.update()
        e.value =''
        e.update()
        message_returned = ChatGpt(question=f"""{search_term}""".rstrip(' '))

        print(message_returned)

        if message_returned:
            self.response_question_container = Gpt_text(input_text=message_returned,color_chat=ft.colors.BLACK12,ask=False)
            self.Search_Gridwiew.controls.append(self.response_question_container)
            self.Search_Gridwiew.scroll_to(key=f"{len(self.Search_Gridwiew.controls)}", duration=1000)
            self.Search_Gridwiew.update()
            # print(search_term)
        else:
            self.response_question_container = Gpt_text(input_text=message_returned,color_chat=ft.colors.BLACK12,ask=False)
            self.Search_Gridwiew.controls.append(self.response_question_container)
            self.Search_Gridwiew.scroll_to(key=f"{len(self.Search_Gridwiew.controls)}", duration=1000)
            self.Search_Gridwiew.update()
######## GptBrowser = GptBrowser(),# <======= Comma

if __name__ == '__main__':
    def main(page: ft.Page):
        ######################
        page.scroll                    = "HIDDEN" #AUTO ADAPTIVE ALWAYS HIDDEN
        page.vertical_alignment        = ft.MainAxisAlignment.CENTER
        page.horizontal_alignment      = ft.CrossAxisAlignment.CENTER
        ######################  COLOR
        page.theme_mode                = ft.ThemeMode.DARK         #ft.ThemeMode.LIGHT
        page.window_bgcolor            = ft.colors.RED_100
        ###################### POSITION OF SC
        page.window_left               = 3
        page.window_top                = 3
        page.window_height             = 600
        page.window_width              = 650
        page.padding                   = 0
        page.spacing                   = 0
        page.add(GptBrowser())
        ######################
    ft.app(target=main)
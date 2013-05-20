import os
import pyperclip
import flet as ft
import time
os.environ["FLET_WS_MAX_MESSAGE_SIZE"] = "8000000"


class Icon_text(ft.UserControl):
    # globalVar='Erase this test'

    def __init__(self,data='Erase this test'):
        super().__init__()
        # self.title='data'
        self.title=data

    def build(self):
        Drop_Icon_text=ft.TextButton(
                                # visible=True,
                                visible=False,
                            content=ft.Container(
                                        visible=False,
                                        # bgcolor=ft.color.BLACK,
                                        content=ft.Column(

                                            controls = [
                                                ft.Icon(
                                                        visible=False,
                                                        name='home',
                                                        size=30
                                                        ),
                                                ft.Text(
                                                    visible=False,
                                                    value      = 'testing',
                                                    size       = 12,
                                                    width      = 100,
                                                    no_wrap    = True,
                                                    text_align = "center",
                                                ),
                                            ],
                                            spacing              = 5,
                                            alignment            = "center",
                                            horizontal_alignment = "center",
                                        ),
                                        alignment=ft.alignment.center,
                                    ),
                                    # tooltip=f"{_}\nClick to copy to a clipboard",
                                    on_click=lambda _:self.copy_to_clipboard(Drop_Icon_text.content.content.controls[0].name),
                                    # data=icon_key,
                                        )
        return Drop_Icon_text

    def copy_to_clipboard(self,e):
        # text_copy = e.control.content.content.controls[1].value
        text_copy = e
        ########################## personal scakbar
        pyperclip.copy(text_copy)
        # self.Drop_IconBrowser.content.controls[2].visible = True
        # self.Drop_IconBrowser.content.controls[2].content.value = f"Copy: {text_copy} "
        # self.Drop_IconBrowser.update()
        # time.sleep(0.5)
        # self.Drop_IconBrowser.content.controls[2].visible = False
        # self.Drop_IconBrowser.update()
        ##########################

        # self.Drop_IconBrowser.content.controls[2].content.update()

######## Icon_text = Icon_text(),# <======= Comma
class IconBrowser(ft.UserControl):
    """
    lite module to find icons by name
    """

    def __init__(self,blur_effect = False):
        super().__init__()

        # preparing list with all icons inside
        self.list_icons = self.preparing_list_icons()

        if blur_effect:
            self.blur = 20
        else:
            self.blur = None
        self.Icontext = Icon_text()


        self.Search_Gridwiew = ft.GridView(
                        # visible=False,
                        ##################### PROPERTY GRIDVIEW
                        runs_count         = 10, # column's number
                        run_spacing        = 5,  # space between widget
                        padding            = 8,
                        spacing            = 5,  # space widget left right
                        expand             = 1,
                        child_aspect_ratio = 1,  # scale of widget
                        max_extent         = 150, # lateral_size max
                        ##################### WIDGETS
                    controls=[ Icon_text() for _ in range(50) ],
                        )

        self.Drop_IconBrowser=ft.Container(
                    ##################### PROPERTY COLUMN
                    expand    = True,
                    ink       = False,                                                      # click effect ripple
                    padding   = ft.padding.all(8),    # inside box                        # padding.only(left=8, top=8, right=8, bottom=8),
                    margin    = ft.margin.all(8),    # outside box                       # margin.only (left=8, top=8, right=8, bottom=8),
                    alignment = ft.alignment.center,                                  # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right.    posicionamiento adentro widget

                    content   = ft.Column(
                        spacing              = 8,
                        alignment            = ft.MainAxisAlignment.SPACE_AROUND,              # horizontal <=> START,CENTER,END SPACE_BETWEEN SPACE_AROUND SPACE_EVENLY
                        horizontal_alignment = ft.CrossAxisAlignment.CENTER,        # vertical       START,CENTER END
                        scroll=False,

                        ##################### PROPERTY BOX
                        controls=[
                                    ft.Container( ##################### TEXT FIELD
                                                ##################### PROPERTY
                                                ink           = False,                                                      # click effect ripple
                                                padding       = ft.padding.all(4), # inside box                        # padding.only(left=8, top=8, right=8, bottom=8),
                                                margin        = ft.margin.all(0),  # outside box                       # margin.only (left=8, top=8, right=8, bottom=8),
                                                alignment     = ft.alignment.center,                                  # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right. posicionamiento adentro widget
                                                border_radius = ft.border_radius.all(30),                  # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                                                blur          = self.blur,
                                                height        = 50,
                                                ##################### WIDGETS
                                            content=ft.TextField(
                                                                label                = " Search Icon name",
                                                                border               = ft.InputBorder.OUTLINE,              # border=ft.InputBorder.[NONE ,OUTLINE ,UNDERLINE]
                                                                bgcolor              = ft.colors.BLACK12,                               # inside box
                                                                focused_bgcolor      = ft.colors.BLACK12,                     # inside box after click
                                                                border_color         = ft.colors.TEAL,                           # border box
                                                                focused_border_color = ft.colors.TRANSPARENT,                 # border box after click
                                                                border_radius        = 30,                              # corner
                                                                text_size            = 15,
                                                                # icon=ft.icons.FIND_REPLACE,
                                                                prefix_icon=ft.icons.SEARCH,
                                                                # border    = ft.InputBorder.NONE,
                                                                content_padding=ft.padding.only(left=16, top=2, right=16, bottom=2),
                                                            on_submit            = lambda _: self.search_icons(_),
                                                                ),
                                                ##################### EVENTS
                                                # on_click=lambda _:print(_),   # on_hover=print('on click over'), on_long_press=print('long press'),
                                    ),#<=== NOTE COMA <==> ERASE COMA IF MAKE 1 ERROR
                                    ft.Container( ##################### GRID VIEW
                                                ##################### PROPERTY
                                                ##################### [rotate,offset] , [scale,aspect_ratio] , [visible,disabled]
                                                # expand      = True,
                                                ink           = False,                                                # click effect ripple
                                                bgcolor       = ft.colors.BLACK38,                                    # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                                                padding       = ft.padding.all(8),    # inside box                # padding.only(left=8, top=8, right=8, bottom=8),
                                                margin        = ft.margin.all(0),    #outside box                # margin.only (left=8, top=8, right=8, bottom=8),
                                                alignment     = ft.alignment.center,                            # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right.    posicionamiento adentro widget
                                                border_radius = ft.border_radius.all(30),            # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
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
                                        visible=False,
                                        height=40,
                                        width=240,
                                        bgcolor='red',
                                        offset=(0,-1.5),
                                        alignment     = ft.alignment.center,                                  # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right. posicionamiento adentro widget
                                        border_radius = ft.border_radius.all(16),
                                    content=ft.Text(
                                            value='None',
                                            # bold=True,
                                        )
                                        )
                                 ],
                    ),#<=== NOTE COMA [NOTE]                     for x in range(1,50): widget.content.controls.append(ft.ElevatedButton("press buttom",tooltip='buttom'))
                    ##################### EVENTS
                    # on_click=lambda _:print(_),                            # on_hover=print('on click over'), on_long_press=print('long press'),
        )#<=== NOTE COMA

    def build(self):

        return self.Drop_IconBrowser

    def preparing_list_icons(self):
        icons_list   = []
        list_started = False

        for key, value in vars(ft.icons).items():
            if key == "TEN_K":
                list_started = True
            if list_started:
                icons_list.append(value)

        return icons_list

    def search_icons(self,e):
        # print('hello',e.control.value)
        search_term = e.control.value
        # self.Search_Gridwiew.controls = list()
        # del self.Search_Gridwiew.controls[::]
        def run_upload_icons():
            global num_count
            num_count = 0
            self.ico_widget =''
            # self.Search_Gridwiew.visible=True
            # self.Search_Gridwiew.controls[0].content.content.controls[0].visible=True
            # self.Search_Gridwiew.controls[0].content.content.controls[1].visible=True
            for _ in self.list_icons:
                if _.startswith(search_term) and num_count < len(self.Search_Gridwiew.controls):
                    # self.Search_Gridwiew.controls[num_count].visible= True
                    # print(self.Search_Gridwiew.controls[num_count])
                    # self.Search_Gridwiew.controls[num_count].visible= True
                    # self.Search_Gridwiew.controls[num_count].content.visible = True

                    # self.Search_Gridwiew.controls[num_count].content.content.controls[0].visible=True
                    # self.Search_Gridwiew.controls[num_count].content.content.controls[1].visible=True
                    # self.Search_Gridwiew.controls[num_count].content.content.controls[0].name=_
                    # self.Search_Gridwiew.controls[num_count].content.content.controls[1].value=_
                    self.ico_widget = self.Search_Gridwiew.controls[num_count].controls[0]
                    # self.ico_widget = self.Search_Gridwiew.controls[num_count].controls[0].visible=True

                    # print(len(self.Search_Gridwiew.controls),len(self.list_icons),self.ico_widget.content.content.controls[1].value)
                    self.ico_widget.visible         = True
                    self.ico_widget.content.visible = True
                    # text button
                    self.ico_widget.visible         = True
                    # self.Search_Gridwiew.controls[num_count].controls[0].disable=True
                    print(self.ico_widget)

                    self.ico_widget.content.content.visible             = True
                    self.ico_widget.content.content.controls[0].visible = True
                    self.ico_widget.content.content.controls[1].visible = True
                    # self.ico_widget.content.content.controls[1].autofocus=False

                    self.ico_widget.content.content.controls[0].name=_
                    self.ico_widget.content.content.controls[1].value=_

                    # print(_,num_count)



                    # print(self.ico_widget.content.content.controls[1].value,'<======')
                    # if not str(self.ico_widget.content.content.controls[1].value) == 'testing':
                        # self.ico_widget.update()
                    self.ico_widget.update()
                    # else:
                    #     self.ico_widget.content.content.controls[0].visible=False
                    #     self.ico_widget.content.content.controls[1].visible=False
                    #     self.ico_widget.update()


                        # break
                    # data.update()
                    # data.content.content.controls[1].value=_
                    # self.Search_Gridwiew.controls[0].content.content.controls[1].value=_
                    # self.Search_Gridwiew.controls[1].content.content.controls[1].value=_

                    # print(self.Search_Gridwiew.controls[num_count],'==============',_,num_count)
                    # yield _
                    # self.Search_Gridwiew.controls.append(
                    num_count+= 1

                    # self.Search_Gridwiew.update()
                    #     ft.TextButton(
                    #                 content=ft.Container(
                    #                     # bgcolor=ft.color.BLACK,
                    #                     content=ft.Column(
                    #                         [
                    #                             ft.Icon(name=_, size=30),
                    #                             ft.Text(
                    #                                 value      = _,
                    #                                 size       = 12,
                    #                                 width      = 100,
                    #                                 no_wrap    = True,
                    #                                 text_align = "center",
                    #                             ),
                    #                         ],
                    #                         spacing              = 5,
                    #                         alignment            = "center",
                    #                         horizontal_alignment = "center",
                    #                     ),
                    #                     alignment=ft.alignment.center,
                    #                 ),
                    #                 # tooltip=f"{_}\nClick to copy to a clipboard",
                    #                 on_click=lambda _:self.copy_to_clipboard(_),
                    #                 # data=icon_key,
                    #                     )
                    #     )
                    # print(self.Search_Gridwiew.controls)
                    # self.Search_Gridwiew.controls[num_count].content.update()
                # else:
                #     # num_count+= 1
                #     if num_count <= 12:

                #         print(num_count)
                #         break
                #     # self.ico_widget = self.Search_Gridwiew.controls[num_count].controls[0]
                #     num_count+= 1

                    # self.ico_widget.visible=False
                    # self.ico_widget.content.visible=False
                    # self.ico_widget.content.content.visible=False
                    # self.ico_widget.content.content.controls[0].visible=False
                    # self.ico_widget.content.content.controls[1].visible=False
                    # self.ico_widget.update()
            print(num_count)

            if num_count<=50:
                for _ in range(num_count,50):
                    self.ico_widget = self.Search_Gridwiew.controls[_].controls[0]

                    self.ico_widget.content.content.controls[0].disabled=True
                    self.ico_widget.content.content.controls[1].disabled=True
                    self.ico_widget.content.content.controls[0].visible=False
                    # self.ico_widget.content.content.controls[0].hint=False
                    self.ico_widget.content.content.controls[1].visible=False


                    self.ico_widget.update()

        run_upload_icons()
        # self.Search_Gridwiew.update()
        # self.Search_Gridwiew.update()

        # self.Search_Gridwiew.update()
        # self.Drop_IconBrowser.update()

######## IconBrowser = IconBrowser(),# <======= Comma

if __name__ == '__main__':
    def main(page: ft.Page):
        page.scroll                    = "HIDDEN" #AUTO ADAPTIVE ALWAYS HIDDEN
        page.vertical_alignment        = ft.MainAxisAlignment.CENTER
        page.horizontal_alignment      = ft.CrossAxisAlignment.CENTER
        ######################  COLOR
        page.theme_mode                = ft.ThemeMode.DARK         #ft.ThemeMode.LIGHT
        page.window_bgcolor            = ft.colors.RED_100
        ###################### POSITION OF SC
        page.window_left               = 3
        page.window_top                = 3
        page.window_height             = 800
        page.window_width              = 400
        page.padding                   = 0
        page.spacing                   = 0
        page.add(IconBrowser())

    ft.app(target=main)
####################################################
from ..settings_var.save_export import MakeJasonFile
###################### CALL GLOBAL VAR #############
from extra_utils.settings_var.settings_widget import GLOBAL_VAR
####################################################
import flet as ft
####################################################

visible = False


# class TextEditorStream(ft.Stack):
#     # globalVar='Erase this test'

#     def __init__(self,data_stream='Erase this test',width_stream=None):
#         super().__init__()
#         # self.title='data'
#         self.data_stream  = data_stream
#         self.width_stream = width_stream
#     def build(self):
#         Drop_TextEditorStream=ft.Container(
#                     ##################### PROPERTY
#                     ##################### [rotate,offset] , [scale,aspect_ratio] , [visible,disabled]
#                     # expand=True,
#                     ink           = False,                                                      # click effect ripple
#                     # bgcolor       = ft.colors.CYAN,
#                     padding       = ft.padding.all(0), # inside box                        # padding.only(left=8, top=8, right=8, bottom=8),
#                     margin        = ft.margin.all(4),  # outside box                       # margin.only (left=8, top=8, right=8, bottom=8),
#                     alignment     = ft.alignment.center_left,                                  # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right. posicionamiento adentro widget
#                     # border_radius = ft.border_radius.all(12),                  # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
#                     # border=ft.border.all(2, ft.colors.BLACK),                     # ft.border.only(Left=8, top=8, right=8, bottom=8),
#                     # ===================
#                     # image_src = f"/home/mjay/Pictures/3d_neon_pink-2560x1440.jpg",
#                     # image_opacity=0.1,
#                     # image_fit='COVER',                                            # CONTAIN, COVER, FILL, FIT_HEIGHT, FIT_WIDTH, SCALE_DOWN
#                     # ===================
#                     width= self.width_stream,
#                     # width= 600,
#                     # height=750,
#                     # tooltip='Container',
#                     # scale=0.8,
#                     ##################### EFFECTS
#                     # gradient=ft.LinearGradient( begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=[ft.colors.BLACK87, ft.colors.BLACK87],),
#                     # gradient=ft.RadialGradient( colors=[ft.colors.YELLOW, ft.colors.BLUE],),
#                     ##################### WIDGETS
#                     content=ft.Column(
#                             scroll=True,
#                             spacing=0,
#                             run_spacing=0,
#                             expand_loose=True,

#                             controls = [

#                             ft.Markdown(
#                                 value = self.data_stream, # content = ft.Text(value="Compound button", size=12,),
#                                 # size=10            selectable=True,
#                                 extension_set=ft.MarkdownExtensionSet.COMMON_MARK, # COMMON_MARK ,GITHUB_FLAVORED ,GITHUB_WEB
#                                 # extension_set="gitHubWeb", GITHUB_FLAVORED
#                                 on_tap_link=lambda e: page.launch_url(e.data),
#                                 # code_theme="brown-paper",
#                                 code_theme='vs2015',

#                     # on_click=lambda _:print(_),   # on_hover=print('on click over'), on_long_press=print('long press'),
#         )]),)#<=== NOTE COMA <==> ERASE COMA IF MAKE 1 ERROR
#         return Drop_TextEditorStream
# ######## TextEditorStream = TextEditorStream(),# <======= Comma
class TextEditorTextStream(ft.Stack):
    # globalVar='Erase this test'

    def __init__(self,data_stream='Erase this test',width_stream=None ,header_code=''):
        super().__init__()
        # self.title='data'
        self.data_stream  = data_stream
        self.width_stream = width_stream
        self.header_code  = header_code
    def build(self):
        global Drop_TextEditorStream
        Drop_TextEditorStream=ft.Container(
                                    ##################### PROPERTY
                                    ##################### [rotate,offset] , [scale,aspect_ratio] , [visible,disabled]
                                    expand=True,
                                    expand_loose=True,
                                    ink           = False,                                                      # click effect ripple
                                    bgcolor       = ft.colors.WHITE12,
                                    padding       = ft.padding.all(0), # inside box                        # padding.only(left=8, top=8, right=8, bottom=8),
                                    margin        = ft.margin.all(0),  # outside box                       # margin.only (left=8, top=8, right=8, bottom=8),
                                    alignment     = ft.alignment.top_left,                                  # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right. posicionamiento adentro widget
                                    border_radius = ft.border_radius.all(24),                  # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                                    border=ft.border.all(2, ft.colors.BLACK),                     # ft.border.only(Left=8, top=8, right=8, bottom=8),
                                    # ===================
                                    # image_src = f"/home/mjay/Pictures/3d_neon_pink-2560x1440.jpg",
                                    # image_opacity=0.1,
                                    # image_fit='COVER',                                            # CONTAIN, COVER, FILL, FIT_HEIGHT, FIT_WIDTH, SCALE_DOWN
                                    # ===================
                                    width= self.width_stream,
                                    # width= 600,
                                    height=720,
                                    # tooltip='Container',
                                    # scale=0.8,
                                    ##################### EFFECTS
                                    # gradient=ft.LinearGradient( begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=[ft.colors.BLACK87, ft.colors.BLACK87],),
                                    # gradient=ft.RadialGradient( colors=[ft.colors.YELLOW, ft.colors.BLUE],),
                                    ##################### WIDGETS
                                    content=ft.Column(
                                            expand=True,
                                            expand_loose=True,
                                            scroll="HIDDEN",
                                            spacing=0,
                                            run_spacing=0,
                                            alignment=ft.MainAxisAlignment.CENTER,              # horizontal <=> START,CENTER,END SPACE_BETWEEN SPACE_AROUND SPACE_EVENLY
                                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,          # vertical       START,CENTER END

                                            controls = [
                                                        ft.TextField(
                                                        label=self.header_code,
                                                        # hint_text="INFO inside Box",
                                                        # counter_text="INFO down Box",
                                                        # suffix_text=".com"                           # "INFO right inside Box",
                                                        # ====================== EMOJI_EMOTIONS
                                                        # icon=ft.icons.EMOJI_EMOTIONS,                # Icon left  out    box
                                                        # prefix_icon=ft.icons.COLOR_LENS,             # Icon left  inside box
                                                        # suffix_icon=ft.icons.COLOR_LENS,             # Icon right inside box
                                                        # ================================
                                                        multiline=True,
                                                        # min_lines=1,
                                                        # max_lines=3,
                                                        # ======================
                                                        # disabled=True,
                                                        read_only=True,
                                                        # ====================== password
                                                        # password=True,
                                                        # can_reveal_password=True
                                                        # ====================== color
                                                        border=ft.InputBorder.NONE,              # border=ft.InputBorder.[NONE ,OUTLINE ,UNDERLINE]
                                                        # filled=True,
                                                        # ==========
                                                        # bgcolor=ft.colors.WHITE12,                               # inside box
                                                        # color=ft.colors.BLACK45,                                  # letter color
                                                        # focused_bgcolor='yellow',                     # inside box after click
                                                        # border_color='red',                           # border box
                                                        # focused_border_color='yellow'                 # border box after click
                                                        border_radius=8,                              # corner
                                                        # border_width=1,                               # border
                                                        # capitalization=True,
                                                        text_size=10,
                                                        # keyboard_type=ft.KeyboardType.URL                        # [MULTILINE,NUMBER,PHONE,DATETIME,EMAIL,URL,VISIBLE_PASSWORD,NAME,STREET_ADDRESS,NONE]
                                                        # text_align=ft.TextAlign.LEFT,
                                                        # # ft.Markdown(
                                                        #     # weight          = ft.FontWeight.BOLD,
                                                        #     # extension_set=ft.MarkdownExtensionSet.COMMON_MARK, # COMMON_MARK ,GITHUB_FLAVORED ,GITHUB_WEB
                                                        value = self.data_stream, # content = ft.Text(value="Compound button", size=12,),
                                                        #     # code_theme='vs2015',

                                                        #     # size=12,
                                                        # smart_quotes_type=True,

                                                        #     multiline=True,
                                                            )
                                                        ]

                        ),)#<=== NOTE COMA <==> ERASE COMA IF MAKE 1 ERROR
        return Drop_TextEditorStream
######## TextEditorStream = TextEditorStream(),# <======= Comma
class TreeViewTextEditor(ft.Stack):
    # globalVar='Erase this test'

    def __init__(self,data='Erase this test'):
        super().__init__()
        # self.title='data'
        self.title=data

        self.widget = MakeJasonFile()
    def build(self):
        global Drop_TextEditor
        # path = '/home/mjay/Desktop/git_hub/flet_box/test/test/test.md'

        # with open(path,'r') as f:
        #     self.data_stream = f.read()
        self.data_stream = ''
        self.text_path = ft.Container(
                    ##################### PROPERTY
                    ##################### [rotate,offset] , [scale,aspect_ratio] , [visible,disabled]
                    expand=True,
                    ink=False,                                                      # click effect ripple
                    bgcolor="#44CCCC00",                                            # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                    padding= ft.padding.all(0), # inside box                        # padding.only(left=8, top=8, right=8, bottom=8),
                    margin = ft.margin.only (left=8, top=0, right=0, bottom=0),  # outside box                       # margin.only (left=8, top=8, right=8, bottom=8),
                    alignment=ft.alignment.center,                                  # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right. posicionamiento adentro widget
                    # gradient=ft.LinearGradient( begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=[ft.colors.BLUE, ft.colors.YELLOW],),
                    # gradient=ft.RadialGradient( colors=[ft.colors.YELLOW, ft.colors.BLUE],),
                    ##################### WIDGETS
                    content=ft.Text(
                                # expand          = True,
                                # data            = 'value of the button',                                  # store data in the button
                                value           = "simple text", # content = ft.Text(value="Compound button", size=12,),
                                # tooltip         = 'ElevatedButton',
                                text_align        = ft.TextAlign.CENTER,                                    # LEFT (default),RIGHT,CENTER,JUSTIFY,START,END
                                # style           = ft.TextStyle(decoration=ft.TextDecoration.UNDERLINE ), # OVERLINE,
                                # weight          = ft.FontWeight.BOLD,                                    # NORMAL (default), BOLD, W_100, W_200,  W_300, W_400, W_500, W_600, W_700, W_800,W_900
                                # italic          = True,
                                font_family     = "Consolas", #"Consolas ,RobotoSlab
                                ##################### COLOR
                                # color           = 'yellow',  # text color
                                # bgcolor         = 'red',     # back color
                                ##################### ATTRIB
        ),)#<=== NOTE COMA <==> ERASE COMA IF MAKE 1 ERROR
        Drop_TextEditor=ft.Container(
                    ##################### PROPERTY
                    ##################### [rotate,offset] , [scale,aspect_ratio] , [visible,disabled]
                    expand=True,
                    bgcolor=ft.colors.BLACK,                                    # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                    padding= ft.padding.only (left=0, top=24, right=0, bottom=24),    # inside box                # padding.only(left=8, top=8, right=8, bottom=8),
                    margin = ft.margin.only (left=0, top=0, right=0, bottom=0),    #outside box                # margin.only (left=8, top=8, right=8, bottom=8),
                    alignment=ft.alignment.center,                            # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right.    posicionamiento adentro widget
                    ##################### WIDGETS
                    content=ft.Row(
                                    ##################### PROPERTY BOX
                                    expand=True,
                                    alignment=ft.MainAxisAlignment.CENTER,              # horizontal <=> START,CENTER,END SPACE_BETWEEN SPACE_AROUND SPACE_EVENLY
                                    vertical_alignment=ft.CrossAxisAlignment.CENTER,          # vertical       START,CENTER END
                                    ##################### LET MAKE SCROLL IN LONG QUANTITY
                                    scroll=True,                                              # center widget
                                    spacing=0,                                                # space widget left right
                                    run_spacing=0,                                            # space widget up down
                                    ##################### WIDGETS

                                    controls=[
                                                # TextEditorStream(data_stream=self.data_stream,width_stream=200),
                                                # TextEditorStream(data_stream=self.data_stream,width_stream=200),
                                                # TextEditorStream(data_stream=self.data_stream,width_stream=200),
                                                ft.Container(
                                                    # alignment=ft.alignment.center,                            # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right.    posicionamiento adentro widget

                                                    content= (ft.Column(
                                                                    alignment=ft.MainAxisAlignment.CENTER,              # horizontal <=> START,CENTER,END SPACE_BETWEEN SPACE_AROUND SPACE_EVENLY
                                                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,          # vertical       START,CENTER END

                                                                controls = [
                                                                            ft.Container(
                                                                                        ##################### PROPERTY
                                                                                        tooltip='UPDATE',
                                                                                        # expand=True,
                                                                                        ink=False,                                                # click effect ripple
                                                                                        bgcolor=ft.colors.GREEN_700,                                    # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                                                                                        padding= ft.padding.all(0),    # inside box                # padding.only(left=8, top=8, right=8, bottom=8),
                                                                                        margin = ft.margin.all(0),    #outside box                # margin.only (left=8, top=8, right=8, bottom=8),
                                                                                        alignment=ft.alignment.center,                            # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right.    posicionamiento adentro widget
                                                                                        border_radius= ft.border_radius.only(top_left=8, top_right=8, bottom_left=8, bottom_right=8),          # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                                                                                        width=30,
                                                                                        height=30,
                                                                                        content=ft.Icon(name=ft.icons.UPDATE_OUTLINED),
                                                                                        ##################### EVENTS
                                                                                    on_click=lambda _:self.update_text_editor(self.widget),                            # on_hover=print('on click over'), on_long_press=print('long press'),
                                                                            ),#<=== NOTE COMA
                                                                            ft.Container(
                                                                                        ##################### PROPERTY
                                                                                        # expand=True,
                                                                                        tooltip='EXIT',
                                                                                        ink=False,                                                # click effect ripple
                                                                                        bgcolor=ft.colors.RED_900,                                    # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                                                                                        padding= ft.padding.all(0),    # inside box                # padding.only(left=8, top=8, right=8, bottom=8),
                                                                                        margin = ft.margin.all(0),    #outside box                # margin.only (left=8, top=8, right=8, bottom=8),
                                                                                        alignment=ft.alignment.center,                            # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right.    posicionamiento adentro widget
                                                                                        border_radius= ft.border_radius.only(top_left=16, top_right=0, bottom_left=16, bottom_right=0),          # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                                                                                        width=30,
                                                                                        height=250,
                                                                                        content=ft.Icon(name=ft.icons.ARROW_LEFT),
                                                                                        ##################### EVENTS
                                                                                    on_click=lambda _:self.show_text_editor(),                            # on_hover=print('on click over'), on_long_press=print('long press'),
                                                                            ),#<=== NOTE COMA
                                                            ])),),
                                                ft.Container(
                                                        bgcolor=ft.colors.BLACK45,
                                                    content = ft.Column(
                                                                    controls=[
                                                                            # self.text_path,
                                                                            TextEditorTextStream(data_stream=self.data_stream,width_stream=180 , header_code = "\tIndex Code"),
                                                                                ],
                                                                        ),
                                                            ),
                                                ft.Container(
                                                        bgcolor=ft.colors.BLACK45,
                                                    content = ft.Column(
                                                                    controls=[
                                                                            # self.text_path,
                                                                            TextEditorTextStream(data_stream=self.data_stream,width_stream=840 , header_code = "\tAll code box"),
                                                                                ],
                                                                        ),
                                                            ),
                                                ft.Container(
                                                        bgcolor=ft.colors.BLACK45,
                                                    content = ft.Column(
                                                                    controls=[
                                                                            # self.text_path,
                                                                            TextEditorTextStream(data_stream=self.data_stream,width_stream=300 , header_code = "\tJson style box"),
                                                                                ],
                                                                        ),
                                                            ),
                                             ],),
                    ##################### EVENTS
                    # on_click=lambda _:print(_),                            # on_hover=print('on click over'), on_long_press=print('long press'),
        )#<=== NOTE COMA

        # print(Drop_TextEditor.content.controls[0].controls)
        # print(Drop_TextEditor.content.controls[1].controls[0].content.controls[0])
        # print(Drop_TextEditor.content.controls[2].controls[0].content.controls[0])

        return Drop_TextEditor

    def show_text_editor(self):
        self.widget_off = GLOBAL_VAR(get_global_var='TEXT_EDITOR_CONTAINER')
        self.widget_off.visible = False
        self.widget_off.update()

######## TextEditor = TextEditor(),# <======= Comma

# ######## TreeViewJsonFile = TreeViewJsonFile(),# <======= Comma
    def update_text_editor(self,widget):

        # build_json_file
        # INPUT DATA IN TEXT EDITOR
        build_json_file = widget.build_json_file(widget_show=GLOBAL_VAR(get_global_var='EXPORT_DATA_PHONE'))
        # print(Drop_TextEditor.content.controls[1].content.controls[0].data_stream)

        # FIRST
        Drop_TextEditor.content.controls[1].content.controls[0].controls[0].content.controls[0].value=build_json_file.get('second')
        Drop_TextEditor.content.controls[1].content.controls[0].controls[0].content.controls[0].update()

        # SECOND
        Drop_TextEditor.content.controls[2].content.controls[0].controls[0].content.controls[0].value=build_json_file.get('main_code')
        Drop_TextEditor.content.controls[2].content.controls[0].controls[0].content.controls[0].update()

        # SECOND
        Drop_TextEditor.content.controls[3].content.controls[0].controls[0].content.controls[0].value=build_json_file.get('thirds')
        Drop_TextEditor.content.controls[3].content.controls[0].controls[0].content.controls[0].update()


        # print(Drop_TextEditor.content.controls[2].content.controls[0].controls[0].content.controls[0])
        # print(Drop_TextEditor.content.controls[3].content.controls[0].controls[0].content.controls[0])


        # Drop_TreeView_text_editor.content.controls[0].value      = build_json_file
        # Drop_TreeView_text_editor.content.controls[0].size       = 11
        # Drop_TreeView_text_editor.content.controls[0].text_align = ft.TextAlign.LEFT
        # Drop_TreeView_text_editor.content.update()

#     def visible_view():
#         global visible
#         visible = True if not visible else False
#         Drop_TreeView_text_editor.visible=visible
#         Drop_TreeView_text_editor.update()

if __name__ == '__main__':
    def main(page: ft.Page):
        ######################
        # page.window_title_bar_hidden         = True
        # page.window_title_bar_buttons_hidden = True
        # page.window_focused                  = True
        # page.window_skip_task_bar    = True
        # page.window_frameless
        # print(dir(page))
        # page.window_frameless        = True
        # page.auto_scroll             = True #scroll_to()
        # page.fonts                   = {"RobotoSlab": "https://github.com/google/fonts/raw/main/apache/robotoslab/RobotoSlab%5Bwght%5D.ttf"}
        # page.splash                  = ft.Image(src=f"/home/mjay/Pictures/3d_neon_pink-2560x1440.jpg")
        # page.splash                    = True
        page.scroll                    = "AUTO" #AUTO ADAPTIVE ALWAYS HIDDEN
        page.vertical_alignment        = ft.MainAxisAlignment.CENTER
        page.horizontal_alignment      = ft.CrossAxisAlignment.CENTER
        ######################  COLOR
        page.theme_mode                = ft.ThemeMode.DARK         #ft.ThemeMode.LIGHT
        page.window_bgcolor            = ft.colors.RED_100
        # page.bgcolor                 = ft.colors.BLACK
        # page.window_bgcolor          =  ft.colors.RED
        # page.window_bgcolor          =  ft.colors.TRANSPARENT
        ###################### POSITION OF SC
        page.window_left               = 3
        page.window_top                = 3
        # page.window_center()
        ###################### SIZE
        page.window_height             = 650
        page.window_width              = 1200
        ######################
        # page.window_width            = 800
        # page.window_height           = 400
        ######################
        page.padding                   = 0
        page.spacing                   = 0
        # page.expand                    = True
        page.add(TreeViewTextEditor())
        ######################
    ft.app(target=main)
import flet as ft

class MarkDownEditor(ft.Stack):
    # globalVar='Erase this test'

    def __init__(self,theme_name='theme',value=''):
        super().__init__()
        self.theme_name = theme_name
        self.value = value
    def build(self):

        # path = './README.md'
        # path = './test.md'
        # path = './WIDGET.md'

        # themes = [
        # "a11y-dark","a11y-light","agate","an-old-hope","androidstudio","arduino-light","arta","ascetic","atelier-cave-dark",
        # "atelier-cave-light","atelier-dune-dark","atelier-dune-light","atelier-estuary-dark","atelier-estuary-light","atelier-forest-dark",
        # "atelier-forest-light","atelier-heath-dark","atelier-heath-light","atelier-lakeside-dark","atelier-lakeside-light","atelier-plateau-dark",
        # "atelier-plateau-light","atelier-savanna-dark","atelier-savanna-light","atelier-seaside-dark","atelier-seaside-light",
        # "atelier-sulphurpool-dark","atelier-sulphurpool-light","atom-one-dark-reasonable","atom-one-dark","atom-one-light",
        # "brown-paper","codepen-embed","color-brewer","darcula","dark","default","docco","dracula","far","foundation",
        # "github-gist","github (default)","gml","googlecode","gradient-dark","grayscale","gruvbox-dark","gruvbox-light",
        # "hopscotch","hybrid","idea","ir-black","isbl-editor-dark","isbl-editor-light","kimbie.dark","kimbie.light","lightfair",
        # "magula","mono-blue","monokai-sublime","monokai","night-owl","nord","obsidian","ocean","paraiso-dark","paraiso-light",
        # "pojoaque","purebasic","qtcreator_dark","qtcreator_light","railscasts","rainbow","routeros","school-book","shades-of-purple",
        # "solarized-dark","solarized-light","sunburst","tomorrow-night-blue","tomorrow-night-bright","tomorrow-night-eighties",
        # "tomorrow-night","tomorrow","vs","vs2015","xcode","xt256","zenburn"
        # ]
        # with open(path,'r') as f:
        #     md1 = f.read()

        Drop_MarkDownEditor=ft.Markdown(
            # md1,
            self.value,
            selectable=True,
            extension_set=ft.MarkdownExtensionSet.COMMON_MARK, # COMMON_MARK ,GITHUB_FLAVORED ,GITHUB_WEB
            # extension_set="gitHubWeb", GITHUB_FLAVORED
            on_tap_link=lambda e: page.launch_url(e.data),
            # code_theme="brown-paper",
            code_theme=self.theme_name,
            # expand=True
            )
        # Drop_MarkDownEditor.scale=0.8
        builder_mark_down = ft.Container(
                    ##################### PROPERTY COLUMN
                    ##################### [rotate,offset] , [scale,aspect_ratio] , [visible,disabled]
                    # expand=True,
                    ink=False,                                                      # click effect ripple
                    bgcolor=ft.colors.BLACK45,                                              # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                    padding= ft.padding.all(16),    # inside box                        # padding.only(left=8, top=8, right=8, bottom=8),
                    margin = ft.margin.all(8),    # outside box                       # margin.only (left=8, top=8, right=8, bottom=8),
                    alignment=ft.alignment.center,                                  # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right.    posicionamiento adentro widget
                    border_radius= ft.border_radius.all(30),                      # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                    content=ft.Column(
                        controls=[
                                    ft.Text(value=self.theme_name),
                                    Drop_MarkDownEditor,
                                 ],
                    ),#<=== NOTE COMA [NOTE]                     for x in range(1,50): widget.content.controls.append(ft.ElevatedButton("press buttom",tooltip='buttom'))
                    ##################### EVENTS
                    # on_click=lambda _:print(_),                            # on_hover=print('on click over'), on_long_press=print('long press'),
        )#<=== NOTE COMA


        return builder_mark_down
######## MarkDownEditor = MarkDownEditor(),# <======= Comma
def main(page: ft.Page):
    ###################### CONFIGURATION
    # page.title = "Containers - clickable and not"
    # page.window_title_bar_hidden = True
    # page.window_frameless = True
    # page.window_focused=True
    page.scroll=True
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    ######################  COLOR
    page.theme_mode = ft.ThemeMode.DARK         #ft.ThemeMode.LIGHT
    # page.bgcolor = ft.colors.TRANSPARENT
    # page.window_bgcolor =  ft.colors.TRANSPARENT
    ###################### POSITION OF SC
    page.window_left = 8
    page.window_top = 8
    # page.window_center()
    ###################### SIZE
    page.window_height=640
    page.window_width=650
    page.padding=8
    page.spacing=8
    page.expand=True
    ######################
    MarkDown_Editor = MarkDownEditor
    screen_1=ft.Container(
                    padding   = ft.padding.all(8),    # inside box
                    margin    = ft.margin.all(0),     # outside box
                    alignment = ft.alignment.center,
                    width     = 800,
                    # height  = 150,
                    # tooltip = 'Container',
                    ##################### WIDGETS
                    content=ft.Column(
                        ),
                    ##################### EVENTS
                    # on_click=lambda _:print(_),                        # on_hover=print('on click over'), on_long_press=print('long press'),
                )

    themes = [
        "a11y-dark","a11y-light","agate","an-old-hope","androidstudio","arduino-light","arta","ascetic","atelier-cave-dark",
        "atelier-cave-light","atelier-dune-dark","atelier-dune-light","atelier-estuary-dark","atelier-estuary-light","atelier-forest-dark",
        "atelier-forest-light","atelier-heath-dark","atelier-heath-light","atelier-lakeside-dark","atelier-lakeside-light","atelier-plateau-dark",
        "atelier-plateau-light","atelier-savanna-dark","atelier-savanna-light","atelier-seaside-dark","atelier-seaside-light",
        "atelier-sulphurpool-dark","atelier-sulphurpool-light","atom-one-dark-reasonable","atom-one-dark","atom-one-light",
        "brown-paper","codepen-embed","color-brewer","darcula","dark","default","docco","dracula","far","foundation",
        "github-gist","github (default)","gml","googlecode","gradient-dark","grayscale","gruvbox-dark","gruvbox-light",
        "hopscotch","hybrid","idea","ir-black","isbl-editor-dark","isbl-editor-light","kimbie.dark","kimbie.light","lightfair",
        "magula","mono-blue","monokai-sublime","monokai","night-owl","nord","obsidian","ocean","paraiso-dark","paraiso-light",
        "pojoaque","purebasic","qtcreator_dark","qtcreator_light","railscasts","rainbow","routeros","school-book","shades-of-purple",
        "solarized-dark","solarized-light","sunburst","tomorrow-night-blue","tomorrow-night-bright","tomorrow-night-eighties",
        "tomorrow-night","tomorrow","vs","vs2015","xcode","xt256","zenburn"
        ]

    path = './test.md'
    with open(path,'r') as f:
        md1 = f.read()

    for _ in themes:
        screen_1.content.controls.append(MarkDownEditor(theme_name=_,value=md1))

    page.add(screen_1)
    page.update()

if __name__ == '__main__':
    ft.app(target=main)
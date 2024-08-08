import flet as ft

def json_style(code):
    tmp_json_style = {

    "_2921": {
        "alignment": {"x":0,"y":0},
        "bgcolor": "Black38",
        "border": {"l":{"w":0,"c":"transparent"},"t":{"w":0,"c":"transparent"},"r":{"w":0,"c":"transparent"},"b":{"w":0,"c":"transparent"}},
        "ink": "true",
        "ink_color": "yellow",
        # "n": "content",
        # "on_click": "true",
        "on_hover": "false",
        "padding": {"l":6,"t":6,"r":6,"b":6},
        "tooltip": "Column: 1"
    },
    "_2922": {
        "horizontal_alignment": "center",
        # "n": "content",
        "scroll": "ALWAYS"
    },
    "_2925": {
        "alignment": {"x":0,"y":0},
        "bgcolor": "transparent",
        "border": {"l":{"w":0,"c":"transparent"},"t":{"w":0,"c":"transparent"},"r":{"w":0,"c":"transparent"},"b":{"w":0,"c":"transparent"}},
        "ink": "true",
        "ink_color": "red",
        "margin": {"l":0,"t":0,"r":0,"b":0},
        # "n": "content",
        # "on_click": "true",
        "on_hover": "false",
        "padding": {"l":6,"t":6,"r":6,"b":6},
        "tooltip": "Text: 2"
    },
    "_2926": {
        # "n": "content",
        "size": "10",
        "tooltip": "Text",
        "value": "Ready to make your first app!!nBegin your journey..."
    },
    "_2929": {
        "alignment": {"x":0,"y":0},
        "bgcolor": "transparent",
        "border": {"l":{"w":0,"c":"transparent"},"t":{"w":0,"c":"transparent"},"r":{"w":0,"c":"transparent"},"b":{"w":0,"c":"transparent"}},
        "ink": "true",
        "ink_color": "red",
        "margin": {"l":0,"t":0,"r":0,"b":0},
        # "n": "content",
        # "on_click": "true",
        "on_hover": "false",
        "padding": {"l":6,"t":6,"r":6,"b":6},
        "tooltip": "Text Field: 3"
    },
    "_2930": {
        "border_color": "white",
        "border_radius": {"bl":30,"br":30,"tl":30,"tr":30},
        "content_padding": {"l":16,"t":16,"r":16,"b":16},
        "cursor_height": "20",
        "focused_border_color": "red",
        "height": "32",
        "label": "what's your name ?",
        # "n": "content",
        "text_size": "12",
        "tooltip": "TextField",
        "width": "240"
    },
    "_2933": {
        "alignment": {"x":0,"y":0},
        "bgcolor": "transparent",
        "border": {"l":{"w":0,"c":"transparent"},"t":{"w":0,"c":"transparent"},"r":{"w":0,"c":"transparent"},"b":{"w":0,"c":"transparent"}},
        "ink": "true",
        "ink_color": "red",
        "margin": {"l":0,"t":0,"r":0,"b":0},
        # "n": "content",
        # "on_click": "true",
        "on_hover": "false",
        "padding": {"l":6,"t":6,"r":6,"b":6},
        "tooltip": "Elevated Button: 4"
    },
    "_2934": {
        "height": "28",
        # "n": "content",
        # "style": {"elevation":20},
        "text": "Accept",
        "tooltip": "ElevatedButton"
    }
}
    return tmp_json_style.get(code)

class CustomPage(ft.Container):
    def __init__(self):
        super().__init__()

        dict_keys: dict = json_style('_2921')
        self: list  = [self.__setattr__(_ , dict_keys.get(_)) for _ in dict_keys]

    def build(self):
        self.content = ft.Container(
                                # **json_style('_2921'),
                                content = ft.Column(
                                            **json_style('_2922'),
                                            controls = [
                                                    ft.Container(
                                                            **json_style('_2925'),
                                                            content = ft.Text(
                                                                    **json_style('_2926'),
                                                            ),),
                                                    ft.Container(
                                                            **json_style('_2929'),
                                                            content = ft.TextField(
                                                                    **json_style('_2930'),
                                                            ),),
                                                    ft.Container(
                                                            **json_style('_2933'),
                                                            content = ft.ElevatedButton(
                                                                    **json_style('_2934'),
                                                            ),),
                                    ],),) # <<< LAYER 0 END BRAKETS


def main(page: ft.Page):
    page.scroll               =True
    page.vertical_alignment   = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode           = ft.ThemeMode.DARK         #ft.ThemeMode.LIGHT
    page.window_left          = 8
    page.window_top           = 8
    # page.window_center()
    page.window_height        =640
    page.window_width         =320
    page.padding              =8
    page.spacing              =8
    # page.expand             =True
    ######################

    screen_1=CustomPage()


    page.add(screen_1)
    page.update()

if __name__ == '__main__':
    ft.app(target=main)
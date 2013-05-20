import flet as ft
import os


click_avalidation: bool = False

class PhotoSelection(ft.Container):

    def __init__(self,photo_selection: str=''):
        super().__init__()

        self.photo_selection=photo_selection
        self.width  = 80
        self.height = 80
        self.border_radius= ft.border_radius.all(24)

        self.shadow = ft.BoxShadow(
                           spread_radius = 1,
                           blur_radius   = 16,
                           color         = ft.colors.with_opacity(1,ft.colors.BLACK12),
                           offset        = ft.Offset(0, 0),
                           blur_style    = ft.ShadowBlurStyle.OUTER,
                     )
    def build(self):
        self.container = ft.Container(
                                image_fit =    'COVER',
                                image_src =    self.photo_selection,
                                padding   =    ft.padding.all(0),
                                margin    =    ft.margin.all(0),
                                alignment =    ft.alignment.center,
                                border_radius= ft.border_radius.all(24),
                                # border    =    ft.border.all(2, ft.colors.BLACK38),
                                on_hover  =    lambda _: self.active_border_color(border_container = self.container),
                        )

        self.content  = self.container
        self.on_click = lambda _:print(self.photo_selection)

    def active_border_color(self,border_container):
        border_container.border = ft.border.all(2, ft.colors.TRANSPARENT) if border_container.border == ft.border.all(2, ft.colors.WHITE54) else ft.border.all(2, ft.colors.WHITE54)
        border_container.update()

class Screen_photo_selection(ft.Container):

    def __init__(self,data='Erase this test'):
        super().__init__()

        self.padding  = ft.padding.only(left=0,top=2,bottom=2,right=0)
        self.margin   = ft.margin.all(0)    #outside box
        self.alignment= ft.alignment.top_center
        self.width    = 600
        self.height   = 300
        # self.bgcolor  = ft.colors.BLACK45
        self.border   = ft.border.all(1, ft.colors.WHITE38)
        self.border_radius = 30
        self.gradient = ft.LinearGradient( begin = ft.alignment.top_center,
                                           end   = ft.alignment.center_left,
                                           colors= [
                                                    ft.colors.with_opacity(0.7,ft.colors.TEAL_400),
                                                    ft.colors.BLACK26,
                                                    ],)
        self.shadow = ft.BoxShadow(
                                   spread_radius= 1,
                                   blur_radius  = 18,
                                   # color        = ft.colors.with_opacity(0.3,ft.colors.TEAL_400),
                                   offset       = ft.Offset(0, 0),
                                   blur_style   = ft.ShadowBlurStyle.OUTER,
                             )
        # self.blur = (12,12)
    def build(self):

        list_started = False
        screen_1=ft.Row(
                        scroll  = True,
                        wrap    = True,
                        spacing = 4,
                        run_spacing=4,
                        controls= [
                                  ],
                        )
        self.content =ft.Container(
                    # bgcolor  = ft.colors.RED,
                    border_radius = 20,
                    padding  = ft.padding.all(0),
                    margin   = ft.margin.all(0),
                    on_hover= lambda _: self.validate_click(),
                   content=screen_1,

                   )
        # self.content=screen_1

        current_dir_path = os.path.relpath(path='./test/proyect_name/proyect_name/assets')
        basename_dict    = self.selection_photo_files(path_to_check_filename=current_dir_path)

        for _ in basename_dict:
            tmp_path  = basename_dict.get(_)
            full_path = os.path.join(current_dir_path, tmp_path)
            screen_1.controls.append(PhotoSelection(photo_selection=full_path))

    def validate_click(self):
        global click_avalidation

        if click_avalidation:
            click_avalidation = False
            print('do the code after leave the box')

        else:
            click_avalidation = True


        print(click_avalidation)

    def selection_photo_files(self,path_to_check_filename: str=""):
        all_files_list = os.listdir(path_to_check_filename)
        basename_dict: dict={}

        for full_name in all_files_list:
            curren_name = os.path.splitext(full_name)[0]
            basename_dict[curren_name]=full_name

        return basename_dict

if __name__ == '__main__':

    def main(page: ft.Page):
        page.vertical_alignment   = ft.MainAxisAlignment.CENTER
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        page.theme_mode  = ft.ThemeMode.DARK         #ft.ThemeMode.LIGHT
        page.window_left = 0
        page.window_top  = 0
        page.window_height=600
        page.window_width=800
        page.padding=0
        page.spacing=0
        page.add(Screen_photo_selection())
        page.update()

    ft.app(
            target=main,
            )
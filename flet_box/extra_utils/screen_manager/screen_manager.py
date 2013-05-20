from settings_screens import GLOBAL_VAR
import flet as ft
import os
import json

CURRENT_PATH = os.path.join('./flet_box/extra_utils/screen_manager','screens.js')

main_screen_dict = dict()

class NameScreen(ft.Container):
    def __init__(self, id_name: str='0'):
        super().__init__()
        self.id_name       = id_name
        self.visible       = False
        self.border_radius = ft.border_radius.all(30)
        self.bgcolor       = ft.colors.BLACK45
        self.padding       = ft.padding.all(0)
        self.margin        = ft.margin.all(0)
        self.alignment     = ft.alignment.center
        self.border        = ft.border.all(2, ft.colors.BLACK)
        self.blur          = (12,12)
        # self.on_click    = lambda _:self.escape_data_in_sqlite()
        self.right  = 0
        self.left   = 0
        self.top    = 0
        self.bottom = 0


    def build(self):

        self.content = ft.Container(
                    ink       = False,
                    padding   = ft.padding.all(16),
                    margin    = ft.margin.all(8),
                    alignment = ft.alignment.center,
                    # width     = 380,
                    # height    = 380,
                    gradient  = ft.RadialGradient( colors=[ft.colors.BLACK26, ft.colors.BLUE_900 ,ft.colors.BLACK26,ft.colors.BLACK12],),
                    content = ft.Container(
                                padding       = ft.padding.all(20),
                                margin        = ft.margin.all(0),
                                bgcolor       = ft.colors.BLACK26,
                                blur          = (32,32),
                                width         = 348,
                                height        = 348,
                                border_radius = ft.border_radius.all(32),
                                border        = ft.border.all(0.2, ft.colors.BLUE_900),
                                content = ft.Column(
                                    alignment            = ft.MainAxisAlignment.SPACE_AROUND,
                                    horizontal_alignment = ft.CrossAxisAlignment.CENTER,
                                    spacing              = 8,
                                    run_spacing          = 8,
                                    controls=[
                                        ft.Container(
                                                    padding   = ft.padding.all(8),
                                                    margin    = ft.margin.all(8),    #outside box
                                                    alignment = ft.alignment.center_left,
                                                    content   = ft.Text(
                                                                        value       = "Screen name\nwill be save in database",
                                                                        color       = ft.colors.WHITE70,
                                                                        size        = 16,
                                                                        text_align  = ft.TextAlign.LEFT,
                                                                        weight      = ft.FontWeight.BOLD,
                                                                        font_family = "Consolas",
                                                                        ),
                                        ),#<=== NOTE COMA

                                        ft.Container(
                                            content = ft.TextField(
                                                    smart_quotes_type    = True,
                                                    label                = "Name",
                                                    counter_text         = "Please give short name like: main_1...\n",
                                                    value                = "",
                                                    autofocus            = True,
                                                    bgcolor              = ft.colors.BLACK26,
                                                    border               = ft.InputBorder.OUTLINE,
                                                    border_color         = ft.colors.BLACK45,
                                                    focused_border_color = ft.colors.YELLOW_900 ,
                                                    border_radius        = 18,
                                                    text_align           = ft.TextAlign.LEFT,

                                                on_change                = lambda _:self.save_data_in_sqlite(screen_name = self.content.content.content.controls[1].content)
                                                ),),
                                        ft.Container(
                                            content = ft.TextField(
                                                    smart_quotes_type    = True,
                                                    label                = "Description",
                                                    counter_text         = "Small description..\n",
                                                    value                = "",
                                                    bgcolor              = ft.colors.BLACK26,
                                                    border               = ft.InputBorder.OUTLINE,
                                                    border_color         = ft.colors.BLACK45,
                                                    focused_border_color = ft.colors.YELLOW_900 ,
                                                    border_radius        = 18,
                                                    text_align           = ft.TextAlign.LEFT,
                                                on_change                = lambda _:self.save_data_in_sqlite(description= self.content.content.content.controls[2].content)

                                                    ),),

                                        ft.Row(
                                            vertical_alignment =ft.CrossAxisAlignment.CENTER,
                                            alignment          = ft.MainAxisAlignment.CENTER,
                                            controls = [
                                                        ft.Container(
                                                                    content = ft.ElevatedButton("Accept" ,
                                                                                                icon       = ft.icons.SAVE_OUTLINED,
                                                                                                # icon_color = ft.colors.YELLOW_900,
                                                                                                bgcolor    = ft.colors.GREEN_900,
                                                                                                on_click   = lambda _:self.save_data_in_sqlite(check_data=True),
                                                                                                )),
                                                        ft.Container(
                                                                    content = ft.ElevatedButton("Cancel" ,
                                                                                                icon       = ft.icons.CANCEL,
                                                                                                bgcolor    = ft.colors.RED_900,
                                                                                                # icon_color = ft.colors.YELLOW_900,
                                                                                                on_click   = lambda _:self.escape_data_in_sqlite(),
                                                                                                )),
                                         ]),],),
                    ),
        )#<=== NOTE COMA

    def colored(self):
        self.ink_color = 'Red'

    def escape_data_in_sqlite(self):
        name_screen.visible = False
        name_screen.update()


    def save_data_in_sqlite(self,check_data = False ,screen_name: str=''  ,description: str=''):

        if screen_name:
            # IF NOT EMPTY INPUT SCREEN NAME
            GLOBAL_VAR(set_global_var={'screen_name':{'widget':screen_name,'value':screen_name.value}})

        if description:
            # IF NOT EMPTY INPUT SCREEN DESCRIPTION

            GLOBAL_VAR(set_global_var={'description':{'widget':description,'value':description.value}})

        if check_data:

            #: WIDGET NAME
            self.widget_name  = GLOBAL_VAR(get_global_var='screen_name')
            if self.widget_name:

                #: SCREEN NAME
                self.data_name    = self.widget_name.get('value')

                #: SCREEN VALUE
                self.widget_value = GLOBAL_VAR(get_global_var='description')

                #: IF IS EMPTY DESCRIPTION
                description = 'description' if self.widget_value == None else self.widget_value.get('value')
                if description == "": description = 'description'

                #: SET VISIBLE BOX
                name_screen.visible = False
                name_screen.update()

                #: ADDING WIDGETS TO GRIDVIEW
                data = GLOBAL_VAR(get_global_var='javier').get('GridView')
                data.controls.append(ScreenContainer(
                                                    id_name = self.data_name,
                                                    id_description = description,
                                                    ))
                data.update()

                #: ADD TO LIST TO GET INDEX OF SELECTED TO ERASE
                update_list = GLOBAL_VAR(add_list=self.data_name)
                main_screen_dict.update({self.data_name:description})

                # #: READ AND DELETE AND UPDATE
                def crud_data(type_file: str='read_update'):

                    with open(CURRENT_PATH,'r') as f:
                        #: READ DATA FROM JSON
                        load_data = json.loads(f.read())

                        # UPDATE NEW DATA
                        with open(CURRENT_PATH,'w+') as new:
                            load_data.update(type_file)
                            data = json.dumps(load_data,indent=4 )
                            new.write(data)

                            #: RUN ONLY IN PRODUCTION
                            # print(load_data.update(dict(type_file)))
                            # print(type_file)

                crud_data(type_file=main_screen_dict)


class ScreenContainer(ft.Container):
    def __init__(   self,
                    id_name: str           =' screen_1',
                    id_description: str    = 'description',
                    container_editor: bool = False
                    ):
        super().__init__()

        #: VALIDATION
        self.container_editor = container_editor
        self.id_name          = id_name
        self.id_description   = id_description

        self.border_radius = ft.border_radius.all(30)
        self.ink           = True
        self.ink_color     = 'Red'
        self.bgcolor       = ft.colors.BLACK45
        self.padding       = ft.padding.all(0)
        self.margin        = ft.margin.only(left=0,right=0,bottom=12,top=12)
        self.alignment     = ft.alignment.center
        self.border_radius = ft.border_radius.all(30)
        self.border        = ft.border.all(3, ft.colors.BLACK45)
        self.gradient      = ft.LinearGradient(
                                                begin  = ft.alignment.top_center,
                                                end    = ft.alignment.bottom_center,
                                                colors = [ft.colors.BLACK,ft.colors.BLACK,ft.colors.BLACK54, ft.colors.BLACK12],)

        #: SIZE OF CARD SCREENS
        self.width         = 130
        self.height        = 170

    def build(self):
        #: EVENT

        if not self.container_editor:
            self.content  = ft.Column(
                                controls = [

                                ft.Container(
                                        alignment = ft.alignment.top_right,
                                        padding   = ft.padding.only(left=0,right=4,bottom=0,top=6),
                                        margin    = ft.margin.only(left=0,right=4,bottom=0,top=6),

                                        content   = ft.IconButton(
                                                                icon       = ft.icons.RECYCLING,
                                                                icon_size  = 19,
                                                                icon_color = ft.colors.RED_600,
                                                                bgcolor    = ft.colors.BLACK54,
                                                                on_click   = lambda _:self.delete_id_name(self.id_name),
                                                             ),
                                            ),

                                ft.Container(
                                        padding   = ft.padding.all(0),
                                        margin    = ft.margin.only(left=12,right=8,top=0,bottom=0),
                                        alignment = ft.alignment.top_left,
                                        content   = ft.Text(
                                                            value       = self.id_name,
                                                            color       = ft.colors.YELLOW_900,
                                                            size        = 16,
                                                            text_align  = ft.TextAlign.LEFT,
                                                            weight      = ft.FontWeight.BOLD,
                                                            font_family = "Consolas",
                                                             ),
                                            ),

                                ft.Container(

                                        padding   = ft.padding.all(0),
                                        margin    = ft.margin.only(left=12,right=8,top=0,bottom=0),
                                        alignment = ft.alignment.top_left,
                                        content   = ft.Text(
                                                            value       = self.id_description,
                                                            color       = ft.colors.BLUE_ACCENT_200,
                                                            size        = 12,
                                                            text_align  = ft.TextAlign.LEFT,
                                                            weight      = ft.FontWeight.BOLD,
                                                            font_family = "Consolas",
                                                             ),
                                            ),
                                        ]
                            )
        else:
            self.content  = ft.Container(
                                        alignment = ft.alignment.center,
                                        padding=ft.padding.all(8),
                                        content = ft.Column(
                                                # scroll="HIDDEN",
                                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,              # horizontal <=> START,CENTER,END SPACE_BETWEEN SPACE_AROUND SPACE_EVENLY
                                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                                controls = [
                                                            ft.Container(height=24),
                                                            ft.Icon(
                                                                    name=ft.icons.ADD,
                                                                    color=ft.colors.BLUE_900,

                                                                    ),

                                                            ft.ElevatedButton(
                                                                            text='CLEAN',
                                                                            bgcolor=ft.colors.RED_900,
                                                                            on_click=lambda _:self.remove_all(),
                                                                            ),
                                                            ],
                                                ),
                                        )
            self.on_click = lambda _:self.show_screen_name()

    def show_screen_name(self):
        # ONLY FUNCTIONALITY IS SHOW BOX INPUT DIALOG
        name_screen.visible = True
        name_screen.update()

    def colored(self):
        self.ink_color = 'Red'

    def remove_all(self):
        with open(CURRENT_PATH,'w') as f:
            f.write('{}')

        # GLOBAL_VAR(empty_list=True)
        data = GLOBAL_VAR(get_global_var='javier').get('GridView')
        data_ = data.controls
        data.controls = data_[:2]
        data.update()

        # RUN ONLY IN PRODUCTION
        # print(data_)

    def delete_id_name(self,id_name):
        # GET INDEX NUMBER FROM LIST TO DELETE IN CONTROLS
        my_list = GLOBAL_VAR(get_index_list=id_name)

        # EVOIT ERASE MAIN SCREEN
        if id_name == 'main_screen':
            return

        # ERASE FROM CONTROL WITH CURRENT SELECTED WIDGET
        data = GLOBAL_VAR(get_global_var='javier').get('GridView')
        data.controls.pop(my_list.index(id_name))
        data.update()

        # UPDATE LIST
        my_list = GLOBAL_VAR(remove_list=my_list.index(id_name))

        #: READ AND DELETE AND UPDATE
        def crud_data(type_file: str='read_update'):
            with open(CURRENT_PATH,'r') as f:
                load_data = json.loads(f.read())
                # DELETE FROM JSON FILE
                del load_data[id_name]
                # UPDATE NEW DATA
                with open(CURRENT_PATH,'w') as new:
                    data = json.dumps(load_data,indent=4 )
                    new.write(data)
                # print(load_data)

        crud_data(type_file='read_update')

        #: RUN ONLY IN PRODUCTION
        #: CHECK ALL LIST
        # data = GLOBAL_VAR(get_list= True)
        # print(data)

class ScreenManager(ft.Stack):
    def __init__(self,data='Erase this test'):
        super().__init__()
        self.ink           = False
        self.bgcolor       = ft.colors.BLACK45
        self.padding       = ft.padding.all(8)
        self.margin        = ft.margin.all(8)
        self.alignment     = ft.alignment.center
        self.border_radius = ft.border_radius.all(30)
        self.border        = ft.border.all(2, ft.colors.BLACK)

        # REMEMBER SAVE IN DATABASE
        global name_screen

        name_screen = NameScreen()
    def build(self):
        self.gird_view = ft.Container( #: GRID VIEW
                                    bgcolor       = ft.colors.BLACK54,
                                    height        = 520,
                                    width         = 1185,
                                    border_radius = ft.border_radius.all(30),
                                    border        = ft.border.all(2, ft.colors.BLACK),
                                    padding       = ft.padding.only(
                                                                    left   = 12,
                                                                    right  = 12,
                                                                    top    = 0,
                                                                    bottom = 0,
                                                                    ),

                                content= ft.Row(
                                        wrap        = True,
                                        scroll      = 'HIDDEN',
                                        run_spacing = 2,

                                   controls = [
                                                #: ADD CONTAINER EDITOR
                                                ScreenContainer(id_name='screen_editor' ,container_editor=True),

                                                #: MAIN SCREEN
                                                ScreenContainer(id_name='main_screen'),
                                             ],
                        ))

        #: LOAD JSON FILE
        def load_json(controls_list: list=[]):

            with open(CURRENT_PATH,'r+') as f:
                load_data = json.loads(f.read())
                controls_list.controls += [ ScreenContainer(id_name=_ ) for _ in load_data]

                for _ in load_data:
                    GLOBAL_VAR(add_list=_)

        load_json(controls_list=self.gird_view.content)


        self.footer_bar = ft.Container( #: FOOTER BAR
                            ink           = False,
                            bgcolor       = ft.colors.BLUE_900,
                            padding       = ft.padding.all(8),
                            margin        = ft.margin.all(8),    #outside box
                            alignment     = ft.alignment.center,
                            border_radius = ft.border_radius.all(30),
                            border        = ft.border.all(4, ft.colors.BLACK),

                        content=ft.Row(

                                controls=[
                                            ft.ElevatedButton("Delete",   tooltip='buttom'),
                                            ft.ElevatedButton("press row",tooltip='buttom'),
                                            ft.ElevatedButton("press row",tooltip='buttom'),
                                         ],),

        )#<=== NOTE COMA
        self.controls = [

                    ft.Container(
                            ink       = False,
                            padding   = ft.padding.all(0),
                            margin    = ft.margin.all(0),
                            alignment = ft.alignment.center,

                        content = ft.Column(
                                alignment            = ft.MainAxisAlignment.SPACE_BETWEEN,
                                horizontal_alignment = ft.CrossAxisAlignment.CENTER,

                                controls=[
                                            self.gird_view,
                                            # self.footer_bar,
                                         ],
                            ),
                        ),
                        name_screen,
                        ]

        GLOBAL_VAR(set_global_var={
                                    'javier':{
                                            'GridView':self.gird_view.content
                                  }})


if __name__ == '__main__':
    def main(page: ft.Page):

        page.vertical_alignment   = ft.MainAxisAlignment.CENTER
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        page.theme_mode           = ft.ThemeMode.DARK         #ft.ThemeMode.LIGHT
        page.window_left          = 8
        page.window_top           = 8
        page.window_height        = 640
        page.window_width         = 1180
        page.padding              = 8
        page.spacing              = 8
        page.expand               = True
        screen_1                  = ScreenManager()
        page.add(screen_1)
        page.update()
    ft.app(
            target=main,
            )
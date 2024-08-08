import flet as ft
import os
import json

from .settings_screens import SCREEN_GLOBAL_VAR
from ..settings_var.settings_widget import GLOBAL_VAR

#: VERY IMPORTANT IT'S MAIN PHONE THAT WILL CONTENT ALL SCREENS
from extra_utils.phone_container.widget_phone_editor import Build_Phone_Editor

all_screens_in_app: dict = {

                            }


# tmp_screen = Build_Phone_Editor(color_data='Blue')

# row_box_content_phone = GLOBAL_VAR(get_global_var='row_phone')
# tmp_new_phone = Build_Phone_Editor(color_data=ft.colors.TRANSPARENT).build()        #: ADD SCREEN PHONE IN DICT all_screens_in_app
# row_box_content_phone.controls.append(tmp_new_phone)                    #: ADD PHONE inside row_box_content_phone
# GLOBAL_VAR(set_global_var= {'main_screen':row_box_content_phone.controls[0]})

# print(row_box_content_phone)


def screen_manager(
                   add_screen:    str = "",
                   delete_screen: str = "" ,
                   selected_screen: str = "" ,
                   load_screen:   str = "",
                   set_screen:    str = "",
                   get_screen:    str = "",
                   clear_screen: bool = False,
                   ):

    #: THIS METOD WILL MANAGE ALL SCREENS INSIDE LET'US MODIFY EXACLTY SELECTED SCREEN
    global all_screens_in_app
    if add_screen:
        """
        add_screen var is sleceted widget name in screen manager buton on menu fotter bar

        1. take name snew screen
        2. add new screen inside row_box_content_phone
        3. row_box_content_phone update
        3. add to global var dict
        """
        tmp_new_screen_name   = add_screen                                      #: take only name of new screen
        row_box_content_phone = GLOBAL_VAR(get_global_var='row_phone')

        # ============================== SCREEN PHONE IN DICT ====================================
        #: ADD SCREEN PHONE IN DICT all_screens_in_app
        tree_view_new_phone = Build_Phone_Editor(
                                                 color_data     = ft.colors.TRANSPARENT,
                                                 )

        tmp_new_phone = tree_view_new_phone.build()          #: ADD SCREEN PHONE IN DICT all_screens_in_app
        row_box_content_phone.controls.append(tmp_new_phone) #: ADD PHONE inside row_box_content_phone
        row_box_content_phone.update()
        # ========================================================================================

        #: ADD SCREEN PHONE IN DICT DATA_GLOBAL
        #: PATH extra_utils/settings_var/settings_widget.py
        #: WIDGET AFTER PASS TO ROW GET ID
        GLOBAL_VAR( set_global_var= {tmp_new_screen_name:tmp_new_phone})


        #: HIDE NEW SCREEN CONTAINER BOX
        tmp_new_phone.visible = False
        tmp_new_phone.update()

        #: HIDE SCREEN MANAGER CONTAINER BOX
        show_screen_manager = GLOBAL_VAR(get_global_var='SCREEN_CONTAINER')
        show_screen_manager.visible = False
        show_screen_manager.update()

        # ========================================================================================
        #: CREATE NEW SCREEN IN ALL SCREENS DICT VERY IMPORTATN CONTAIN ALL SCREENS IN
        current_screen_id = GLOBAL_VAR(get_global_var='SELECTED_SCREEN').uid
        GLOBAL_VAR(set_global_var = {'ALL_SCREEN_IN_DICT':{current_screen_id: dict() }})
        # ========================================================================================

    elif delete_screen:
        #: DELETE SCREEN PHONE IN DICT SCREENS
        del all_screens_in_app[delete_screen]

    elif selected_screen:
        #: ROW_PHONE IT'S MAIN ROW THAT HAVE PHONE WIDGET INSIDE WILL BE HOT RELOAD EVERY TIME WE CALL
        #: THAT'S WHY I WILL PAS TO A GLOVAL VAR NAME "SCREEN_CONTAINER"

        #: ROW_PHONE IT'S MAIN ROW THAT HAVE PHONE WIDGET INSIDE WILL BE HOT RELOAD EVERY TIME WE CALL
        #: THAT'S WHY I WILL PAS TO A G
        # GLOVAL VAR NAME "SCREEN_CONTAINER"

        row_box_content_phone = GLOBAL_VAR(get_global_var='row_phone')
        tmp_new_screen_name = selected_screen




        #: HIDE OLD SCREEN CONTAINER BOX
        old_selected_screen = GLOBAL_VAR(get_global_var='SELECTED_SCREEN')
        new_selected_screen = GLOBAL_VAR(get_global_var=tmp_new_screen_name)

        #: SWITCH VISIBLE ON OFF BETEWNS SCREENS
        old_selected_screen.visible, new_selected_screen.visible = new_selected_screen.visible ,old_selected_screen.visible
        # old_selected_screen.visible = True
        # new_selected_screen.visible = True

        tab_one_confic_container = GLOBAL_VAR(get_global_var='CONFIG_TABS_PHONE')
        tab_one = tab_one_confic_container.content.controls
        #: TAB 0 NAME COLOR PHONE
        color_phone           = tab_one[0]
        color_phone_controls  = color_phone.controls[0].content.controls[1].content
        #: TAB 0 NAME IMAGE PHONE
        image_phone           = tab_one[1]
        image_phone_controls  = image_phone.controls[0].content.controls[1].content
        #: TAB 0 NAME COLUMN PHONE
        column_phone          = tab_one[2]
        column_phone_controls = column_phone.controls[0].content.controls[1].content

        def update_widget_config_container(widget_update,widget_to_edit):
            """WIL UPDATE WIDGET TO CONFIG STRAMING IN SCREEN MANAGER BOX"""

            for _ in widget_update:

                if _.id_name_widget_dict == "main_phone":
                    _.widget = widget_to_edit

                if _.id_name_widget_dict == "main_phone_conainer":
                    _.widget = widget_to_edit.content.content.content

                if _.id_name_widget_dict == "main_phone_conainer_conent":
                    _.widget = widget_to_edit.content.content.content.content


        update_widget_config_container(
                                       widget_update  = color_phone_controls.controls,
                                       widget_to_edit = new_selected_screen
                                       )

        update_widget_config_container(
                                       widget_update  = image_phone_controls.controls,
                                       widget_to_edit = new_selected_screen
                                       )
        update_widget_config_container(
                                       widget_update  = column_phone_controls.controls,
                                       widget_to_edit = new_selected_screen
                                       )
        old_selected_screen.update()
        new_selected_screen.update()
        row_box_content_phone.update()

        GLOBAL_VAR(set_global_var={'SELECTED_SCREEN':new_selected_screen})
        # GLOBAL_VAR(set_global_var={'EXPORT_DATA_PHONE':new_selected_screen})

        # print(new_selected_screen._get_children())

        # GLOBAL_VAR(set_global_var={'EXPORT_DATA_PHONE':{'INAMGE':new_selected_screen}})
        # ========================================================================================
        #: CREATE NEW SCREEN IN ALL SCREENS DICT VERY IMPORTATN CONTAIN ALL SCREENS IN
        current_screen_id = GLOBAL_VAR(get_global_var='SELECTED_SCREEN').uid
        get_curent_id = GLOBAL_VAR(get_global_var='ALL_SCREEN_IN_DICT').get(current_screen_id)
        # ========================================================================================

    elif clear_screen:
        #: CLEAR ALL SCREENS PHONES IN DICT SCREENS

        tmp_main_screen = all_screens_in_app.pop("main_screen")
        all_screens_in_app = {"main_screen":tmp_main_screen}


    elif set_screen:
        all_screens_in_app["main_screen"]= GLOBAL_VAR(get_global_var="main_screen")

    elif get_screen:
        return all_screens_in_app.get(get_screen)

    # print(all_screens_in_app)

CURRENT_PATH: str = os.path.join('./flet_box/extra_utils/screen_manager','screens.js')
main_screen_dict: dict = {}

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

                                                on_change                = lambda _:self.add_screen_widget(screen_name = self.content.content.content.controls[1].content)
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
                                                on_change                = lambda _:self.add_screen_widget(description= self.content.content.content.controls[2].content)

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
                                                                                                on_click   = lambda _:self.add_screen_widget(check_data=True),
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

    def escape_data_in_sqlite(self):
        name_screen.visible = False
        name_screen.update()


    def add_screen_widget(self,check_data = False ,screen_name: str=''  ,description: str=''):

        if screen_name:
            # IF NOT EMPTY INPUT SCREEN NAME
            SCREEN_GLOBAL_VAR(set_global_var={'screen_name':{'widget':screen_name,'value':screen_name.value}})

        if description:
            # IF NOT EMPTY INPUT SCREEN DESCRIPTION

            SCREEN_GLOBAL_VAR(set_global_var={'description':{'widget':description,'value':description.value}})

        if check_data:

            #: WIDGET NAME
            self.widget_name  = SCREEN_GLOBAL_VAR(get_global_var='screen_name')
            if self.widget_name:

                #: SCREEN NAME
                self.data_name    = self.widget_name.get('value')

                #: SCREEN VALUE
                self.widget_value = SCREEN_GLOBAL_VAR(get_global_var='description')

                #: IF IS EMPTY DESCRIPTION
                description = 'description' if self.widget_value == None else self.widget_value.get('value')
                if description == "": description = 'description'

                #: SET VISIBLE BOX
                name_screen.visible = False
                name_screen.update()

                #: ADDING WIDGETS TO GRIDVIEW
                data = SCREEN_GLOBAL_VAR(get_global_var='javier').get('GridView')
                data.controls.append(ScreenContainer(
                                                    id_name        = self.data_name,
                                                    id_description = description,
                                                    ))
                data.update()

                #: ADD TO LIST TO GET INDEX OF SELECTED TO ERASE
                update_list = SCREEN_GLOBAL_VAR(add_list=self.data_name)
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
                            #:===================================================
                            #: ADDING REAL SCREEN TO DICT WITH ALL REAL SCREENS
                            print(f"ADD Widget {self.data_name} <====")
                            screen_manager(add_screen=self.data_name)
                            #:===================================================

                crud_data(type_file=main_screen_dict)


class ScreenContainer(ft.Container):
    def __init__(   self,
                    id_name:          str  = ' screen_1',
                    id_description:   str  = 'description',
                    container_editor: bool = False,
                    main_screen_color:bool = False,
                    ):
        super().__init__()

        #: VALIDATION
        self.container_editor = container_editor
        self.id_name          = id_name
        self.id_description   = id_description

        #: MAIN SCREEN COLOR
        self.main_screen_color= main_screen_color

        #: GLOBAL VAR SCREEN MANAGER
        self.show_screen_manager = GLOBAL_VAR(get_global_var='SCREEN_CONTAINER')

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
        #: ADD AND CLEAN BUTTON SCREEN
        if self.container_editor:
            self.content  = ft.Container(
                                alignment = ft.alignment.center,
                                padding   = ft.padding.all(8),
                                content   = ft.Column(
                                        # scroll="HIDDEN",
                                        alignment            = ft.MainAxisAlignment.SPACE_BETWEEN,
                                        horizontal_alignment = ft.CrossAxisAlignment.CENTER,
                                        controls= [
                                                    ft.Container(height=24),
                                                    ft.Icon(
                                                            name=ft.icons.ADD,
                                                            color=ft.colors.BLUE_900,

                                                            ),

                                                    ft.ElevatedButton(
                                                                    text='CLEAN',
                                                                    bgcolor=ft.colors.RED_900,
                                                                    on_click=lambda _:self.remove_all(id_name= self.id_name),
                                                                    ),
                                                    ],
                                        ),
                                )
            self.on_click = lambda _:self.show_screen_name()

        else:
            #: ALL NEW SCREEN
            self.screen_selected =ft.Container(
                            on_click      = lambda _:self.selected_widget_to_edit(),
                            ink_color     = ft.colors.RED_900,
                            ink           = True,
                            border_radius = ft.border_radius.all(30),
                            bgcolor       = ft.colors.RED_900 if self.main_screen_color else ft.colors.TRANSPARENT,

                            content = ft.Column(
                                            controls = [

                                            ft.Container(
                                                    alignment = ft.alignment.top_right,
                                                    padding   = ft.padding.only(left= 0,right= 4,bottom= 0,top= 6),
                                                    margin    = ft.margin.only( left= 0,right= 4,bottom= 0,top= 6),

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
                                        ))

            self.content = self.screen_selected

            if self.main_screen_color:
                SCREEN_GLOBAL_VAR(set_global_var= {'widget_selected':self.screen_selected})
                SCREEN_GLOBAL_VAR(set_global_var= {'reset':self.screen_selected})

    def selected_widget_to_edit(self):
        # ACTION CONTAINER BOX OF ALL NEW SCREENS
        # RESTART TRANSPARENT
        old_selected         = SCREEN_GLOBAL_VAR(get_global_var= 'widget_selected')
        old_selected.bgcolor = ft.colors.TRANSPARENT
        old_selected.update()

        SCREEN_GLOBAL_VAR(set_global_var    = {'widget_selected':self.screen_selected})
        self.screen_selected.bgcolor = ft.colors.RED_900
        self.screen_selected.update()

        #: HIDE SCREEN MANAGER
        self.show_screen_manager.visible = False
        self.show_screen_manager.update()

        screen_name: str = self.screen_selected.content.controls[1].content.value

        change_text_screen = GLOBAL_VAR(get_global_var='change_text_screen')
        change_text_screen.value = screen_name
        change_text_screen.update()

        # #:===================================================
        # #: UPDATE SELECTED WIDGET DICT
        # print(f"UPDATE Widget {screen_name} <====")
        # print(screen_name,'<<< this is <<<<<<<<<<<<<<<<<<')
        # screen_now = GLOBAL_VAR(get_global_var=screen_name)
        screen_manager(selected_screen=screen_name)
        # screen_manager(selected_screen=screen_now)

        # print(screen_name)
        #:===================================================

        # print(screen_now,'<<< this is <<<<<<<<<<<<<<<<<<')

    def show_screen_name(self):
        # ONLY FUNCTIONALITY IS SHOW BOX INPUT DIALOG
        name_screen.visible = True
        name_screen.update()

    def remove_all(self,id_name):
        with open(CURRENT_PATH,'w') as f:
            f.write('{}')

        # SCREEN_GLOBAL_VAR(empty_list=True)
        data = SCREEN_GLOBAL_VAR(get_global_var='javier').get('GridView')
        data_ = data.controls
        data.controls = data_[:2]
        data.update()

        #: RESET MAIN SCREEN COLOR
        defauld_color = SCREEN_GLOBAL_VAR(get_global_var='reset')
        SCREEN_GLOBAL_VAR(set_global_var = {'widget_selected':defauld_color})
        defauld_color.bgcolor     = ft.colors.RED_900
        defauld_color.update()

        #:===================================================
        #: REMOVE ALL REAL SCREEN TO DICT WITH ALL REAL SCREENS
        screen_manager(clear_screen=True)
        # print(id_name,'idname')
        #:===================================================


    def delete_id_name(self,id_name):
        # GET INDEX NUMBER FROM LIST TO DELETE IN CONTROLS
        my_list = SCREEN_GLOBAL_VAR(get_index_list=id_name)

        if id_name == 'main_screen': # EVOIT ERASE MAIN SCREEN
            return

        defauld_color = SCREEN_GLOBAL_VAR(get_global_var= 'widget_selected')

        # ERASE FROM CONTROL WITH CURRENT SELECTED WIDGET
        data = SCREEN_GLOBAL_VAR(get_global_var='javier').get('GridView')
        data.controls.pop(my_list.index(id_name))
        data.update()

        # UPDATE LIST
        my_list = SCREEN_GLOBAL_VAR(remove_list=my_list.index(id_name))

        def crud_data(type_file: str='read_update'):
            #: READ AND DELETE AND UPDATE
            with open(CURRENT_PATH,'r') as f:
                load_data = json.loads(f.read())
                # DELETE FROM JSON FILE
                del load_data[id_name]
                # UPDATE NEW DATA
                with open(CURRENT_PATH,'w') as new:
                    data = json.dumps(load_data, indent= 4 )
                    new.write(data)

            #:===================================================
            #: ADDING REAL SCREEN TO DICT WITH ALL REAL SCREENS
            self.data_name: str=id_name
            print(f"DELETE Widget {self.data_name} <====")
            screen_manager(delete_screen=self.data_name)
            #:===================================================

        def reset_main_screen():
            #: RESET MAIN SCREEN COLOR
            defauld_color = SCREEN_GLOBAL_VAR(get_global_var='reset')
            SCREEN_GLOBAL_VAR(set_global_var = {'widget_selected': defauld_color})
            defauld_color.bgcolor     = ft.colors.RED_900
            defauld_color.update()
            crud_data(type_file= 'read_update')

        if defauld_color.bgcolor == ft.colors.RED_900:

            # VERY IMPORTANT if name_screen == selected_screen pass exemple screen_1 == screen_1
            # THIS EVOID ERASE SAME SELECTED WIDGET AND RETURN ERROR NO EXIST IN MAIN WIDGET
            if id_name == defauld_color.content.controls[1].content.value:

                #: RESET MAIN SCREEN COLOR
                reset_main_screen()
                return

            defauld_color.bgcolor = ft.colors.TRANSPARENT
            defauld_color.update()

            #: RESET MAIN SCREEN COLOR
            reset_main_screen()

class ScreenManager(ft.Stack):
    def __init__(self,data='Erase this test'):
        super().__init__()

        self.fit    = ft.StackFit.EXPAND

        # REMEMBER SAVE IN DATABASE
        global name_screen

        name_screen = NameScreen()
    def build(self):
        self.gird_view = ft.Container( #: GRID VIEW
                                bgcolor       = ft.colors.WHITE10,
                                height      = 750,
                                width       = 1185,
                                # expand        = True,
                                blur          = (24,24),
                                # alignment   = ft.alignment.center,
                                border_radius = ft.border_radius.all(30),
                                border        = ft.border.all(2, ft.colors.WHITE24),
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
                                                ScreenContainer(id_name= 'screen_editor' ,container_editor=  True),

                                                #: MAIN SCREEN
                                                ScreenContainer(id_name= 'main_screen'   ,main_screen_color= True),
                                             ],
                        ))

        #: LOAD JSON FILE
        self.load_json(controls_list= self.gird_view.content)

        # self.footer_bar = ft.Container( #: FOOTER BAR
        #                     ink           = False,
        #                     bgcolor       = ft.colors.BLUE_900,
        #                     padding       = ft.padding.all(8),
        #                     margin        = ft.margin.all(8),    #outside box
        #                     alignment     = ft.alignment.center,
        #                     border_radius = ft.border_radius.all(30),
        #                     border        = ft.border.all(4, ft.colors.BLACK),

        #                 content=ft.Row(

        #                         controls=[
        #                                     ft.ElevatedButton("Delete",   tooltip='buttom'),
        #                                     ft.ElevatedButton("press row",tooltip='buttom'),
        #                                     ft.ElevatedButton("press row",tooltip='buttom'),
        #                                  ],),

        # )#<=== NOTE COMA
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

        SCREEN_GLOBAL_VAR(set_global_var={
                                    'javier':{
                                            'GridView':self.gird_view.content
                                  }})

    #: LOAD JSON FILE
    def load_json(self,controls_list: list=[]):
        """ LOAD JSON FILE TO INSERT SCREEN IN INIT"""
        with open(CURRENT_PATH,'r+') as f:
            load_data = json.loads(f.read())
            controls_list.controls += [ ScreenContainer(id_name=_ ) for _ in load_data]

            for _ in load_data:
                SCREEN_GLOBAL_VAR(add_list=_)

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
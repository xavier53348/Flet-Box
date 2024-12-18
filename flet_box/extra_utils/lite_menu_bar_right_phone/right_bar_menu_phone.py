from ..settings_var.settings_widget import GLOBAL_VAR
from ..tree_view.tree_view import TreeView
import flet as ft


class LiteMenuUpContainer(ft.Stack):
    def __init__(
                self,
                main_page=None,
                phone_widget_container=None,
                menu_left_container=None,
                menu_right_container=None,
                space_widget=None,
            ):
        super().__init__()
        # self.main_page              = main_page
        # self.menu_left_container    = menu_left_container
        # self.phone_widget_container = phone_widget_container
        # self.menu_right_container   = menu_right_container

        self.main_page = GLOBAL_VAR(get_global_var="PAGE")
        self.menu_left_container = menu_left_container

        # HEIGHT
        self.height = 542

        self.space_widget_1, self.space_widget_2 = space_widget

        #: only in production
        #: print(self.space_widget_1)

    def build(self):
        self.Drop_LiteMenuUpContainer = ft.Container(
            # offset=(0.1,0),
            ink=False,
            padding=ft.padding.all(2),
            margin=ft.margin.only(left=2, top=0, right=0, bottom=0),
            alignment=ft.alignment.center,
            border_radius=ft.border_radius.all(30),
            # height        = 450,
            gradient=ft.LinearGradient(
                begin=ft.alignment.top_center,
                end=ft.alignment.bottom_center,
                colors=[ft.colors.TEAL, ft.colors.BLACK12],
            ),
            bgcolor="Red",
            border=ft.border.all(0.6, ft.colors.WHITE12),
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=18,
                color=ft.colors.with_opacity(0.8, ft.colors.BLACK26),
                offset=ft.Offset(0, 0),
                blur_style=ft.ShadowBlurStyle.OUTER,
            ),
            content=ft.Column(
                controls=[
                    ft.Container(
                        ink=False,
                        bgcolor=ft.colors.BLACK26,
                        padding=ft.padding.only(left=0, top=0, right=0, bottom=0),
                        alignment=ft.alignment.center,
                        border_radius=ft.border_radius.all(30),
                        border=ft.border.all(2, ft.colors.BLACK12),
                        content=ft.Column(
                            spacing=8,
                            controls=[
                                ft.IconButton(
                                    icon=ft.icons.EDIT_SQUARE,
                                    tooltip="EDIT WIDGET",
                                    on_click=lambda _: self.modify_widget_in_phone_container(),
                                    bgcolor="Blue",
                                    icon_color="White",
                                ),
                                ft.IconButton(
                                    icon=ft.icons.TOUCH_APP,
                                    tooltip="UN SELECT\nBORDER WIDGET",
                                    on_click=lambda _: self.action_button(
                                        action="UNSELECT"
                                    ),
                                    bgcolor=ft.colors.WHITE24,
                                    icon_color="White",
                                ),
                                ft.IconButton(
                                    icon=ft.icons.SMARTPHONE,
                                    tooltip="SMARTPHONE",
                                    on_click=lambda _: self.action_button(
                                        action="SMARTPHONE"
                                    ),
                                ),
                                ft.IconButton(
                                    icon=ft.icons.TABLET_ANDROID,
                                    tooltip="TABLET",
                                    on_click=lambda _: self.action_button(
                                        action="TABLET"
                                    ),
                                ),
                                ft.IconButton(
                                    icon=ft.icons.TV_OUTLINED,
                                    tooltip="PC",
                                    on_click=lambda _: self.action_button(action="PC"),
                                ),
                                ft.IconButton(
                                    icon=ft.icons.SCREENSHOT_MONITOR,
                                    tooltip="FULL SCREEN",
                                    on_click=lambda _: self.action_button(
                                        action="SHOW PC"
                                    ),
                                ),
                            ],
                        ),
                    ),  # <=== NOTE COMA
                    ft.Container(
                        padding=ft.padding.only(left=0, top=2, right=0, bottom=2),
                        bgcolor=ft.colors.BLACK26,
                        ink=False,
                        alignment=ft.alignment.center,
                        border_radius=ft.border_radius.all(30),
                        border=ft.border.all(2, ft.colors.BLACK12),
                        content=ft.Column(
                            spacing=8,
                            controls=[
                                ft.IconButton(
                                    icon=ft.icons.SCREEN_ROTATION,
                                    tooltip="ROTATE",
                                    on_click=lambda _: self.action_button(
                                        action="rotation"
                                    ),
                                ),
                                ft.IconButton(
                                    icon=ft.icons.DEBLUR,
                                    tooltip="LIGHT / DARK",
                                    on_click=lambda _: self.action_button(
                                        action="LIGHT / DARK"
                                    ),
                                ),
                                ft.IconButton(
                                    icon=ft.icons.SCHEMA,
                                    tooltip="TREE",
                                    on_click=lambda _: self.action_button(
                                        action="TREE"
                                    ),
                                ),
                                ft.IconButton(
                                    icon=ft.icons.DELETE_SWEEP_OUTLINED,
                                    tooltip="DELETE_",
                                    on_click=lambda _: self.action_button(
                                        action="delete"
                                    ),
                                ),
                                ft.IconButton(
                                    icon=ft.icons.RECYCLING,
                                    tooltip="CLEAR",
                                    on_click=lambda _: self.action_button(
                                        action="clear"
                                    ),
                                    bgcolor=ft.colors.RED_900,
                                ),
                            ],
                        ),
                    ),  # <===
                ],
            ),
        )  # <=== NOTE COMA

        return self.Drop_LiteMenuUpContainer

    def modify_widget_in_phone_container(self):
        """
        GLOBAL VARS:
                       CONFIG_TABS_CONTAINERS
                       CONFIG_TABS_CONTAINERS_CONTENT

        NOTE:
             IS NECESSARY ADD THIS 2 GLOVAL VAR TO CALL TAB MENU AND MAKE CHANGES IN STRAMING

        GLOBAL VARS:
                       SELECT_DROPP_WIDGET_CONTAINER
                       SELECT_DROPP_WIDGET_CONTAINER_CONTENT

        NOTE:
             EVERY TIME THAT IS SELECTED WIDGET INSIDE THE PHONE.
             THIS 2 VAR ARE CHANGE EVERY TIME THAT DETECT ONE CLICK
             AND AFTER PERES BUTTON EDIT WILL CALL THIS METOD TO
             CHANGE PROPERTY

        """
        BOOL_SHOW_SELECTED = GLOBAL_VAR(get_global_var="BOOL_SHOW_SELECTED")

        LIST_KEYS_DICT_USED = GLOBAL_VAR(get_global_var="LIST_KEYS_DICT_USED")

        CONFIG_TABS_CONTAINERS = GLOBAL_VAR(get_global_var="CONFIG_TABS_CONTAINERS")
        CONFIG_TABS_CONTAINERS_CONTENT = GLOBAL_VAR(
            get_global_var="CONFIG_TABS_CONTAINERS_CONTENT"
        )

        SELECT_DROPP_WIDGET_CONTAINER = GLOBAL_VAR(
            get_global_var="SELECT_DROPP_WIDGET_CONTAINER"
        )
        SELECT_DROPP_WIDGET_CONTAINER_CONTENT = GLOBAL_VAR(
            get_global_var="SELECT_DROPP_WIDGET_CONTAINER_CONTENT"
        )

        #: 'Position','Modification','Color','Image',
        control_tab_2 = CONFIG_TABS_CONTAINERS.content.controls
        control_tab_3 = CONFIG_TABS_CONTAINERS_CONTENT.content.controls

        print(f"Im modificating....{CONFIG_TABS_CONTAINERS}")

        def insert_data_in_box_container(column_tab):
            """
            THIS METOD WALK IN TABS number #2 EACH COLUMN WITH WIDGETS INSIDE 4 COLUMNS

            """
            print("tab {control_tab_2}")
            #: TAB 2

            if column_tab == "2_0":
                control_2_inside = control_tab_2[0]  #
                tmp_value = (
                    control_2_inside.controls[0].content.controls[1].content.controls
                )

            if column_tab == "2_1":
                control_2_inside = control_tab_2[1]  #
                tmp_value = (
                    control_2_inside.controls[0].content.controls[1].content.controls
                )

            if column_tab == "2_2":
                control_2_inside = control_tab_2[2]  #
                tmp_value = (
                    control_2_inside.controls[0].content.controls[1].content.controls
                )

            if column_tab == "2_3":
                control_2_inside = control_tab_2[3]  #
                tmp_value = (
                    control_2_inside.controls[0].content.controls[1].content.controls
                )

            #: FINISH

            for _ in tmp_value:
                _.controls[0].visible = True
                _.widget = SELECT_DROPP_WIDGET_CONTAINER
                # print(_.widget)

        def insert_data_in_box_container_content(column_tab, column=0):
            """
            THIS METOD WALK IN TABS number #3 EACH COLUMN WITH WIDGETS INSIDE 4 COLUMNS

            """

            #: TAB 3

            if column_tab == "3_0":
                control_3_inside = control_tab_3[0]  #
                tmp_value_tab_widget = (
                    control_3_inside.controls[0].content.controls[1].content.controls
                )

            if column_tab == "3_1":
                control_3_inside = control_tab_3[1]  #
                tmp_value_tab_widget = (
                    control_3_inside.controls[0].content.controls[1].content.controls
                )

            if column_tab == "3_2":
                control_3_inside = control_tab_3[2]  #
                tmp_value_tab_widget = (
                    control_3_inside.controls[0].content.controls[1].content.controls
                )

            if column_tab == "3_3":
                control_3_inside = control_tab_3[3]  #
                tmp_value_tab_widget = (
                    control_3_inside.controls[0].content.controls[1].content.controls
                )

            if column_tab == "3_4":
                control_3_inside = control_tab_3[4]  #
                tmp_value_tab_widget = (
                    control_3_inside.controls[0].content.controls[1].content.controls
                )

            if column_tab == "3_5":
                control_3_inside = control_tab_3[5]  #
                tmp_value_tab_widget = (
                    control_3_inside.controls[0].content.controls[1].content.controls
                )

            if column_tab == "3_6":
                control_3_inside = control_tab_3[6]  #
                tmp_value_tab_widget = (
                    control_3_inside.controls[0].content.controls[1].content.controls
                )

            if column_tab == "3_7":
                control_3_inside = control_tab_3[7]  #
                tmp_value_tab_widget = (
                    control_3_inside.controls[0].content.controls[1].content.controls
                )

            #: FINISH

            #: NEED CHECK IF THE WIDGET IT'S IN LIST_KEYS_DICT_USED
            #: IF IS TRUE THE CONTAINER CONFIG
            #:
            #: WILL PUT          VISIBLE TRUE
            #: IF NOT WILL PUT   VISIBLE OFF
            #: print(LIST_KEYS_DICT_USED)

            for _ in tmp_value_tab_widget:
                #: WALK ALL TABS TO INSERT THE VALUE THAT WE

                #: if _.id_name_widget_dict in LIST_KEYS_DICT_USED:
                if (
                    _.id_name_widget_dict
                    in SELECT_DROPP_WIDGET_CONTAINER_CONTENT.__dir__()
                ):
                    data = (
                        _.id_name_widget_dict
                        in SELECT_DROPP_WIDGET_CONTAINER_CONTENT.__dir__()
                    )

                    #: print(_.id_name_widget_dict,data)
                    #: print(SELECT_DROPP_WIDGET_CONTAINER_CONTENT._wrap_attr_dict('name')  )
                    #: print(SELECT_DROPP_WIDGET_CONTAINER_CONTENT._Control__attrs  )
                    #: FILTER THAT IS USE TO COMPARE WIDGET SELECTED
                    #: if _.id_name_widget_dict in LIST_KEYS_DICT_USED or dict of all widget inside widget_editor.py

                    _.visible = True
                    #: _.controls[0].visible = True
                    _.widget = SELECT_DROPP_WIDGET_CONTAINER_CONTENT
                    #: _.update()  #:<==== update exactly widget <<<
                else:
                    _.visible = False
                    #: _.controls[0].visible = False
                    _.widget = SELECT_DROPP_WIDGET_CONTAINER_CONTENT
                    #: _.update()  #:<==== update exactly widget <<<

            #: WE GET A LIS WITH ALL WIDGET IN EACH BOX IN TAB 3
            #: AFTER WE FILTER ALL DATA LIST TO A EVOID DUPLICATES FALSE OR TRUE
            #: RETURNING { False } OR { False , True }
            #: IF DATA SET RETURNING HAVE 2 CONTENT INSIDE THE SET
            #: IS TRUE IS VISEBLE ALL CONTENT BOX
            #: IF NOT NO APEAR IN BOX

            is_visible = set()
            make_visible_on_off = (
                control_tab_3[column].controls[0].content.controls[1].content.controls
            )

            visible = [is_visible.add(_.visible) for _ in make_visible_on_off]
            if len(is_visible) == 2:
                control_tab_3[column].visible = True
                control_tab_3[column].update()

            else:
                control_tab_3[column].visible = False
                control_tab_3[column].update()

            for _ in make_visible_on_off:
                _.update()

        if BOOL_SHOW_SELECTED:
            #: TAB 2 <== CALLING METHOD VISIBLE OR ONT VISIBLE

            CONFIG_TABS_CONTAINERS.visible = True
            CONFIG_TABS_CONTAINERS.update()

            insert_data_in_box_container(column_tab="2_0")
            insert_data_in_box_container(column_tab="2_1")
            insert_data_in_box_container(column_tab="2_2")
            insert_data_in_box_container(column_tab="2_3")

            #: TAB 3 <== CALLING METHOD VISIBLE OR ONT VISIBLE
            CONFIG_TABS_CONTAINERS_CONTENT.visible = True
            CONFIG_TABS_CONTAINERS_CONTENT.update()

            insert_data_in_box_container_content(column_tab="3_0", column=0)
            insert_data_in_box_container_content(column_tab="3_1", column=1)
            insert_data_in_box_container_content(column_tab="3_2", column=2)
            insert_data_in_box_container_content(column_tab="3_3", column=3)
            insert_data_in_box_container_content(column_tab="3_4", column=4)
            insert_data_in_box_container_content(column_tab="3_5", column=5)
            insert_data_in_box_container_content(column_tab="3_6", column=6)
            insert_data_in_box_container_content(column_tab="3_7", column=7)

        else:
            #: TAB 2
            CONFIG_TABS_CONTAINERS.visible = False
            CONFIG_TABS_CONTAINERS.update()

            #: TAB 3

            CONFIG_TABS_CONTAINERS_CONTENT.visible = False
            CONFIG_TABS_CONTAINERS_CONTENT.update()

    def action_button(self, action):
        self.phone_widget_blur_cont = GLOBAL_VAR(
            get_global_var="GENERIC_CONTAINER_PHONE"
        )
        self.phone_widget_container = GLOBAL_VAR(get_global_var="SELECTED_SCREEN")

        self.menu_left_container = GLOBAL_VAR(get_global_var="DRAGG_SHOW")
        self.menu_right_container = GLOBAL_VAR(get_global_var="CONFI_SHOW")

        if action == "delete":
            """
            WE DELETE ALL WIDGETS IT'S NOT THE CORRECT WAY
            """
            touch_widget_in_phone = GLOBAL_VAR(get_global_var="LIST_SELECTED_WIDGETS")
            main_page = GLOBAL_VAR(get_global_var="PAGE")

            #: get the corret way to delete widget <===

            if touch_widget_in_phone:
                #: ERASE DICT SELECT WIDGET #
                """
                WE GO BACK 2 PATH TO GET MAIN WIDGET STACK() AND DELETE WIDGET FROM DICT

                LIST_SELECTED_WIDGETS
                EXPORT_DATA_PHONE

                """
                id_widget = self.main_page.get_control(touch_widget_in_phone.uid)

                #: CHECK DATA TO ERASE PHONE WIDGET
                #: CHECK IF WIDGET ID EXIST IN DATABASE [LIST_SELECTED_WIDGETS]
                #: IF TRUE REMOVE CURRENT WIDGET FROM MAIN DATABASE
                #: GLOBAL_VAR(remove_global_var=touch_widget_in_phone.id)

                main_phone = GLOBAL_VAR(
                    get_global_var="SELECTED_SCREEN"
                )  #: <===== GET CURRENT SCREEN
                edit_dict = GLOBAL_VAR(
                    get_global_var="ALL_SCREEN_IN_DICT"
                )  #: <===== GET ALL SCREENS GET FROM MAIN PAGE
                selected_widget = GLOBAL_VAR(
                    get_global_var="LIST_SELECTED_WIDGETS"
                )  #: <===== GET CURRENT WIDGET SELECTED

                SELECT_DROPP_WIDGET_CONTAINER = GLOBAL_VAR(
                    get_global_var="SELECT_DROPP_WIDGET_CONTAINER"
                )  #: <===== GET CURRENT WIDGET SELECTED

                #: REMOVE FROM DICT ALL_SCREEN_IN_DICT
                if edit_dict.get(main_phone.uid).get(selected_widget.tooltip):
                    del edit_dict[main_phone.uid][selected_widget.tooltip]

                else:
                    for tmp_key in edit_dict[main_phone.uid]:
                        """
                        Fixed middle anywhere widget lost in middle of the screen phone Container
                        """
                        the_widget = edit_dict[main_phone.uid][tmp_key]
                        selected_control_id = f"_{int(selected_widget.uid.replace('_','')) - 2}"  #: <===== ID Stack() - 2
                        only_recursive = ["column", "row", "gridview", "stack"]

                        def recursive_erase(data):
                            #: PERSONALLY DONT LIKE RECURSIVE BECOUSE NEED LOT CPU AND MEMORY MORE THAN NORMAL NESTED LOOPS
                            #: BUT NO LIKE MAKE LOT CODE NOW THIS ON FUTURE MAY CHANGE IF APP GET LOST HAVY

                            for index, _ in enumerate(data):
                                # data.pop()
                                if _.uid == selected_control_id:
                                    data.pop(index)
                                    return

                                if (
                                    _.controls[0].content.content._get_control_name()
                                    in only_recursive
                                ):
                                    recursive_erase(
                                        data=_.controls[0].content.content.controls
                                    )

                        # print(the_widget.content.controls) #[InfinityBoxLayerOne(clipbehavior='none')]
                        recursive_erase(data=the_widget.content.controls)
                # ===================
                del main_page._index[
                    selected_widget.uid
                ]  #: <===== DELETE INDEX IN MAIN PAGE

                #: BACK 2 ID BEFORE TO GET DRAGGTARGET AND CORRECTLY DELETE
                get_control_id = f"_{int(id_widget.uid.replace('_','')) - 2}"  #: <===== ID Stack() - 2
                page_control = self.main_page.get_control(
                    get_control_id
                )  #: <===== GET EXACTLY DRAG TARGET

                # RUN ONLY IN PRODUCTION
                # print(page_control,get_control_id,'simple erase')

                page_control.controls.pop()  #: <===== ERASE CONTROL WIDGET
                touch_widget_in_phone = GLOBAL_VAR(
                    set_global_var={"LIST_SELECTED_WIDGETS": None}
                )  #: <===== RESET SELECTED WIDGET TO NONE
                del main_page._index[
                    get_control_id
                ]  #: <===== DELETE INDEX IN MAIN PAGE
                page_control.update()  #: <===== UPDATE PAGE

                # print(edit_dict[main_phone.uid]['Column: 1'].content.controls)
                for tmp_key in edit_dict[main_phone.uid]:
                    edit_dict[main_phone.uid].get(tmp_key).update()

        if action == "UNSELECT":
            #: SET GLOBAL VAR // LIST_SELECTED_WIDGETS // TO RESET AFTER PRESS SELECTED BORDER IN PHONE CONTAINER
            selected_widget_clicked = GLOBAL_VAR(get_global_var="LIST_SELECTED_WIDGETS")
            if selected_widget_clicked:
                selected_widget_clicked.border = ft.border.all(0, ft.colors.TRANSPARENT)
                selected_widget_clicked.update()

        if action == "clear":
            #: GET BLOVAL VAR
            main_phone = GLOBAL_VAR(get_global_var="SELECTED_SCREEN")
            edit_dict = GLOBAL_VAR(get_global_var="ALL_SCREEN_IN_DICT")

            #: ERASE ALL WIDGETS FROM CRONTROLS
            main_phone.content.content.content.content.controls.clear()
            main_phone.update()  #: <===== UPDATE PAGE

            #: SET DEFAULD EMPTY PHONE
            edit_dict[main_phone.uid] = dict()

            #: RUN ONLY IN PRODUCTION
            # print(self.edit_dict )

            #: RESET SELECTED WIDGET
            GLOBAL_VAR(set_global_var={"LIST_SELECTED_WIDGETS": []})

        if action == "TREE":
            TreeView.visible_view()

        if action == "rotation":
            self.phone_widget_blur_cont.width, self.phone_widget_blur_cont.height = (
                self.phone_widget_blur_cont.height,
                self.phone_widget_blur_cont.width,
            )
            self.phone_widget_container.width, self.phone_widget_container.height = (
                self.phone_widget_container.height,
                self.phone_widget_container.width,
            )
            self.phone_widget_blur_cont.update()
            self.phone_widget_container.update()

            if self.phone_widget_container.width >= 600:
                self.menu_right_container.visible = (
                    False if self.menu_right_container.visible else True
                )
                self.menu_left_container.visible = (
                    False if self.menu_right_container.visible else True
                )
                self.menu_left_container.update()
                self.menu_right_container.update()

            else:
                self.Drop_LiteMenuUpContainer.update()

        if action == "LIGHT / DARK":
            self.phone_widget_container.bgcolor = (
                ft.colors.WHITE
                if self.phone_widget_container.bgcolor == "#070707"
                else "#070707"
            )
            self.phone_widget_container.update()

        if action == "SMARTPHONE":
            self.phone_widget_container.width = 320
            self.phone_widget_blur_cont.width = self.phone_widget_container.width
            self.phone_widget_container.height = 567
            self.phone_widget_blur_cont.height = self.phone_widget_container.height
            self.phone_widget_blur_cont.update()
            self.phone_widget_container.update()

            self.menu_left_container.visible = True
            self.menu_right_container.visible = True
            self.menu_left_container.update()
            self.menu_right_container.update()

        if action == "TABLET":
            #: Phone Container offset
            self.phone_widget_container.width = 460
            self.phone_widget_blur_cont.width = self.phone_widget_container.width
            self.phone_widget_container.height = 625
            self.phone_widget_blur_cont.height = self.phone_widget_container.height

            self.phone_widget_blur_cont.update()
            self.phone_widget_container.update()

            self.menu_left_container.visible = True
            self.menu_right_container.visible = True
            self.menu_left_container.update()
            self.menu_right_container.update()

        if action == "PC":
            self.phone_widget_container.width = 780
            self.phone_widget_blur_cont.width = self.phone_widget_container.width
            self.phone_widget_container.height = 525
            self.phone_widget_blur_cont.height = self.phone_widget_container.height
            self.phone_widget_blur_cont.update()
            self.phone_widget_container.update()

            self.menu_right_container.visible = (
                False if self.menu_right_container.visible else True
            )
            self.menu_left_container.visible = (
                False if self.menu_right_container.visible else True
            )
            self.menu_left_container.update()
            self.menu_right_container.update()

        if action == "SHOW PC":
            self.width_ = 780

            if self.menu_left_container.visible and self.menu_right_container.visible:
                self.menu_left_container.visible = False
                self.menu_right_container.visible = False

            elif (
                not self.menu_left_container.visible
                and not self.menu_right_container.visible
            ):
                if self.phone_widget_container.width >= 500:
                    self.phone_widget_container.width = 460
                    self.phone_widget_blur_cont.width = (
                        self.phone_widget_container.width
                    )

                    self.phone_widget_container.height = 625
                    self.phone_widget_blur_cont.height = (
                        self.phone_widget_container.height
                    )

                    self.phone_widget_blur_cont.update()
                    self.phone_widget_container.update()

                self.menu_left_container.visible = True
                self.menu_right_container.visible = True

            elif (
                not self.menu_left_container.visible
                and self.menu_right_container.visible
            ):
                self.menu_left_container.visible = False
                self.menu_right_container.visible = False

            elif (
                self.menu_left_container.visible
                and not self.menu_right_container.visible
            ):
                self.menu_left_container.visible = False
                self.menu_right_container.visible = False

            self.menu_left_container.update()
            self.menu_right_container.update()

    def action_windows(self, action):
        self.phone_widget_container.width, self.phone_widget_container.height = (
            self.phone_widget_container.height,
            self.phone_widget_container.width,
        )
        self.phone_widget_container.update()


if __name__ == "__main__":

    def main(page: ft.Page):
        page.scroll = "HIDDEN"  # AUTO ADAPTIVE ALWAYS HIDDEN
        page.vertical_alignment = ft.MainAxisAlignment.CENTER
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        page.theme_mode = ft.ThemeMode.DARK  # ft.ThemeMode.LIGHT
        page.window_bgcolor = ft.colors.RED_100
        page.window_left = 20
        page.window_top = 20
        page.window_height = 400
        page.window_width = 600
        page.padding = 0
        page.spacing = 0
        page.expand = True
        Lite_MenuUpContainer = LiteMenuUpContainer()
        page.add(Lite_MenuUpContainer)
        page.update()

    ft.app(
        target=main,
    )

import json

from .skeleton_class_screens import get_skeleton
from ..settings_var.settings_widget import GLOBAL_VAR
from ..settings_var.save_export import MakeJasonFile


class saving_all_class_screens_in_file:
    """
    VERY IMPORTANT TO CREATE STRUCTURE OF ALL CLASS SCREENS AFTER
    WILL WRITE JUST STRUCTURE AND THEN WILL PASS TO OTHER MODULE
    AND WILL REFACTORY REMPLACING SOME SPECIAL WORDS

    EXEMPLE:

    from .[SYTLE_RENAME_styles] import styles
    from .[EVENT_RENAME_events] import *

    SYTLE_RENAME_styles  WILL BE REMLACED BY SPECIFIC DATA
    EVENT_RENAME_events

    RETURN:

    WILL RETURN STRUCTURE OF ALL WIDGES IN VIEWS IN THIS VARIABLES

    streaming_phone_data:   PATH
    style_code:             CLASS STYLE CODE
    self.main_event_code:   CLASS EVENTS CODE
    self.id_name:           WIDGET ID

    # IMPORT CLASS AND USED
    import saving_all_class_screens_in_file as create_frame_app

    self.dumped_data = self.create_frame_app(
                                main_node_phone=tmp_widgets,
                                main_node_phone_id=tmp_widgets.uid
                                )

    self.streaming_phone_data = self.dumped_data.dumped_data.get("main_widget_form_skeleton")
    self.style_code           = self.dumped_data.dumped_data.get("main_style_code")
    self.main_event_code      = self.dumped_data.dumped_data.get("main_event_code")
    self.id_name              = self.dumped_data.dumped_data.get("id_name")

    """
    # VAR ALWAYS WILL BE REMOVED OR RESET TO EMPTY
    tmp_data: dict = {}
    dumped_data: dict={}

    builder_jason_file_widget = MakeJasonFile()

    all_elements_in_phone_container: dict = {
                        "MAIN_CONTAINER": str(),
                        "MAIN_EFFECTS_CONTAINER": str(),
                        "COLUMN_CONTAINER": str(),
                    }

    #: MAIN PHONE
    main_container_atributes_to_delete = [
                        "borderradius",
                        "border",
                        "ink",
                        "n",
                        "onhover",
                        "visible",
                        "onclick",
                    ]
    main_container_atributes_to_rename = [
                        "borderradius",
                        "imagesrc",
                        "imageopacity",
                        "imagefit",
                    ]
    #: MAIN PHONE
    main_effect_container_atributes_to_delete = [
                        "borderradius",
                        "border",
                        "n",
                        "onclick",
                        "onhover",
                    ]
    # main_effect_atributes_to_rename = [
    #                     # "borderradius",
    #                     # "imagesrc",
    #                     # "imageopacity",
    #                     # "imagefit",
    #                     ]
    #: MAIN PHONE
    column_container_atributes_to_delete = [
                                            "n",
                                            "onhover",
                                            "onclick",
                                        ]
    column_container_atributes_to_rename = [
                                            "horizontalalignment",
                                        ]

    def __init__(
            self,
            main_node_phone:    str = "OBJECT WIDGET",
            main_node_phone_id: str = "ID OBJECT WIDGET"
            ):
        super().__init__()

        #: INSTANCE MAIN PHONE
        self.main_phone = main_node_phone

        #: BUILD FRAME PHONE
        PHONE_MAIN = self.main_phone
        PHONE_CONTAINER = self.main_phone.content.content.content
        COLUMN_CONTAINER = self.main_phone.content.content.content.content
        # ALL_SCREEN_IN_DICT = self.main_phone.content.content.content.content.controls

        #: =========================================================================
        #: // NEW COPY ATTRIBUTES PHONE_MAIN                             DATA PHONE: [1]
        PHONE_MAIN.copy_attrs(dest=self.tmp_data)

        self.tmp_data = self.delete_attributes(
                                            list_atributes=self.main_container_atributes_to_delete,
                                            dict_to_edit=self.tmp_data
                                            )
        self.tmp_data = self.rename_attributes(
                                            list_atributes=self.main_container_atributes_to_rename,
                                            dict_to_edit=self.tmp_data
                                            )
        #: =========================================================================
        #: RUN ONLY IN PRODUCTION                                        DATA PHONE: [1]
        # print(tmp_data,' DATA PHONE: [1]')
        self.delete_one_attribute(attribute="n")

        #: SET NEW DATA OF CONTAIER
        self.all_elements_in_phone_container["MAIN_CONTAINER"] = self.tmp_data
        self.tmp_data: dict = {}  #: RESET TO EMPTY
        #: =========================================================================
        #: // NEW COPY ATTRIBUTES PHONE_CONTAINER                       DATA PHONE: [2]
        PHONE_CONTAINER.copy_attrs(dest=self.tmp_data)

        self.tmp_data = self.delete_attributes(
                                                list_atributes=self.main_effect_container_atributes_to_delete,
                                                dict_to_edit=self.tmp_data)
        # tmp_data = self.rename_attributes(
        #                                      list_atributes= atributes_to_rename,
        #                                      dict_to_edit  = tmp_data
        #                                 )

        #: =========================================================================
        #: RUN ONLY IN PRODUCTION                                        DATA PHONE: [2]
        # print(tmp_data,' DATA PHONE: [2]')
        self.delete_one_attribute(attribute="n")

        #: SET NEW DATA OF CONTAIER
        self.all_elements_in_phone_container["MAIN_EFFECTS_CONTAINER"] = self.tmp_data
        self.tmp_data: dict = {}  #: RESET TO EMPTY
        #: =========================================================================
        #: // NEW COPY ATTRIBUTES PHONE_MAIN                             DATA PHONE: [3]
        COLUMN_CONTAINER.copy_attrs(dest=self.tmp_data)

        self.tmp_data = self.delete_attributes(
                                        list_atributes=self.column_container_atributes_to_delete,
                                        dict_to_edit=self.tmp_data
                                        )
        self.tmp_data = self.rename_attributes(
                                        list_atributes=self.column_container_atributes_to_rename,
                                        dict_to_edit=self.tmp_data
                                        )

        #: =========================================================================
        #: RUN ONLY IN PRODUCTION                                        DATA PHONE: [3]
        self.delete_one_attribute(attribute="n")

        #: SET NEW DATA OF CONTAIER
        self.all_elements_in_phone_container["COLUMN_CONTAINER"] = self.tmp_data
        self.tmp_data: dict = {}  #: RESET TO EMPTY
        #: =========================================================================
        #: BUILD ALL DATA TO EXPORT

        self.main_phone_style = (
            json.dumps(self.all_elements_in_phone_container,indent=4).replace("\\", "")
                                                                     .replace("borderradius", "border_radius")
                                                                     .replace("horizontalalignment", "horizontal_alignment")
            )

        self.main_screen_attributes: str = f"{self.main_phone_style}".replace('"{', "{").replace('}"', "}")

        #: RECODING TO MAKE MAIN SCREEN FROM SKELETON CLASS SCREEN THIS IS MAIN_SCREEN_BUILDER
        self.main_widget_form_skeleton: str = get_skeleton(name="class_flet_box")
        self.main_widget_form_skeleton = self.main_widget_form_skeleton.replace("CHANGE_STYLE",
                                                                                self.main_screen_attributes)  #: SET ATRIBUTES

        #: CONTENT OF THE PHONE WILL WALK THOUGH HONE TO GET ALL DATA
        self.data_to_treview = GLOBAL_VAR(get_global_var="ALL_SCREEN_IN_DICT").get(main_node_phone_id)
        self.build_json_file = self.builder_jason_file_widget.build_json_file(widget_show=self.data_to_treview)

        print("======= saving all")
        # print(self.data_to_treview)
        #: WILL RELACE [ CHANGE_ATTRIBUTES ] BY NEW ATTRIBUTES
        self.main_widget_form_skeleton = self.main_widget_form_skeleton.replace(
                                                                    "CHANGE_ATTRIBUTES",
                                                                    self.build_json_file.get("main_code")
                                                                )  #: SET BOX CONTENT

        # #: RECODING TO MAKE STYLE SCREEN FROM SKELETON CLASS SCREEN
        self.main_style_code = f"#: THIS IS NOT JSON FILE IT'S PYTHON DICTIONARY{self.build_json_file.get('style_code')}"

        # #: RECODING TO MAKE EVENT MANAGER SCREEN FROM SKELETON CLASS SCREEN
        self.event_manager: str = get_skeleton(name="event_manager")
        self.main_event_code = f"{self.event_manager}{self.build_json_file.get('event_code')}"

        #: GET CURRENT NAME ID FOT EACH PROYECT
        self.id_name = GLOBAL_VAR(get_global_var=main_node_phone_id)

        #: RUN ONLY PRODUCTON
        # print(all_elements_in_phone_container)
        # print(f'ID: {self.main_phone.uid} PHONE_MAIN 1')
        # print(f'ID: {self.main_phone.content.content.content.uid } PHONE_CONTAINER 2')
        # print(f'ID: {self.main_phone.content.content.content.content.uid } PHONE_CONTAINER 4')

        # print(self.build_json_file.get('main_code'))
        # print(self.build_json_file.get('event_code'))
        # print(self.build_json_file.get('style_code'))
        # print(self.build_json_file)

        # print(
        #     self.main_widget_form_skeleton,
        #     self.main_style_code,
        #     self.main_event_code,
        #     self.id_name,
        #     )
        # print('>>>>>>>>>>>>>>',self.main_widget_form_skeleton)

        self.dumped_data = {
                            "main_widget_form_skeleton":self.main_widget_form_skeleton,
                            "main_style_code":self.main_style_code,
                            "main_event_code":self.main_event_code,
                            "id_name":self.id_name
                        }

        # self.return_all_data()
        #
        #: RESET COLOR
        # if selected_widget_clicked:
        #      selected_widget_clicked.border = ft.border.all(0, ft.colors.TRANSPARENT)
        #      selected_widget_clicked.update()

    def delete_one_attribute(self, attribute="n"):
        """
        DELETE ONE ATTRIBUTE

        self.delete_one_attribute(attribute="n")
        """
        if self.tmp_data.get(attribute):
            del self.tmp_data[attribute]

    def delete_attributes(
                            self,
                            list_atributes: list = [],
                            dict_to_edit: dict = {}
                        ):
        """
        "DELETE ATRIBUTES IF EXIST BECOUSE MAKE SOME TROUBLES"

        atributes_to_delete = [
                            "borderradius",
                            "border",
                            "ink",
                            "n",
                            "onhover",
                            "visible",
                            "onclick",
                        ]

        """
        for _ in list_atributes:
            #: IF EXIST DATA or DATA == ""
            if dict_to_edit.get(_):
                del dict_to_edit[_]

        return dict_to_edit

    def rename_attributes(
                        self,
                        list_atributes: list = "",
                        dict_to_edit: dict = {},
                        attributes_to_rename: dict = {},
                    ):
        """
        "RENAME ATRIBUTES IF EXIST BECOUSE MAKE SOME TROUBLES"

        attributes_to_rename = {
                "imagesrc":     "image_src",
                "imageopacity": "image_opacity",
                "imagefit":     "image_fit",
                "borderradius": "border_radius",
                "horizontalalignment": "horizontal_alignment",
            }

        """
        attributes_to_rename = {

                        "imagesrc":     "image_src",
                        "imageopacity": "image_opacity",
                        "imagefit":     "image_fit",
                        "borderradius": "border_radius",
                        "horizontalalignment": "horizontal_alignment",
                    }

        for _ in list_atributes:
            # RENAME ALL ATTRIBUTES IN DICT TO EVOID TROUBLES
            if dict_to_edit.get(_):
                #: GET NEW NAME
                new_name = attributes_to_rename.get(_)

                # RENAME OLD BY NEW KEY
                dict_to_edit[new_name] = dict_to_edit.get(_)

                #: DELETE OLD KEY
                del dict_to_edit[_]

            else:
                if dict_to_edit.get(_) == "":
                    del dict_to_edit[_]

        return dict_to_edit

    def return_all_data(self):
        # print(dumped_data)
        # print(f'>>> {self.dumped_data}')
        return self.dumped_data
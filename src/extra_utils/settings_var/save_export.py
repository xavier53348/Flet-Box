###################### CALL GLOBAL VAR #############
from ..settings_var.settings_widget import GLOBAL_VAR
####################################################
import flet as ft
import json
####################################################
from flet_core.embed_json_encoder import EmbedJsonEncoder


class WrapWidgetNode():
    container_string_node = ''
    contents__string_node = ''
    tmp_controls_all_node = []

    def __init__(self,):
        super().__init__()

        self.show_tree_nodews(widget_show=GLOBAL_VAR(get_global_var='EXPORT_DATA_PHONE'))

    def show_tree_nodews(self,widget_show):
        """
        BUILDER TREE WITH ALL WIDGET INSIDE CALLING ONE BY ONE
        TO MAKE A TREE WITH ALL WIDGETS OREDERER


        container_string_node = ''                  # CONTAIN MAIN CONTAINER WIDGET
        contents__string_node = ''                  # CONTENT OF MAIN CONTAINER
        tmp_controls_all_node = []                  # LIST WITH ALL WIDGET TO SHOW IN TREVIEW

        self.data = '\n'.join(self.all_data_list)   # WILL TRANSFOR FROM LIST TO STRING

        """
        self.all_widgets = widget_show

        list_controls  = ['row','column','stack','gridview']
        # ##################### >>> 0
        # self.container_string_node = self.main_node
        # self.contents__string_node = self.container_string_node.content
        # self.all_data_list.append(f"0 ⫺ {self.container_string_node._get_control_name()}")
        # self.all_data_list.append(f"0 ⫺ {self.contents__string_node._get_control_name()}")
        # ####################################################################################
        self.all_data_list = []

        for _ in self.all_widgets:
            self.main_node = self.all_widgets.get(_)
            self.container_string_node = self.main_node
            self.contents__string_node = self.container_string_node.content

            # self.all_data_list.append(f"0 ⫺ {self.container_string_node._get_control_name()}")
            self.all_data_list.append(f"🯰 ⫺ █━ {self.contents__string_node._get_control_name()}")

            if self.contents__string_node._get_control_name() in list_controls:
                """ IF IT'S TRUE GET ALL CONTROLS"""
                tmp_controls_all_node = self.contents__string_node.controls
                for _ in tmp_controls_all_node:
                    if _.controls:
                        self.container_string_node = _.controls[0].content
                        self.contents__string_node = self.container_string_node.content

                        # self.all_data_list.append(f"1 ⫺    {self.container_string_node._get_control_name()}")
                        self.all_data_list.append(f"🯱 ⫺ █ ▐━ {self.contents__string_node._get_control_name()}")

                        if self.contents__string_node._get_control_name() in list_controls:
                            """ IF TRUE GET ALL CONTROLS"""
                            tmp_controls_all_node = self.contents__string_node.controls

                            for _ in tmp_controls_all_node:
                                if _.controls:
                                    self.container_string_node = _.controls[0].content
                                    self.contents__string_node = self.container_string_node.content

                                    # self.all_data_list.append(f"2 ⫺        {self.container_string_node._get_control_name()}")
                                    self.all_data_list.append(f"🯲 ⫺ █ ▐  ▐━ {self.contents__string_node._get_control_name()}")

                                    if self.contents__string_node._get_control_name() in list_controls:
                                        """ IF TRUE GET ALL CONTROLS"""
                                        tmp_controls_all_node = self.contents__string_node.controls

                                        for _ in tmp_controls_all_node:
                                            if _.controls:
                                                self.container_string_node = _.controls[0].content
                                                self.contents__string_node = self.container_string_node.content

                                                # self.all_data_list.append(f"3 ⫺            {self.container_string_node._get_control_name()}")
                                                self.all_data_list.append(f"🯳 ⫺ █ ▐  ▐  ▐━ {self.contents__string_node._get_control_name()}")

                                                if self.contents__string_node._get_control_name() in list_controls:
                                                    """ IF TRUE GET ALL CONTROLS"""
                                                    tmp_controls_all_node = self.contents__string_node.controls

                                                    for _ in tmp_controls_all_node:
                                                        if _.controls:
                                                            self.container_string_node = _.controls[0].content
                                                            self.contents__string_node = self.container_string_node.content

                                                            # self.all_data_list.append(f"4 ⫺                {self.container_string_node._get_control_name()}")
                                                            self.all_data_list.append(f"🯴 ⫺ █ ▐  ▐  ▐  ▐━ {self.contents__string_node._get_control_name()}")

                                                            if self.contents__string_node._get_control_name() in list_controls:
                                                                """ IF TRUE GET ALL CONTROLS"""
                                                                tmp_controls_all_node = self.contents__string_node.controls

                                                                for _ in tmp_controls_all_node:
                                                                    if _.controls:
                                                                        self.container_string_node = _.controls[0].content
                                                                        self.contents__string_node = self.container_string_node.content

                                                                        # self.all_data_list.append(f"5 ⫺                    {self.container_string_node._get_control_name()}")
                                                                        self.all_data_list.append(f"🯵 ⫺ █ ▐  ▐  ▐  ▐  ▐━ {self.contents__string_node._get_control_name()}")

                                                                        if self.contents__string_node._get_control_name() in list_controls:
                                                                            """ IF TRUE GET ALL CONTROLS"""
                                                                            tmp_controls_all_node = self.contents__string_node.controls

                                                                            for _ in tmp_controls_all_node:
                                                                                if _.controls:
                                                                                    self.container_string_node = _.controls[0].content
                                                                                    self.contents__string_node = self.container_string_node.content

                                                                                    # self.all_data_list.append(f"6 ⫺                        {self.container_string_node._get_control_name()}")
                                                                                    self.all_data_list.append(f"🯶 ⫺ █ ▐  ▐  ▐  ▐  ▐  ▐━ {self.contents__string_node._get_control_name()}")

                                                                                    if self.contents__string_node._get_control_name() in list_controls:
                                                                                        """ IF TRUE GET ALL CONTROLS"""
                                                                                        tmp_controls_all_node = self.contents__string_node.controls

                                                                                        for _ in tmp_controls_all_node:
                                                                                            if _.controls:
                                                                                                self.container_string_node = _.controls[0].content
                                                                                                self.contents__string_node = self.container_string_node.content

                                                                                                # self.all_data_list.append(f"7 ⫺                            {self.container_string_node._get_control_name()}")
                                                                                                self.all_data_list.append(f"🯷 ⫺ █ ▐  ▐  ▐  ▐  ▐  ▐  ▐━ {self.contents__string_node._get_control_name()}")

                                                                                                if self.contents__string_node._get_control_name() in list_controls:
                                                                                                    """ IF TRUE GET ALL CONTROLS"""
                                                                                                    tmp_controls_all_node = self.contents__string_node.controls

                                                                                                    for _ in tmp_controls_all_node:
                                                                                                        if _.controls:
                                                                                                            self.container_string_node = _.controls[0].content
                                                                                                            self.contents__string_node = self.container_string_node.content

                                                                                                            # self.all_data_list.append(f"8 ⫺                                {self.container_string_node._get_control_name()}")
                                                                                                            self.all_data_list.append(f"🯸 ⫺ █ ▐  ▐  ▐  ▐  ▐  ▐  ▐  ▐━ {self.contents__string_node._get_control_name()}")

                                                                                                            if self.contents__string_node._get_control_name() in list_controls:
                                                                                                                """ IF TRUE GET ALL CONTROLS"""
                                                                                                                tmp_controls_all_node = self.contents__string_node.controls

                                                                                                                for _ in tmp_controls_all_node:
                                                                                                                    if _.controls:
                                                                                                                        self.container_string_node = _.controls[0].content
                                                                                                                        self.contents__string_node = self.container_string_node.content

                                                                                                                        # self.all_data_list.append(f"9 ⫺                                    {self.container_string_node._get_control_name()}")
                                                                                                                        self.all_data_list.append(f"🯹 ⫺ █ ▐  ▐  ▐  ▐  ▐  ▐  ▐  ▐  ▐━ {self.contents__string_node._get_control_name()}")

                                                                                                                        # if self.contents__string_node._get_control_name() in list_controls:
                                                                                                                        #     """ IF TRUE GET ALL CONTROLS"""
                                                                                                                        #     tmp_controls_all_node = self.contents__string_node.controls

                                                                                                                        #     for _ in tmp_controls_all_node:
                                                                                                                        #         self.container_string_node = _.controls[0].content
                                                                                                                        #         self.contents__string_node = self.container_string_node.content

                                                                                                                        #         # self.all_data_list.append(f"1 ⫺0                                        {self.container_string_node._get_control_name()}")
                                                                                                                        #         self.all_data_list.append(f"🯰 ⫺ █ ▐  ▐  ▐  ▐  ▐  ▐  ▐  ▐  ▐  └──{self.contents__string_node._get_control_name()}")

        ####################################################################################
        # for _ in self.all_data_list:
        #     print(_)
        # print(self.all_data_list)
        self.data = '\n'.join(self.all_data_list)
        return self.data

class MakeJasonFile():


    def __init__(self,):
        super().__init__()
        self.build_json_file(widget_show=GLOBAL_VAR(get_global_var='EXPORT_DATA_PHONE'))


    def return_view(self,main_node):

        """ return {'_1':'Container','_2':'Image'}"""

        #################### ID ####################################
        self._uid_box  = self.main_node.uid
        self._uid_con  = self.main_node.content.uid
        #################### NAME
        self._name_box  = self.main_node._get_control_name().capitalize()                 #change _get_control_name() by attributes
        self._name_con  = self.main_node.content._get_control_name().capitalize()         #change _get_control_name() by attributes
        #################### NAME
        self._box_tag  = self.main_node.tooltip                 #change _get_control_name() by attributes
        self._con_tag  = self.main_node.content.tooltip         #change _get_control_name() by attributes        #################### UPDATE DICT
        #################### TOOLTIP
        self.dict_all_names[self._box_tag] = {self._uid_box : self._name_box }
        self.dict_all_names[self._box_tag].update({self._uid_con : self._name_con })
        # self.dict_all_names[self._name_box] = {self._uid_con : self._name_con }
        # self.dict_all_names.update({self._box_tag:{self._uid_con : self._name_con }})
        ############################################################

    def return_attributes_code(self,main_node):

        """ return {'_1':'Attributes','_2':'Attributes'}"""
        #################### Create a copy
        self.attributes = {}
        self.attributes_content = {}
        #################### ID ####################################
        self._uid_box  = self.main_node.uid
        self._uid_con  = self.main_node.content.uid
        #################### NAME
        self.main_node.copy_attrs(dest=self.attributes)
        self.main_node.content.copy_attrs(dest=self.attributes_content)
        #################### UPDATE DICT
        self.dict_all_attribute[self._uid_box] = self.attributes
        self.dict_all_attribute[self._uid_con] = self.attributes_content
        ############################################################

    def return_full_code(self,main_node,tab_one = 4 ,tab_two=4  ,tab_tree=4):

        """ return {'_1':'Attributes','_2':'Attributes'}"""
        #################### Create a copy
        self.attributes = {}
        self.attributes_content = {}
        #################### ID ###################
        self._uid_box  = self.main_node.uid
        self._uid_con  = self.main_node.content.uid
        #################### NAME
        self._name_box  = self.main_node._get_control_name().capitalize()                 #change _get_control_name() by attributes
        self._name_con  = self.main_node.content._get_control_name().capitalize()         #change _get_control_name() by attributes
        #################### NAME
        self.main_node.copy_attrs(dest=self.attributes)
        self.main_node.content.copy_attrs(dest=self.attributes_content)
        ########################################### single content
        tab_ = '\t'

        list_controls      = ['Row','Column','Stack','Gridview']

        if not self._name_con in list_controls:
            """ if is a normal widget"""
            self.all_code_list.append(f"{tab_*tab_one}ft.{self._name_box}(")
            self.all_code_list.append(f"{tab_*tab_two}self.json_style('{self._uid_box}'),")
            self.all_code_list.append(f"{tab_*tab_two}content = ft.{self._name_con}(")
            self.all_code_list.append(f"{tab_*tab_tree}self.json_style('{self._uid_con}'),")
            self.all_code_list.append(f"{tab_*tab_tree}),")
        else:
            self.all_code_list.append(f"{tab_*tab_one}ft.{self._name_box}(")
            self.all_code_list.append(f"{tab_*tab_two}self.json_style('{self._uid_box}'),")
            self.all_code_list.append(f"{tab_*tab_two}content = ft.{self._name_con}(")
            self.all_code_list.append(f"{tab_*tab_tree}self.json_style('{self._uid_con}'),")
            self.all_code_list.append(f"{tab_*tab_tree}controls = [")

    def build_json_file(self,widget_show):
        # GET GLOBVAL VAR OF MAIN PHONE ATTRIBUTES
        self.all_widgets        = widget_show
        self.dict_all_names     = dict()
        self.dict_all_attribute = dict()
        self.all_code_list      = list()


        list_controls      = ['row','column','stack','gridview']
        for _ in self.all_widgets:
            # LEVEL 0
            tmp = {}

            self.main_node                        = self.all_widgets.get(_)                            # get main widget
            self.return_view(main_node            = self.main_node)       # get main name
            self.return_attributes_code(main_node = self.main_node) # get widget attributes
            self.return_full_code(main_node       = self.main_node ,tab_one=0,tab_two=8,tab_tree=16) # get widget attributes

            # LEVEL 1
            self.contents__string_node = self.main_node.content
            if self.contents__string_node._get_control_name() in list_controls:
                tmp_controls_all_node = self.contents__string_node.controls
                for _ in tmp_controls_all_node:
                    if _.controls:
                        self.main_node = _.controls[0].content
                        self.return_view(main_node            = self.main_node )       # get main name
                        self.return_attributes_code(main_node = self.main_node ) # get widget attributes
                        self.return_full_code(main_node       = self.main_node ,tab_one=24,tab_two=32,tab_tree=40) # get widget attributes

                        # LEVEL 2
                        self.contents__string_node = self.main_node.content
                        if self.contents__string_node._get_control_name() in list_controls:
                            tmp_controls_all_node = self.contents__string_node.controls
                            for _ in tmp_controls_all_node:
                                if _.controls:
                                    self.main_node = _.controls[0].content
                                    self.return_view(main_node            = self.main_node )       # get main name
                                    self.return_attributes_code(main_node = self.main_node ) # get widget attributes
                                    self.return_full_code(main_node       = self.main_node ,tab_one=48,tab_two=56,tab_tree=64) # get widget attributes

                                    # LEVEL 3
                                    self.contents__string_node = self.main_node.content
                                    if self.contents__string_node._get_control_name() in list_controls:
                                        tmp_controls_all_node = self.contents__string_node.controls
                                        for _ in tmp_controls_all_node:
                                            if _.controls:
                                                self.main_node = _.controls[0].content
                                                self.return_view(main_node            = self.main_node )       # get main name
                                                self.return_attributes_code(main_node = self.main_node ) # get widget attributes
                                                self.return_full_code(main_node       = self.main_node ,tab_one=72,tab_two=80,tab_tree=88) # get widget attributes

                                                # LEVEL 4
                                                self.contents__string_node = self.main_node.content
                                                if self.contents__string_node._get_control_name() in list_controls:
                                                    tmp_controls_all_node = self.contents__string_node.controls
                                                    for _ in tmp_controls_all_node:
                                                        if _.controls:
                                                            self.main_node = _.controls[0].content
                                                            self.return_view(main_node            = self.main_node )       # get main name
                                                            self.return_attributes_code(main_node = self.main_node ) # get widget attributes
                                                            self.return_full_code(main_node       = self.main_node ,tab_one=80,tab_two=88,tab_tree=96) # get widget attributes

        ######################################################################################
                                                    self.all_code_list.append(f"{' '*80}],),")  # LEVEL 4
                                        self.all_code_list.append(f"{' '*64}],),")  # LEVEL 3
                            self.all_code_list.append(f"{' '*48}],),")      # LEVEL 2
                self.all_code_list.append(f"{' '*32}],),")          # LEVEL 1
        self.all_code_list.append(f"{' '*16}),")             # LEVEL 0

        ##############################
        # self.full_code_json = '\n'.join(self.all_code_list)
        # self.json_file = json.dumps(self.dict_all_names,cls=EmbedJsonEncoder, indent=4 ,separators=(",", ":"))
        # self.json_file = self.json_file.replace('"_', '<b>_ </b>')
        ############
        # return self.json_file
        # return  json.dumps(self.dict_all_names, indent=4)
        # return  json.dumps(self.dict_all_attribute, indent=4)
        # return self.full_code_json

        self.main_code  =  '\n'.join(self.all_code_list)
        self.second    = json.dumps(self.dict_all_names,     indent=4 , cls=EmbedJsonEncoder ,separators=(",", ":"))

        self.thirds    = json.dumps(self.dict_all_attribute, indent=4 , cls=EmbedJsonEncoder ,separators=(",", ":"))
        self.thirds    = self.thirds.replace('\\', '')


        return {'main_code': f"\n\n{self.main_code}",'second': f"\n\n{self.second}",'thirds':f"\n\n{self.thirds}"}
        ###########################################
    # def before_update(self):
    #     super().before_update()
    #     self._set_attr_json("codeStyle", self.__code_style)
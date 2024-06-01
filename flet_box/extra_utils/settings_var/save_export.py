from flet_core.embed_json_encoder import EmbedJsonEncoder
from ..settings_var.settings_widget import GLOBAL_VAR
from ..menu_tab_up_phone.skeleton_class_screens import get_skeleton

import flet as ft
import json

class WrapWidgetNode():

    container_string_node = ''
    contents__string_node = ''
    tmp_controls_all_node = []

    def __init__(self,):
        super().__init__()

        # data = GLOBAL_VAR(get_global_var='EXPORT_DATA_PHONE')
        self.show_tree_nodews(widget_show=GLOBAL_VAR(get_global_var='EXPORT_DATA_PHONE'))
        # print(data)

    def show_tree_nodews(self,widget_show):
        """
        BUILDER TREE WITH ALL WIDGET INSIDE CALLING ONE BY ONE
        TO MAKE A TREE WITH ALL WIDGETS OREDERER


        container_string_node = ''                  #: CONTAIN MAIN CONTAINER WIDGET
        contents__string_node = ''                  #: CONTENT OF MAIN CONTAINER
        tmp_controls_all_node = []                  #: LIST WITH ALL WIDGET TO SHOW IN TREVIEW

        self.data = '\n'.join(self.all_data_list)   #: WILL TRANSFOR FROM LIST TO STRING

        """
        self.all_widgets = widget_show
        print(self.all_widgets,'hello')

        list_controls  = ['row','column','stack','gridview']

        #: self.container_string_node = self.main_node
        #: self.contents__string_node = self.container_string_node.content
        #: self.all_data_list.append(f"0 ⫺ {self.container_string_node._get_control_name()}")
        #: self.all_data_list.append(f"0 ⫺ {self.contents__string_node._get_control_name()}")

        self.all_data_list = []

        for _ in self.all_widgets:
            self.main_node = self.all_widgets.get(_)
            self.container_string_node = self.main_node
            self.contents__string_node = self.container_string_node.content

            #: self.all_data_list.append(f"0 ⫺ {self.container_string_node._get_control_name()}")
            self.all_data_list.append(f"🯰 ⫺ █━ {self.contents__string_node._get_control_name()}")

            if self.contents__string_node._get_control_name() in list_controls:
                """ IF IT'S TRUE GET ALL CONTROLS"""
                tmp_controls_all_node = self.contents__string_node.controls
                for _ in tmp_controls_all_node:
                    if _.controls:
                        self.container_string_node = _.controls[0].content
                        self.contents__string_node = self.container_string_node.content

                        #: self.all_data_list.append(f"1 ⫺    {self.container_string_node._get_control_name()}")
                        self.all_data_list.append(f"🯱 ⫺ █ ▐━ {self.contents__string_node._get_control_name()}")

                        if self.contents__string_node._get_control_name() in list_controls:
                            """ IF TRUE GET ALL CONTROLS"""
                            tmp_controls_all_node = self.contents__string_node.controls

                            for _ in tmp_controls_all_node:
                                if _.controls:
                                    self.container_string_node = _.controls[0].content
                                    self.contents__string_node = self.container_string_node.content

                                    #: self.all_data_list.append(f"2 ⫺        {self.container_string_node._get_control_name()}")
                                    self.all_data_list.append(f"🯲 ⫺ █ ▐  ▐━ {self.contents__string_node._get_control_name()}")

                                    if self.contents__string_node._get_control_name() in list_controls:
                                        """ IF TRUE GET ALL CONTROLS"""
                                        tmp_controls_all_node = self.contents__string_node.controls

                                        for _ in tmp_controls_all_node:
                                            if _.controls:
                                                self.container_string_node = _.controls[0].content
                                                self.contents__string_node = self.container_string_node.content

                                                #: self.all_data_list.append(f"3 ⫺            {self.container_string_node._get_control_name()}")
                                                self.all_data_list.append(f"🯳 ⫺ █ ▐  ▐  ▐━ {self.contents__string_node._get_control_name()}")

                                                if self.contents__string_node._get_control_name() in list_controls:
                                                    """ IF TRUE GET ALL CONTROLS"""
                                                    tmp_controls_all_node = self.contents__string_node.controls

                                                    for _ in tmp_controls_all_node:
                                                        if _.controls:
                                                            self.container_string_node = _.controls[0].content
                                                            self.contents__string_node = self.container_string_node.content

                                                            #: self.all_data_list.append(f"4 ⫺                {self.container_string_node._get_control_name()}")
                                                            self.all_data_list.append(f"🯴 ⫺ █ ▐  ▐  ▐  ▐━ {self.contents__string_node._get_control_name()}")

                                                            if self.contents__string_node._get_control_name() in list_controls:
                                                                """ IF TRUE GET ALL CONTROLS"""
                                                                tmp_controls_all_node = self.contents__string_node.controls

                                                                for _ in tmp_controls_all_node:
                                                                    if _.controls:
                                                                        self.container_string_node = _.controls[0].content
                                                                        self.contents__string_node = self.container_string_node.content

                                                                        #: self.all_data_list.append(f"5 ⫺                    {self.container_string_node._get_control_name()}")
                                                                        self.all_data_list.append(f"🯵 ⫺ █ ▐  ▐  ▐  ▐  ▐━ {self.contents__string_node._get_control_name()}")

                                                                        if self.contents__string_node._get_control_name() in list_controls:
                                                                            """ IF TRUE GET ALL CONTROLS"""
                                                                            tmp_controls_all_node = self.contents__string_node.controls

                                                                            for _ in tmp_controls_all_node:
                                                                                if _.controls:
                                                                                    self.container_string_node = _.controls[0].content
                                                                                    self.contents__string_node = self.container_string_node.content

                                                                                    #: self.all_data_list.append(f"6 ⫺                        {self.container_string_node._get_control_name()}")
                                                                                    self.all_data_list.append(f"🯶 ⫺ █ ▐  ▐  ▐  ▐  ▐  ▐━ {self.contents__string_node._get_control_name()}")

                                                                                    if self.contents__string_node._get_control_name() in list_controls:
                                                                                        """ IF TRUE GET ALL CONTROLS"""
                                                                                        tmp_controls_all_node = self.contents__string_node.controls

                                                                                        for _ in tmp_controls_all_node:
                                                                                            if _.controls:
                                                                                                self.container_string_node = _.controls[0].content
                                                                                                self.contents__string_node = self.container_string_node.content

                                                                                                #: self.all_data_list.append(f"7 ⫺                            {self.container_string_node._get_control_name()}")
                                                                                                self.all_data_list.append(f"🯷 ⫺ █ ▐  ▐  ▐  ▐  ▐  ▐  ▐━ {self.contents__string_node._get_control_name()}")

                                                                                                if self.contents__string_node._get_control_name() in list_controls:
                                                                                                    """ IF TRUE GET ALL CONTROLS"""
                                                                                                    tmp_controls_all_node = self.contents__string_node.controls

                                                                                                    for _ in tmp_controls_all_node:
                                                                                                        if _.controls:
                                                                                                            self.container_string_node = _.controls[0].content
                                                                                                            self.contents__string_node = self.container_string_node.content

                                                                                                            #: self.all_data_list.append(f"8 ⫺                                {self.container_string_node._get_control_name()}")
                                                                                                            self.all_data_list.append(f"🯸 ⫺ █ ▐  ▐  ▐  ▐  ▐  ▐  ▐  ▐━ {self.contents__string_node._get_control_name()}")

                                                                                                            if self.contents__string_node._get_control_name() in list_controls:
                                                                                                                """ IF TRUE GET ALL CONTROLS"""
                                                                                                                tmp_controls_all_node = self.contents__string_node.controls

                                                                                                                for _ in tmp_controls_all_node:
                                                                                                                    if _.controls:
                                                                                                                        self.container_string_node = _.controls[0].content
                                                                                                                        self.contents__string_node = self.container_string_node.content

                                                                                                                        #: self.all_data_list.append(f"9 ⫺                                    {self.container_string_node._get_control_name()}")
                                                                                                                        self.all_data_list.append(f"🯹 ⫺ █ ▐  ▐  ▐  ▐  ▐  ▐  ▐  ▐  ▐━ {self.contents__string_node._get_control_name()}")

                                                                                                                        #: if self.contents__string_node._get_control_name() in list_controls:
                                                                                                                        #:     """ IF TRUE GET ALL CONTROLS"""
                                                                                                                        #:     tmp_controls_all_node = self.contents__string_node.controls

                                                                                                                        #:     for _ in tmp_controls_all_node:
                                                                                                                        #:         self.container_string_node = _.controls[0].content
                                                                                                                        #:         self.contents__string_node = self.container_string_node.content

                                                                                                                        #:         #: self.all_data_list.append(f"1 ⫺0                                        {self.container_string_node._get_control_name()}")
                                                                                                                        #:         self.all_data_list.append(f"🯰 ⫺ █ ▐  ▐  ▐  ▐  ▐  ▐  ▐  ▐  ▐  └──{self.contents__string_node._get_control_name()}")


        #: for _ in self.all_data_list:
        #:     print(_)
        #: print(self.all_data_list)

        self.data = '\n'.join(self.all_data_list)

        return self.data

class MakeJasonFile():

    def __init__(self,):
        super().__init__()
        self.build_json_file(widget_show=GLOBAL_VAR(get_global_var='EXPORT_DATA_PHONE'))

    def return_view(self,main_node):

        """ return {'_1':'Container','_2':'Image'}"""

        #: ID

        self._uid_box  = self.main_node.uid
        self._uid_con  = self.main_node.content.uid

        #: NAME

        self._name_box  = self.main_node._get_control_name().capitalize()                   #: change _get_control_name() by attributes
        self._name_con  = self.main_node.content._get_control_name().capitalize()           #: change _get_control_name() by attributes

        #: NAME

        self._box_tag  = self.main_node.tooltip                                             #: change _get_control_name() by attributes
        self._con_tag  = self.main_node.content.tooltip                                     #: change _get_control_name() by attributes #: UPDATE DICT

        #: TOOLTIP

        self.dict_all_names[self._box_tag] = {self._uid_box : self._name_box }
        self.dict_all_names[self._box_tag].update({self._uid_con : self._name_con })

    def return_attributes_code(self,main_node):

        #: return {'_1':'Attributes','_2':'Attributes'}
        #: Create a copy

        self.attributes = {}
        self.attributes_content = {}
        self.atipic_attributes = {}
        self.atipic_attributes_2 = {}

        #: ID

        self._uid_box  = self.main_node.uid
        self._uid_con  = self.main_node.content.uid

        #: NAME
        self.attributes.update({'WIDGET_NAME':f'CONTAINER_{self.main_node.content._get_control_name().upper()}'})
        self.main_node.copy_attrs(dest=self.attributes)

        #: NAME CONTENT
        self.attributes_content.update({'WIDGET_NAME':f'CONTENT_{self.main_node.content._get_control_name().upper()}'})
        self.main_node.content.copy_attrs(dest=self.attributes_content)

        if (self.main_node.content._get_control_name() == 'chip'):                    #: SPECIAL WIDGET THAT CONTAIN MORE WIDGETS INSIDE
            #: SPECIAL WIDGET
            self.main_node.content.label.copy_attrs(dest=self.atipic_attributes)
            del self.atipic_attributes['n']
            self.dict_all_attribute[self.main_node.content.label.uid]   = self.atipic_attributes

            self.main_node.content.leading.copy_attrs(dest=self.atipic_attributes_2)
            del self.atipic_attributes_2['n']
            self.dict_all_attribute[self.main_node.content.leading.uid] = self.atipic_attributes_2

        if (self.main_node.content._get_control_name() == 'radiogroup'):                    #: SPECIAL WIDGET THAT CONTAIN MORE WIDGETS INSIDE
            #: SPECIAL WIDGET
            # self.main_node.content.label.copy_attrs(dest=self.atipic_attributes)
            # del self.atipic_attributes['n']
            # self.dict_all_attribute[self.main_node.content.controls.uid]   = self.atipic_attributes

            # self.main_node.content.leading.copy_attrs(dest=self.atipic_attributes_2)
            # del self.atipic_attributes_2['n']
            # self.dict_all_attribute[self.main_node.content.leading.uid] = self.atipic_attributes_2
            ...

        #: DEL 'n':'content' from dict
        del self.attributes['n']
        del self.attributes['onclick']
        del self.attributes['onhover']
        del self.attributes_content['n']

        if self.attributes.get('style'):
            del self.attributes['style']

        if self.attributes_content.get('style'):
            del self.attributes_content['style']

        if self.main_node._get_control_name() not in ['container','row','column','stack','gridview']:
            del self.attributes_content['onclick']
            del self.attributes_content['onhover']



        #: UPDATE DICT

        self.dict_all_attribute[self._uid_box] = self.attributes
        self.dict_all_attribute[self._uid_con] = self.attributes_content

        #: TESTING
        # print(self.attributes)
        # print(self.main_node.content._get_control_name())
        # print(self.main_node.content.label.uid)
        # print(self.main_node.content.label)

    def return_full_code(self,main_node,tab_one = 4 ,tab_two=4  ,tab_tree=4 ,check = True):

        """ return {'_1':'Attributes','_2':'Attributes'}"""

        #: Create a copy

        self.attributes = {}
        self.attributes_content = {}

        #: ID

        self._uid_box  = self.main_node.uid
        self._uid_con  = self.main_node.content.uid

        #: NAME

        self._name_box  = self.main_node._get_control_name().capitalize()                 #: change _get_control_name() by attributes
        self._name_con  = self.main_node.content._get_control_name().capitalize()         #: change _get_control_name() by attributes

        #: NAME
        self.main_node.copy_attrs(dest=self.attributes)
        self.main_node.content.copy_attrs(dest=self.attributes_content)

        #: single content

        tab_ = '\t'
        list_controls      = ['Row','Column','Stack','Gridview']

        # TESTING
        # print(self.main_node.content.label)

        if not self._name_con in list_controls:
            """ if is a normal widget

            self.all_code_list.append(f"{tab_*tab_one}ft.{self._name_box}(")
            self.all_code_list.append(f"{tab_*tab_two}self.self.dict_style('{self._uid_box}'),")
            self.all_code_list.append(f"{tab_*tab_two}content = ft.{self._name_con}(")
            self.all_code_list.append(f"{tab_*tab_tree}self.self.dict_style('{self._uid_con}'),")
            self.all_code_list.append(f"{tab_*(tab_tree-2)}),),")

            """
            self.all_code_list.append(f"{tab_*tab_one}ft.{self._name_box}( # {self._name_con}")                               #: CONTAINER WIDGET
            self.all_code_list.append(f"{tab_*tab_two}**self.dict_style('{self._uid_box}'),")                                 #: CONTAINER STYLE

            #: CONDITION
            list_condition: list = ['Image','Circleavatar',"Icon","Textfield"]
            no_press_condition: list = ["Column","Stack","Container",'Row',"Textfield","Divider",
                                        "Verticaldivider","Checkbox","Cupertinocheckbox","Radiogroup",
                                        "Switch","Cupertinoslider","Text"]

            print(self._name_con)

            if self._name_con in list_condition and not self._name_con in no_press_condition:
                self.all_code_list.append(f"{tab_*tab_two}on_click= lambda _: event{self._uid_con}(data='{self._uid_con}'),")     #: ALL CALL EVENTS IN ONE LIST
            else:
                self.all_code_list.append(f"{tab_*tab_two}# on_click= lambda _: event{self._uid_con}(data='{self._uid_con}'),")     #: ALL CALL EVENTS IN ONE LIST

            self.all_code_list.append(f"{tab_*tab_two}content= ft.{self._name_con}(")                                         #: SELECTED WIDGET
            self.all_code_list.append(f"{tab_*tab_tree}**self.dict_style('{self._uid_con}'),")                                #: CONTENT STYLE

            if self._name_con in list_condition:
                self.all_code_list.append(f"{tab_*tab_tree}# on_click= lambda _: event{self._uid_con}(data='{self._uid_con}'),")  #: ALL CALL EVENTS IN ONE LIST
            else:
                if not self._name_con in no_press_condition:
                    self.all_code_list.append(f"{tab_*tab_tree}on_click= lambda _: event{self._uid_con}(data='{self._uid_con}'),")  #: ALL CALL EVENTS IN ONE LIST
                else:
                    self.all_code_list.append(f"{tab_*tab_tree}# on_click= lambda _: event{self._uid_con}(data='{self._uid_con}'),")  #: ALL CALL EVENTS IN ONE LIST

            #: SOME WIDGETS
            if self._name_con == 'Chip':
                self.all_code_list.append(f"{tab_*(tab_tree+2)}label= ft.Text(**self.dict_style('{self.main_node.content.label.uid}')),")   #: ALL CALL EVENTS IN ONE LIST
                self.all_code_list.append(f"{tab_*(tab_tree+2)}leading= ft.Icon(**self.dict_style('{self.main_node.content.leading.uid}')),")   #: ALL CALL EVENTS IN ONE LIST

            #: VERY IMPORTANT THIS CODE BECOUSE MANAGE ALL EVENT CODE IN THIS SECTION
            #: CONTINUE EXPECIAL ATTRIBUTES
            self.all_code_list.append(f"{tab_*(tab_tree-2)}),),\n")

            #:RECODING  ALL EVENTS IN ONE LIST FROM SKELETON CLASS SCREEN
            event_manager = get_skeleton(name="event_skeleton")
            event_manager = event_manager.replace('RENAME', self._uid_con)    #: EVENT ID NUMBER
            event_manager = event_manager.replace('NAME_ID',self._name_con)   #: EVENT ID NAME

            self.all_events_list.append(event_manager)

        else:
            if check:
                """
                self.all_code_list.append(f"{tab_*tab_one}ft.{self._name_box}(")
                self.all_code_list.append(f"{tab_*tab_two}self.self.dict_style('{self._uid_box}'),")
                self.all_code_list.append(f"{tab_*tab_two}content = ft.{self._name_con}(")
                self.all_code_list.append(f"{tab_*tab_tree}self.self.dict_style('{self._uid_con}'),")
                self.all_code_list.append(f"{tab_*tab_tree}controls = [")
                """
                self.all_code_list.append(f"{tab_*tab_one}ft.{self._name_box}(  # {self._name_box}_{self._name_con}")
                self.all_code_list.append(f"{tab_*tab_two}**self.dict_style('{self._uid_box}'),")
                self.all_code_list.append(f"{tab_*tab_two}content= ft.{self._name_con}( # {self._name_con}")
                self.all_code_list.append(f"{tab_*tab_tree}**self.dict_style('{self._uid_con}'),")
                self.all_code_list.append(f"{tab_*tab_tree}controls= [\n")

    def build_json_file(self,widget_show):

        #: GET GLOBAL VAR OF MAIN PHONE ATTRIBUTES

        self.all_widgets        = widget_show
        self.dict_all_names     = dict()
        self.dict_all_attribute = dict()
        self.all_code_list      = list()
        self.all_events_list    = list()

        tab_ = '\t'
        list_controls      = ['row','column','stack','gridview']

        #: LAYERS IN FLET_BOX
        check_second   = True
        check_second_2 = True
        check_second_3 = True
        check_second_4 = True
        check_second_5 = True
        check_second_6 = True
        check_second_7 = True
        check_second_8 = True

        #: testing data
        # PHONE_MAIN      = GLOBAL_VAR(get_global_var='PHONE_MAIN')
        # PHONE_CONTAINER = GLOBAL_VAR(get_global_var='PHONE_CONTAINER')
        # PHONE_COLUMN    = PHONE_CONTAINER.content

        # print(PHONE_MAIN)
        # #: THIS CODE IS ONE EXTRACT OF PHONE NECCESARY TO HAVE PHONE ATTRIBUES BY DEFAULD
        # tmp_data_1 = dict()                                       #: TMP DICT()
        # tmp_data_2 = dict()                                       #: TMP DICT()
        # tmp_data_3 = dict()                                       #: TMP DICT()

        # tmp_data_1.update({'WIDGET_NAME':'PHONE_BOX'})
        # PHONE_MAIN.copy_attrs(dest=tmp_data_1)                    #: NEW COPY ATTRIBUTES
        # if tmp_data_1.get('n'):            del tmp_data_1['n']                                #: DELETE 'n':'content' MAKE ERROR
        # if tmp_data_1.get('border'):       del tmp_data_1['border']                           #: DELETE 'n':'content' MAKE ERROR
        # if tmp_data_1.get('style'):        del tmp_data_1['style']                            #: DELETE 'n':'content' MAKE ERROR
        # if tmp_data_1.get('borderradius'): del tmp_data_1['borderradius']                     #: DELETE 'n':'content' MAKE ERROR

        # self.dict_all_attribute[PHONE_MAIN.uid] = tmp_data_1      #: UPDATE DATA

        # tmp_data_2.update({'WIDGET_NAME':'PHONE_BOX LAYER 2 '})
        # PHONE_CONTAINER.copy_attrs(dest=tmp_data_2)               #: NEW COPY ATTRIBUTES
        # if tmp_data_2.get('n'):            del tmp_data_2['n']                                #: DELETE 'n':'content' MAKE ERROR
        # if tmp_data_2.get('border'):       del tmp_data_2['border']                           #: DELETE 'n':'content' MAKE ERROR
        # if tmp_data_2.get('style'):        del tmp_data_2['style']                            #: DELETE 'n':'content' MAKE ERROR
        # if tmp_data_2.get('borderradius'): del tmp_data_2['borderradius']                     #: DELETE 'n':'content' MAKE ERROR

        # self.dict_all_attribute[PHONE_CONTAINER.uid]=tmp_data_2   #: UPDATE DATA

        # tmp_data_3.update({'WIDGET_NAME':f'PHONE_BOX_{PHONE_CONTAINER.content._get_control_name().upper()}'})
        # PHONE_COLUMN.copy_attrs(dest=tmp_data_3)                  #: NEW COPY ATTRIBUTES
        # if tmp_data_3.get('n'):            del tmp_data_3['n']                               #: DELETE 'n':'content' MAKE ERROR
        # if tmp_data_3.get('style'):        del tmp_data_3['style']                           #: DELETE 'n':'content' MAKE ERROR

        # self.dict_all_attribute[PHONE_COLUMN.uid]=tmp_data_3   #: UPDATE DATA
        # print( self.dict_all_attribute)


        #:
        for _ in self.all_widgets:
            #:LEVEL 0
            tmp = {}

            self.main_node                        = self.all_widgets.get(_)         #:get main widget
            self.return_view(main_node            = self.main_node)                 #:get main name
            self.return_attributes_code(main_node = self.main_node)                 #:get widget attributes
            self.return_full_code(main_node       = self.main_node ,tab_one=2,tab_two=3,tab_tree=5) # get widget attributes

            # print(self.main_node)
            #: LEVEL 1

            self.contents__string_node = self.main_node.content
            if self.contents__string_node._get_control_name() in list_controls:
                tmp_controls_all_node = self.contents__string_node.controls

                #: LAYER 0
                #: CHECK []

                check = self.contents__string_node.controls
                if not check:
                    self.all_code_list.append(f"{tab_*4}],\n{tab_*2}),), #// CLOSE LAYER 0") # get widget attributes

                for _ in tmp_controls_all_node:
                    if _.controls:
                        self.main_node = _.controls[0].content
                        self.return_view(main_node            = self.main_node )       # get main name
                        self.return_attributes_code(main_node = self.main_node ) # get widget attributes
                        self.return_full_code(main_node       = self.main_node ,tab_one=6,tab_two=8,tab_tree=10) # get widget attributes

                        #: LEVEL 2

                        self.contents__string_node = self.main_node.content
                        if self.contents__string_node._get_control_name() in list_controls:
                            tmp_controls_all_node = self.contents__string_node.controls

                            #: LAYER 1
                            #: CHECK []

                            check = self.contents__string_node.controls
                            if not check:
                                self.all_code_list.append(f"{tab_*10}],\n{tab_*8}),), #// CLOSE LAYER 1") # get widget attributes
                                check = True
                                check_second = False
                            #:

                            for _ in tmp_controls_all_node:
                                if _.controls:
                                    self.main_node = _.controls[0].content
                                    self.return_view(main_node            = self.main_node )       #: get main name
                                    self.return_attributes_code(main_node = self.main_node )       #: get widget attributes
                                    self.return_full_code(main_node       = self.main_node ,tab_one=12,tab_two=14,tab_tree=16) # get widget attributes

                                    #: LEVEL 3
                                    self.contents__string_node = self.main_node.content
                                    if self.contents__string_node._get_control_name() in list_controls:
                                        tmp_controls_all_node = self.contents__string_node.controls

                                        #: LAYER 2
                                        #: CHECK []

                                        check = self.contents__string_node.controls
                                        if not check:
                                            self.all_code_list.append(f"{tab_*16}],\n{tab_*14}),), #// CLOSE LAYER 2") # get widget attributes
                                            check = True
                                            check_second_2 = False

                                        for _ in tmp_controls_all_node:
                                            if _.controls:
                                                self.main_node = _.controls[0].content
                                                self.return_view(main_node            = self.main_node ) #: get main name
                                                self.return_attributes_code(main_node = self.main_node ) #: get widget attributes
                                                self.return_full_code(main_node       = self.main_node ,tab_one=18,tab_two=20,tab_tree=22) # get widget attributes

                                                #: LEVEL 4

                                                self.contents__string_node = self.main_node.content
                                                if self.contents__string_node._get_control_name() in list_controls:
                                                    tmp_controls_all_node = self.contents__string_node.controls

                                                    #: LAYER 3
                                                    #: CHECK []

                                                    check = self.contents__string_node.controls
                                                    if not check:
                                                        self.all_code_list.append(f"{tab_*22}],\n{tab_*20}),), #// CLOSE LAYER 3") # get widget attributes
                                                        check = True
                                                        check_second_3 = False

                                                    for _ in tmp_controls_all_node:
                                                        if _.controls:
                                                            self.main_node = _.controls[0].content
                                                            self.return_view(main_node            = self.main_node ) #: get main name
                                                            self.return_attributes_code(main_node = self.main_node ) #: get widget attributes
                                                            self.return_full_code(main_node       = self.main_node ,tab_one=24,tab_two=26,tab_tree=28) # get widget attributes

                                                            # LEVEL 5

                                                            self.contents__string_node = self.main_node.content
                                                            if self.contents__string_node._get_control_name() in list_controls:
                                                                tmp_controls_all_node = self.contents__string_node.controls

                                                                #: LAYER 4
                                                                #: CHECK []

                                                                check = self.contents__string_node.controls
                                                                if not check:
                                                                    self.all_code_list.append(f"{tab_*28}],\n{tab_*26}),), #// CLOSE LAYER 4") # get widget attributes
                                                                    check          = True
                                                                    check_second_4 = False
                                                                #:


                                                                for _ in tmp_controls_all_node:
                                                                    if _.controls:
                                                                        self.main_node = _.controls[0].content
                                                                        self.return_view(main_node            = self.main_node ) #: get main name
                                                                        self.return_attributes_code(main_node = self.main_node ) #: get widget attributes
                                                                        self.return_full_code(main_node       = self.main_node ,tab_one=30,tab_two=32,tab_tree=34) # get widget attributes

                                                                        #: LEVEL 5

                                                                        self.contents__string_node = self.main_node.content
                                                                        if self.contents__string_node._get_control_name() in list_controls:
                                                                            tmp_controls_all_node = self.contents__string_node.controls

                                                                            #: LAYER 5
                                                                            #: CHECK []

                                                                            check = self.contents__string_node.controls
                                                                            if not check:
                                                                                self.all_code_list.append(f"{tab_*34}],\n{tab_*32}),), #// CLOSE LAYER 5") #: get widget attributes
                                                                                check          = True
                                                                                check_second_5 = False
                                                                            #:


                                                                            for _ in tmp_controls_all_node:
                                                                                if _.controls:
                                                                                    self.main_node = _.controls[0].content
                                                                                    self.return_view(main_node            = self.main_node ) #: get main name
                                                                                    self.return_attributes_code(main_node = self.main_node ) #: get widget attributes
                                                                                    self.return_full_code(main_node       = self.main_node ,tab_one=36,tab_two=38,tab_tree=40) # get widget attributes

                                                                                    #: LEVEL 6

                                                                                    self.contents__string_node = self.main_node.content
                                                                                    if self.contents__string_node._get_control_name() in list_controls:
                                                                                        tmp_controls_all_node = self.contents__string_node.controls

                                                                                        #: LAYER 6
                                                                                        #: CHECK []

                                                                                        check = self.contents__string_node.controls
                                                                                        if not check:
                                                                                            self.all_code_list.append(f"{tab_*40}],\n{tab_*38}),), #// CLOSE LAYER 6") #: get widget attributes
                                                                                            check          = True
                                                                                            check_second_6 = False


                                                                                        #:


                                                                                        for _ in tmp_controls_all_node:
                                                                                            if _.controls:
                                                                                                self.main_node = _.controls[0].content
                                                                                                self.return_view(main_node            = self.main_node ) #: get main name
                                                                                                self.return_attributes_code(main_node = self.main_node ) #: get widget attributes
                                                                                                self.return_full_code(main_node       = self.main_node ,tab_one=42,tab_two=44,tab_tree=46) # get widget attributes

                                                                                                #: LEVEL 7

                                                                                                self.contents__string_node = self.main_node.content
                                                                                                if self.contents__string_node._get_control_name() in list_controls:
                                                                                                    tmp_controls_all_node = self.contents__string_node.controls

                                                                                                    #: LAYER 7
                                                                                                    #: CHECK []

                                                                                                    check = self.contents__string_node.controls
                                                                                                    if not check:
                                                                                                        self.all_code_list.append(f"{tab_*46}],\n{tab_*44}),), #// CLOSE LAYER 7") #: get widget attributes
                                                                                                        check          = True
                                                                                                        check_second_7 = False
                                                                                                    #:

                                                                                                    for _ in tmp_controls_all_node:
                                                                                                        if _.controls:
                                                                                                            self.main_node = _.controls[0].content
                                                                                                            self.return_view(main_node            = self.main_node ) #: get main name
                                                                                                            self.return_attributes_code(main_node = self.main_node ) #: get widget attributes
                                                                                                            self.return_full_code(main_node       = self.main_node ,tab_one=48,tab_two=50,tab_tree=52) # get widget attributes

                                                                                                            #: LEVEL 8

                                                                                                            self.contents__string_node = self.main_node.content
                                                                                                            if self.contents__string_node._get_control_name() in list_controls:
                                                                                                                tmp_controls_all_node = self.contents__string_node.controls

                                                                                                                #: LAYER 8
                                                                                                                #: CHECK []

                                                                                                                check = self.contents__string_node.controls
                                                                                                                if not check:
                                                                                                                    self.all_code_list.append(f"{tab_*52}],\n{tab_*50}),), #// CLOSE LAYER 8") #: get widget attributes
                                                                                                                    check          = True
                                                                                                                    check_second_8 = False
                                                                                                                #:









                                                                                                                #: LAYER 8
                                                                                                                if check and check_second_8:
                                                                                                                    self.all_code_list.append(f"{tab_*36}],),), #// LAYER 8 END")
                                                                                                                    #: check_second_8 = False

                                                                                                                if not check and check_second_8:
                                                                                                                    self.all_code_list.append(f"{tab_*16}],),), #// LAYER 8 END ")

                                                                                                    #: LAYER 7
                                                                                                    if check and check_second_7:
                                                                                                        self.all_code_list.append(f"{tab_*32}],),), #// LAYER 7 END")
                                                                                                        #: check_second_7 = False

                                                                                                    if not check and check_second_7:
                                                                                                        self.all_code_list.append(f"{tab_*14}],),), #// LAYER 7 END ")



                                                                                        #: LAYER 6
                                                                                        if check and check_second_6:
                                                                                            self.all_code_list.append(f"{tab_*28}],),), #// LAYER 6 END")
                                                                                            #: check_second_6 = False

                                                                                        if not check and check_second_6:
                                                                                            self.all_code_list.append(f"{tab_*12}],),), #// LAYER 6 END ")
                                                                                            check_second_6 = True



                                                                            #: LAYER 5
                                                                            if check and check_second_5:
                                                                                self.all_code_list.append(f"{tab_*24}],),), #// LAYER 5 END")
                                                                                #: check_second_5 = False

                                                                            if not check and check_second_5:
                                                                                self.all_code_list.append(f"{tab_*10}],),), #// LAYER 5 END ")
                                                                                check_second_5 = True


                                                                #: LAYER 4
                                                                if check and check_second_4:
                                                                    self.all_code_list.append(f"{tab_*20}],),), #// LAYER 4 END")
                                                                    #: check_second_4 = False

                                                                if not check and check_second_4:
                                                                    self.all_code_list.append(f"{tab_*8}],),), #// LAYER 4 END ")
                                                                    check_second_4 = True

                                                    #: LAYER 3
                                                    if check and check_second_3:
                                                        self.all_code_list.append(f"{tab_*16}],),), #// LAYER 3 END")
                                                        #: check_second_3 = False

                                                    if not check and check_second_3:
                                                        self.all_code_list.append(f"{tab_*6}],),), #// LAYER 3 END ")
                                                        check_second_3 = True

                                        #: LAYER 2
                                        if check and check_second_2:
                                            self.all_code_list.append(f"{tab_*12}],),), #// LAYER 2 END")
                                            #: check_second_2 = False

                                        if not check and check_second_2:
                                            self.all_code_list.append(f"{tab_*4}],),), #// LAYER 2 END")
                                            check_second_2 = True

                            #: LAYER 1
                            if check and check_second:
                                self.all_code_list.append(f"{tab_*8}],),), #// LAYER 1 END")
                                #: check_second = False

                            if not check and check_second:
                                self.all_code_list.append(f"{tab_*2}],),), #// LAYER 1 END")
                                check_second = True

                #: LAYER 0
                if check:
                    self.all_code_list.append(f"{tab_*2}],),),  ") #// LAYER 0 END

        #: BUILDING ALL TO EXPORT DATA

        self.main_code  = '\n'.join(self.all_code_list)                      #: MAIN CODE
        self.main_code  = self.replace_main_code(code=self.main_code)
        #:
        self.event_code = '\n'.join(self.all_events_list)                    #: EVENT CODE
        self.index_code = json.dumps(self.dict_all_names,     indent=4 )     #: INDEX CODE

        #: JOIN MAIN PHONE CONTAINER AND MAIN CONTAINER CONTAINER WITH ALL STYLES IN PHONE

        self.style_code = json.dumps(self.dict_all_attribute, indent=4 )     #: STYLE ATTRIBUTES CODE
        self.style_code = self.recode_style_json(code=self.style_code)

        #: run only in production
        # print(self.all_code_list)

        # for _ in self.all_code_list:
        #     print(_)

        # for _ in self.all_events_list:
        #     print(_)

        return {'main_code': f"\n\n{self.main_code}",'index_code': f"\n\n{self.index_code}",'style_code':f"\n\nstyles={self.style_code}",'event_code':f"\n\n{self.event_code}"}

    def replace_main_code(self,code=''):

        #: new_code = new_code.replace('','')

        new_code = code.replace('Textfield', 'TextField')
        new_code = new_code.replace('Elevatedbutton', 'ElevatedButton').replace('Textbutton', 'TextButton').replace('Iconbutton', 'IconButton').replace('Gridview', 'GridView')
        new_code = new_code.replace('Cupertinocheckbox','CupertinoCheckbox').replace('Cupertinoslider','CupertinoSlider').replace('Cupertinoradio','CupertinoRadio')
        new_code = new_code.replace('Circleavatar','CircleAvatar').replace('Outlinedbutton','OutlinedButton').replace('Verticaldivider','VerticalDivider')
        new_code = new_code.replace('Radiogroup','RadioGroup')

        return new_code

    def recode_style_json(self,code=''):

        #: new_code = new_code.replace('','')

        new_code = code.replace('\\', '').replace('"{', '{').replace('}"', '}').replace('"[', '[').replace(']"', ']')

        #: This line of code is delete in build_json_file
        # new_code = new_code.replace('"n":', '# "n":').replace('"on_hover": "true",','# "on_hover": "false",').replace('"on_click": "true"','# "on_click": "false"').replace('"style"','# "style"')
        new_code = new_code.replace('"onclick":','# "onclick"')
        new_code = new_code.replace('"WIDGET_NAME','# "WIDGET_NAME').replace('"on', '"on_').replace('inkcolor', 'ink_color').replace('"style"','# "style"')
        new_code = new_code.replace('horizontalalignment', 'horizontal_alignment').replace('verticalalignment', 'vertical_alignment')
        new_code = new_code.replace('bordercolor','border_color').replace('borderradius','border_radius').replace('contentpadding','content_padding')
        new_code = new_code.replace('cursorheight','cursor_height').replace('focusedborder_color','focused_border_color').replace('textsize','text_size')
        new_code = new_code.replace('imagefit', 'image_fit').replace('imageopacity', 'image_opacity').replace('imagesrc', 'image_src')
        new_code = new_code.replace('runscount','runs_count').replace('runspacing','run_spacing').replace('backgroundimage_src','background_image_src')
        new_code = new_code.replace('hinttext','hint_text').replace('countertext','counter_text').replace('suffixtext','suffix_text')
        new_code = new_code.replace('urltarget','url_target').replace('semanticslabel','semantics_label').replace('srcbase64','src_base64')
        new_code = new_code.replace('blurradius','blur_radius').replace('spreadradius','spread_radius').replace('childaspect_ratio','child_aspect_ratio')
        new_code = new_code.replace('maxextent','max_extent').replace('minlines','min_lines').replace('maxlines','max_lines').replace('borderwidth','border_width')
        return new_code
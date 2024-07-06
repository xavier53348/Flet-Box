#: MAIN WIDGET SCREEN CLASS
import flet as ft

from .class_menu_screen_styles import styles
from .class_menu_screen_events import *
from .keys_db import index_database
from .keys_all_data_db import all_index_database

ft.colors.WHITE

#: STYLE TO MAIN SCREEN WIDGET
phone_style_widget = {
    "MAIN_CONTAINER": {
        "alignment": {"x":0,"y":0},
        "height": "566",
        "margin": {"l":0,"t":0,"r":0,"b":0},
        "padding": {"l":0,"t":0,"r":0,"b":0},
        "width": "295",
        # "blur": {"sigma_x":20,"sigma_y":20,"tile_mode":"mirror"},
        "bgcolor":"white58",
        "image_src": "RestauranteBuffet.png",
        "image_fit": "cover"
    },
    "MAIN_EFFECTS_CONTAINER": {
        "alignment": {"x":0,"y":0},
        # "bgcolor": "transparent",
        "blur": {"sigma_x":8,"sigma_y":4,"tile_mode":"mirror"},
        "padding": {"l":8,"t":8,"r":8,"b":32}
    },
    "COLUMN_CONTAINER": {
        "scroll": "HIDDEN",
        "spacing": "2"
    }
}

selected_cap:   str = "Capitulo 1"
selected_key:   str = "1.1 Surgimiento y evolución de los servicios gastronómicos."

GLOBAL_VAR(set_global_var={
                            "selected_cap": "Capitulo 1",
                            "selected_key": "1.1 Surgimiento y evolución de los servicios gastronómicos.",
           })

class TextToDocument(ft.Container):
    # globalVar='Erase this test'

    def __init__(self,data='Erase this test',attribute_value: str="" ,value_title: str=""):
        super().__init__()
        # self.title='data'
        self.title=data
        # selected_key = data
        self.value_title = all_index_database.get(value_title)



        # dict_keys: dict = self.dict_style(attribute_value)
        # self: list      = [self.__setattr__(_ , dict_keys.get(_)) for _ in dict_keys]

    def build(self):
        self.content = ft.Container( # Text
                                    **self.dict_style('_4124'),
                                    # on_click= lambda x:print(self.title,self.value_title),
                                    on_click= lambda _: event_4124(data={
                                                                   'title':self.title,
                                                             'value_title':self.value_title,
                                                                   }),

                                    content= ft.Text(
                                            **self.dict_style('_4125'),
                                            value = self.title,
                                            # on_click= lambda _: event_4125(data='_4125'),
                                    ),)

    def class_menu_screen_style(self,code: str=''):
        #: SET MAIN STYLE WIDGET
        return phone_style_widget.get(code)

    def dict_style(self,code: str=''):
        #: SET CONTENT STYLE WIDGET
        return styles.get(code)


class TextData(ft.Container):
    # globalVar='Erase this test'

    def __init__(self,main_key , data='Erase this test',attribute_value: str = "",second_attribute_value: str="1.1 Surgimiento y evolución de los servicios gastronómicos."):
        super().__init__()
        self.main_key = main_key
        self.title=data
        self.second_attribute_value = second_attribute_value
        dict_keys: dict = self.dict_style(attribute_value)
        self: list      = [self.__setattr__(_ , dict_keys.get(_)) for _ in dict_keys]

    def build(self):
        self.content=ft.Text(
                             **self.dict_style(self.second_attribute_value),
                             value = f"{self.title}",
                             )

        self.on_click = lambda _:self.update_secondary_card(data=self.title)


    def class_menu_screen_style(self,code: str=''):
        #: SET MAIN STYLE WIDGET
        return phone_style_widget.get(code)

    def dict_style(self,code: str=''):
        #: SET CONTENT STYLE WIDGET
        return styles.get(code)



    def update_secondary_card(self,data):
        selected_key = data
        text_data.value = selected_key
        text_data.update()
        # print(selected_key)



        class_card_in_row.content.controls[0].content.controls.clear()

        selected_cap = self.main_key

        # print(f"selected_cap {selected_cap} <<<<<<<<")
        # print(f"selected_key {selected_key} <<<<<<<<")


        GLOBAL_VAR(
                   set_global_var={
                                    "selected_cap": selected_cap,
                                    "selected_key": selected_key,
                   })

        for _ in index_database.get(self.main_key).get(selected_key):

            class_card_in_row.content.controls[0].content.controls.append(
                                                                          TextToDocument(data=_,
                                                                                         value_title=index_database.get(self.main_key).get(selected_key).get(_),
                                                                                         attribute_value = '_4124',
                                                                                         )
                                                                          )
        class_card_in_row.content.controls[0].content.update()




    def class_menu_screen_style(self,code: str=''):
        #: SET MAIN STYLE WIDGET
        return phone_style_widget.get(code)

    def dict_style(self,code: str=''):
        #: SET CONTENT STYLE WIDGET
        return styles.get(code)



class class_menu_screen(ft.Container):

    def __init__(self):
        super().__init__()

        dict_keys: dict = self.class_menu_screen_style(code='MAIN_CONTAINER')
        self: list      = [self.__setattr__(_ , dict_keys.get(_)) for _ in dict_keys]

    def build(self):
        global text_data ,class_card_in_row
        text_data = ft.Text(
                        **self.dict_style('_4089'),
                        # on_click= lambda _: event_4089(data='_4089'),
                    )

        self.header_class_row_card = ft.Container(  # Container_Column
                **self.dict_style('_4084'),
                content= ft.Column( # Column
                        **self.dict_style('_4085'),
                        controls= [

                            ft.Container( # Text
                                    **self.dict_style('_4088'),
                                    # on_click= lambda _: event_4089(data='_4089'),
                                    content= text_data,),
            ],),)

        #:
        self.card_class = ft.Container(  # Container_Row
                                **self.dict_style('_4040'),
                                content= ft.Row( # Row
                                        **self.dict_style('_4041'),
                                        controls= [
                                        # self.id_class_main,
                                ],),) #// LAYER 1 END

        #: CLASS ID CONTAINER
        class_card_in_row = ft.Container(  # Container_Column
            **self.dict_style('_4096'),
            content= ft.Column( # Column
                    **self.dict_style('_4097'),
                    controls= [
                            ft.Container(  # Container_Column
                                    **self.dict_style('_4120'),
                                    content= ft.Column( # Column
                                            **self.dict_style('_4121'),
                                            # height=80,
                                            # wrap=True,
                                            controls= [

                                                    # ft.Container( # Text
                                                    #         **self.dict_style('_4124'),
                                                    #         on_click= lambda _: event_4124(data='_4124'),
                                                    #         content= ft.Text(
                                                    #                 **self.dict_style('_4125'),
                                                    #                 # on_click= lambda _: event_4125(data='_4125'),
                                                    #         ),),

            ],),), #// LAYER 1 END
        ],),
            )

        #: SECOND CARD IN ROW
        self.class_row_card = ft.Container(  # Container_Row
            **self.dict_style('_4092'),
            content= ft.Row( # Row
                    **self.dict_style('_4093'),
                    controls= [
                            class_card_in_row,
        ],
        )

        ,)

        #: BUTTONS CONTAINER
        self.button_cap = ft.Container(  # Container_Row
            **self.dict_style('_4032'),
            content= ft.Row( # Row
                    **self.dict_style('_4033'),
                    controls= [

                            # ft.Container( # ElevatedButton
                            #         **self.dict_style('_4036'),
                            #         # on_click= lambda _: event_4037(data='_4037'),
                            #         content= ft.ElevatedButton(
                            #                 **self.dict_style('_4037'),
                            #                 on_click= lambda _: event_4037(data='_4037'),
                            #         ),),

            ],),) #// LAYER 1 END

        #: MAIN PHONE CONTAINER
        self.content_box = [

		ft.Container(  # Container_Column
			**self.dict_style('_4020'),
			content= ft.Column( # Column
					**self.dict_style('_4021'),
					controls= [

						ft.Container( # Text
								**self.dict_style('_4028'),
								# on_click= lambda _: event_4029(data='_4029'),
								content= ft.Text(
										**self.dict_style('_4029'),
										# on_click= lambda _: event_4029(data='_4029'),
								),),

		],),),
		ft.Container(  # Container_Column
			**self.dict_style('_4024'),
			content= ft.Column( # Column
					**self.dict_style('_4025'),
					controls= [

                        self.button_cap,
                        self.card_class,
		],),),
		# ft.Container(  # Container_Column
		# 	**self.dict_style('_4056'),
		# 	content= ft.Column( # Column
		# 			**self.dict_style('_4057'),
		# 			controls= [

		# 		],
		# ),), #// CLOSE LAYER 0

        self.header_class_row_card,
        self.class_row_card,

        ]

        #: MAIN PHONE CONTAINER
        self.content = ft.Container(
                            **self.class_menu_screen_style(code='MAIN_EFFECTS_CONTAINER'),
                            content = ft.Column(
                                        **self.class_menu_screen_style(code='COLUMN_CONTAINER'),
                                        controls = self.content_box
                                        ),
                                )

        # self.star_buttons()
        self.star_card_buttons()
        self.star_card_topic_class()

    def star_buttons(self):

        for _ in index_database:
            self.tmp_buttons = ft.Container( # ElevatedButton
                                                        **self.dict_style('_4036'),
                                                        content= ft.ElevatedButton(
                                                                text=_,
                                                                tooltip=_,
                                                                **self.dict_style('_4037'),
                                                                on_click= lambda x: event_4037(data=_),
                                                        ),)
            self.button_cap.content.controls.append(
                                                    self.tmp_buttons
                                                    )

    def star_card_buttons(self):

        for _ in index_database:
            # print(self.id_class_main.content.controls[1].content.controls)
            self.id_class_main = ft.Container(  # Container_Column
                                      **self.dict_style('_4044'),
                                      content= ft.Column( # Column
                                              **self.dict_style('_4045'),
                                              controls= [

                                                      ft.Container(  # Container_Row
                                                              **self.dict_style('_4100'),
                                                              content= ft.Row( # Row
                                                                      **self.dict_style('_4101'),
                                                                      controls= [

                                                                              ft.Container( # Icon
                                                                                      **self.dict_style('_4108'),
                                                                                      on_click= lambda _: event_4109(data='_4109'),
                                                                                      content= ft.Icon(
                                                                                              **self.dict_style('_4109'),
                                                                                              # on_click= lambda _: event_4109(data='_4109'),

                                                                                      ),),
                                                                              ft.Container( # Icon
                                                                                      **self.dict_style('_4100'),
                                                                                      # on_click= lambda _: event_4109(data='_4109'),
                                                                                      content= ft.Text(
                                                                                              # **self.dict_style('_4125'),
                                                                                              size=20,
                                                                                              value=_,
                                                                                              weight="Bold",

                                                                                              # on_click= lambda _: event_4109(data='_4109'),

                                                                                      ),),

                                              ],),), #// LAYER 3 END
                                                      ft.Container(  # Container_Column
                                                              **self.dict_style('_4104'),
                                                              content= ft.Column( # Column
                                                                      **self.dict_style('_4105'),
                                                                      controls= [

                                                                              # ft.Container( # Text
                                                                              #         **self.dict_style('_4112'),
                                                                              #         # on_click= lambda _: event_4113(data='_4113'),
                                                                              #         content= ft.Text(
                                                                              #                 **self.dict_style('_4113'),
                                                                              #                 # on_click= lambda _: event_4113(data='_4113'),
                                                                              #         ),),

                                              ],),), #// LAYER 3 END
                                ],),) #// LAYER 2 END

            self.card_class.content.controls.append(
                                                self.id_class_main
                                                    )

            for x in index_database.get(_):
                self.box_id_card  = TextData(
                                                       main_key = _,
                                                       data=x,
                                                       attribute_value = '_4112',
                                                       second_attribute_value = '_4113',
                                      # content= ft.Text(
                                              # **self.dict_style('_4113'),
                                              # value=x,
                                              # on_click= lambda _: event_4113(data='_4113'),
                                      )
                self.id_class_main.content.controls[1].content.controls.append(

                                                                               self.box_id_card
                                                                               )



    def star_card_topic_class(self):

        self.selected_cap = GLOBAL_VAR(get_global_var="selected_cap")
        self.selected_key = GLOBAL_VAR(get_global_var="selected_key")


        for _ in index_database.get(self.selected_cap).get(self.selected_key):

            class_card_in_row.content.controls[0].content.controls.append(
                                                                          TextToDocument(
                                                                                         data=_,
                                                                                         value_title=index_database.get(self.selected_cap).get(self.selected_key).get(_),
                                                                                         attribute_value = '_4124',
                                                                                         )
                                                                          )
        # class_card_in_row.content.controls[0].content.update()

    def class_menu_screen_style(self,code: str=''):
        #: SET MAIN STYLE WIDGET
        return phone_style_widget.get(code)

    def dict_style(self,code: str=''):
        #: SET CONTENT STYLE WIDGET
        return styles.get(code)


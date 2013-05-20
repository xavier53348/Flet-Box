import flet as ft
import os
from flet import Container
# from data_in_module import data


class wraper_widget():
    # globalVar='Erase this test'
    list_data = ''

    def __init__(self,widget_wraper='Erase this test'):
        super().__init__()
        # self.title='data'
        self.widget_wraper=widget_wraper


        self.tree_levels ={}

    def build(self):
        # Drop_Container_exemple=
        #       ft.Container(
        #                     content=ft.Column(
        #                                         controls=[
        #                                                     ft.Container()
        #                                                     self.data_share,
        #                                                     ft.ElevatedButton("WRITE",tooltip='buttom',on_click=lambda _:self.write_flet_app(_)),
                                                            # ft.Row(controls=[
                                                                            # ft.ElevatedButton('dell')
                                                                            # ]),
        #                                                     ft.ElevatedButton("READ",tooltip='buttom',on_click=lambda _:self.run_comand(_)),
        #                                                     ft.ElevatedButton("DELETE",tooltip='buttom',on_click=lambda _:self.delete(_)),
        #                                                  ],


        self.id   = self.widget_wraper.uid
        self.name = self.widget_wraper._get_control_name()
        #####################

        list_controls = ['row','column','stack',]
        for _ in range(8):

            if not self.list_data == '':
                #####################
                # print('here')
                # print('LAYER 1')
                #####################

                if not type(self.list_data) == type(list()):
                    # print(self.list_data,'==============')
                    if not self.list_data._get_control_name() in list_controls:


                        if not self.list_data.content == None:
                            self.list_data = self.list_data.content
                            print('LAYER 1    ',self.list_data._get_control_name(),)

                        else:
                            break
                            # print('data')
                            # print('LAYER 4   sss ',self.list_data._get_control_name(),)
                            # self.list_data = self.list_data.controls
                            # print(self.list_data)
                    else:
                        self.list_data = self.list_data.controls

                else:
                    print('LAYER 2')
                    for _ in self.list_data:
                        # print(_._get_control_name())
                        # self.list_data = _.content

                        if not _._get_control_name() in list_controls:
                            self.list_data = _
                            print('LAYER 3        ',self.list_data._get_control_name(),'<=== content')

                        else:
                            self.list_data = _
                            print('LAYER 3        ',self.list_data._get_control_name(),'<=== controls')
                            self.list_data = _.controls

                            # print(self.list_data )
                            for _ in self.list_data:
                                print('LAYER 4            ',_._get_control_name(),'<===')
                                if _._get_control_name() in list_controls:
                                    self.list_data = _.controls

                                    for _ in self.list_data:
                                        print('LAYER 5                ',_._get_control_name(),'<=== ')

                                        if _._get_control_name() in list_controls:
                                            self.list_data = _.controls
                                            # print('LAYER 6                ',_._get_control_name(),'<===')

                                            for _ in self.list_data:
                                                self.list_data = _
                                                print('LAYER 6                    ',_._get_control_name(),'<===')

                                                if _._get_control_name() in list_controls:
                                                    self.list_data = _.controls
                                                    print('LAYER 7                        ',_._get_control_name(),'<===')

                                                    for _ in self.list_data:
                                                        print('LAYER 8                            ',_._get_control_name(),'<===')

                                    # print(_)
                                # self.list_data = _.content
                                # print('LAYER 3            ',_._get_control_name(),'<<<<')

            else:
                self.list_data = self.widget_wraper
                print('LAYER 0',self.list_data._get_control_name(),)

        list_content = ['container']

        return '====================='

######## wraper_widget = wraper_widget(),# <======= Comma
class Container_exemple(ft.UserControl):
    # globalVar='Erase this test'

    def __init__(self,data='Erase this test',pag_in=''):
        super().__init__()
        # self.title='data'
        self.title=data
        self.pag_in = pag_in
    def build(self):
        global Drop_Container_exemple

        self.data_share = ft.Container(
                    ##################### PROPERTY
                    # expand=True,
                    # ink=False,                                                # click effect ripple
                    # bgcolor="#44CCCC00",                                    # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                    # padding= ft.padding.all(8),    # inside box                # padding.only(left=8, top=8, right=8, bottom=8),
                    # margin = ft.margin.all(8),    #outside box                # margin.only (left=8, top=8, right=8, bottom=8),
                    # alignment=ft.alignment.center,                            # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right.    posicionamiento adentro widget
                    border_radius= ft.border_radius.all(30),            # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                    border=ft.border.all(2, ft.colors.BLACK),             # ft.border.only(Left=8, top=8, right=8, bottom=8),
                    # image_src=f"/icons/icon-512.png",
                    width=150,
                    height=40,
                    # tooltip='Container',
                    ##################### EFFECTS
                    # gradient=ft.LinearGradient( begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=[ft.colors.BLUE, ft.colors.YELLOW],),
                    # gradient=ft.RadialGradient( colors=[ft.colors.YELLOW, ft.colors.BLUE],),
                    ##################### WIDGETS
                    content=ft.ElevatedButton("press container",tooltip='buttom'),
                    ##################### EVENTS
                    on_click=lambda _:print(_),                            # on_hover=print('on click over'), on_long_press=print('long press'),
        )#<=== NOTE COMA

        Drop_Container_exemple=ft.Container(
                    ##################### PROPERTY COLUMN
                    ##################### [rotate,offset] , [scale,aspect_ratio] , [visible,disabled]
                    # expand=True,
                    ink=False,                                                      # click effect ripple
                    # bgcolor="#3f449a",                                              # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                    # padding= ft.padding.all(8),    # inside box                        # padding.only(left=8, top=8, right=8, bottom=8),
                    # margin = ft.margin.all(8),    # outside box                       # margin.only (left=8, top=8, right=8, bottom=8),
                    alignment=ft.alignment.center,                                  # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right.    posicionamiento adentro widget
                    # border_radius= ft.border_radius.all(30),                      # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                    border=ft.border.all(2, ft.colors.BLACK),                     # ft.border.only(Left=8, top=8, right=8, bottom=8),
                    # ===================
                    # image_src = f"/home/mjay/Pictures/3d_neon_pink-2560x1440.jpg",
                    # image_opacity=0.1,
                    # image_fit='COVER',                                            # CONTAIN, COVER, FILL, FIT_HEIGHT, FIT_WIDTH, SCALE_DOWN
                    # ===================
                    width=320,
                    height=320,
                    tooltip='Container',
                    #################### EFFECTS
                    # gradient=ft.LinearGradient( begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=[ft.colors.BLUE, ft.colors.YELLOW],),
                    # gradient=ft.RadialGradient( colors=[ft.colors.YELLOW, ft.colors.BLUE],),
                    ##################### WIDGETS
                    content=ft.Column(
                        ##################### PROPERTY BOX
                        # expand=True,
                        alignment=ft.MainAxisAlignment.SPACE_AROUND,              # horizontal <=> START,CENTER,END SPACE_BETWEEN SPACE_AROUND SPACE_EVENLY
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,        # vertical       START,CENTER END
                        ##################### LET MAKE SCROLL IN LONG QUANTITY
                        scroll=True,                                              # center widget
                        tight=True,
                        ##################### ADAPT TO SCREEN
                        wrap=True,                                                  # justify in all screen
                        spacing=8,                                                # space widget left right
                        run_spacing=8,                                            # space widget up down
                        ##################### WIDGETS
                        controls=[
                                    ft.Container(
                                                ##################### PROPERTY
                                                ##################### [rotate,offset] , [scale,aspect_ratio] , [visible,disabled]
                                                # expand=True,
                                                ink=False,                                                # click effect ripple
                                                bgcolor="red",                                    # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                                                padding= ft.padding.all(2),    # inside box                # padding.only(left=8, top=8, right=8, bottom=8),
                                                margin = ft.margin.all(2),    #outside box                # margin.only (left=8, top=8, right=8, bottom=8),
                                                alignment=ft.alignment.center,                            # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right.    posicionamiento adentro widget
                                                border_radius= ft.border_radius.all(30),            # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
                                                border=ft.border.all(2, ft.colors.BLACK),             # ft.border.only(Left=8, top=8, right=8, bottom=8),
                                                # ===================
                                                image_src = f"/home/mjay/Pictures/3d_neon_pink-2560x1440.jpg",
                                                image_opacity=0.1,
                                                image_fit='COVER',                                            # CONTAIN, COVER, FILL, FIT_HEIGHT, FIT_WIDTH, SCALE_DOWN
                                                # ===================
                                                width=150,
                                                height=70,
                                                tooltip='Container',
                                                ##################### EFFECTS
                                                gradient=ft.LinearGradient( begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=[ft.colors.BLUE, ft.colors.YELLOW],),
                                                # gradient=ft.RadialGradient( colors=[ft.colors.YELLOW, ft.colors.BLUE],),
                                                # shadow = ft.BoxShadow(
                                                #            spread_radius=1,
                                                #            blur_radius=15,
                                                #            color=ft.colors.BLUE_GREY_300,
                                                #            offset=ft.Offset(0, 0),
                                                #            blur_style=ft.ShadowBlurStyle.OUTER,
                                                #      ),
                                                ##################### WIDGETS
                                                content=ft.ElevatedButton("press container",tooltip='buttom'),
                                                ##################### EVENTS
                                                on_click=lambda _:print(_),                            # on_hover=print('on click over'), on_long_press=print('long press'),
                                    ),#<=== NOTE COMA
                                    self.data_share,
                                    ft.ElevatedButton("WRITE",tooltip='buttom',on_click=lambda _:self.write_flet_app(_)),
                                    ft.Row(controls=[
                                                    ft.Row(controls=[ft.ElevatedButton()]),
                                                    ft.Row(controls=[
                                                                    ft.Row(controls=[
                                                                                    ft.Text(),
                                                                                    ft.Text(),
                                                                                    ft.Text(),
                                                                                    ft.Text(),
                                                                                    ft.Row(controls=[
                                                                                                    ft.Text(),
                                                                                                    ft.Text(),
                                                                                                    ft.Text(),
                                                                                                    ft.Text(),
                                                                                        ]),
                                                                                    ])]),

                                                    ft.Text('dell'),
                                                    ft.Text('dell'),
                                                    ft.Text('dell'),

                                                    ]),
                                    ft.ElevatedButton("READ",tooltip='buttom',on_click=lambda _:self.run_comand(_)),
                                    ft.ElevatedButton("DELETE",tooltip='buttom',on_click=lambda _:self.delete(_)),
                                 ],
                    ),#<=== NOTE COMA [NOTE]                     for x in range(1,50): widget.content.controls.append(ft.ElevatedButton("press buttom",tooltip='buttom'))
                    ##################### EVENTS
                    # on_click=lambda _:print(_),                            # on_hover=print('on click over'), on_long_press=print('long press'),
        )#<=== NOTE COMA


        return Drop_Container_exemple

    def write_flet_app(self,e):

        # screen_1.content = screen_1.content


#         data = """
# from flet import Container ,ElevatedButton

# SCREEN={
#             'screen_1':REPLACE_

#         }

# def return_data(widget_name):
#     global SCREEN
#     return SCREEN.get(widget_name)
# """.replace('REPLACE_', f"{self.data_share.content.__repr__()}")

# # """.replace('REPLACE_', f"{self.data_share.content.__repr__()}")
# # """.replace('REPLACE_', f"{self.data_share.content.__repr__()}")      #<====== contentido
# # """.replace('REPLACE_', f"{self.data_share.__repr__()}")              #<======

#         with open('./test/data_in_module.py','w') as f:
#             f.write(data)

#         path_dir = './test/data_in_module.py'
#         with open(path_dir,'r') as f:
#             show = f.read()
#             show = show.replace("'{", "{").replace("}'", "}")
#             show = show.replace('borderradius', 'border_radius').replace('imagesrc','image_src')
#             show = show.replace("n='content'", '')
#             with open(path_dir,'w') as f:
#                 f.write(show)

#         # screen_1.update()
#         print(screen_1)
          global data_returned

          # from views.building_code_traslator import write_flet_code_to_builder_screens


          # ################################################################################################ CREATING DATABASE
          # from views.building_code_traslator import create_index_page
          # create_index_page(module_path ='./test/views/SCREENS_DB.py',widget_screen=self.data_share)
          # ################################################################################################ TRASLATING TO FLET MACHINE
          # from views.building_code_traslator import tralating_index_page
          # data_returned = tralating_index_page(
          #                                       read_module_path  = './test/views/SCREENS_DB.py',
          #                                       write_module_path = './test/views/FLET_TRASLATED_SCREEN_DB.py',
          #                                       code_to_traslate  = self.data_share,
          #                                       write_lines       = True,
          #                                       )
          # ################################################################################################
          from views.building_code_traslator import read_index_page_db
          add_screens   = read_index_page_db(
                                                    # read_module_path       ='./test/views/FLET_TRASLATED_SCREEN_DB.py',
          #                                           widget_name       = 'widge_1',
          #                                           widget_attributes = data_returned,
                                                    index='_9'
                                                    )

          screen_1.content.controls[0].content.controls.append(add_screens)
          screen_1.content.update()

    def delete(self,e):
        screen_1.content.controls[0].content.controls.pop()
        screen_1.content.update()

    def load_flet_app(self,e):
        # import data_in_module

        # screen_1.content = screen_1.content
        # screen_1.content.controls[0].content.controls.append(ft.Container(bgcolor='red',height=50,width=120))

        # print(data)



        print(data_returned)
        # screen_1.content.controls[0].content.controls.append(data_returned)
        screen_1.content.update()


    def run_comand(self,e):
        ############################################################### ATTRIBUTES
        # GET SPECIFIC ATTRIBUTE PASSED
        # tmp_data = screen_1.__getattribute__('content')
        # GET ATTRIBUTE OF THE WIDGET
        # tmp_data = screen_1._Control__attrs
        # GET ATTIBUTE IN DICT
        # tmp_data = screen_1._wrap_attr_dict(self.data_share)
        # GET ATTIBUTE LIKE STR
        # tmp_data = screen_1.__str__()
        # GET ATTRIBUTE LIKE A WIDGET
        # tmp_data = screen_1.__repr__()                # ******
        ############################################################### ID
        # GET ID
        # tmp_data = screen_1.uid
        ############################################################### CHILDRENS
        # GET ONE WIDGET BEFORE
        # tmp_data = screen_1._Control__previous_children
        # GET ONE WIDGET BEFORE LIST
        # tmp_data = screen_1._get_children()
        # tmp_data = screen_1._previous_children
        ############################################################### NAME WIDGET STR
        # WRAP LIKE A DICT
        # print(Drop_Make_data._wrap_attr_dict({'new_value':Drop_Make_data}))
        # Drop_Make_data.invoke_method('on_click')

        # GET NAME MODULE
        # tmp_data = screen_1.__module__
        # GET NAME OF THE WIDGET
        # tmp_data = screen_1._get_control_name()
        ############################################################### REMOVE CONTROLS
        # print(ft.FLET_APP.controls)
        # tmp_data = self.pag_in._remove_control_recursively(
        #                                                 '_7' ,
        #                                                 Drop_Container_exemple.content
        #                                                 )
        ############################################################### GET INFO PAGE FROM A CONTAINER
        # KWON INFO ABOUT PAGE FROM EVERY WHERE
        # tmp_data = Drop_Container_exemple.__dict__.get('_Control__page')    #  s.__dict__.get('_Control__page')
        # tmp_data.route                                                    # <=== route platform platform_brightness theme_mode
        # tmp_data.window_width
        # tmp_data.window_height
        # tmp_data._id
        # tmp_data.media.padding
        # tmp_data.media.view_padding
        # tmp_data.media.view_insets
        ###############################################################
        # KWON INFO ABOUT PAGE FROM EVERY WHERE
        # tmp_data = Drop_Container_exemple.__dict__.get('_Control__page')    #  s.__dict__.get('_Control__page')
        # tmp_data._Page__next_control_id                                     ####<=== very important
        # tmp_data._Page__views                                               ####<=== very important
        #########################################
        # tmp_data._index                                                     ####<=== very important DICT OF ALL WWIDGETS
        # tmp_data._index.get('_9')                                           ####<=== GET BY INDEX
        # tmp_data.get_control(id='_5').controls                              ####<=== GET BY INDEX
        ###############################################################
        # tmp_data.index['_5'].controls.pop()
        # tmp_data.index['_5'].update()
        # print(self.data_share._wrap_attr_dict({'data':tmp_data.index['_5']}))



        # tmp_data = Drop_Container_exemple._get_control_name().capitalize()

        filters = {

                'Container':'content'
        }

        tmp_data = Drop_Container_exemple


        # tmp_data

        # if tmp_data._get_control_name() == 'container':
        #     layer_0 = {'layer_0':{
        #                         tmp_data.uid:{
        #                                     ################## CURRENT WIDGET
        #                                     'father_name':  tmp_data._get_control_name(),
        #                                     'father_level':'layer_0', # cUrremt widget
        #                                     'father_id':    tmp_data.uid,

        #                                     ################### NEXT WIDGET
        #                                     'widget_name': tmp_data.content._get_control_name(),
        #                                     'widget_level':'layer_1',
        #                                     'widget_id':tmp_data.content.uid,
        #                                     }
        #                           },
        #                }
        #     # if layer_0.get('layer_0').get(tmp_data.uid):

        #     # print(layer_0.get('layer_0').get(tmp_data.uid)layer_0.get('layer_0').get(tmp_data.uid))

        #     if tmp_data.content._get_control_name() == 'container':
        #         ...
        #     else:
        #         layer_1 = {'layer_1':{
        #                             tmp_data.content.uid:{
        #                                         ################## CURRENT WIDGET
        #                                         'father_name': tmp_data._get_control_name(),
        #                                        'father_level': 'layer_0', # cUrremt widget
        #                                           'father_id': tmp_data.uid,

        #                                         ################### NEXT WIDGET
        #                                         'widget_name': tmp_data.content._get_control_name(),
        #                                         'widget_level':'layer_1',
        #                                         'widget_id':tmp_data.content.uid,
        #                                         }
        #                               },
        #                    }

        result = wraper_widget(widget_wraper=Drop_Container_exemple)

        print(result.build())
            # if layer_0.get('lay
                # print(layer_1)
                # print(tmp_data.content)
######## Container_exemple = Container_exemple(),# <======= Comma
def main(page: ft.Page):
    ###################### CONFIGURATION
    page.scroll               = True
    page.vertical_alignment   = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    ######################  COLOR
    page.theme_mode           = ft.ThemeMode.DARK         #ft.ThemeMode.LIGHT
    # page.bgcolor            = ft.colors.TRANSPARENT
    # page.window_bgcolor     = ft.colors.TRANSPARENT
    ###################### POSITION OF SC
    page.window_left          = 8
    page.window_top           = 8
    # page.window_center()
    ###################### SIZE
    page.window_height        = 420
    page.window_width         = 320
    page.padding              = 8
    page.spacing              = 8
    page.expand               = True
    ######################
    global screen_1
    # print(page.__dir__())
    screen_1=ft.Container(
                    ##################### PROPERTY
                    # expand=True,
                    ink=True,                                           # click effect ripple
                    bgcolor="#44CCCC00",                                # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
                    padding= ft.padding.all(8),    # inside box         # padding.only(left=8, top=8, right=8, bottom=8),
                    margin = ft.margin.all(8),     # outside box        # margin.only (left=8, top=8, right=8, bottom=8),
                    alignment=ft.alignment.center,                      # top_left, top_center, top_right, center_left, center, center_right, bottom_left, bottom_center, bottom_right.    posicionamiento adentro widget
                    # gradient=ft.LinearGradient( begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=[ft.colors.BLUE, ft.colors.YELLOW],),
                    # gradient=ft.RadialGradient( colors=[ft.colors.YELLOW, ft.colors.BLUE],),
                    ##################### WIDGETS
                    # content=ft.ElevatedButton("press buttom",tooltip='buttom'),
                    ##################### EVENTS
                    content=Container_exemple(pag_in = page),                        # on_hover=print('on click over'), on_long_press=print('long press'),
                )




    page.add(screen_1)
    page.update()

    # ft.Page(conn, session_id, loop)
if __name__ == '__main__':
    ft.app(target=main)
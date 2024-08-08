import flet as ft
import time

from ..config_container.widget_editor import Build_Editor
from ..lite_menu_bar_down_phone.selected_widget import SelectedWidget
from ..settings_var.settings_widget import GLOBAL_VAR

numWidget        = GLOBAL_VAR(get_global_var='NUM_WIDGETS_DROPPED')
numClick         = GLOBAL_VAR(get_global_var='NUM_CLICKS')
listWidgetUpdate = GLOBAL_VAR(get_global_var='LIST_SELECTED_WIDGETS')

PRESENTATION_TEXT: str = """
Ready to make your first app!!
Begin your journey...
"""

class InfinityBoxLayerOne(ft.Stack):
     """
     NOTE:

     1. THIS IS VERY IMPORTANT WIDGET TO DRAGG AND DROP
        IS A LOOP DRAGGTARGET THAT WILL CONTAIN ALL WIDGET INSIDE.

     AND IT SELF WILL ADD WIDGETS DEPENDIND
     ROW , COLUMN , GRIDVIEW ... USE CONTROLS=[ WIDGETS, WIDGETS... ]
     REST WIDGETS USE CONTENT = WIDGET()

     2. Make widget need
     """

     def __init__(self,dataPassed=''):
          super().__init__()

          self.dataPassed    = dataPassed
          self.clip_behavior = ft.ClipBehavior.NONE

     def build(self):
          global numWidget

          """
          check CircleAvatar, VerticalDivider
          """

          self.widgets={

               #: CONTAINERS LAYOUTS

                       "Row": [    ft.Container(bgcolor=ft.colors.BLACK54,alignment=ft.alignment.center,padding=ft.padding.all(6),border=ft.border.all(2, ft.colors.CYAN_900),tooltip='Row',
                                   ink=True,
                                   ink_color='cyan',
                                   on_hover=lambda _:self.resetClick(),
                                   on_click=lambda _:self.touchWidgetIndex(self.infinityDropWidget),
                                   content=ft.Row( scroll="ALWAYS",
                                        controls= [
                                                       ],),),
                              ],
                    "Column": [    ft.Container(bgcolor=ft.colors.BLACK54,alignment=ft.alignment.center,padding=ft.padding.all(6),border=ft.border.all(2, ft.colors.CYAN_900),tooltip='Column',
                                   ink=True,
                                   ink_color='yellow',                                   on_hover=lambda _:self.resetClick(),
                                   on_click=lambda _:self.touchWidgetIndex(self.infinityDropWidget),
                                   content=ft.Column( scroll="ALWAYS",horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                        controls= [
                                                       ],),),
                              ],
                     "Stack": [    ft.Container(bgcolor=ft.colors.BLACK54,alignment=ft.alignment.center,padding=ft.padding.all(6),border=ft.border.all(2, ft.colors.CYAN_900),tooltip='Stack',
                                   ink=True,
                                   ink_color='purple',                                   on_hover=lambda _:self.resetClick(),
                                   on_click=lambda _:self.touchWidgetIndex(self.infinityDropWidget),
                                   content=ft.Stack(
                                        controls= [
                                                       ],),),
                              ],
                  "GridView": [    ft.Container(bgcolor=ft.colors.BLACK54,alignment=ft.alignment.center,border=ft.border.all(2, ft.colors.CYAN_900),tooltip='GridView',
                                   ink=True,
                                   ink_color='green',                                   on_hover=lambda _:self.resetClick(),
                                   on_click=lambda _:self.touchWidgetIndex(self.infinityDropWidget),
                                   content=ft.GridView(runs_count=2,run_spacing=4,padding=ft.padding.all(6), spacing=4,
                                        controls= [
                                                       ],),),
                              ],
               #: SPACE LAYOUTS

                   "Divider": [    ft.Container(bgcolor=ft.colors.TRANSPARENT,alignment=ft.alignment.center,padding=ft.padding.all(6),margin=ft.margin.all(0),border=ft.border.all(0, ft.colors.TRANSPARENT),tooltip='Divider',
                                   ink=True,
                                   ink_color='red',                                   on_hover=lambda _:self.resetClick(),
                                   on_click=lambda _:self.touchWidgetIndex(self.infinityDropWidget),
                                   content=ft.Divider(),),
                              ],
                              # VerticalDivider most set propertie [container height ] becouse no work onVerticalDivider
                  "Vertical": [    ft.Container(bgcolor=ft.colors.TRANSPARENT,alignment=ft.alignment.center,padding=ft.padding.all(6),height=25,margin=ft.margin.all(0),border=ft.border.all(0, ft.colors.TRANSPARENT),tooltip='VerticalDivider',
                                   ink=True,
                                   ink_color='red',                                   on_hover=lambda _:self.resetClick(),
                                   on_click=lambda _:self.touchWidgetIndex(self.infinityDropWidget),
                                   content=ft.VerticalDivider(width=1, color="white"),),
                              ],

               #: IMAGE WIDGET

                     "Image": [    ft.Container(bgcolor=ft.colors.TRANSPARENT,alignment=ft.alignment.center,padding=ft.padding.all(6),margin=ft.margin.all(0),border=ft.border.all(0, ft.colors.TRANSPARENT),tooltip='Image',
                                   ink=True,
                                   ink_color='red',                                   on_hover=lambda _:self.resetClick(),
                                   on_click=lambda _:self.touchWidgetIndex(self.infinityDropWidget),
                                   content=ft.Image(src=f'no_imagen.jpg',fit=ft.ImageFit.FILL,width=110,height=110,tooltip='Image'),),
                              ],
                    "Avatar": [    ft.Container(bgcolor=ft.colors.TRANSPARENT,alignment=ft.alignment.center,padding=ft.padding.all(6),margin=ft.margin.all(0),border=ft.border.all(0, ft.colors.TRANSPARENT),tooltip='Avatar',
                                   ink=True,
                                   ink_color='red',                                   on_hover=lambda _:self.resetClick(),
                                   on_click=lambda _:self.touchWidgetIndex(self.infinityDropWidget),
                                   content=ft.CircleAvatar(background_image_src='avatar.jpg'),),
                              ],
                      "Icon": [    ft.Container(bgcolor=ft.colors.TRANSPARENT,alignment=ft.alignment.center,padding=ft.padding.all(6),margin=ft.margin.all(0),border=ft.border.all(0, ft.colors.TRANSPARENT),tooltip='Icon',
                                   ink=True,
                                   ink_color='red',                                   on_hover=lambda _:self.resetClick(),
                                   on_click=lambda _:self.touchWidgetIndex(self.infinityDropWidget),
                                   content=ft.Icon(name=ft.icons.ADD_REACTION_OUTLINED,tooltip='Icon'),),
                              ],
               #: TEXT  WIDGET

                     "Text":  [    ft.Container(bgcolor=ft.colors.TRANSPARENT,alignment=ft.alignment.center,padding=ft.padding.all(6),margin=ft.margin.all(0),border=ft.border.all(0, ft.colors.TRANSPARENT),tooltip='Text',
                                   ink=True,
                                   ink_color='red',                                   on_hover=lambda _:self.resetClick(),
                                   on_click=lambda _:self.touchWidgetIndex(self.infinityDropWidget),
                                   content=ft.Text(value=PRESENTATION_TEXT,tooltip='Text',size=10),),
                              ],
                "Text Field": [    ft.Container(bgcolor=ft.colors.TRANSPARENT,alignment=ft.alignment.center,padding=ft.padding.all(6),margin=ft.margin.all(0),border=ft.border.all(0, ft.colors.TRANSPARENT),tooltip='TextField',
                                   ink=True,
                                   ink_color='red',                                   on_hover=lambda _:self.resetClick(),
                                   on_click=lambda _:self.touchWidgetIndex(self.infinityDropWidget),
                                   content=ft.TextField(label="what's your name ?",tooltip='TextField',border_radius= ft.border_radius.all(30),height=32, cursor_height=20,content_padding= ft.padding.all(16),border_color=ft.colors.WHITE,focused_border_color=ft.colors.RED,
                                        text_size=12,
                                        width=240,
                                        ),),
                              ],

               #: BUTTONS WIDGET

           "Elevated Button": [    ft.Container(bgcolor=ft.colors.TRANSPARENT,alignment=ft.alignment.center,padding=ft.padding.all(6),margin=ft.margin.all(0),border=ft.border.all(0, ft.colors.TRANSPARENT),tooltip='ElevatedButton',
                                   ink=True,
                                   ink_color='red',                                   on_hover=lambda _:self.resetClick(),
                                   on_click=lambda _:self.touchWidgetIndex(self.infinityDropWidget),
                                   content=ft.ElevatedButton("Accept",tooltip='ElevatedButton',elevation=20,height=28),),
                              ],
               "Text Button": [    ft.Container(bgcolor=ft.colors.TRANSPARENT,alignment=ft.alignment.center,padding=ft.padding.all(6),margin=ft.margin.all(0),border=ft.border.all(0, ft.colors.TRANSPARENT),tooltip='TextButton',
                                   ink=True,
                                   ink_color='red',                                   on_hover=lambda _:self.resetClick(),
                                   on_click=lambda _:self.touchWidgetIndex(self.infinityDropWidget),
                                   content=ft.TextButton("Accept",tooltip='TextButton',height=28),),
                              ],
               "Icon Button": [    ft.Container(bgcolor=ft.colors.TRANSPARENT,alignment=ft.alignment.center,padding=ft.padding.all(6),margin=ft.margin.all(0),border=ft.border.all(0, ft.colors.TRANSPARENT),tooltip='IconButton',
                                   ink=True,
                                   ink_color='red',                                   on_hover=lambda _:self.resetClick(),
                                   on_click=lambda _:self.touchWidgetIndex(self.infinityDropWidget),
                                   content=ft.IconButton(tooltip='Accept',icon=ft.icons.ADD_LINK_SHARP),),
                              ],
                    "Filled": [    ft.Container(bgcolor=ft.colors.TRANSPARENT,alignment=ft.alignment.center,padding=ft.padding.all(6),margin=ft.margin.all(0),border=ft.border.all(0, ft.colors.TRANSPARENT),tooltip='FilledButton',
                                   ink=True,
                                   ink_color='red',                                   on_hover=lambda _:self.resetClick(),
                                   on_click=lambda _:self.touchWidgetIndex(self.infinityDropWidget),
                                   content=ft.FilledButton("Accept",tooltip='FilledButton',height=28),),
                              ],
                     "Tonal": [    ft.Container(bgcolor=ft.colors.TRANSPARENT,alignment=ft.alignment.center,padding=ft.padding.all(6),margin=ft.margin.all(0),border=ft.border.all(0, ft.colors.TRANSPARENT),tooltip='FilledTonalButton',
                                   ink=True,
                                   ink_color='red',                                   on_hover=lambda _:self.resetClick(),
                                   on_click=lambda _:self.touchWidgetIndex(self.infinityDropWidget),
                                   content=ft.FilledTonalButton("Accept",tooltip='FilledTonalButton',height=28),),
                              ],
                   "Outline": [    ft.Container(bgcolor=ft.colors.TRANSPARENT,alignment=ft.alignment.center,padding=ft.padding.all(6),margin=ft.margin.all(0),border=ft.border.all(0, ft.colors.TRANSPARENT),tooltip='OutlinedButton',
                                   ink=True,
                                   ink_color='red',                                   on_hover=lambda _:self.resetClick(),
                                   on_click=lambda _:self.touchWidgetIndex(self.infinityDropWidget),
                                   content=ft.OutlinedButton("Accept",tooltip='OutlinedButton',height=28),),
                              ],

               #: SELECTIONS WIDGET

                 "Checkbox":  [    ft.Container(bgcolor=ft.colors.TRANSPARENT,alignment=ft.alignment.center,padding=ft.padding.all(6),margin=ft.margin.all(0),border=ft.border.all(0, ft.colors.TRANSPARENT),tooltip='Checkbox',
                                   ink=True,
                                   ink_color='red',                                   on_hover=lambda _:self.resetClick(),
                                   on_click=lambda _:self.touchWidgetIndex(self.infinityDropWidget),
                                   content=ft.Checkbox(label="  Accept the target",tooltip='Checkbox',value=False,height=28),),
                              ],
                 "Cupertino": [    ft.Container(bgcolor=ft.colors.TRANSPARENT,alignment=ft.alignment.center,padding=ft.padding.all(6),margin=ft.margin.all(0),border=ft.border.all(0, ft.colors.TRANSPARENT),tooltip='CupertinoCheckbox',
                                   ink=True,
                                   ink_color='red',                                   on_hover=lambda _:self.resetClick(),
                                   on_click=lambda _:self.touchWidgetIndex(self.infinityDropWidget),
                                   content=ft.CupertinoCheckbox(label="  Accept the target",tooltip='CupertinoCheckbox',value=False,height=28),),
                              ],
                    "Switch": [    ft.Container(bgcolor=ft.colors.TRANSPARENT,alignment=ft.alignment.center,padding=ft.padding.all(12),margin=ft.margin.all(0),border=ft.border.all(0, ft.colors.TRANSPARENT),tooltip='Switch',
                                   ink=True,
                                   ink_color='red',                                   on_hover=lambda _:self.resetClick(),
                                   on_click=lambda _:self.touchWidgetIndex(self.infinityDropWidget),
                                   content=ft.Switch(label="  Accept the target",tooltip='Switch',value=False,height=28),),
                              ],

                      "Chip": [    ft.Container(bgcolor=ft.colors.TRANSPARENT,alignment=ft.alignment.center,padding=ft.padding.all(6),margin=ft.margin.all(0),border=ft.border.all(0, ft.colors.TRANSPARENT),tooltip='Chip',
                                   ink=True,
                                   ink_color='red',                                   on_hover=lambda _:self.resetClick(),
                                   on_click=lambda _:self.touchWidgetIndex(self.infinityDropWidget),
                                   content=ft.Chip(label=ft.Text("  Accept the target"), leading=ft.Icon(ft.icons.CAMERA_ROUNDED),tooltip='Chip',on_click=lambda _:print('help')),),
                              ],

                    "Slider": [    ft.Container(bgcolor=ft.colors.TRANSPARENT,alignment=ft.alignment.center,padding=ft.padding.all(6),margin=ft.margin.all(0),border=ft.border.all(0, ft.colors.TRANSPARENT),tooltip='CupertinoRadio',
                                   ink=True,
                                   ink_color='red',                                   on_hover=lambda _:self.resetClick(),
                                   on_click=lambda _:self.touchWidgetIndex(self.infinityDropWidget),
                                   content=ft.CupertinoSlider(value=50,tooltip='CupertinoSlider',max=100,height=28,),),
                              ],

                 #: RadioGroup <==== need solve that issue

                 "Cup Radio": [    ft.Container(bgcolor=ft.colors.TRANSPARENT,alignment=ft.alignment.center,padding=ft.padding.all(12),margin=ft.margin.all(0),border=ft.border.all(0, ft.colors.TRANSPARENT),tooltip='CupertinoRadio',
                                   ink=True,
                                   ink_color='red',                                   on_hover=lambda _:self.resetClick(),
                                   on_click=lambda _:self.touchWidgetIndex(self.infinityDropWidget),
                                   content=ft.RadioGroup(content=ft.CupertinoRadio(label="  Accept the target",tooltip='CupertinoRadio',value=False,height=28),),),
                              ],

                     "Radio": [    ft.Container(bgcolor=ft.colors.TRANSPARENT,alignment=ft.alignment.center,padding=ft.padding.all(12),margin=ft.margin.all(0),border=ft.border.all(0, ft.colors.TRANSPARENT),tooltip='Radio',
                                   ink=True,
                                   ink_color='red',                                   on_hover=lambda _:self.resetClick(),
                                   on_click=lambda _:self.touchWidgetIndex(self.infinityDropWidget),
                                   content=ft.RadioGroup(content=ft.Radio(label="  Accept the target",tooltip='Radio',value='False',height=28),),),
                              ],
               }

          #: ALERTS STATUS

          #: WIDGETS STATUS

          #: ESPECIAL WIDGET

          #: CHARTS LAYOUTS

          selectWidgetBox                    = GLOBAL_VAR(get_global_var='SELECT_DRAGG')
          self.infinityDropWidget            = self.widgets.get(selectWidgetBox)
          self.infinityDropWidget[0].id      = f"{self.dataPassed}: {numWidget}"              # OUR ID
          self.infinityDropWidget[0].tooltip = f"{self.dataPassed}: {numWidget}"              # TOOLTIP ID

          #: run only production
          #: print(self.infinityDropWidget[0].id)
          #: print(self.infinityDropWidget[0]._Control__uid)


          #: SET WIDGET DROPPED TO DICT DATABASE TO EXPORT PROYECT
          #: GLOBAL_VAR(set_global_var={'EXPORT_DATA_PHONE':{self.infinityDropWidget[0].id:self.infinityDropWidget[0]}})

          print('============')
          print(f"""
                [+]             selected_widget: {self.dataPassed},
                [+]             ID_widget: {numWidget},
                [+]             UID: {self.infinityDropWidget[0].uid}
                [+]             ID tooltip: {self.infinityDropWidget[0].tooltip}
                [+]  Content: {self.infinityDropWidget}""")
          print('============')

          self.drag_boxs =ft.DragTarget(
                                             group     = "GroupDragg",
                                             content   = self.infinityDropWidget[0],

                                        on_will_accept = self.drag_will_accept,           # Traslate Drop
                                        on_leave       = self.drag_leave,                 # Leafing Drop Line Border
                                        on_accept      = lambda _:self.drag_accept(_),                # Accept Drop
                                        )

          numWidget+=1
          #: return self.infinityDropWidget
          return self.drag_boxs

     def resetClick(self):
          global numClick
          numClick=1

          #: SET TEXT IN FLOAT CONTAINER SELECTED WIDGET
          #: SELECT_DROPP_WIDGET_CONTAINER = GLOBAL_VAR(get_global_var='SELECT_DROPP_WIDGET_CONTAINER')

          #: if not SELECT_DROPP_WIDGET_CONTAINER == None:  #: <<===== YOU SELECTED ONE WIDGET IN PHONE
          #:      #: IF LEAVE THIS BOX WILL RESET BORDER PHONE
          #:      SELECT_DROPP_WIDGET_CONTAINER.border = None
          #:      SELECT_DROPP_WIDGET_CONTAINER.update()

          #: SET TEXT IN FLOAT CONTAINER SELECTED WIDGET


     def touchWidgetIndex(self,listWidget):
     # def touchWidgetIndex(self,listWidget,e: ft.ContainerTapEvent):
          """
          NOTE:

          WE CAPTURE THE CLICK SELECTION_WIDGET SHOWING BORDER COLOR YELLOW

          IF PRESS IN OTHER WIDGET WE COMPARE tmp_list listWidgetUpdate
          IF IS DIFERENT SHOW BLACK COLOR THE PREVIEW SELECT_WIDGET

          NOTE:

          WE PASS TO Build_Editor => self.infinityDropWidget[0] THAT IS CLICKED SELECTION
          Build_Editor.update_widget_attributes(widget_cliked=ft.Container(content=ft.Text()))

          """
          global numClick

          CHECK_DATA = GLOBAL_VAR(get_global_var='BOOL_SHOW_SELECTED')

          click_time      = time.time()
          last_click_time = GLOBAL_VAR(get_global_var='CHECK_CURRENT_TIME_DOBLE_CLICKS')  #< == DEFAULD 0


          #: CHECK IF SCAPE DOBLE CLICKS PEASE DON'T EDIT THIS LINE IF NO HAVE SOLUTION IMPLEMENTED
          #: end_thread_time = time.time()

          if (click_time - last_click_time) < 0.3:

               #: IF CURRENT TIME IT GRADER THAN 0.1 SEGUND ITS OK LESS IS DETECTED AS DOUBLE CLIKS
               #: print('<==============> START')
               #: print(current_time_performance_clicks,' :SECONDS')
               #: print('<==============> END')

               print(f'ESCAPE DOUBLE CLICK: TIME: {click_time - last_click_time}')

          else:
               if CHECK_DATA:
                    #: HIDE TAB 2
                    #: HIDE TABS 2 and 3 IF CLICK PRESS IS NO IN PHONE CONTAINER WIDGET

                    CONFIG_TABS_CONTAINERS                 = GLOBAL_VAR(get_global_var='CONFIG_TABS_CONTAINERS')
                    CONFIG_TABS_CONTAINERS.visible         = False
                    CONFIG_TABS_CONTAINERS.update()

                    #: HIDE TAB 3
                    #: HIDE TABS 2 and 3 IF CLICK PRESS IS NO IN PHONE CONTAINER WIDGET

                    CONFIG_TABS_CONTAINERS_CONTENT         = GLOBAL_VAR(get_global_var='CONFIG_TABS_CONTAINERS_CONTENT')
                    CONFIG_TABS_CONTAINERS_CONTENT.visible = False
                    CONFIG_TABS_CONTAINERS_CONTENT.update()
                    #: HIDE TAB 3

               if numClick == 1:
                    tmp_list         = GLOBAL_VAR(get_global_var='LIST_SELECTED_WIDGETS')
                    listWidgetUpdate = listWidget

                    if tmp_list:
                         if not tmp_list.tooltip == listWidgetUpdate[0].tooltip:
                              tmp_list.border = ft.border.all(0, ft.colors.TRANSPARENT)
                              tmp_list.update()

                    #: WE HAVE TO FIX THIS PROBLEM MULTY TOUCH IS INVOKET EVERY TIME THAT MAKE ONE CLICK OVER A BOX

                    widgetConfig = listWidgetUpdate

                    """
                    THIS MODULE CALL TO BUILD EDITOR TO CHANGE ATTRIBUTES
                    """
                    #: Build_Editor.update_widget_attributes(widget_cliked=self.infinityDropWidget[0])
                    #: SET SELECTED WIDGET IN DICT TO ERASE IF PRESS REMOVE
                    GLOBAL_VAR(set_global_var={'SELECT_DATA_ERASE_PHONE':listWidget[0].id})

                    # time.sleep(0.1)

                    #: SET TEXT IN FLOAT CONTAINER SELECTED WIDGET

                    TEXT_PHONE_WIDGET = GLOBAL_VAR(get_global_var='SHOW_TEXT_SELECTED_PHONE_WIDGET')
                    TEXT_PHONE_WIDGET.controls[0].content.controls[1].spans[0].text = listWidget[0].tooltip
                    TEXT_PHONE_WIDGET.controls[0].bgcolor = ft.colors.BLUE_GREY_900
                    TEXT_PHONE_WIDGET.controls[0].update()

                    TEXT_DRAGG_WIDGET = GLOBAL_VAR(get_global_var='SHOW_TEXT_SELECTED_DRAGG_WIDGET')
                    TEXT_DRAGG_WIDGET.controls[0].content.controls[1].spans[0].text = "None"
                    TEXT_DRAGG_WIDGET.controls[0].bgcolor = ft.colors.BLACK12
                    TEXT_DRAGG_WIDGET.controls[0].update()

                    #: SET GLOBAL VAR // SELECTED_WIDGET // IN PHONE_CONTAINER AND PHONE CONTENT

                    GLOBAL_VAR(set_global_var={'SELECT_DROPP_WIDGET_CONTAINER':listWidget[0]})
                    GLOBAL_VAR(set_global_var={'SELECT_DROPP_WIDGET_CONTAINER_CONTENT':listWidget[0].content})


                    GLOBAL_VAR(set_global_var={'LIST_SELECTED_WIDGETS':listWidget[0]})
                    GLOBAL_VAR(set_global_var={'BOOL_SHOW_SELECTED':True})

                    widgetConfig[0].border = ft.border.all(2, ft.colors.YELLOW_900)
                    widgetConfig[0].update()


                    #: WILL BE A DEATH LINE IF MAKE THE SOLUTION TO:
                    #: DOUBLE CLICK IN CONTAINER ON_CLIK EVENT THAT PASS THROUG IT SELF 2 CLICKS IN SAME TIME

                    GLOBAL_VAR(set_global_var={'CHECK_CURRENT_TIME_DOBLE_CLICKS':click_time}) # <==== TO CHECK CLICKS SCAPED IN CONTAINERS

               numClick+=1

     def drag_accept(self,widgetDropBox):
          """
          NOTE:

          THIS PART IS VERY IMPORTANT BECAUSE IS THE LOOP OF THE DROP WIDGET THAT WE NEED APPEND OR PASS
          IN DEPENDENCY IF IS A CONTROLS USE APPEND AND IF IS A CONTENT WE PASS
          """

          #: widget to add
          self.widgetFilter      = ['Row',"GridView","Column","Stack",]
          self.widget_Filter     = ['row',"gridview","column","stack",]

          selectWidgetBox        = GLOBAL_VAR(get_global_var='SELECT_DRAGG')

          self.InstanceNewWidget = InfinityBoxLayerOne(selectWidgetBox)
          right_content          = widgetDropBox.control.content.content._get_control_name()

          if selectWidgetBox in self.widgetFilter:

               #
               #: IF DROPPED WIDGET HAS CONTENT ROW , GRIDVIEW,COLUMN,STACK WILL APPEND TO CONTROLS
               #
               if right_content in self.widget_Filter:
                    # AVOID COLLIDE CONTROLS WITH CONTENT
                    # print(right_content,'---------',selectWidgetBox.lower())
                    widgetDropBox.control.content.content.controls.append(self.InstanceNewWidget)
               # else:
               #      pass

          else:
               if right_content in self.widget_Filter:
                    """
                         IF WIDGET TO DROP_WIDGET IS A CONTROLS APPEND 'Row',"GridView","Column","Stack"
                    """

                    #
                    # IF DROPPED WIDGET HAS CONTENT ROW , GRIDVIEW,COLUMN,STACK WILL APPEND TO CONTROLS
                    #
                    # print(widgetDropBox.control.content.content.uid,'-----------------')
                    widgetDropBox.control.content.content.controls.append(self.InstanceNewWidget)

               # else:
               #      """
               #           IF WIDGET TO DROP_WIDGET IS A CONTENT PASS
               #      """
               #      # widgetDropBox.control.content.content.content=self.InstanceNewWidget
               #      pass

          #: UPDATE COLOR WIDGET
          widgetDropBox.control.content.border = True
          widgetDropBox.control.content.border = ft.border.all(0, ft.colors.TRANSPARENT)
          widgetDropBox.control.update()
          self.page.update()


     def drag_will_accept(self,widgetDropBox):
          #: UPDATE COLOR WIDGET
          widgetDropBox.control.content.border = None
          widgetDropBox.control.content.border = ft.border.all(4, ft.colors.CYAN_900)

          widgetDropBox.control.update()
          self.page.update()

     def drag_leave(self,widgetDropBox):
          #: UPDATE COLOR WIDGET
          widgetDropBox.control.content.border = True
          widgetDropBox.control.content.border = ft.border.all(0, ft.colors.TRANSPARENT)
          widgetDropBox.control.update()

          self.page.update()
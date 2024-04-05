from ..settings_var.settings_widget import global_var, get_global_var
from ..config_container.widget_editor import Build_Editor
from ..lite_menu_bar_down_phone.selected_widget import SelectedWidget

#####################
import flet as ft
import time

#####################
numWidget        = get_global_var(get_var='numWidget')
numClick         = get_global_var(get_var='numClick')
listWidgetUpdate = get_global_var(get_var='listWidgetUpdate')
#####################

class InfinityBoxLayerOne(ft.UserControl):
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
          # assd=''
          self.dataPassed = dataPassed
          # self.InstanceNewWidget = NewWidget()
     def build(self):
          global numWidget
          # self.tmp=ft.Container()
          """
          check <========== CircleAvatar, VerticalDivider

          """
          self.widgets={

               ####################### CONTAINERS LAYOUTS

                       "Row": [    ft.Container(bgcolor=ft.colors.BLACK45,alignment=ft.alignment.center,padding=ft.padding.all(6),border=ft.border.all(0.8, ft.colors.BLACK12),tooltip='Row',
                                   on_hover=lambda _:self.resetClick(),
                                   on_click=lambda _:self.touchWidgetIndex(self.infinityDropWidget),
                                   content=ft.Row( scroll="ALWAYS",
                                        controls= [
                                                       ],),),
                              ],
                    "Column": [    ft.Container(bgcolor=ft.colors.BLACK45,alignment=ft.alignment.center,padding=ft.padding.all(6),border=ft.border.all(0.8, ft.colors.BLACK12),tooltip='Column',
                                   on_hover=lambda _:self.resetClick(),
                                   on_click=lambda _:self.touchWidgetIndex(self.infinityDropWidget),
                                   content=ft.Column( scroll="ALWAYS",horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                        controls= [
                                                       ],),),
                              ],
                     "Stack": [    ft.Container(bgcolor=ft.colors.BLACK45,alignment=ft.alignment.center,padding=ft.padding.all(6),border=ft.border.all(0.8, ft.colors.BLACK12),tooltip='Stack',
                                   on_hover=lambda _:self.resetClick(),
                                   on_click=lambda _:self.touchWidgetIndex(self.infinityDropWidget),
                                   content=ft.Stack(
                                        controls= [
                                                       ],),),
                              ],
                  "GridView": [    ft.Container(bgcolor=ft.colors.BLACK45,alignment=ft.alignment.center,border=ft.border.all(0.8, ft.colors.BLACK12),tooltip='GridView',
                                   on_hover=lambda _:self.resetClick(),
                                   on_click=lambda _:self.touchWidgetIndex(self.infinityDropWidget),
                                   content=ft.GridView(runs_count=2,run_spacing=4,padding=8, spacing=4,
                                        controls= [
                                                       ],),),
                              ],
               ####################### SPACE LAYOUTS
                   "Divider": [    ft.Container(bgcolor=ft.colors.TRANSPARENT,alignment=ft.alignment.center,padding=ft.padding.all(6),margin=ft.margin.all(0),border=ft.border.all(0, ft.colors.TRANSPARENT),tooltip='Divider',
                                   on_hover=lambda _:self.resetClick(),
                                   on_click=lambda _:self.touchWidgetIndex(self.infinityDropWidget),
                                   content=ft.Divider(),),
                              ],
                              # VerticalDivider most set propertie [container height ] becouse no work onVerticalDivider
                  "Vertical": [    ft.Container(bgcolor=ft.colors.TRANSPARENT,alignment=ft.alignment.center,padding=ft.padding.all(6),height=25,margin=ft.margin.all(0),border=ft.border.all(0, ft.colors.TRANSPARENT),tooltip='VerticalDivider',
                                   on_hover=lambda _:self.resetClick(),
                                   on_click=lambda _:self.touchWidgetIndex(self.infinityDropWidget),
                                   content=ft.VerticalDivider(width=1, color="white"),),
                              ],

               ####################### IMAGE WIDGET
                     "Image": [    ft.Container(bgcolor=ft.colors.TRANSPARENT,alignment=ft.alignment.center,padding=ft.padding.all(6),margin=ft.margin.all(0),border=ft.border.all(0, ft.colors.TRANSPARENT),tooltip='Image',
                                   on_hover=lambda _:self.resetClick(),
                                   on_click=lambda _:self.touchWidgetIndex(self.infinityDropWidget),
                                   content=ft.Image(src=f'no_imagen.jpg',fit=ft.ImageFit.FILL,width=110,height=110,tooltip='Image'),),
                              ],
                    "Avatar": [    ft.Container(bgcolor=ft.colors.TRANSPARENT,alignment=ft.alignment.center,padding=ft.padding.all(6),margin=ft.margin.all(0),border=ft.border.all(0, ft.colors.TRANSPARENT),tooltip='Avatar',
                                   on_hover=lambda _:self.resetClick(),
                                   on_click=lambda _:self.touchWidgetIndex(self.infinityDropWidget),
                                   content=ft.CircleAvatar(content=ft.Image(src=f'img.jpg',fit=ft.ImageFit.FILL,width=110,height=110,tooltip='Avatar',border_radius= ft.border_radius.all(36)),),),
                              ],
                      "Icon": [    ft.Container(bgcolor=ft.colors.TRANSPARENT,alignment=ft.alignment.center,padding=ft.padding.all(6),margin=ft.margin.all(0),border=ft.border.all(0, ft.colors.TRANSPARENT),tooltip='Icon',
                                   on_hover=lambda _:self.resetClick(),
                                   on_click=lambda _:self.touchWidgetIndex(self.infinityDropWidget),
                                   content=ft.Icon(name=ft.icons.ADD_REACTION_OUTLINED,tooltip='Icon'),),
                              ],
               ####################### TEXT  WIDGET
                     "Text":  [    ft.Container(bgcolor=ft.colors.TRANSPARENT,alignment=ft.alignment.center,padding=ft.padding.all(6),margin=ft.margin.all(0),border=ft.border.all(0, ft.colors.TRANSPARENT),tooltip='Text',
                                   on_hover=lambda _:self.resetClick(),
                                   on_click=lambda _:self.touchWidgetIndex(self.infinityDropWidget),
                                   content=ft.Text(value="Text",tooltip='Text'),),
                              ],
                "Text Field": [    ft.Container(bgcolor=ft.colors.TRANSPARENT,alignment=ft.alignment.center,padding=ft.padding.all(6),margin=ft.margin.all(0),border=ft.border.all(0, ft.colors.TRANSPARENT),tooltip='TextField',
                                   on_hover=lambda _:self.resetClick(),
                                   on_click=lambda _:self.touchWidgetIndex(self.infinityDropWidget),
                                   content=ft.TextField(label="TextField",tooltip='TextField',border_radius= ft.border_radius.all(30),height=40, cursor_height=20,content_padding= ft.padding.all(16),border_color=ft.colors.WHITE,focused_border_color=ft.colors.RED,),),
                              ],

               ####################### BUTTONS WIDGET

           "Elevated Button": [    ft.Container(bgcolor=ft.colors.TRANSPARENT,alignment=ft.alignment.center,padding=ft.padding.all(6),margin=ft.margin.all(0),border=ft.border.all(0, ft.colors.TRANSPARENT),tooltip='ElevatedButton',
                                   on_hover=lambda _:self.resetClick(),
                                   on_click=lambda _:self.touchWidgetIndex(self.infinityDropWidget),
                                   content=ft.ElevatedButton("Elevated Button",tooltip='ElevatedButton'),),
                              ],
               "Text Button": [    ft.Container(bgcolor=ft.colors.TRANSPARENT,alignment=ft.alignment.center,padding=ft.padding.all(6),margin=ft.margin.all(0),border=ft.border.all(0, ft.colors.TRANSPARENT),tooltip='TextButton',
                                   on_hover=lambda _:self.resetClick(),
                                   on_click=lambda _:self.touchWidgetIndex(self.infinityDropWidget),
                                   content=ft.TextButton("Text Button",tooltip='TextButton'),),
                              ],
               "Icon Button": [    ft.Container(bgcolor=ft.colors.TRANSPARENT,alignment=ft.alignment.center,padding=ft.padding.all(6),margin=ft.margin.all(0),border=ft.border.all(0, ft.colors.TRANSPARENT),tooltip='IconButton',
                                   on_hover=lambda _:self.resetClick(),
                                   on_click=lambda _:self.touchWidgetIndex(self.infinityDropWidget),
                                   content=ft.IconButton(tooltip='Icon Button',icon=ft.icons.ADD_LINK_SHARP),),
                              ],
                    "Filled": [    ft.Container(bgcolor=ft.colors.TRANSPARENT,alignment=ft.alignment.center,padding=ft.padding.all(6),margin=ft.margin.all(0),border=ft.border.all(0, ft.colors.TRANSPARENT),tooltip='FilledButton',
                                   on_hover=lambda _:self.resetClick(),
                                   on_click=lambda _:self.touchWidgetIndex(self.infinityDropWidget),
                                   content=ft.FilledButton("Filled Button",tooltip='FilledButton'),),
                              ],
                     "Tonal": [    ft.Container(bgcolor=ft.colors.TRANSPARENT,alignment=ft.alignment.center,padding=ft.padding.all(6),margin=ft.margin.all(0),border=ft.border.all(0, ft.colors.TRANSPARENT),tooltip='FilledTonalButton',
                                   on_hover=lambda _:self.resetClick(),
                                   on_click=lambda _:self.touchWidgetIndex(self.infinityDropWidget),
                                   content=ft.FilledTonalButton("Filled Tonal Button",tooltip='FilledTonalButton'),),
                              ],
                   "Outline": [    ft.Container(bgcolor=ft.colors.TRANSPARENT,alignment=ft.alignment.center,padding=ft.padding.all(6),margin=ft.margin.all(0),border=ft.border.all(0, ft.colors.TRANSPARENT),tooltip='OutlinedButton',
                                   on_hover=lambda _:self.resetClick(),
                                   on_click=lambda _:self.touchWidgetIndex(self.infinityDropWidget),
                                   content=ft.OutlinedButton("Outlined Button",tooltip='OutlinedButton'),),
                              ],

               ####################### SELECTIONS WIDGET
                 "Checkbox":  [    ft.Container(bgcolor=ft.colors.TRANSPARENT,alignment=ft.alignment.center,padding=ft.padding.all(6),margin=ft.margin.all(0),border=ft.border.all(0, ft.colors.TRANSPARENT),tooltip='Checkbox',
                                   on_hover=lambda _:self.resetClick(),
                                   on_click=lambda _:self.touchWidgetIndex(self.infinityDropWidget),
                                   content=ft.Checkbox(label="  Checkbox",tooltip='Checkbox',value=False),),
                              ],
                 "Cupertino": [    ft.Container(bgcolor=ft.colors.TRANSPARENT,alignment=ft.alignment.center,padding=ft.padding.all(6),margin=ft.margin.all(0),border=ft.border.all(0, ft.colors.TRANSPARENT),tooltip='CupertinoCheckbox',
                                   on_hover=lambda _:self.resetClick(),
                                   on_click=lambda _:self.touchWidgetIndex(self.infinityDropWidget),
                                   content=ft.CupertinoCheckbox(label="Cupertino Checkbox",tooltip='CupertinoCheckbox',value=False),),
                              ],
                    "Switch": [    ft.Container(bgcolor=ft.colors.TRANSPARENT,alignment=ft.alignment.center,padding=ft.padding.all(12),margin=ft.margin.all(0),border=ft.border.all(0, ft.colors.TRANSPARENT),tooltip='Switch',
                                   on_hover=lambda _:self.resetClick(),
                                   on_click=lambda _:self.touchWidgetIndex(self.infinityDropWidget),
                                   content=ft.Switch(label="    Cupertino Switch",tooltip='Switch',value=False),),
                              ],

                      "Chip": [    ft.Container(bgcolor=ft.colors.TRANSPARENT,alignment=ft.alignment.center,padding=ft.padding.all(6),margin=ft.margin.all(0),border=ft.border.all(0, ft.colors.TRANSPARENT),tooltip='Chip',
                                   on_hover=lambda _:self.resetClick(),
                                   on_click=lambda _:self.touchWidgetIndex(self.infinityDropWidget),
                                   content=ft.Chip(label=ft.Text("Chip"), leading=ft.Icon(ft.icons.CAMERA_ROUNDED),tooltip='Chip'),),
                              ],

                    "Slider": [    ft.Container(bgcolor=ft.colors.TRANSPARENT,alignment=ft.alignment.center,padding=ft.padding.all(6),margin=ft.margin.all(0),border=ft.border.all(0, ft.colors.TRANSPARENT),tooltip='CupertinoRadio',
                                   on_hover=lambda _:self.resetClick(),
                                   on_click=lambda _:self.touchWidgetIndex(self.infinityDropWidget),
                                   content=ft.CupertinoSlider(value=50,tooltip='CupertinoSlider',max=100),),
                              ],

                 # RadioGroup <==== need solve that issue
                 "Cup Radio": [    ft.Container(bgcolor=ft.colors.TRANSPARENT,alignment=ft.alignment.center,padding=ft.padding.all(12),margin=ft.margin.all(0),border=ft.border.all(0, ft.colors.TRANSPARENT),tooltip='CupertinoRadio',
                                   on_hover=lambda _:self.resetClick(),
                                   on_click=lambda _:self.touchWidgetIndex(self.infinityDropWidget),
                                   content=ft.RadioGroup(content=ft.CupertinoRadio(label="    Cupertino Radio",tooltip='CupertinoRadio',value=False),),),
                              ],

                     "Radio": [    ft.Container(bgcolor=ft.colors.TRANSPARENT,alignment=ft.alignment.center,padding=ft.padding.all(12),margin=ft.margin.all(0),border=ft.border.all(0, ft.colors.TRANSPARENT),tooltip='Radio',
                                   on_hover=lambda _:self.resetClick(),
                                   on_click=lambda _:self.touchWidgetIndex(self.infinityDropWidget),
                                   content=ft.RadioGroup(content=ft.Radio(label="    Radio",tooltip='Radio',value='False'),),),
                              ],
               }

          ####################### ALERTS STATUS

          ####################### WIDGETS STATUS

          ####################### ESPECIAL WIDGET

          ####################### CHARTS LAYOUTS
          selectWidgetBox                    = get_global_var(get_var='selectWidgetBox')
          self.infinityDropWidget            = self.widgets.get(selectWidgetBox)
          self.infinityDropWidget[0].id      = f"{self.dataPassed}: {numWidget}"              # OUR ID
          self.infinityDropWidget[0].tooltip = f"{self.dataPassed}: {numWidget}"              # TOOLTIP ID

          print('============')
          print(f"""
     selected_widget: {self.dataPassed},
     ID_widget: {numWidget},
     ID tooltip: {self.infinityDropWidget[0].tooltip}
     Content: {self.infinityDropWidget}""")
          print('============')

          self.drag_boxs =ft.DragTarget(
                                             group     = "GroupDragg",
                                             content   = self.infinityDropWidget[0],

                                        on_will_accept = self.drag_will_accept,           # Traslate Drop
                                        on_leave       = self.drag_leave,                 # Leafing Drop Line Border
                                        on_accept      = lambda _:self.drag_accept(_),                # Accept Drop
                                        )

          numWidget+=1
          # return self.infinityDropWidget
          return self.drag_boxs

     def resetClick(self):
          global numClick

          numClick=1

     def touchWidgetIndex(self,listWidget):
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


          if numClick == 1:
               # listWidgetUpdate.append(listWidget[0])
               # time.sleep(0.3)

               tmp_list         = get_global_var(get_var='listWidgetUpdate')
               listWidgetUpdate = listWidget

               if tmp_list:
                    if not tmp_list.tooltip == listWidgetUpdate[0].tooltip:
                         tmp_list.border = ft.border.all(0, ft.colors.TRANSPARENT)
                         tmp_list.update()

               widgetConfig = listWidgetUpdate
               #############################################################################
               # this function will update right box attribute
               # print(f'Widget New number: {listWidgetUpdate[0].tooltip} and ID: {listWidgetUpdate[0].uid}')
               # print(f"all list {listWidgetUpdate}")

               # self.infinityDropWidget[0]  #<<<<<<<<<<<<<<< CLICKED WIDGET
               Build_Editor.update_widget_attributes(widget_cliked=self.infinityDropWidget[0])
               ############################################################################
               time.sleep(0.1)

               # print(get_global_var(get_var='page'))
               ############################################################################
               # on click over widget <===
               data_widget = get_global_var(get_var='text_widget_selected')
               data_widget.controls[0].content.controls[1].spans[0].text = listWidget[0].tooltip
               data_widget.controls[0].update()

               print(data_widget.controls[0].content.controls[1].spans[0].text)

               print(listWidget[0].uid ,'selected_widget BOX IN PHONE listWidgetUpdate')

               # listWidget[0].content = None
               # print(listWidget[0] ,'selected_widget BOX IN PHONE listWidgetUpdate')
               # print(self.infinityDropWidget[0] ,'selected_widget BOX IN PHONE listWidgetUpdate')

               global_var(data_global={'listWidgetUpdate':listWidget[0]})
               widgetConfig[0].border = ft.border.all(0.03, ft.colors.CYAN)
               widgetConfig[0].update()
               # print(widgetConfig[0].uid,'<<<<,')
               # listWidgetUpdate=[]

          numClick+=1

     def drag_accept(self,widgetDropBox):
          """
          NOTE:

          THIS PART IS VERY IMPORTANT BECAUSE IS THE LOOP OF THE DROP WIDGET THAT WE NEED APPEND OR PASS
          IN DEPENDENCY IF IS A CONTROLS USE APPEND AND IF IS A CONTENT WE PASS
          """
          ############################################################################
          ################################# widget to add
          self.widgetFilter      = ['Row',"GridView","Column","Stack",]
          self.widget_Filter     = ['row',"gridview","column","stack",]

          selectWidgetBox        = get_global_var(get_var='selectWidgetBox')

          self.InstanceNewWidget = InfinityBoxLayerOne(selectWidgetBox)
          right_content          = widgetDropBox.control.content.content._get_control_name()

          if selectWidgetBox in self.widgetFilter:
               """ IF WIDGET TO DROP_WIDGET IS A  Row , GridView , Column, Stack  will add to control """
               if right_content in self.widget_Filter:
                    # AVOID COLLIDE CONTROLS WITH CONTENT
                    # print(right_content,'---------',selectWidgetBox.lower())
                    widgetDropBox.control.content.content.controls.append(self.InstanceNewWidget)
               else:
                    pass

          else:
               if right_content in self.widget_Filter:
                    """
                         IF WIDGET TO DROP_WIDGET IS A CONTROLS APPEND 'Row',"GridView","Column","Stack"
                    """

                    # print(widgetDropBox.control.content.content.uid,'-----------------')
                    widgetDropBox.control.content.content.controls.append(self.InstanceNewWidget)

               else:
                    """
                         IF WIDGET TO DROP_WIDGET IS A CONTENT PASS
                    """
                    # widgetDropBox.control.content.content.content=self.InstanceNewWidget
                    pass

          ################################## UPDATE WIDGET ###########################
          widgetDropBox.control.content.border = True
          widgetDropBox.control.content.border = ft.border.all(0, ft.colors.TRANSPARENT)
          widgetDropBox.control.update()
          self.page.update()
          ############################################################################

     def drag_will_accept(self,widgetDropBox):
          widgetDropBox.control.content.border = None
          widgetDropBox.control.content.border = ft.border.all(2, ft.colors.RED)
          widgetDropBox.control.update()
          self.page.update()

     def drag_leave(self,widgetDropBox):
          widgetDropBox.control.content.border = True
          widgetDropBox.control.content.border = ft.border.all(0, ft.colors.TRANSPARENT)
          widgetDropBox.control.update()
          self.page.update()
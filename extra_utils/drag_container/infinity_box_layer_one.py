from extra_utils.settings_var.settings_widget import global_var, get_global_var
import flet as ft
import time

numWidget = get_global_var(get_var='numWidget')
numClick  = get_global_var(get_var='numClick')
listWidgetUpdate = get_global_var(get_var='listWidgetUpdate')




widgetConfig =[ft.Container(
          ##################### PROPERTY ROW
          expand=True,
          ink=False,                                                      # click effect ripple
          bgcolor="#3f9a64",                                              # ft.colors.YELLOW,RED,GREEN,BLACK,WHITE,BLUE,CYAN,GREY,PINK,TEAL
          padding= ft.padding.all(8), # inside box                        # padding.only(left=8, top=8, right=8, bottom=8),
          margin = ft.margin.all(8),  # outside box                       # margin.only (left=8, top=8, right=8, bottom=8),
          alignment=ft.alignment.center,                                  # top_left,top_center,top_right,center_left,center,center_right,bottom_left,bottom_center,bottom_right
          # border_radius= ft.border_radius.all(30),                      # ft.border_radius.only(topLeft=8, topRight=8, bottomLeft=8, bottomRight=8),
          # border=ft.border.all(2, ft.colors.BLACK),                     # ft.border.only(Left=8, top=8, right=8, bottom=8),
          # image_src=f"/icons/icon-512.png",
          # image_fit="FILL",                                             # CONTAIN, COVER, FILL, FIT_HEIGHT, FIT_WIDTH, SCALE_DOWN
          # width=150,
          # height=150,
          # tooltip='Container',
          ##################### EFFECTS
          # blur=(4, 4),              # (Vertical,Horizontal)             # blur=ft.Blur(10, 0, ft.BlurTileMode.MIRROR)
          # gradient=ft.LinearGradient( begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=[ft.colors.BLUE, ft.colors.YELLOW],),
          # gradient=ft.RadialGradient( colors=[ft.colors.YELLOW, ft.colors.BLUE],),
          ##################### WIDGETS

     # content=ft.ElevatedButton("press container",tooltip='buttom'),
     ##################### EVENTS
     # on_click=lambda _:print(_),                                   # on_hover=print('on click over'), on_long_press=print('long press'),
)#<=== NOTE COMA
]

class InfinityBoxLayerOne(ft.UserControl):
     """
     NOTE:

     1. THIS IS VERY IMPORTANT WIDGET TO DRAGG AND DROP
        IS A LOOP DRAGGTARGET THAT WILL CONTAIN ALL WIDGET INSIDE.

     AND IT SELF WILL ADD WIDGETS DEPENDIND

     ROW , COLUMN , GRIDVIEW ... USE CONTROLS=[ WIDGETS, WIDGETS... ]

     REST WIDGETS USE CONTENT = WIDGET()


     """

     def __init__(self,dataPassed=''):
          super().__init__()
          # assd=''
          self.dataPassed = dataPassed
          # self.InstanceNewWidget = NewWidget()
     def build(self):
          global numWidget
          # self.tmp=ft.Container()

          self.widgets={
               #################################################### CONTROLS ####################################################

                       "Row": [    ft.Container(bgcolor='blue',alignment=ft.alignment.center,padding=8,border=ft.border.all(0.8, ft.colors.BLACK),tooltip='Row',
                                   on_hover=lambda _:self.resetClick(),
                                   on_click=lambda _:self.touchWidgetIndex(self.infinityDropWidget),
                                   content=ft.Row( scroll="ALWAYS",
                                        controls= [
                                                       ],),),
                              ],
                    "Column": [    ft.Container(bgcolor='red',alignment=ft.alignment.center,padding=8,border=ft.border.all(0.8, ft.colors.BLACK),tooltip='Column',
                                   on_hover=lambda _:self.resetClick(),
                                   on_click=lambda _:self.touchWidgetIndex(self.infinityDropWidget),
                                   content=ft.Column( scroll="ALWAYS",horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                        controls= [
                                                       ],),),
                              ],
                  "GridView": [    ft.Container(bgcolor='purple',alignment=ft.alignment.center,border=ft.border.all(0.8, ft.colors.BLACK),tooltip='GridView',
                                   on_hover=lambda _:self.resetClick(),
                                   on_click=lambda _:self.touchWidgetIndex(self.infinityDropWidget),
                                   content=ft.GridView(runs_count=2,run_spacing=4,padding=8, spacing=4,
                                        controls= [
                                                       ],),),
                              ],
                     "Stack": [    ft.Container(bgcolor='YELLOW',alignment=ft.alignment.center,padding=8,border=ft.border.all(0.8, ft.colors.BLACK),tooltip='Stack',
                                   on_hover=lambda _:self.resetClick(),
                                   on_click=lambda _:self.touchWidgetIndex(self.infinityDropWidget),
                                   content=ft.Stack(
                                        controls= [
                                                       ],),),
                              ],
               #################################################### WIDGETS ####################################################
                  "Elevated": [    ft.Container(bgcolor='BLACK',alignment=ft.alignment.center,padding=8,border=ft.border.all(0.8, ft.colors.BLACK),tooltip='ElevatedButton',
                                   on_hover=lambda _:self.resetClick(),
                                   on_click=lambda _:self.touchWidgetIndex(self.infinityDropWidget),
                                   content=ft.ElevatedButton("Button",tooltip='ElevatedButton',bgcolor='red'),),
                              ],
                }

          selectWidgetBox = get_global_var(get_var='selectWidgetBox')
          self.infinityDropWidget = self.widgets.get(selectWidgetBox)
          self.infinityDropWidget[0].id=f"{self.dataPassed}: {numWidget}"              # OUR ID
          self.infinityDropWidget[0].tooltip=f"{self.dataPassed}: {numWidget}"         # TOOLTIP ID

          print('============')
          print(f"""
 selected_widget: {self.dataPassed},
 ID_widget: {numWidget},
 ID tooltip: {self.infinityDropWidget[0].tooltip}
 Content: {self.infinityDropWidget}""")
          print('============')


          self.drag_boxs =ft.DragTarget(
                                             group = "GroupDragg",
                                             content = self.infinityDropWidget[0],

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

          """
          global numClick


          if numClick == 1:
               # listWidgetUpdate.append(listWidget[0])
               # time.sleep(0.3)

               tmp_list = get_global_var(get_var='listWidgetUpdate')
               listWidgetUpdate=listWidget

               if tmp_list:
                    if not tmp_list.tooltip == listWidgetUpdate[0].tooltip:
                         tmp_list.border=ft.border.all(2, ft.colors.BLACK)
                         tmp_list.update()

               widgetConfig = listWidgetUpdate
               # print(listWidgetUpdate[0].tooltip,'<<<<<<<<<<<')
               # time.sleep(0.3)

               global_var(data_global={'listWidgetUpdate':listWidget[0]})

               widgetConfig[0].border = ft.border.all(2, ft.colors.YELLOW)
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
          self.widgetFilter = ['Row',"GridView","Column","Stack",]
          self.widget_Filter = ['row',"gridview","column","stack",]

          selectWidgetBox = get_global_var(get_var='selectWidgetBox')

          self.InstanceNewWidget = InfinityBoxLayerOne(selectWidgetBox)
          right_content  = widgetDropBox.control.content.content._get_control_name()

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
                    widgetDropBox.control.content.content.controls.append(self.InstanceNewWidget)

               else:
                    """
                         IF WIDGET TO DROP_WIDGET IS A CONTENT PASS
                    """
                    # widgetDropBox.control.content.content.content=self.InstanceNewWidget
                    pass

          ################################## UPDATE WIDGET ###########################
          widgetDropBox.control.content.border = True
          widgetDropBox.control.content.border=ft.border.all(2, ft.colors.BLACK)
          widgetDropBox.control.update()
          self.page.update()
          ############################################################################

     def drag_will_accept(self,widgetDropBox):
          widgetDropBox.control.content.border = None
          widgetDropBox.control.content.border=ft.border.all(2, ft.colors.RED)
          widgetDropBox.control.update()
          self.page.update()

     def drag_leave(self,widgetDropBox):
          widgetDropBox.control.content.border = True
          widgetDropBox.control.content.border=ft.border.all(2, ft.colors.BLACK)
          widgetDropBox.control.update()
          self.page.update()
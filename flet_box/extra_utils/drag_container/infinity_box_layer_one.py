import flet as ft
# import time

# from ..config_container.widget_editor import Build_Editor
# from ..lite_menu_bar_down_phone.selected_widget import SelectedWidget
# from ..settings_var.settings_widget import GLOBAL_VAR

# numWidget        = GLOBAL_VAR(get_global_var='NUM_WIDGETS_DROPPED')
# numClick         = GLOBAL_VAR(get_global_var='NUM_CLICKS')
# listWidgetUpdate = GLOBAL_VAR(get_global_var='LIST_SELECTED_WIDGETS')

PRESENTATION_TEXT: str = """Ready to make your first app!!"""
numWidget: int = 1

class InfinityBoxLayerOne(ft.DragTarget):
     """
     NOTE:

     1. THIS IS VERY IMPORTANT WIDGET TO DRAGG AND DROP
        IS A LOOP DRAGGTARGET THAT WILL CONTAIN ALL WIDGET INSIDE.

     AND IT SELF WILL ADD WIDGETS DEPENDIND
     ROW , COLUMN , GRIDVIEW ... USE CONTROLS=[ WIDGETS, WIDGETS... ]
     REST WIDGETS USE CONTENT = WIDGET()

     2. Make widget need
     """
     md1 = """# Markdown Example Markdown allows you to easily include formatted text, images, and even formatted Dart code in your app.\n## Titles"""

     def __init__(self,dataPassed='',page: object=None):
          super().__init__(content=ft.Container())
          self.group     = "GroupDragg"
          self.page = page

          self.dataPassed    = dataPassed
          self.clip_behavior = ft.ClipBehavior.NONE

          self.widgets={

               #: CONTAINERS LAYOUTS

                       "Row": [    ft.Container(bgcolor=ft.colors('black54'),alignment=ft.alignment.center,padding=ft.padding.all(6),border=ft.border.all(2, ft.colors('cyan900')),tooltip='Row',
                                   ink=True,
                                   ink_color='cyan',
                                   # on_hover=lambda _:self.resetClick(),
                                   on_click=lambda _:self.touch_widget_in_phone(selected_widget=self.infinityDropWidget),
                                   content=ft.Row( scroll="ALWAYS",
                                        controls= [
                                                       ],),),
                              ],
            "ResponsiveRow": [    ft.Container(bgcolor=ft.colors('black54'),alignment=ft.alignment.center,padding=ft.padding.all(6),border=ft.border.all(2, ft.colors('cyan900')),tooltip='ResponsiveRow',
                                   ink=True,
                                   ink_color='cyan',
                                   # on_hover=lambda _:self.resetClick(),
                                   on_click=lambda _:self.touch_widget_in_phone(selected_widget=self.infinityDropWidget),
                                   content=ft.ResponsiveRow(
                                        controls= [
                                                       ],),),
                              ],
                    "Column": [    ft.Container(bgcolor=ft.colors('black54'),alignment=ft.alignment.center,padding=ft.padding.all(6),border=ft.border.all(2, ft.colors('cyan900')),tooltip='Column',
                                   ink=True,
                                   ink_color='yellow',
                                   # on_hover=lambda _:self.resetClick(),
                                   on_click=lambda _:self.touch_widget_in_phone(selected_widget=self.infinityDropWidget),
                                   content=ft.Column( scroll="ALWAYS",horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                        controls= [
                                                       ],),),
                              ],
              "ListView": [    ft.Container(bgcolor=ft.colors('black54'),alignment=ft.alignment.center,padding=ft.padding.all(12),margin=ft.margin.all(0),border=ft.border.all(0, ft.colors('transparent')),tooltip='Radio',
                                   ink=True,
                                   ink_color='red',
                                   # on_hover=lambda _:self.resetClick(),
                                   on_click=lambda _:self.touch_widget_in_phone(selected_widget=self.infinityDropWidget),
                                   content=ft.ListView(expand=1, spacing=10, auto_scroll=True,
                                                       controls=[
                                                                 ])

                                   ),
                          ],
                     "Stack": [    ft.Container(bgcolor=ft.colors('black54'),alignment=ft.alignment.center,padding=ft.padding.all(6),border=ft.border.all(2, ft.colors('cyan900')),tooltip='Stack',
                                   ink=True,
                                   ink_color='purple',
                                   # on_hover=lambda _:self.resetClick(),
                                   on_click=lambda _:self.touch_widget_in_phone(selected_widget=self.infinityDropWidget),
                                   content=ft.Stack(
                                        controls= [
                                                       ],),),
                              ],
                  "GridView": [    ft.Container(bgcolor=ft.colors('black54'),alignment=ft.alignment.center,border=ft.border.all(2, ft.colors('cyan900')),tooltip='GridView',
                                   ink=True,
                                   ink_color='green',
                                   # on_hover=lambda _:self.resetClick(),
                                   on_click=lambda _:self.touch_widget_in_phone(selected_widget=self.infinityDropWidget),
                                   content=ft.GridView(runs_count=2,run_spacing=4,padding=ft.padding.all(6), spacing=4,
                                        controls= [
                                                       ],),),
                              ],
               #: SPACE LAYOUTS

                   "Divider": [    ft.Container(bgcolor=ft.colors('transparent'),alignment=ft.alignment.center,padding=ft.padding.all(6),margin=ft.margin.all(0),border=ft.border.all(0, ft.colors('transparent')),tooltip='Divider',
                                   ink=True,
                                   ink_color='red',
                                   # on_hover=lambda _:self.resetClick(),
                                   on_click=lambda _:self.touch_widget_in_phone(selected_widget=self.infinityDropWidget),
                                   content=ft.Divider(),),
                              ],
                              # VerticalDivider most set propertie [container height ] becouse no work onVerticalDivider
                  "Vertical": [    ft.Container(bgcolor=ft.colors('transparent'),alignment=ft.alignment.center,padding=ft.padding.all(6),height=25,margin=ft.margin.all(0),border=ft.border.all(0, ft.colors('transparent')),tooltip='VerticalDivider',
                                   ink=True,
                                   ink_color='red',
                                   # on_hover=lambda _:self.resetClick(),
                                   on_click=lambda _:self.touch_widget_in_phone(selected_widget=self.infinityDropWidget),
                                   content=ft.VerticalDivider(color="white"),),
                              ],

               #: IMAGE WIDGET

                     "Image": [    ft.Container(alignment=ft.alignment.center,padding=ft.padding.all(6),margin=ft.margin.all(0),border=ft.border.all(0, ft.colors('transparent')),tooltip='Image',
                                   ink=True,
                                   ink_color='red',
                                   # on_hover=lambda _:self.resetClick(),
                                   on_click=lambda _:self.touch_widget_in_phone(selected_widget=self.infinityDropWidget),
                                   content=ft.Image(src=f'.no_image.jpg',fit=ft.ImageFit.FILL),
                                   # image =ft.DecorationImage(
                                   #                 src='.no_image.jpg',
                                   #                 fit=ft.ImageFit.FILL,  #: CONTAIN, FILL, FIT_WIDTH, SCALE_DOWN, COVER, FIT_HEIGHT, NONE
                                   #                 # opacity = 0.08 if self.page.window.width <= 620 else 0.2,
                                   #             ),
                                   # width=80,height=80,
                                   # content=ft.Container()
                                   # content=ft.Image(src=f'.no_image.jpg',fit=ft.ImageFit.FILL,width=110,height=110,tooltip='Image')
                                   ),
                              ],
                    "Avatar": [    ft.Container(bgcolor=ft.colors('transparent'),alignment=ft.alignment.center,padding=ft.padding.all(6),margin=ft.margin.all(0),border=ft.border.all(0, ft.colors('transparent')),tooltip='Avatar',
                                   ink=True,
                                   ink_color='red',
                                   # on_hover=lambda _:self.resetClick(),
                                   on_click=lambda _:self.touch_widget_in_phone(selected_widget=self.infinityDropWidget),
                                   content=ft.CircleAvatar(background_image_src='.avatar.jpg'),),
                              ],
                      "Icon": [    ft.Container(bgcolor=ft.colors('transparent'),alignment=ft.alignment.center,padding=ft.padding.all(6),margin=ft.margin.all(0),border=ft.border.all(0, ft.colors('transparent')),tooltip='Icon',
                                   ink=True,
                                   ink_color='red',
                                   # on_hover=lambda _:self.resetClick(),
                                   on_click=lambda _:self.touch_widget_in_phone(selected_widget=self.infinityDropWidget),
                                   content=ft.Icon(name=ft.icons('add_reaction_outlined'),tooltip='Icon'),),
                              ],
               #: TEXT  WIDGET

                     "Text":  [    ft.Container(bgcolor=ft.colors('transparent'),alignment=ft.alignment.center,padding=ft.padding.all(6),margin=ft.margin.all(0),border=ft.border.all(0, ft.colors('transparent')),tooltip='Text',
                                   ink=True,
                                   ink_color='red',
                                   # on_hover=lambda _:self.resetClick(),
                                   on_click=lambda _:self.touch_widget_in_phone(selected_widget=self.infinityDropWidget),
                                   content=ft.Text(value=PRESENTATION_TEXT,tooltip='Text',size=10),),
                              ],
                "Text Field": [    ft.Container(bgcolor=ft.colors('transparent'),alignment=ft.alignment.center,padding=ft.padding.all(4),margin=ft.margin.all(0),border=ft.border.all(0, ft.colors('transparent')),tooltip='TextField',
                                   ink=True,
                                   border_radius = ft.border_radius.all(30),
                                   ink_color='red',
                                   # on_hover=lambda _:self.resetClick(),
                                   blur=(8,8),
                                   width=240,
                                   on_click=lambda _:self.touch_widget_in_phone(selected_widget=self.infinityDropWidget),
                                   content=ft.TextField(label="what's your name ?",tooltip='TextField',border_radius= ft.border_radius.all(30),height=32, cursor_height=20,content_padding= ft.padding.all(16),border_color=ft.colors('white'),focused_border_color=ft.colors('red'),
                                        text_size=12,
                                        width=240,
                                        ),),
                              ],

               #: BUTTONS WIDGET

           "Elevated Button": [    ft.Container(bgcolor=ft.colors('transparent'),alignment=ft.alignment.center,padding=ft.padding.all(6),margin=ft.margin.all(0),border=ft.border.all(0, ft.colors('transparent')),tooltip='ElevatedButton',
                                   ink=True,
                                   ink_color='red',
                                   # on_hover=lambda _:self.resetClick(),
                                   on_click=lambda _:self.touch_widget_in_phone(selected_widget=self.infinityDropWidget),
                                   content=ft.ElevatedButton(text="Accept",tooltip='ElevatedButton'),),
                              ],
               "Text Button": [    ft.Container(bgcolor=ft.colors('transparent'),alignment=ft.alignment.center,padding=ft.padding.all(6),margin=ft.margin.all(0),border=ft.border.all(0, ft.colors('transparent')),tooltip='TextButton',
                                   ink=True,
                                   ink_color='red',
                                   # on_hover=lambda _:self.resetClick(),
                                   on_click=lambda _:self.touch_widget_in_phone(selected_widget=self.infinityDropWidget),
                                   content=ft.TextButton(text="Accept",tooltip='TextButton',height=28),),
                              ],
               "Icon Button": [    ft.Container(bgcolor=ft.colors('transparent'),alignment=ft.alignment.center,padding=ft.padding.all(6),margin=ft.margin.all(0),border=ft.border.all(0, ft.colors('transparent')),tooltip='IconButton',
                                   ink=True,
                                   ink_color='red',
                                   # on_hover=lambda _:self.resetClick(),
                                   on_click=lambda _:self.touch_widget_in_phone(selected_widget=self.infinityDropWidget),
                                   content=ft.IconButton(tooltip='Accept',icon=ft.icons('add_link_sharp')),),
                              ],
                    "Filled": [    ft.Container(bgcolor=ft.colors('transparent'),alignment=ft.alignment.center,padding=ft.padding.all(6),margin=ft.margin.all(0),border=ft.border.all(0, ft.colors('transparent')),tooltip='FilledButton',
                                   ink=True,
                                   ink_color='red',
                                   # on_hover=lambda _:self.resetClick(),
                                   on_click=lambda _:self.touch_widget_in_phone(selected_widget=self.infinityDropWidget),
                                   content=ft.FilledButton("Accept",tooltip='FilledButton',height=28),),
                              ],
                     "Tonal": [    ft.Container(bgcolor=ft.colors('transparent'),alignment=ft.alignment.center,padding=ft.padding.all(6),margin=ft.margin.all(0),border=ft.border.all(0, ft.colors('transparent')),tooltip='FilledTonalButton',
                                   ink=True,
                                   ink_color='red',
                                   # on_hover=lambda _:self.resetClick(),
                                   on_click=lambda _:self.touch_widget_in_phone(selected_widget=self.infinityDropWidget),
                                   content=ft.FilledTonalButton("Accept",tooltip='FilledTonalButton',height=28),),
                              ],
                   "Outline": [    ft.Container(bgcolor=ft.colors('transparent'),alignment=ft.alignment.center,padding=ft.padding.all(6),margin=ft.margin.all(0),border=ft.border.all(0, ft.colors('transparent')),tooltip='OutlinedButton',
                                   ink=True,
                                   ink_color='red',
                                   # on_hover=lambda _:self.resetClick(),
                                   on_click=lambda _:self.touch_widget_in_phone(selected_widget=self.infinityDropWidget),
                                   content=ft.OutlinedButton("Accept",tooltip='OutlinedButton',height=28),),
                              ],

               #: SELECTIONS WIDGET

                 "Checkbox":  [    ft.Container(bgcolor=ft.colors('transparent'),alignment=ft.alignment.center,padding=ft.padding.all(6),margin=ft.margin.all(0),border=ft.border.all(0, ft.colors('transparent')),tooltip='Checkbox',
                                   ink=True,
                                   ink_color='red',
                                   # on_hover=lambda _:self.resetClick(),
                                   on_click=lambda _:self.touch_widget_in_phone(selected_widget=self.infinityDropWidget),
                                   content=ft.Checkbox(label="  Accept the target",tooltip='Checkbox',value=False,height=28),),
                              ],
                 "Cupertino": [    ft.Container(bgcolor=ft.colors('transparent'),alignment=ft.alignment.center,padding=ft.padding.all(6),margin=ft.margin.all(0),border=ft.border.all(0, ft.colors('transparent')),tooltip='CupertinoCheckbox',
                                   ink=True,
                                   ink_color='red',
                                   # on_hover=lambda _:self.resetClick(),
                                   on_click=lambda _:self.touch_widget_in_phone(selected_widget=self.infinityDropWidget),
                                   content=ft.CupertinoCheckbox(label="  Accept the target",tooltip='CupertinoCheckbox',value=False,height=28),),
                              ],
                    "Switch": [    ft.Container(bgcolor=ft.colors('transparent'),alignment=ft.alignment.center,padding=ft.padding.all(12),margin=ft.margin.all(0),border=ft.border.all(0, ft.colors('transparent')),tooltip='Switch',
                                   ink=True,
                                   ink_color='red',
                                   # on_hover=lambda _:self.resetClick(),
                                   on_click=lambda _:self.touch_widget_in_phone(selected_widget=self.infinityDropWidget),
                                   content=ft.Switch(label="  Accept the target",tooltip='Switch',value=False,height=28),),
                              ],

                      "Chip": [    ft.Container(bgcolor=ft.colors('transparent'),alignment=ft.alignment.center,padding=ft.padding.all(6),margin=ft.margin.all(0),border=ft.border.all(0, ft.colors('transparent')),tooltip='Chip',
                                   ink=True,
                                   ink_color='red',
                                   # on_hover=lambda _:self.resetClick(),
                                   on_click=lambda _:self.touch_widget_in_phone(selected_widget=self.infinityDropWidget),
                                   content=ft.Chip(
                                                       label=ft.Text("  Accept the target"),
                                                       leading=ft.Icon('camera_rounded'),
                                                       tooltip='Chip',
                                                       on_click=lambda _:print('help')),),
                              ],

                    "Slider": [    ft.Container(bgcolor=ft.colors('transparent'),alignment=ft.alignment.center,padding=ft.padding.all(6),margin=ft.margin.all(0),border=ft.border.all(0, ft.colors('transparent')),tooltip='CupertinoRadio',
                                   ink=True,
                                   ink_color='red',
                                   # on_hover=lambda _:self.resetClick(),
                                   on_click=lambda _:self.touch_widget_in_phone(selected_widget=self.infinityDropWidget),
                                   content=ft.CupertinoSlider(tooltip='CupertinoSlider',max=100,height=28,),),
                              ],

                 #: RadioGroup <==== need solve that issue

                 "Cup Radio": [    ft.Container(bgcolor=ft.colors('transparent'),alignment=ft.alignment.center,padding=ft.padding.all(12),margin=ft.margin.all(0),border=ft.border.all(0, ft.colors('transparent')),tooltip='CupertinoRadio',
                                   ink=True,
                                   ink_color='red',
                                   # on_hover=lambda _:self.resetClick(),
                                   on_click=lambda _:self.touch_widget_in_phone(selected_widget=self.infinityDropWidget),
                                   content=ft.RadioGroup(
                                                       content = ft.DragTarget(
                                                                 group="GroupDragg",
                                                                 content=ft.Container(
                                                                           content=ft.CupertinoRadio(
                                                                                label="  Accept the target",
                                                                                tooltip='CupertinoRadio',
                                                                                value=False,
                                                                                height=28,
                                                       ))))
                                                       ),
                              ],

                     "Radio": [    ft.Container(bgcolor=ft.colors('transparent'),alignment=ft.alignment.center,padding=ft.padding.all(12),margin=ft.margin.all(0),border=ft.border.all(0, ft.colors('transparent')),tooltip='Radio',
                                   ink=True,
                                   ink_color='red',
                                   # on_hover=lambda _:self.resetClick(),
                                   on_click=lambda _:self.touch_widget_in_phone(selected_widget=self.infinityDropWidget),
                                   content=ft.RadioGroup(content=ft.Radio(label="  Accept the target",tooltip='Radio',value='False',height=28),),),
                              ],
                     "Space": [    ft.Container(bgcolor=ft.colors('transparent'),alignment=ft.alignment.center,padding=ft.padding.all(12),margin=ft.margin.all(0),border=ft.border.all(0, ft.colors('transparent')),tooltip='Radio',
                                   ink=True,
                                   ink_color='red',
                                   # on_hover=lambda _:self.resetClick(), height=30, expand=True,
                                   on_click=lambda _:self.touch_widget_in_phone(selected_widget=self.infinityDropWidget),
                                   content=ft.Container(expand=True),
                                   ),
                              ],
               ##
               ## { item_description }
               ##
               ##
               # "": [    ft.Container(bgcolor=ft.colors('transparent'),alignment=ft.alignment.center,padding=ft.padding.all(12),margin=ft.margin.all(0),border=ft.border.all(0, ft.colors('transparent')),tooltip='Radio',
               #                     ink=True,
                                   # ink_color='red',
                                   # on_hover=lambda _:self.resetClick(),
               #                     on_click=lambda _:self.touch_widget_in_phone(selected_widget=self.infinityDropWidget),
               #                     content=
               #                     ),),
               #         ],

          "PieChart": [    ft.Container(bgcolor=ft.colors('transparent'),alignment=ft.alignment.center,padding=ft.padding.all(12),margin=ft.margin.all(0),border=ft.border.all(0, ft.colors('transparent')),tooltip='Radio',
                                   ink=True,
                                   ink_color='red',
                                   # on_hover=lambda _:self.resetClick(),
                                   on_click=lambda _:self.touch_widget_in_phone(selected_widget=self.infinityDropWidget),
                                   content=ft.PieChart(
                                                  sections=[
                                                         ft.PieChartSection(
                                                             25,
                                                             color=ft.colors('blue'),
                                                             radius=80,
                                                             border_side=ft.BorderSide(0, ft.Colors.with_opacity(0, ft.colors('white'))),
                                                         ),
                                                         ft.PieChartSection(
                                                             25,
                                                             color=ft.colors('yellow'),
                                                             radius=65,
                                                             border_side=ft.BorderSide(0, ft.Colors.with_opacity(0, ft.colors('white'))),
                                                         ),
                                                      ft.PieChartSection(
                                                             25,
                                                             color=ft.colors('red'),
                                                             radius=65,
                                                             border_side=ft.BorderSide(0, ft.Colors.with_opacity(0, ft.colors('white'))),
                                                         ),
                                                     ],
                                                     sections_space=1,
                                                     center_space_radius=0,
                                                     expand=True,
                                   ),),
                       ],

             "Badge": [    ft.Container(bgcolor=ft.colors('transparent'),alignment=ft.alignment.center,padding=ft.padding.all(12),margin=ft.margin.all(0),border=ft.border.all(0, ft.colors('transparent')),tooltip='Radio',
                                   ink=True,
                                   ink_color='red',
                                   # on_hover=lambda _:self.resetClick(),
                                   on_click=lambda _:self.touch_widget_in_phone(selected_widget=self.infinityDropWidget),
                                   content=ft.Badge(
                                        ft.Icon(name=ft.icons('car_crash_rounded')),
                                        # small_size=10,
                                        ),
                                   ),
                         ],

             "Markdown": [    ft.Container(bgcolor=ft.colors('transparent'),alignment=ft.alignment.center,padding=ft.padding.all(12),margin=ft.margin.all(0),border=ft.border.all(0, ft.colors('transparent')),tooltip='Radio',
                                   ink=True,
                                   ink_color='red',
                                   # on_hover=lambda _:self.resetClick(),
                                   on_click=lambda _:self.touch_widget_in_phone(selected_widget=self.infinityDropWidget),
                                   content=ft.Markdown(self.md1,selectable=True,extension_set=ft.MarkdownExtensionSet.GITHUB_WEB,)),
                         ],
             "Ring": [    ft.Container(bgcolor=ft.colors('transparent'),alignment=ft.alignment.center,padding=ft.padding.all(12),margin=ft.margin.all(0),border=ft.border.all(0, ft.colors('transparent')),tooltip='Radio',
                                   ink=True,
                                   ink_color='red',
                                   # on_hover=lambda _:self.resetClick(),
                                   on_click=lambda _:self.touch_widget_in_phone(selected_widget=self.infinityDropWidget),
                                   content=ft.ProgressRing()),
                         ],
     "CupAcIndicator": [    ft.Container(bgcolor=ft.colors('transparent'),alignment=ft.alignment.center,padding=ft.padding.all(12),margin=ft.margin.all(0),border=ft.border.all(0, ft.colors('transparent')),tooltip='Radio',
                                   ink=True,
                                   ink_color='red',
                                   # on_hover=lambda _:self.resetClick(),
                                   on_click=lambda _:self.touch_widget_in_phone(selected_widget=self.infinityDropWidget),
                                   content= ft.CupertinoActivityIndicator(radius=50,color=ft.colors('red'),animating=True,)),
                         ],
          "ProgressBar": [    ft.Container(bgcolor=ft.colors('transparent'),alignment=ft.alignment.center,padding=ft.padding.all(12),margin=ft.margin.all(0),border=ft.border.all(0, ft.colors('transparent')),tooltip='Radio',
                                   ink=True,
                                   ink_color='red',
                                   # on_hover=lambda _:self.resetClick(),
                                   on_click=lambda _:self.touch_widget_in_phone(selected_widget=self.infinityDropWidget),
                                   content=ft.ProgressBar(width=400)),
                         ],
             "WebView": [    ft.Container(bgcolor=ft.colors('transparent'),alignment=ft.alignment.center,padding=ft.padding.all(12),margin=ft.margin.all(0),border=ft.border.all(0, ft.colors('transparent')),tooltip='Radio',
                                   ink=True,
                                   ink_color='red',
                                   # on_hover=lambda _:self.resetClick(),
                                   on_click=lambda _:self.touch_widget_in_phone(selected_widget=self.infinityDropWidget),
                                   content=ft.WebView(
                                        url="http://127.0.0.1:8081",
                                                expand=True,
                                                on_page_started=lambda _: print("Page started"),
                                                on_page_ended=lambda _: print("Page ended"),
                                                on_web_resource_error=lambda e: print("Page error:", e.data),

                                        )),

                         ],
           "Placeholder": [    ft.Container(bgcolor=ft.colors('transparent'),alignment=ft.alignment.center,padding=ft.padding.all(12),margin=ft.margin.all(0),border=ft.border.all(0, ft.colors('transparent')),tooltip='Radio',
                                   ink=True,
                                   ink_color='red',
                                   # on_hover=lambda _:self.resetClick(),
                                   on_click=lambda _:self.touch_widget_in_phone(selected_widget=self.infinityDropWidget),
                                   content= ft.Placeholder(expand=True,color=ft.colors.random()  # random material color
                                   ),),
                         ],

          "ExpPanelList": [    ft.Container(bgcolor=ft.colors('transparent'),alignment=ft.alignment.center,padding=ft.padding.all(12),margin=ft.margin.all(0),border=ft.border.all(0, ft.colors('transparent')),tooltip='Radio',
                                   ink=True,
                                   ink_color='red',
                                   # on_hover=lambda _:self.resetClick(),
                                   on_click=lambda _:self.touch_widget_in_phone(selected_widget=self.infinityDropWidget),
                                   content=ft.ExpansionPanelList(
                                                     expand_icon_color=ft.colors('amber'),
                                                     elevation=8,
                                                     divider_color=ft.colors('amber'),
                                                     controls=[
                                                         ft.ExpansionPanel(
                                                             # has no header and content - placeholders will be used
                                                             bgcolor=ft.colors('blue400'),
                                                             expanded=True,
                                                         )
                                                     ]
                                                 )

                                   ),
                              ],
             "ExpPanelTile": [    ft.Container(bgcolor=ft.colors('transparent'),alignment=ft.alignment.center,padding=ft.padding.all(12),margin=ft.margin.all(0),border=ft.border.all(0, ft.colors('transparent')),tooltip='Radio',
                                   ink=True,
                                   ink_color='red',
                                   # on_hover=lambda _:self.resetClick(),
                                   on_click=lambda _:self.touch_widget_in_phone(selected_widget=self.infinityDropWidget),
                                   content=ft.ExpansionTile(
                                          title=ft.Text("ExpansionTile 1"),
                                          subtitle=ft.Text("Trailing expansion arrow icon"),
                                          affinity=ft.TileAffinity.PLATFORM,
                                          maintain_state=True,
                                          # collapsed_text_color=ft.colors('red'),
                                          text_color=ft.colors('red'),
                                          controls=[ft.ListTile(title=ft.Text("This is sub-tile number 1"))],
                                      ),),
                              ],

          "Table": [    ft.Container(bgcolor=ft.colors('transparent'),alignment=ft.alignment.center,padding=ft.padding.all(12),margin=ft.margin.all(0),border=ft.border.all(0, ft.colors('transparent')),tooltip='DataTable',
                                   ink=True,
                                   ink_color='red',
                                   # on_hover=lambda _:self.resetClick(),
                                   on_click=lambda _:self.touch_widget_in_phone(selected_widget=self.infinityDropWidget),
                                   content=ft.DataTable( columns=[
                                                             ft.DataColumn(ft.Text("First name")),
                                                             ft.DataColumn(ft.Text("Last name")),
                                                             ft.DataColumn(ft.Text("Age"), numeric=True),
                                                         ],
                                                         rows=[
                                                             ft.DataRow(
                                                                 cells=[
                                                                     ft.DataCell(ft.Text("John")),
                                                                     ft.DataCell(ft.Text("Smith")),
                                                                     ft.DataCell(ft.Text("43")),
                                                                 ],
                                                             ),
                                                             ft.DataRow(
                                                                 cells=[
                                                                     ft.DataCell(ft.Text("Alice")),
                                                                     ft.DataCell(ft.Text("Wong")),
                                                                     ft.DataCell(ft.Text("25")),
                                                                 ],
                                                             ),
                                                         ],
                                                     ),),
                              ],
               }

     def build(self):
          global numWidget

          """
          check CircleAvatar, VerticalDivider
          """

          #: ALERTS STATUS

          #: WIDGETS STATUS

          #: ESPECIAL WIDGET

          #: CHARTS LAYOUTS

          # selectWidgetBox                    = GLOBAL_VAR(get_global_var='SELECT_DRAGG')
          session_id = self.page._session_id
          selectWidgetBox = self.page.session.get(session_id)

          self.infinityDropWidget = self.widgets.get(selectWidgetBox)
          # self.infinityDropWidget[0].id      = f"{self.dataPassed}: {numWidget}"              # OUR ID
          # self.infinityDropWidget[0].tooltip = f"{self.dataPassed}: {numWidget}"              # TOOLTIP ID


          #: SET WIDGET DROPPED TO DICT DATABASE TO EXPORT PROYECT
          #: GLOBAL_VAR(set_global_var={'EXPORT_DATA_PHONE':{self.infinityDropWidget[0].id:self.infinityDropWidget[0]}})

          # print('============')
          # print(f"""
          #       [+]             selected_widget: {self.dataPassed},
          #       [+]             ID_widget: {numWidget},
          #       [+]             UID: {self.infinityDropWidget[0].uid}
          #       [+]             ID tooltip: {self.infinityDropWidget[0].tooltip}
          #       [+]  Content: {self.infinityDropWidget}""")
          # print('============')


          print(f"{self.dataPassed} ID: <<< drag_dropped: [infinity_box_layer_one.py]  number: {numWidget} ")

          # MAIN WIDGET THAT WILL BE DROPPED EACH TIME THAT DRAG ACCEPT
          self.content   = self.infinityDropWidget[0]

          self.on_will_accept = self.drag_will_accept           # Traslate Drop
          self.on_leave = self.drag_leave                 # Leafing Drop Line Border
          self.on_accept = lambda widget_passed: self.drag_accept(DragTargetEvent = widget_passed)

          # INDEX OF WIDGET ADDED
          numWidget += 1

          self.page.session.set("dict_widget",self.widgets)

     def show_text_dragg_selected(self, name_selected: str="") -> None:
          # session_id = self.page._session_id
          # self.name_selected = self.page.session.get(session_id)
          self.name_selected   = name_selected
          self.widget_selected = self.page.session.get("SHOW_TEXT_SELECTED_DRAGG_WIDGET")
          self.draggs_selected = self.page.session.get("SHOW_TEXT_SELECTED_PHONE_WIDGET")

          self.widget_selected.content.controls[1].content.spans[0].text = "None"
          self.draggs_selected.content.controls[1].content.spans[0].text = self.name_selected

          self.widget_selected.bgcolor = ft.colors('black12')
          self.draggs_selected.bgcolor = "cyan,0.1"

          self.widget_selected.update()
          self.draggs_selected.update()

     def switch_border_selected(self,selected: object=None):
          selected_widget = self.page.session.get("SELECTED_CONTAINER")

          if not selected_widget == None:
               selected_widget.border = ft.border.all(2, ft.colors('transparent'))
               selected_widget.update()

          selected.border = ft.border.all(2, ft.colors('yellow900'))
          selected.update()

          self.show_text_dragg_selected(name_selected=selected.content._get_control_name())

     def set_selected_widget(self,selected):
          self.page.session.set("SELECTED_CONTAINER",selected)

     def set_selected_widget_id(self,selected):
          self.page.session.set("SELECTED_CONTAINER_ID",selected.uid)

     def touch_widget_in_phone(self,selected_widget: object=None):
     # def touch_widget_in_phone(self,listWidget,e: ft.ContainerTapEvent):
          """
          NOTE:

          WE CAPTURE THE CLICK SELECTION_WIDGET SHOWING BORDER COLOR YELLOW

          IF PRESS IN OTHER WIDGET WE COMPARE tmp_list listWidgetUpdate
          IF IS DIFERENT SHOW BLACK COLOR THE PREVIEW SELECT_WIDGET

          NOTE:

          WE PASS TO Build_Editor => self.infinityDropWidget[0] THAT IS CLICKED SELECTION
          Build_Editor.update_widget_attributes(widget_cliked=ft.Container(content=ft.Text()))

          """

          # SWITCH BORDER COLOR IN SELECTED CONTAINER PHONE
          self.selected = selected_widget[0]
          self.page.session.set("cover_widget",self.selected.parent.parent)

          self.switch_border_selected(selected=selected_widget[0])
          self.set_selected_widget(selected=self.selected)
          self.set_selected_widget_id(selected=self.selected)

          print(f"[-] {self.selected.tooltip} ID: <<< touch_widget_in_phone: [infinity_box_layer_one.py]")

     def return_new_widget(self,selected_widget: str=str()) -> object:
          """
          return selected widget

          :param      selected_widget:  The selected widget
          :type       selected_widget:  str
          """
          widget_selected = self.widgets.get(selected_widget)
          self.page.update()

          return widget_selected

     def drag_accept(self,DragTargetEvent: object=None) -> object:
          """
          NOTE:

          THIS PART IS VERY IMPORTANT BECAUSE IS THE LOOP OF THE DROP WIDGET THAT WE NEED APPEND OR PASS
          IN DEPENDENCY IF IS A CONTROLS USE APPEND AND IF IS A CONTENT WE PASS

          DragTargetEvent.control.parent          << before belong [row , column , gridview]
          DragTargetEvent.control                 << dragg_target
          DragTargetEvent.control.content         << dragg_target content= Container
          DragTargetEvent.control.content.content << content of Container = SelectedWidget

          DragTargetEvent.control.content.content._get_control_name()

          self.testing_wdiget = ft.DragTarget(
                                   group="GroupDragg",
                                   on_will_accept    = lambda dragg_item :self.dragg_on_will_accept(DragTargetEvent=dragg_item), # Traslate Drop
                                   on_leave          = lambda dragg_item :self.dragg_on_leave(DragTargetEvent=dragg_item), # Leafing Drop Line Border
                                   on_accept         = lambda dragg_item :self.dragg_on_accept(DragTargetEvent=dragg_item), # Leafing Drop Line Border
                                   content=ft.Container(width=120,height=120,bgcolor="red")
                                   )

          def drag_will_accept(self,DragTargetEvent: object=None):
               DragTargetEvent.control.content.border = None
               DragTargetEvent.control.content.border = ft.border.all(4, ft.colors('cyan900'))

               DragTargetEvent.control.update()
               self.page.update()

          def dragg_on_leave(self,dragg_item: object=None):
               DragTargetEvent.control.content.border = True
               DragTargetEvent.control.content.border = ft.border.all(0, ft.colors('transparent'))

               DragTargetEvent.control.update()
               self.page.update()

          def dragg_on_accept(self,dragg_item: object=None):
               self.widgetFilter =  self.page.session.get("ONLY_CONTROLS_ADDING_IN_APP")

               session_id = self.page._session_id
               selectWidgetBox = self.page.session.get(session_id)

               self.InstanceNewWidget = InfinityBoxLayerOne(dataPassed=selectWidgetBox,page=self.page)
               self.right_control     = DragTargetEvent.control.content.content._get_control_name()

               if self.right_control in self.widgetFilter:
                    # DragTargetEvent.control.content.content.controls.append(self.testing_wdiget)
                    DragTargetEvent.control.content.content.controls.append(self.InstanceNewWidget)

               else:
                    if self.right_control in self.widgetFilter:
                         DragTargetEvent.control.content.content.controls.append(self.InstanceNewWidget)

                    else:
                         # SWITCH IF IS CONTENT
                         self.over_write_selected = self.return_new_widget(selected_widget=selectWidgetBox)
                         DragTargetEvent.control.content.content = self.over_write_selected[0].content


               # #: UPDATE COLOR WIDGET
               DragTargetEvent.control.content.border = True
               DragTargetEvent.control.content.border = ft.border.all(0, ft.colors('transparent'))
               DragTargetEvent.control.update()

               self.page.update()


          """

          # ROW COLUMN GRIDVIEW
          self.widgetFilter =  self.page.session.get("ONLY_CONTROLS_ADDING_IN_APP")

          session_id = self.page._session_id
          selectWidgetBox = self.page.session.get(session_id)

          self.InstanceNewWidget = InfinityBoxLayerOne(dataPassed=selectWidgetBox, page=self.page)
          self.right_control     = DragTargetEvent.control.content.content._get_control_name()

          if self.right_control in self.widgetFilter:
               # DragTargetEvent.control.content.content.controls.append(self.testing_wdiget)
               DragTargetEvent.control.content.content.controls.append(self.InstanceNewWidget)

          else:
               if self.right_control in self.widgetFilter:
                    DragTargetEvent.control.content.content.controls.append(self.InstanceNewWidget)

               else:
                    # SWITCH IF IS CONTENT
                    self.over_write_selected = self.return_new_widget(selected_widget=selectWidgetBox)
                    DragTargetEvent.control.content.content = self.over_write_selected[0].content


          # #: UPDATE COLOR WIDGET
          DragTargetEvent.control.content.border = True
          DragTargetEvent.control.content.border = ft.border.all(0, ft.colors('transparent'))
          DragTargetEvent.control.update()

          self.page.update()

          # RUN ONLY IN PRODUCTION
          # print(selectWidgetBox,"==",self.right_control)

     def drag_will_accept(self,DragTargetEvent: object=None):
          """
          : UPDATE COLOR WIDGET
          NOTE:

          THIS PART IS VERY IMPORTANT BECAUSE IS THE LOOP OF THE DROP WIDGET THAT WE NEED APPEND OR PASS
          IN DEPENDENCY IF IS A CONTROLS USE APPEND AND IF IS A CONTENT WE PASS

          DragTargetEvent.control.parent          << before belong [row , column , gridview]
          DragTargetEvent.control                 << dragg_target
          DragTargetEvent.control.content         << dragg_target content= Container
          DragTargetEvent.control.content.content << content of Container = SelectedWidget

          DragTargetEvent.control.content.content._get_control_name()

          self.testing_wdiget = ft.DragTarget(
                                   group="GroupDragg",
                                   on_will_accept    = lambda dragg_item :print(f"Traslate:  {dragg_item}"), # Traslate Drop
                                   on_leave          = lambda dragg_item :print(f"Leaving:   {dragg_item}"), # Leafing Drop Line Border
                                   on_accept         = lambda dragg_item :print(f"on_accept: {dragg_item}"), # Leafing Drop Line Border
                                   content=ft.Container(width=120,height=120,bgcolor="red")
                                   )
          """
          DragTargetEvent.control.content.border = None
          DragTargetEvent.control.content.border = ft.border.all(4, ft.colors('cyan900'))

          DragTargetEvent.control.update()
          self.page.update()

     def drag_leave(self,DragTargetEvent):
          """
          : UPDATE COLOR WIDGET
          NOTE:

          THIS PART IS VERY IMPORTANT BECAUSE IS THE LOOP OF THE DROP WIDGET THAT WE NEED APPEND OR PASS
          IN DEPENDENCY IF IS A CONTROLS USE APPEND AND IF IS A CONTENT WE PASS

          DragTargetEvent.control.parent          << before belong [row , column , gridview]
          DragTargetEvent.control                 << dragg_target
          DragTargetEvent.control.content         << dragg_target content= Container
          DragTargetEvent.control.content.content << content of Container = SelectedWidget

          DragTargetEvent.control.content.content._get_control_name()

          self.testing_wdiget = ft.DragTarget(
                                   group="GroupDragg",
                                   on_will_accept    = lambda dragg_item :print(f"Traslate:  {dragg_item}"), # Traslate Drop
                                   on_leave          = lambda dragg_item :print(f"Leaving:   {dragg_item}"), # Leafing Drop Line Border
                                   on_accept         = lambda dragg_item :print(f"on_accept: {dragg_item}"), # Leafing Drop Line Border
                                   content=ft.Container(width=120,height=120,bgcolor="red")
                                   )
          """

          DragTargetEvent.control.content.border = True
          DragTargetEvent.control.content.border = ft.border.all(0, ft.colors('transparent'))

          DragTargetEvent.control.update()
          self.page.update()
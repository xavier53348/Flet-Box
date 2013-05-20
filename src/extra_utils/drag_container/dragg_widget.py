####################################################
import flet as ft
###################### CALL GLOBAL VAR #############
from ..settings_var.settings_widget import GLOBAL_VAR
####################################################

class DraggWidget(ft.UserControl): # <======= dragg widget
     """
     NOTE:

     1. ONLY FUNCTION IS TAKE DRAGGABLE WIDGET AND TRASLATE TO DRAGGABLE_PHONE
     2. SET IN VARIABLE GLOBAL THE SELECTED DRAGGABLE WIDGET
     3. CLEAN THE LIST listWidgetUpdate
     """
     def __init__(self,widget='Erase this test',color='BLACK',icons='/icons/icon-512.png'):
          super().__init__()
          # self.title='data'
          self.widget    = widget
          self.takeClick = False
          self.myColor   = color
          self.icons     = icons

     def build(self):

          self.DropTakeDragg=ft.Draggable(
                                   ################# FRON CONTAINER
                                   group   = "GroupDragg",
                                   content = ft.Container(
                                                       width         = 90,
                                                       height        = 90,
                                                       # bgcolor       = '#0c0d0e',
                                                       border_radius = 16,
                                                       padding       = ft.padding.all(4),
                                                       alignment     = ft.alignment.center,
                                                       border        = ft.border.all(1.5, '#0a1619'),                     # ft.border.only(Left=8, top=8, right=8, bottom=8),
                                                       on_click = lambda _: self.SelectedWidget(self.widget), # on_hover=lambda _: print('on_hover'),   # on_long_press=lambda _: print('on_long_press'),
                                                  gradient=ft.LinearGradient( begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=[ft.colors.BLACK12, '#0c0d0e'],),
                                                  content = ft.Column(
                                                                      alignment            = ft.MainAxisAlignment.SPACE_AROUND,              # horizontal <=> START,CENTER,END SPACE_BETWEEN SPACE_AROUND SPACE_EVENLY
                                                                      horizontal_alignment = ft.CrossAxisAlignment.CENTER,        # vertical       START,CENTER END
                                                            controls = [
                                                                           ft.Icon(
                                                                                     name  = self.icons,
                                                                                     color = ft.colors.CYAN_700,
                                                                                     size  = 50,
                                                                                     ),
                                                                           ft.Text(
                                                                                value      = self.widget,
                                                                                text_align = ft.TextAlign.CENTER,
                                                                                weight     = ft.FontWeight.BOLD,
                                                                                color      = ft.colors.CYAN_700,
                                                                                ),
                                                                           ]
                                                            )
                                   ),
                                   ################# BACK CONTAINER
                                   content_when_dragging=ft.Container(
                                                       padding=2,
                                                       width=80,
                                                       height=80,
                                                       # bgcolor='#131926',   # ft.colors.BLACK,
                                                       border_radius=13,
                                                    # content=ft.Text("Back"),
                                   ),
                                   ################# TRASLATE CONTAINER
                                   content_feedback=ft.Container(
                                                       alignment=ft.alignment.bottom_center,
                                                       width=80,
                                                       height=80,
                                                       bgcolor='#0c0d0e',
                                                       border=ft.border.all(0.5, ft.colors.TEAL),                     # ft.border.only(Left=8, top=8, right=8, bottom=8),

                                                       border_radius=13,
                                                  # image_src=f"{self.icons}",
                                                  # content=ft.Text("Drop",size=12),
                                                    content = ft.Column(
                                                                 spacing=0,
                                                                 controls = [
                                                                      ft.Container(
                                                                           alignment=ft.alignment.center,
                                                                           padding       = ft.padding.all(4),
                                                                           content = ft.Icon(name=self.icons, color=ft.colors.BLUE_300, size=50)),
                                                                      ft.Container(
                                                                           alignment=ft.alignment.center,
                                                                           padding       = ft.padding.all(0),
                                                                           margin       = ft.margin.all(0),
                                                                           content = ft.Text(
                                                                                               # value= self.widget,
                                                                                               color=ft.colors.BLUE_300,
                                                                                               size=16,
                                                                                               weight     = ft.FontWeight.BOLD,
                                                                                               # color      = ft.colors.CYAN_700,
                                                                                               spans=[ft.TextSpan( self.widget, ft.TextStyle( size=16, color=ft.colors.BLUE_300),),],
                                                                                               )),
                                                                      ],),
                                   ),
          )# <======= coma
          return self.DropTakeDragg
     def SelectedWidget(self,data):
          """
          NOTE:

          1. SET IN GLOBAL VAR THE SELECTED WIDGET
          2. RESET THE LIST listWidgetUpdate

          """
          ####################################################################################
          CHECK_DATA = GLOBAL_VAR(get_global_var='BOOL_SHOW_SELECTED')

          if CHECK_DATA:
               #################################################################################### HIDE TAB 2
               # HIDE TABS IF CLICK PRESS IS NO IN PHONE CONTAINER WIDGET
               #
               CONFIG_TABS_CONTAINERS                 = GLOBAL_VAR(get_global_var='CONFIG_TABS_CONTAINERS')
               CONFIG_TABS_CONTAINERS.visible         = False
               CONFIG_TABS_CONTAINERS.update()
               #################################################################################### HIDE TAB 3
               # HIDE TABS IF CLICK PRESS IS NO IN PHONE CONTAINER WIDGET
               #
               CONFIG_TABS_CONTAINERS_CONTENT         = GLOBAL_VAR(get_global_var='CONFIG_TABS_CONTAINERS_CONTENT')
               CONFIG_TABS_CONTAINERS_CONTENT.visible = False
               CONFIG_TABS_CONTAINERS_CONTENT.update()

          ################################## SET GLOBAL VAR // LIST_SELECTED_WIDGETS // TO RESET AFTER PRESS SELECTED IN PHONE CONTAINER
          selected_widget_clicked = GLOBAL_VAR( get_global_var='LIST_SELECTED_WIDGETS')

          ################################## SET GLOBAL VAR // SELECTED_WIDGET // IN DRAGG_DROPP BOX
          widget_selected         = GLOBAL_VAR( set_global_var={
                                                       'SELECT_DRAGG' :data,
                                                       'LIST_SELECTED_WIDGETS':[]  ,
                                                        })
          GLOBAL_VAR(set_global_var={'BOOL_SHOW_SELECTED':False})

          ####################################################################################
          # if selected_widget_clicked is true each time that we press dragg box widget set border none
          # each witdget inside drop_dragg.py or Phone container will be a dragg_widget.py
          TEXT_PHONE_WIDGET = GLOBAL_VAR(get_global_var='SHOW_TEXT_SELECTED_PHONE_WIDGET')
          TEXT_PHONE_WIDGET.controls[0].content.controls[1].spans[0].text = 'None'
          TEXT_PHONE_WIDGET.controls[0].bgcolor = ft.colors.BLACK12
          TEXT_PHONE_WIDGET.controls[0].update()
          TEXT_DRAGG_WIDGET = GLOBAL_VAR(get_global_var='SHOW_TEXT_SELECTED_DRAGG_WIDGET')
          TEXT_DRAGG_WIDGET.controls[0].content.controls[1].spans[0].text = data
          TEXT_DRAGG_WIDGET.controls[0].bgcolor = ft.colors.BLUE_GREY_900
          TEXT_DRAGG_WIDGET.controls[0].update()

         ####################################################################################

          if selected_widget_clicked:
               selected_widget_clicked.border = None
               selected_widget_clicked.update()

          # print(selected_widget_clicked,'<======== from GLOBAL_VAR')
          print(data,'<=== selected DRAGG widget')

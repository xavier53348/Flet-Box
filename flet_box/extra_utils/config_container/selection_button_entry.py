import flet as ft
from ..settings_var.settings_widget import GLOBAL_VAR

click_avalidation: bool = False

class SelectionButtonEntry(ft.Stack):
    """
    box_layout = ft.Container(content = ft.Text())

    Double_Widget = SelectionButtonEntry
    Double_Widget(config_widget='value',widget = box_layout),

    """

    def __init__(self,config_widget='exemple [value,bgcolor,width,height] ....',widget='',id_name_widget_dict=None):
        super().__init__()
        self.widget           = widget
        self.widget_name = config_widget
        self.id_name_widget_dict = id_name_widget_dict

        #: will change name of entry points
        #: ONLY FOR CONTAINER
        if self.widget_name == "image_src" or self.widget_name == "src":
            self.tmp_widget_name = " Open Image "

    def build(self):
        Drop_SelectionButtonEntry =  ft.Container(

                    ink           = False,
                    bgcolor       = '#0c0d0e',
                    padding       = ft.padding.only(left=4, top=4, right=4, bottom=4),
                    margin        = ft.margin.all(0),
                    alignment     = ft.alignment.center,
                    border_radius = ft.border_radius.all(16),
                    border        = ft.border.all(2, ft.colors.BLACK),
                    width         = 165,
                    height        = 80,
                content = ft.Column(
                                wrap=True,
                            controls=[
                                        ft.Container(
                                            ink           = False,
                                            bgcolor       = "#0e0f11",
                                            padding       = ft.padding.only(left=12, top=0, right=12, bottom=0),
                                            alignment     = ft.alignment.center,
                                            border_radius = ft.border_radius.all(30),
                                            height        = 20,
                                        content = ft.Text(
                                                        value       = self.widget_name.capitalize().replace("_"," "),
                                                        font_family = "Consolas", #"Consolas ,RobotoSlab
                                            ),),
                                    ft.Container(

                                            ink           = False,
                                            padding       = ft.padding.all(2),
                                            alignment     = ft.alignment.center,
                                            border_radius = ft.border_radius.all(30),
                                            border        = ft.border.all(0.1, '#0e0f11'),
                                            width         = 152,
                                            height        = 36,
                                        gradient=ft.LinearGradient( begin   = ft.alignment.top_center,
                                                                    end     = ft.alignment.bottom_center,
                                                                    colors  = [ft.colors.CYAN_600, ft.colors.BLACK38],),
                                            content = ft.Row(
                                                        controls=[
                                                            ft.Container(
                                                                    ink           = False,
                                                                    # bgcolor       =ft.colors.TEAL_900,
                                                                    padding       = ft.padding.all(0),
                                                                    margin       = ft.margin.all(0),
                                                                    alignment     = ft.alignment.center,
                                                                    border_radius = ft.border_radius.all(30),
                                                                    width         = 147,
                                                                    height        = 35,
                                                                    gradient=ft.LinearGradient( begin = ft.alignment.top_center,
                                                                                                end   = ft.alignment.center_right,
                                                                                                colors= [
                                                                                                        ft.colors.BLACK12,
                                                                                                        ft.colors.CYAN_900,
                                                                                                        ft.colors.BLACK38,
                                                                                                        ],),

                                                                content = ft.ElevatedButton(
                                                                                    text           = self.tmp_widget_name,
                                                                                    width           = 147,
                                                                                    bgcolor=ft.colors.TRANSPARENT,
                                                                            on_click   = lambda _:self.modify_widget_attributes(
                                                                                                                                widget_name        = self.widget_name,
                                                                                                                                attribute_to_change= self.widget,
                                                                                                                                ),
                                                                        ),
                                                                ),
                                                                 ],),
                                )
                                 ],
                    ),
        )

        return Drop_SelectionButtonEntry

    def modify_widget_attributes(self,widget_name, attribute_to_change):
        self.imagen_editor  = GLOBAL_VAR(get_global_var='IMAGEN_EDITOR_CONTAINER')
        self.imagen_editor.visible = True
        self.imagen_editor.update()

        #: SET WIDGET SELETED TO EDIT IN REAL TIME
        GLOBAL_VAR(set_global_var={
                   'WIDGET_SELECTION_EDITOR_CONTAINER':{
                                                         "widget_name":widget_name,
                                                  "attribute_to_change":attribute_to_change,
                                                        }
                   })
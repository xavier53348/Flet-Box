
import flet as ft

class SelectionEntry(ft.Stack):
    """
    box_layout = ft.Container(content = ft.Text())

    Double_Widget = SelectionEntry
    Double_Widget(config_widget='value',widget = box_layout),

    """

    def __init__(self,config_widget='exemple [value,bgcolor,width,height] ....',widget='',id_name_widget_dict=None):
        super().__init__()
        self.widget           = widget
        self.attribute_widget = config_widget
        self.id_name_widget_dict = id_name_widget_dict

        #: will change name of entry points
        #: ONLY FOR CONTAINER
        if self.attribute_widget == "alignment ":
            self.alignment_tmp_name = " Center "
            self.alignment_tmp = [
                                    ft.dropdown.Option(" Top Left "),
                                    ft.dropdown.Option(" Top Center "),
                                    ft.dropdown.Option(" Top Right "),
                                    ft.dropdown.Option(" Center Left "),
                                    ft.dropdown.Option(" Center "),
                                    ft.dropdown.Option(" Center Right "),
                                    ft.dropdown.Option(" Bottom Left "),
                                    ft.dropdown.Option(" Bottom Center "),
                                    ft.dropdown.Option(" Bottom Right "),

                                    ]
        #: ONLY FOR CONTENT <<<=========== *********
        #: alignment

        if self.attribute_widget == "alignment":
            self.alignment_tmp_name = " Start"
            self.alignment_tmp = [
                                    ft.dropdown.Option(" Start"),
                                    ft.dropdown.Option(" Center"),
                                    ft.dropdown.Option(" End"),
                                    ft.dropdown.Option(" Space Between"),
                                    ft.dropdown.Option(" Space Around"),
                                    ft.dropdown.Option(" Space Evenly"),

                                ]
        #: ONLY FOR CONTENT <<<=========== *********
        #: image_fit
        if self.attribute_widget == "image_fit":
            self.alignment_tmp_name =" Contain"
            self.alignment_tmp = [
                                    ft.dropdown.Option(" Contain"),
                                    ft.dropdown.Option(" Cover"),
                                    ft.dropdown.Option(" Fill"),
                                    ft.dropdown.Option(" Fit Height"),
                                    ft.dropdown.Option(" Fit Width"),
                                    ft.dropdown.Option(" Scale Down"),

                                    ]
        #: vertical_alignment
        if self.attribute_widget == "vertical_alignment":

            self.alignment_tmp_name = " Vertical Start"
            self.alignment_tmp = [
                                    ft.dropdown.Option(" Vertical Start"),
                                    ft.dropdown.Option(" Vertical Center"),
                                    ft.dropdown.Option(" Vertical End"),

                                    ]
        #: horizontal_alignment
        if self.attribute_widget == "horizontal_alignment":

            self.alignment_tmp_name = " Horizontal Start"
            self.alignment_tmp = [
                                    ft.dropdown.Option(" Horizontal Start"),
                                    ft.dropdown.Option(" Horizontal Center"),
                                    ft.dropdown.Option(" Horizontal End"),

                                    ]

        #: keyboard_type
        if self.attribute_widget == "keyboard_type":
            self.alignment_tmp_name = " Multiline"
            self.alignment_tmp = [
                                    ft.dropdown.Option(" Multiline"),
                                    ft.dropdown.Option(" Number"),
                                    ft.dropdown.Option(" Phone"),
                                    ft.dropdown.Option(" Datetime"),
                                    ft.dropdown.Option(" Email"),
                                    ft.dropdown.Option(" Url"),
                                    ft.dropdown.Option(" Show Password"),
                                    ft.dropdown.Option(" Name"),
                                    ft.dropdown.Option(" Street Address"),
                                    ft.dropdown.Option(" None"),

                                    ]
        #: label_position
        if self.attribute_widget == "text_align":
            self.alignment_tmp_name = " Text Left"
            self.alignment_tmp = [
                                    ft.dropdown.Option(" Text Left"),
                                    ft.dropdown.Option(" Text Right"),
                                    ft.dropdown.Option(" Text Center"),
                                    ft.dropdown.Option(" Text Justify"),
                                    ft.dropdown.Option(" Text Start"),
                                    ft.dropdown.Option(" Text End"),

                                    ]

        #: weight
        if self.attribute_widget == "weight":
            self.alignment_tmp_name = " Weight NORMAL"
            self.alignment_tmp = [
                                    ft.dropdown.Option(" Weight NORMAL"),
                                    ft.dropdown.Option(" Weight BOLD"),
                                    ft.dropdown.Option(" Weight W_100"),
                                    ft.dropdown.Option(" Weight W_200"),
                                    ft.dropdown.Option(" Weight W_300"),
                                    ft.dropdown.Option(" Weight W_400"),
                                    ft.dropdown.Option(" Weight W_500"),
                                    ft.dropdown.Option(" Weight W_600"),
                                    ft.dropdown.Option(" Weight W_700"),
                                    ft.dropdown.Option(" Weight W_800"),
                                    ft.dropdown.Option(" Weight W_900"),

                                    ]
        #: only in production
        #: print(self.attribute_widget)

    def build(self):
        Drop_SelectionEntry =  ft.Container(

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
                                                        value       = self.attribute_widget.capitalize().replace("_"," "),
                                                        font_family = "Consolas", #"Consolas ,RobotoSlab
                                            ),),
                                    ft.Container(

                                            ink           = False,
                                            bgcolor       = '#0e0f11',
                                            padding       = ft.padding.all(2),
                                            alignment     = ft.alignment.center,
                                            border_radius = ft.border_radius.all(30),
                                            border        = ft.border.all(0.1, '#0e0f11'),
                                            width         = 152,
                                            height        = 36,
                                        gradient=ft.LinearGradient( begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=[ft.colors.CYAN_800, ft.colors.BLACK38],),
                                            content = ft.Row(
                                                        controls=[
                                                            ft.Container(
                                                                    ink           = False,
                                                                    bgcolor       = "#0e0f11",
                                                                    padding       = ft.padding.all(0),
                                                                    alignment     = ft.alignment.center,
                                                                    border_radius = ft.border_radius.all(30),
                                                                    width         = 147,
                                                                    height        = 35,
                                                                content = ft.Dropdown(
                                                                                    hint_text       = self.alignment_tmp_name,
                                                                                    width           = 140,
                                                                                    content_padding = ft.padding.only(left=0, top=0, right=8, bottom=14),
                                                                                    alignment       = ft.alignment.center_left,
                                                                                    border_radius   = ft.border_radius.all(15),
                                                                                    border          = ft.InputBorder.NONE,
                                                                                    options         = self.alignment_tmp,
                                                                            on_change   = lambda _:self.modify_widget_attributes(config_widget=_.__dict__.get('data')),
                                                                        ),
                                                                ),
                                                                 ],),
                                )
                                 ],
                    ),
        )

        return Drop_SelectionEntry

    def modify_widget_attributes(self,config_widget):
        """
    NOTE:

        Will modify all attrib inside the widget that we selected

        on_change= lambda x:self.modify_widget_attributes(config_widget =self.attribute_widget ,value = Drop_SelectionEntry),

    EXEMPLE:

        width:      value
        height:     value
        bgcolor:    value
        value:      value
        """
        #: print(config_widget)
        #: print(value)

        #: self.widget.content.value = value if config_widget  == "value" else None
        #: will modify attributes of the widget class in real time

        #: ONLY FOR CONTAINER
        #: IMAGE_FIT CONTAINER
        #: CONTAIN, COVER, FILL, FIT_HEIGHT, FIT_WIDTH, SCALE_DOWN

        if config_widget == " Top Left ":
            self.widget.alignment      = ft.alignment.top_left
        if config_widget == " Top Center ":
            self.widget.alignment      = ft.alignment.top_center
        if config_widget == " Top Right ":
            self.widget.alignment      = ft.alignment.top_right
        if config_widget == " Center Left ":
            self.widget.alignment      = ft.alignment.center_left
        if config_widget == " Center ":
            self.widget.alignment      = ft.alignment.center
        if config_widget == " Center Right ":
            self.widget.alignment      = ft.alignment.center_right
        if config_widget == " Bottom Left ":
            self.widget.alignment      = ft.alignment.bottom_left
        if config_widget == " Bottom Center ":
            self.widget.alignment      = ft.alignment.bottom_center
        if config_widget == " Bottom Right ":
            self.widget.alignment      = ft.alignment.bottom_right

        #: ONLY FOR CONTENT
        #: IMAGE FIT
        #: CONTAIN, COVER, FILL, FIT_HEIGHT, FIT_WIDTH, SCALE_DOWN

        if config_widget == " Contain":
            self.widget.image_fit              = ft.ImageFit.CONTAIN
        if config_widget == " Cover"  :
            self.widget.image_fit              = ft.ImageFit.COVER
        if config_widget == " Fill"   :
            self.widget.image_fit              = ft.ImageFit.FILL
        if config_widget == " Fit Height":
            self.widget.image_fit              = ft.ImageFit.FIT_HEIGHT
        if config_widget == " Fit Width":
            self.widget.image_fit              = ft.ImageFit.FIT_WIDTH
        if config_widget == " Scale Down":
            self.widget.image_fit              = ft.ImageFit.SCALE_DOWN

        #: CONTAINER.content = ft.Widget()
        #: VERTICAL ALIGMENT
        #: START,CENTER,END

        if config_widget == " Vertical Start":
            self.widget.vertical_alignment   = ft.CrossAxisAlignment.START
        if config_widget == " Vertical Center":
            self.widget.vertical_alignment   = ft.CrossAxisAlignment.CENTER
        if config_widget == " Vertical End":
            self.widget.vertical_alignment   = ft.CrossAxisAlignment.END

        #: HORIZONTAL ALIGMENT
        #: START,CENTER,END

        if config_widget == " Horizontal Start":
            self.widget.horizontal_alignment = ft.CrossAxisAlignment.START
        if config_widget == " Horizontal Center":
            self.widget.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        if config_widget == " Horizontal End":
            self.widget.horizontal_alignment = ft.CrossAxisAlignment.END

        #: ALIGMENT
        #: START,CENTER,END SPACE_BETWEEN SPACE_AROUND SPACE_EVENLY

        if config_widget == " Start":
            self.widget.alignment     = ft.MainAxisAlignment.START
        if config_widget == " Center":
            self.widget.alignment     = ft.MainAxisAlignment.CENTER
        if config_widget == " End":
            self.widget.alignment     = ft.MainAxisAlignment.END
        if config_widget == " Space Between":
            self.widget.alignment     = ft.MainAxisAlignment.SPACE_BETWEEN
        if config_widget == " Space Around":
            self.widget.alignment     = ft.MainAxisAlignment.SPACE_AROUND
        if config_widget == " Space Evenly":
            self.widget.alignment     = ft.MainAxisAlignment.SPACE_EVENLY

        #: KEYBOARD TYPE
        #: MULTILINE,NUMBER,PHONE,DATETIME,EMAIL,URL,VISIBLE_PASSWORD,NAME,STREET_ADDRESS,NONE

        if config_widget == " Multiline":
            self.widget.keyboard_type = ft.KeyboardType.MULTILINE
        if config_widget == " Number":
            self.widget.keyboard_type = ft.KeyboardType.NUMBER
        if config_widget == " Phone":
            self.widget.keyboard_type = ft.KeyboardType.PHONE
        if config_widget == " Datetime":
            self.widget.keyboard_type = ft.KeyboardType.DATETIME
        if config_widget == " Email":
            self.widget.keyboard_type = ft.KeyboardType.EMAIL
        if config_widget == " Url":
            self.widget.keyboard_type = ft.KeyboardType.URL
        if config_widget == " Show Password":
            self.widget.keyboard_type = ft.KeyboardType.VISIBLE_PASSWORD
        if config_widget == " Name":
            self.widget.keyboard_type = ft.KeyboardType.NAME
        if config_widget == " Street Address":
            self.widget.keyboard_type = ft.KeyboardType.STREET_ADDRESS
        if config_widget == " None":
            self.widget.keyboard_type = ft.KeyboardType.NONE

        #: LABEL POSITION
        #: LEFT,RIGHT,CENTER,JUSTIFY,START,END

        if config_widget == " Text Left":
            self.widget.text_align    = ft.TextAlign.LEFT
        if config_widget == " Text Right":
            self.widget.text_align    = ft.TextAlign.RIGHT
        if config_widget == " Text Center":
            self.widget.text_align    = ft.TextAlign.CENTER
        if config_widget == " Text Justify":
            self.widget.text_align    = ft.TextAlign.JUSTIFY
        if config_widget == " Text Start":
            self.widget.text_align    = ft.TextAlign.START
        if config_widget == " Text End":
            self.widget.text_align    = ft.TextAlign.END

        #: CONTAINER.content = ft.Widget()
        #: NORMAL (default), BOLD, W_100, W_200,  W_300, W_400, W_500, W_600, W_700, W_800,W_900
        #: weight          = ft.FontWeight.BOLD,

        if config_widget == " Weight NORMAL":
            self.widget.weight    = ft.FontWeight.NORMAL
        if config_widget == " Weight BOLD":
            self.widget.weight    = ft.FontWeight.BOLD
        if config_widget == " Weight W_100":
            self.widget.weight    = ft.FontWeight.W_100
        if config_widget == " Weight W_200":
            self.widget.weight    = ft.FontWeight.W_200
        if config_widget == " Weight W_300":
            self.widget.weight    = ft.FontWeight.W_300
        if config_widget == " Weight W_400":
            self.widget.weight    = ft.FontWeight.W_400
        if config_widget == " Weight W_500":
            self.widget.weight    = ft.FontWeight.W_500
        if config_widget == " Weight W_600":
            self.widget.weight    = ft.FontWeight.W_600
        if config_widget == " Weight W_700":
            self.widget.weight    = ft.FontWeight.W_700
        if config_widget == " Weight W_800":
            self.widget.weight    = ft.FontWeight.W_800
        if config_widget == " Weight W_900":
            self.widget.weight    = ft.FontWeight.W_900

        #: only in production
        #: print(self.widget.uid)

        self.widget.update()

#######

###  VAR USED IN FLET_BOX
```python
self.page.session.set("SELECTED_SCREEN",self.phone_container)  # <== SELECTED PHONE SCREEN
self.page.session.set("SELECTED_CONTAINER",selected)           # <== SELECTED PHONE DROPP CONATINER
self.page.session.set("SELECTED_CONTAINER_ID",selected.uid)

self.page.session.set("SHOW_TEXT_SELECTED_DRAGG_WIDGET",self.selected_dragg_container)  # <== LITE CONTAINER SHOW  TEXT SELECTED PHONE WIDGET TO CONFIG
self.page.session.set("SHOW_TEXT_SELECTED_PHONE_WIDGET",self.selected_phone_container) # <== LITE CONTAINER SHOW  TEXT SELECTED DRAGG WIDGET TO CONFIG

self.page.session.set('drag_dropped',self.dataPassed)                           # <== JUST NAME OF SELECTED
self.page.session.set("list_filter_controls",self.ONLY_CONTROLS_ADDING_IN_APP)  # <== 'Row',"GridView","Column","Stack",

self.page.session.set('PHOTO_SELECTION',self.content)        # <== SHOW SELECTION PHOTO

self.page.session.set('set_attribute_color',self.attribute_color) # <== SET (BGCOLOR, ...)
self.page.session.set('set_edit_widget_color',self.widget_color)  # <== SET (ft.Container, Image)

self.page.session.set('set_attribute_image',self.attribute_image) # <== SET (BGCOLOR, ...)
self.page.session.set('set_edit_widget_image',self.widget_image)  # <== SET (ft.Container, Image)

self.page.session.set('user_name', {'user_name': user_name, 'pasword': pasword})   # <== SET MAIN USER
self.page.session.set('user_name_phone', self.Build_Phone_Editor)  # <== SET MAIN PHONE

ft.colors('blue300')
ft.colors('cyan700')
ft.colors('cyan800')
ft.colors('cyan900')
ft.colors('yellow900')
ft.colors('black38')
ft.colors('black')
ft.colors('black26')
ft.colors('black12')
ft.colors('black54')
ft.colors('shadow')
ft.colors('background')
ft.colors('red')
ft.colors('purple600')
ft.colors('transparent')
ft.colors('white')


def hello(data):
    match data:
        case "hello":
            print('hello')

        case "hello":
            print('hello')

        case "hello":
            print('hello')

        case "hello":
            print('hello')
```

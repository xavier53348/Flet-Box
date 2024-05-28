<!-- markdownserver http://localhost:8009/WIDGET.md -->
### ROUTES OF ALL MODULES

##### LEFT DRAGG CONTAINER
```bash
>>> extra_utils/config_container/widget_editor       metod Build_Editor
>>> extra_utils/drag_container  /widget_drag_editor  metod Build_Drag_Editor
```
##### PHONE CONTAINER
```bash
>>> extra_utils/phone_container/widget_phone_editor  metod Build_Phone_Editor
```
##### TAB MENU CONTAINER
```bash
>>> extra_utils/menu_tab_up_phone/widget_menu_tab_editor       metod MenuUpContainer
>>> extra_utils/menu_tab_left_phone/widget_menu_left_editor    metod MenuLeftContainer
```
##### LITE MENU RIGHT PHONE AND DOWN
```bash
>>> extra_utils/lite_menu_bar_up_phone/head_bar_menu_phone     metod LiteMenuUpContainer
>>> extra_utils/lite_menu_bar_down_phone/footer_bar_menu_phone metod LiteMenuDownContainer
>>> extra_utils/lite_menu_bar_down_phone/selected_widget       metod SelectedWidget
```
##### ICON AND COLOR BROWSER CONTAINER
```bash
>>> extra_utils / icon_browser / icon_browser         metod IconBrowser
>>> extra_utils / color_browser / color_browser       metod ColorBrowser
```
##### MORE USED PATH

**It's the widget that we dropp inside phone and on method on_accept itself drop a new widget inside it**

- infitiy_box_layer_one.py

**It's a box that content all widget to dropp and is necesary to make new widgets**

- Build_Drag_Editor

**It's a box builder that contain all widgets to modify selected widget's properties**

- Build_Editor

##### [Parh more datail to make own modules ](https://github.com/xavier53348/Flet-Box/blob/features/new_features/full_path.txt)

## Widgets Flet-Box:
**All widget** in flet-box are Stack() container that have inside a container with the selected widget
we may manipulate attributes we find the selected widget by ID and make a CRUD create read use and delete.


#### know your id widget

```python3
>>> widget._Control__uid
>>> '_6'

```

#### DEFAULD attributes by ID

```python3
>>> page.get_control(id='_5').controls[0]
>>> ft.Stack()

```
#### Get attributes by ID

```python3
>>> page.get_control(id='_5').controls[0]
>>> container {'width': 150, 'bgcolor': 'cyan', 'ink': False, 'onhover': True, 'border': '{"l":{"w":2,"c":"black"},"t":{"w":2,"c":"black"},"r":{"w":2,"c":"black"},"b":{"w":2,"c":"black"}}', 'margin': '{"l":8,"t":8,"r":8,"b":8}', 'padding': '{"l":8,"t":8,"r":8,"b":8}', 'alignment': '{"x":0,"y":0}'}

```

#### ERASE Controls by ID

```python3
>>> id_widget = page.get_control(id='_5')
>>> id_widget.controls = None
>>> id_widget.update()

```
#### ADD Controls by ID

```python3
>>> id_widget = page.get_control(id='_5')
>>> id_widget.controls.append( ft.Widget(attributes) )
>>> id_widget.update()

```

#### REPLACE Controls by ID

```python3
>>> id_widget = page.get_control(id='_5')
>>> id_widget.controls = [ft.Widget(attributes)]
>>> id_widget.update()

```

#### REPLACE Controls by ID

```python3
>>> id_widget = page.get_control(id='_5').controls[0]
>>> id_widget.controls.bgcolor = 'Red'
>>> id_widget.update()

```

#### UNIQ Class

```python

class InfinityObjects(ft.Controls):
    pass

unique_object = InfinityObjects()


>>>  EXEMPLE = ft.Row(
>>>                controls = [
>>>                            ################################################################
>>>                            unique_object,       # <=== SAME OBJECT IF MODIFY MODIFY ALL SAME TIME
>>>                            unique_object,       # <=== SAME OBJECT IF MODIFY MODIFY ALL SAME TIME
>>>                            unique_object,       # <=== SAME OBJECT IF MODIFY MODIFY ALL SAME TIME
>>>                            ################################################################
>>>                            InfinityObjects(),   # <=== NEW  OBJECT IF MODIFY MODIFY ALL DIFERENTS PROPERTIES
>>>                            InfinityObjects(),   # <=== NEW  OBJECT IF MODIFY MODIFY ALL DIFERENTS PROPERTIES
>>>                            InfinityObjects(),   # <=== NEW  OBJECT IF MODIFY MODIFY ALL DIFERENTS PROPERTIES
>>>                            ################################################################
>>>                ]
>>>
>>>    )

```

#### MAKE A PIP PACKAGE

Sure, creating a simple pip package involves a few steps. Here's a basic example to create a pip package in Python 3:

1. **Project Structure:** Create a directory for your project with the following structure:
    ```shell
>>>    your_project_name/
>>>    ├── your_project_name/
>>>    │   └── __init__.py
>>>    ├── README.md
>>>    ├── LICENSE
>>>    └── setup.py
    ```

2. **Code File:** Inside the inner `your_project_name` directory, create a Python file, for example, `your_module.py`, with your code.

3. **setup.py:** Create or edit the `setup.py` file like so:

   ```python
>>>   from setuptools import setup, find_packages
>>>   setup(
>>>       name='your_project_name',
>>>       version='0.1',
>>>       packages=find_packages(),
>>>       install_requires=[
>>>           # Add any dependencies here
>>>       ],
>>>   )
   ```

4. **Package File:** Inside the inner `your_project_name` directory, create an empty `__init__.py` file. If your package has modules, you can include them here.

5. **README and LICENSE:** Create a `README.md` and a `LICENSE` file, including appropriate content.

6. **Build the Package:** In the terminal, navigate to the outer directory (`your_project_name`) and run:
   ```shell
>>>   python setup.py sdist bdist_wheel
   ```

7. **Publishing:** You can distribute your package to the Python Package Index (PyPI) by using `twine`:
   ```shell
>>>   pip install twine
>>>   twine upload dist/*
   ```

This will upload your package to PyPI, making it accessible to others using `pip install your_project_name`.

Remember to replace `your_project_name` with your actual package name and adjust the version as needed.

#### MAKE HACK TIPS

#### ATTRIBUTES
- GET SPECIFIC ATTRIBUTE PASSED
```shell
>>>  tmp_data = screen_1.__getattribute__('content')
```
- GET ATTRIBUTE OF THE WIDGET
```shell
>>> tmp_data = screen_1._Control__attrs
```

- GET ATTIBUTE IN DICT
```shell
>>> tmp_data = screen_1._wrap_attr_dict(self.data_share)
```

- GET ATTIBUTE LIKE STR
```shell
>>> tmp_data = screen_1.__str__()
```

- GET ATTRIBUTE LIKE A WIDGET
```shell
>>> tmp_data = screen_1.__repr__()
```

#### GET SPECIFIC ATTRIBUTES
- GET SPECIFIC
```shell
>>> tmp_data.__getattribute__('text')
>>> tmp_data._get_attr('text')
```

#### DEL SPECIFIC ATTRIBUTES
- DEL SPECIFIC
```shell
>>> tmp_data.__delattr__('text')
```

#### ATTRIBUTES ID
- GET ID
```shell
>>> tmp_data = screen_1.uid
```

#### CHILDRENS
- GET ONE WIDGET BEFORE
```shell
>>>  tmp_data = screen_1._Control__previous_children
```
- GET ONE WIDGET BEFORE LIST
```shell
>>> tmp_data = screen_1._get_children()
>>> tmp_data = screen_1._previous_children
```

#### WRAP LIKE A DICT
```shell
>>> print(Drop_Make_data._wrap_attr_dict({'new_value':Drop_Make_data}))
>>> Drop_Make_data.invoke_method('on_click')
```
#### GET WIDGET NAME
- GET NAME MODULE
```shell
>>> tmp_data = screen_1.__module__
```
- GET NAME OF THE WIDGET
```shell
>>> tmp_data = screen_1._get_control_name()
```

#### DELETE WIDGET FROM APP
```
>>> tmp_data._index                                             ####<=== very important DICT OF ALL WWIDGETS
>>> del tmp_data._index[widget._Control__uid]                   ####<=== delete from index page very important
```

#### KWON INFO ABOUT PAGE FROM EVERY WHERE
```shell
>>> tmp_data = Drop_Container_exemple.__dict__.get('_Control__page')    #  s.__dict__.get('_Control__page') ####<=== GET MAIN PAGE
>>> tmp_data._Page__next_control_id                                     ####<=== very important
>>> tmp_data._Page__views                                               ####<=== very important

>>> tmp_data._index                                             ####<=== very important DICT OF ALL WWIDGETS
>>> tmp_data._index.get('_9')                                   ####<=== GET BY INDEX
>>> tmp_data.get_control(id='_5').controls                      ####<=== GET BY INDEX
```
<!-- markdownserver http://localhost:8009/WIDGET.md -->
### CAPTURE EVENT WIDGET DATA
```python
event_widget=ft.Container(
               on_click = lambda tmp_widget: self.edit_widget(target=tmp_widget)
            )


def edit_widget(self,target: object=None):
   self.tmp_widget = target.control
   self.tmp_widget.bgcolor=ft.colore('red')
   self.tmp_widget.parent.update()

```

### STORAGE DATA
```python
>>> page.session.set("key", "value")
>>> value = page.session.get("key")
>>> page.session.contains_key("key")
>>> page.session.get_keys()
>>> page.session.remove("key")
>>> page.session.clear()
```

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
>>> container {'width': 150,
               'bgcolor': 'cyan',
               'ink': False,
               'onhover': True,
               'margin': '{"l":8,"t":8,"r":8,"b":8}',
               'padding': '{"l":8,"t":8,"r":8,"b":8}',
               'alignment': '{"x":0,"y":0}'
            }

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

EXEMPLE = ft.Row(
             controls = [
               InfinityObjects(),   # <=== NEW  OBJECT IF MODIFY MODIFY ALL DIFERENTS PROPERTIES
             ]
 )
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

- GET ATTRIBUTE LIKE A DICT [ get all values <====s]
```shell
>>> tmp_data = screen_1.__dict__
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

#### CHILDRENS PARENT
- GET ONE WIDGET BEFORE
```shell
>>>  tmp_data = screen_1._Control__previous_children
```
- GET ONE WIDGET BEFORE LIST
```shell
>>> tmp_data = screen_1.parent
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

#### DIFERENTS WAYS TO GET ATTRIBUTES
```python
print(screen_1._Control__attrs)                     >>> {'width': (240, False), 'height': (120, False),
print(screen_1._Container__content)                 >>> row {'wrap': True, 'n': 'content'}
print(screen_1._get_control_name())                 >>> container
print(screen_1._get_attr('width'))                  >>> 240

print(screen_1._wrap_attr_dict({'hello':screen_1})) >>> {'hello': Container(width=240, height=120,
print(screen_1.__str__())                           >>> container {'width': 240, 'height': 120, 'bgcolor': '#44CCCC00' <<< +++++
print(screen_1.__repr__() )                         >>> Container(width=240, height=120, bgcolor='#44CCCC00',


 # ONLY WAY TO GET ATTRIBUTES CORRECTLY AND SET ATTRIBUTES
data = {}                                           >>> {'alignment': '{"x":0,"y":0}', 'bgcolor': ''}
screen_1.copy_attrs(dest=data)                      >>> {'alignment': '{"x":0,"y":0}', 'bgcolor': ''}

screen_1._set_attr('width',10)                      >>> 10
screen_1.update()

```



#### TYPE RETURNED CODE
```python
def refactory_code(self, string_widget: object = object()) -> str:
   string_widget: object = object()
   string_widget: string = str()
   string_widget: tuple = tuple()
   string_widget: dict = dict()
   string_widget: float = float()
   string_widget: int = int()
   string_widget: set = set()
   string_widget: bool = bool()
```

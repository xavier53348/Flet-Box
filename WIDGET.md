<!-- markdownserver http://localhost:8009/WIDGET.md -->

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
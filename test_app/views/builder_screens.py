from flet import Container ,ElevatedButton
#
# SCREEN={

# 'screen_1':'REMPLACE__'

#         }

SCREEN={

'REMPLACE_NAME_WIDGET':'REMPLACE_WIDGET_ATTRIBUTS',

        }

def builder_screens(widget_name):
    """.replace("'REPLACE_'", f"{self.data_share.content.__repr__()}")"""

    global SCREEN
    return SCREEN.get(widget_name)




DATA_GLOBAL =  {
                     'user_name' : dict(),                           # <== DICT WITH ALL WIDGET IN PHONE TO EXPORT APP
                           'list': ['no erase','main_screen'],       # <== LIST WITH INDEX LIST
                'widget_selected': 'widget_object',                  # <== WIDGET OBGET CHANGE COLOR
               }

def SCREEN_GLOBAL_VAR(
               set_global_var:    dict = {'var_name':'value_in'},
               get_global_var:     str = 'var_name',
               remove_global_var: dict = {'user_name':'screen_name'},
               add_list:           str = 'add_list',
               remove_list:        str = 'remove_list',
               get_index_list:     str = 'get_index_list',
               get_list:          bool = False,
               empty_list:        bool = False,
               ):
     """
     #### SCREEN_GLOBAL_VAR IS A DICT THAT COINTEN ALL DATA THAT WE WANT CALL IN ALL FLET-BOX
     #### WE MAY CALL IN ALL MOMENT IMPORTING LITE CONFIG

     ### EXEMPLE:

     >>> from ..settings_var.settings_widget import SCREEN_GLOBAL_VAR

     ### Set the global var by Name and Value:

     >>> SCREEN_GLOBAL_VAR(set_global_var={'var_name':'value_in'})

     ### Get the gloval bar by name:

     >>> SCREEN_GLOBAL_VAR(get_global_var='var_name'})

     ### Remove the gloval bar by name:

     >>> SCREEN_GLOBAL_VAR(remove_global_var='var_remove'})

     """
     global DATA_GLOBAL

     if not set_global_var == {'var_name':'value_in'}:
          DATA_GLOBAL.update(set_global_var)

     elif not get_global_var == 'var_name':
          TMP_DATA_GLOBAL  =  DATA_GLOBAL.get(get_global_var)
          return TMP_DATA_GLOBAL

     elif not remove_global_var == {'user_name':'screen_name'}:
          """ REMOVE SPECIFIC WIDGET FROM SELECTED WIDGET PHONE"""
          DATA_GLOBAL.get(remove_global_var.key()).pop(remove_global_var[remove_global_var.key()])

     elif not add_list == 'add_list':
          DATA_GLOBAL.get('list').append(add_list)

     elif not get_index_list == 'get_index_list':
          return DATA_GLOBAL.get('list')

     elif not remove_list == 'remove_list':
          DATA_GLOBAL.get('list').pop(remove_list)

     elif get_list:
          return DATA_GLOBAL.get('list')

     elif empty_list:
          DATA_GLOBAL['list']= ['no erase','main_screen']

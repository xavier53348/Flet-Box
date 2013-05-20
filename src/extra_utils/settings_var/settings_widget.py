
DATA_GLOBAL = {
               ########################
             'LIST_SELECTED_WIDGETS'      : list(), #<== LIST OF DROPP_WIDGET INSIDE PHONE THAT WILL BE RESET EVERY TIME

                'NUM_CLICKS'              : 1,      #<== COUNT WIDGET DRAGG_WIDGET BOX TO RESET WIDGET TO DROPP
        'NUM_WIDGETS_DROPPED'             : 1,      #<== COUNT DRAGG_WIDGET BOX THAT WILL BE NEW ASSIGNED BY _ID NUMBER
               ########################
                 'PAGE'                   : None,
                 'SELECT_DRAGG'           : None,   #<== LITE BOX DRAGG_DROP BOX
                 'BOOL_SHOW_SELECTED'     : False,  #<== ONLY SHOW TRUE O FALSE IN SELECTED IN PHONE
               ########################
         'SHOW_TEXT_SELECTED_PHONE_WIDGET': 'None',   #<== LITE CONTAINER THAT SHOW SELECTED PHONE WIDGET TO CONFIG
         'SHOW_TEXT_SELECTED_DRAGG_WIDGET': 'None',   #<== LITE CONTAINER THAT SHOW SELECTED DRAGG WIDGET TO CONFIG
               ########################
                      'CONFIG_TABS_PHONE' : None,   #<== CONFIGURATION PHONE     BOX THAT CONTAIN ALL WIDGET TO MODIFY PROPERTY
                 'CONFIG_TABS_CONTAINERS' : None,   #<== CONFIGURATION CONTAINER BOX THAT CONTAIN ALL WIDGET TO MODIFY PROPERTY
         'CONFIG_TABS_CONTAINERS_CONTENT' : None,   #<== CONFIGURATION CONTENT   BOX THAT CONTAIN ALL WIDGET TO MODIFY PROPERTY
               ########################
                        'PHONE_CONTAINER' : None,   #<== PHONE
                'PHONE_CONTAINER_CONTENT' : None,   #<== PHONE CONTENT

        'SELECT_DROPP_WIDGET_CONTAINER'   : None,   #<== SELECTED WIDGET IN PHONE
'SELECT_DROPP_WIDGET_CONTAINER_CONTENT'   : None,   #<== SELECTED WIDGET IN PHONE CONTENT
               ########################
               'ICON_BROWSER_CONTAINER'   : None,   #<== BOX CONTAINER WITH SEARCH ICON
              'COLOR_BROWSER_CONTAINER'   : None,   #<== BOX CONTAINER WITH SEARCH COLORS
                }

def GLOBAL_VAR(set_global_var = {'var_name':'value_in'}, get_global_var= 'var_name'):
     """
     #### GLOBAL_VAR IS A DICT THAT COINTEN ALL DATA THAT WE WANT CALL IN ALL FLET-BOX
     #### WE MAY CALL IN ALL MOMENT IMPORTING LITE CONFIG

     ### EXEMPLE:

     >>> from ..settings_var.settings_widget import GLOBAL_VAR

     ### Set the global var by Name and Value:

     >>> GLOBAL_VAR(set_global_var={'var_name':'value_in'})

     ### Get the gloval bar by name:

     >>> GLOBAL_VAR(get_global_var='var_name'})

     """
     global DATA_GLOBAL

     if not set_global_var == {'var_name':'value_in'}:
          DATA_GLOBAL.update(set_global_var)

     elif not get_global_var == 'var_name':
          TMP_DATA_GLOBAL  =  DATA_GLOBAL.get(get_global_var)
          return TMP_DATA_GLOBAL
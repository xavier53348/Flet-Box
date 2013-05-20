
#: DICT REFERENCE TO KNOW ALL WIDGET IN GLOVAL VAR
DATA_GLOBAL = {

                      'EXPORT_DATA_PHONE' : dict(), # <== DICT WITH ALL WIDGET IN PHONE TO EXPORT APP
                'SELECT_DATA_ERASE_PHONE' : None,   # <== SELECTED ID WIDGET IN PHONE

        'CHECK_CURRENT_TIME_DOBLE_CLICKS' : 0,      # <== CURRENT PERFORMANSE TIME TO CHECK 2 CLICKS IN CONTAINER OVER CONTAINERS <== IS A ISSUE IN CONTAINERS

                  'LIST_SELECTED_WIDGETS' : list(), # <== LIST OF DROPP_WIDGET INSIDE PHONE THAT WILL BE RESET EVERY TIME
                    'LIST_KEYS_DICT_USED' : None,   # <== LIST WIDGET_DICT TO CALL IN TAB 3 INIDE WIDGET_CONFIG

                             'NUM_CLICKS' : 1,      # <== COUNT WIDGET DRAGG_WIDGET BOX TO RESET WIDGET TO DROPP
                    'NUM_WIDGETS_DROPPED' : 1,      # <== COUNT DRAGG_WIDGET BOX THAT WILL BE NEW ASSIGNED BY _ID NUMBER

                                   'PAGE' : None,
                           'SELECT_DRAGG' : None,   # <== LITE BOX DRAGG_DROP BOX
                     'BOOL_SHOW_SELECTED' : False,  # <== ONLY SHOW TRUE O FALSE IN SELECTED IN PHONE

         'SHOW_TEXT_SELECTED_PHONE_WIDGET': 'None', # <== LITE CONTAINER THAT SHOW SELECTED PHONE WIDGET TO CONFIG
         'SHOW_TEXT_SELECTED_DRAGG_WIDGET': 'None', # <== LITE CONTAINER THAT SHOW SELECTED DRAGG WIDGET TO CONFIG

                      'CONFIG_TABS_PHONE' : None,   # <== CONFIGURATION PHONE     BOX THAT CONTAIN ALL WIDGET TO MODIFY PROPERTY
                 'CONFIG_TABS_CONTAINERS' : None,   # <== CONFIGURATION CONTAINER BOX THAT CONTAIN ALL WIDGET TO MODIFY PROPERTY
         'CONFIG_TABS_CONTAINERS_CONTENT' : None,   # <== CONFIGURATION CONTENT   BOX THAT CONTAIN ALL WIDGET TO MODIFY PROPERTY
             'HIDE_CONFIG_TABS_CONTAINERS': None,   # <== HIDE CONTAINER          BOX THAT CONTAIN ALL WIDGET TO MODIFY PROPERTY

                        'SELECTED_SCREEN' : None,   # <== SELECTED PHONE SCREEN
                'GENERIC_CONTAINER_PHONE' : None,   # <== GENERIC SELECTED PHONE SCREEN BLUR FRAMEWORK

          'SELECT_DROPP_WIDGET_CONTAINER' : None,   # <== SELECTED WIDGET IN PHONE
  'SELECT_DROPP_WIDGET_CONTAINER_CONTENT' : None,   # <== SELECTED WIDGET IN PHONE CONTENT

                 'ICON_BROWSER_CONTAINER' : None,   # <== BOX CONTAINER WITH SEARCH ICON
                'COLOR_BROWSER_CONTAINER' : None,   # <== BOX CONTAINER WITH SEARCH COLORS
                  'GPT_BROWSER_CONTAINER' : None,   # <== BOX CONTAINER WITH SEARCH GPT

                        'ABOUT_CONTAINER' : None,   # <== BOX CONTAINER WITH ABOUT PAGE

                  'TEXT_EDITOR_CONTAINER' : None,   # <== BOX CONTAINER WITH TEXT  EDITOR LIKE SUBL

                 'COLOR_EDITOR_CONTAINER' : None,   # <== BOX CONTAINER WITH COLOR EDITOR LIKE SELECT COLOR
                'IMAGEN_EDITOR_CONTAINER' : None,   # <== BOX CONTAINER WITH IMAGE EDITOR LIKE SELECT COLOR
      'WIDGET_SELECTION_EDITOR_CONTAINER' : None,   # <== WIDGET THAT ITS SELECTED TO EDIT IN CONFIG CONTAINER      WORK IN STREAMING ALWAYS CHANGE


                          'ALERT_WIDGET ' : None,   # <== GREEN ALERT SELECTED WIDGET

                       'SCREEN_CONTAINER' : None,   # <== SCREEN_MANAGER BOX CONTAINER
                              'TREE_VIEW' : None,   # <== TREE_VIEW BOX CONTAINER


                              'DRAGG_SHOW': None,   # <== BOX DRAGG
                              'CONFI_SHOW': None,   # <== BOX CONFIG


                     'ALL_SCREEN_IN_DICT' : dict(),   # <== ALL SCREENS IN SCREEN MANAGER

                              'row_phone' : dict(),   # <== ALL SCREENS IN ROW TO SAVE DATA
               }

def GLOBAL_VAR(
               set_global_var:     dict = {'var_name':'value_in'},
               get_global_var:     str  = 'var_name',
               remove_global_var:  str  = 'var_remove',
               remove_screen_var:  str  = 'var_screen_remove',
               remove_all_screen_var:  bool  = True,
               ):
     """
     #### GLOBAL_VAR IS A DICT THAT COINTEN ALL DATA THAT WE WANT CALL IN ALL FLET-BOX
     #### WE MAY CALL IN ALL MOMENT IMPORTING LITE CONFIG

     ### EXEMPLE:

     >>> from ..settings_var.settings_widget import GLOBAL_VAR

     ### Set the global var by Name and Value:

     >>> GLOBAL_VAR(set_global_var={'var_name':'value_in'})

     ### Get the gloval bar by name:

     >>> GLOBAL_VAR(get_global_var='var_name'})

     ### Remove the gloval bar by name:

     >>> GLOBAL_VAR(remove_global_var='var_remove'})

     """
     global DATA_GLOBAL

     if not set_global_var == {'var_name':'value_in'}:
          DATA_GLOBAL.update(set_global_var)

     elif not get_global_var == 'var_name':
          TMP_DATA_GLOBAL  =  DATA_GLOBAL.get(get_global_var)
          return TMP_DATA_GLOBAL

     elif not remove_global_var == 'var_remove':
          """ REMOVE SPECIFIC WIDGET FROM SELECTED WIDGET PHONE"""
          DATA_GLOBAL.get('EXPORT_DATA_PHONE').pop(remove_global_var)

     elif remove_all_screen_var:
          """ REMOVE SPECIFIC WIDGET FROM SELECTED SCREEN PHONE"""
          DATA_GLOBAL['ALL_SCREEN_IN_DICT']=dict()
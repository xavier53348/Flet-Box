import flet as ft
import time

DATA_GLOBAL =  {
                  'main_page' : None,
                'all_screens' : None,
             'current_screen' : 'main_screen',
                  'to_screen' : None,
               }

def GLOBAL_VAR(set_global_var = {'var_name':'value_in'}, get_global_var= 'var_name',remove_global_var = 'var_remove'):
     """
        GLOBAL_VAR IS A DICT THAT COINTEN ALL DATA THAT WE WANT CALL IN ALL FLET-BOX
        WE MAY CALL IN ALL MOMENT IMPORTING LITE CONFIG

        ### EXEMPLE:
        >>> from ..settings_var.settings_widget import GLOBAL_VAR

        ### Set the global var by Name and Value:
        >>> GLOBAL_VAR(set_global_var={'var_name':'value_in'})

        ### Get the global bar by name:
        >>> GLOBAL_VAR(get_global_var='var_name'})
     """
     global DATA_GLOBAL

     if not set_global_var == {'var_name':'value_in'}:
          DATA_GLOBAL.update(set_global_var)

     elif not get_global_var == 'var_name':
          TMP_DATA_GLOBAL  =  DATA_GLOBAL.get(get_global_var)
          return TMP_DATA_GLOBAL


def builder_app(styles,screen,main_page):
    """ Will return a dictionary with all screens and main screen contents"""
    GLOBAL_VAR(set_global_var={'all_screens':screen,'main_page':main_page})
    tmp_data = {
                'show_all_screens': screen.keys(),
                'builder_app' :screen.get('main_screen'),
                }

    # print(screen)
    return tmp_data

def got_to_screen(to_screen , style='bar' , time_style=0.8 ):
    """
    clean the view and add and update new view

    got_to_screen(to_screen='screen_1' , style='ring')
    style = 'ring' , 'bar'
    """
    main_page      = GLOBAL_VAR(get_global_var='main_page')
    all_screens    = GLOBAL_VAR(get_global_var='all_screens')
    current_screen = GLOBAL_VAR(get_global_var='current_screen')

    # from_screen = all_screens.get(current_screen)
    next_screen = all_screens.get(to_screen)

    # main_page.remove(all_screens.get(current_screen))
    main_page.clean()

    if style == "ring":
        main_page.splash = ft.Container(
                                        content   = ft.ProgressRing(),
                                        alignment = ft.alignment.center,
                                       )
    elif style == "bar":
        main_page.splash = ft.ProgressBar()

    # update page
    main_page.update()

    # effect time
    time.sleep(time_style)

    main_page.add(next_screen)    # < diferents effects
    main_page.splash = None
    main_page.update()

    # GLOBAL_VAR(set_global_var={'to_screen':to_screen})
    GLOBAL_VAR(set_global_var={'current_screen':to_screen})

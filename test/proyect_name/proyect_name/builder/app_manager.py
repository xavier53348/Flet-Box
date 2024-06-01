import flet as ft
import time
# from controls.app_style_manager   import styles

DATA_GLOBAL: dict = {
                'screen_size' : {'width':720,'height':600},

                  'main_page' : None,
                'all_screens' : None,
             'current_screen' : 'main_screen',
                  'to_screen' : None,

                        'home':'main_screen', #: default path
                 'main_screen':'main_screen', #: current
               }

def GLOBAL_VAR(set_global_var: dict={'var_name':'value_in'}, get_global_var: str='var_name', remove_global_var: str='var_remove'):
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
    DEFAULD:     dict = {'var_name':'value_in'}
    DEFAULD_GET: str  = 'var_name'

    if not set_global_var == DEFAULD:
         DATA_GLOBAL.update(set_global_var)

    elif not get_global_var == DEFAULD_GET:
         return DATA_GLOBAL.get(get_global_var)

def builder_app(screen, main_page):
    """ Will return a dictionary with all screens and main screen contents"""

    GLOBAL_VAR(set_global_var={'all_screens':screen,'main_page':main_page})

    tmp_data = {
                'show_all_screens': screen.keys(),
                'builder_app' :screen.get('main_screen'),
                }

    #: Run only in production
    # print(screen)
    return tmp_data

def got_to_screen(to_screen: str, style: str='bar', time_style: float=0.8 ):
    """
    Clean the view and add and update new view

    got_to_screen(to_screen='screen_1' , style='ring')

    effects:
    style = 'ring' , 'bar'

    """
    main_page:      dict = GLOBAL_VAR(get_global_var='main_page')
    all_screens:    dict = GLOBAL_VAR(get_global_var='all_screens')
    current_screen: str  = GLOBAL_VAR(get_global_var='current_screen')

    from_screen: dict = all_screens.get(current_screen)
    next_screen: dict = all_screens.get(to_screen)

    if style == "ring":
        main_page.splash = ft.Container(
                                        content   = ft.ProgressRing(),
                                        alignment = ft.alignment.center,
                                       )
    elif style == "bar":
        main_page.splash = ft.ProgressBar()

    #: UPDATE COLOR STREAMING
    # ITS NECESSARY MARK MAIN WIDGET index 0 "BECAUSE MARK ALL COLOR BY DEFAULD"
    # styles['_2921']['bgcolor']  = next_screen.bgcolor
    # styles['_2921']['gradient'] = next_screen.gradient

    main_page.update()

    #: TIME EFFECTS
    time.sleep(time_style)
    main_page.clean()
    main_page.add(next_screen)    # <= diferents effects

    #: UPDATE SIZE STREAMING
    next_screen.height , next_screen.width  = main_page.height , main_page.width

    next_screen.update()
    main_page.splash = None
    main_page.update()

    #: GLOBAL_VAR(set_global_var={'to_screen':to_screen})
    GLOBAL_VAR(set_global_var={'current_screen':to_screen})

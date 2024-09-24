#: ALL SCREENS IN APP
from .views.main_screen import main_screen
from .views.main_screen_events import *

from .views.class_menu_screen import class_menu_screen
from .views.class_menu_screen_events import *

from .views.documentation_screen import documentation_screen
from .views.documentation_screen_events import *

screens: dict={
                # 'main_screen': class_menu_screen(),
				'main_screen': main_screen(),
				'class_menu_screen': class_menu_screen(),
				'documentation_screen': documentation_screen(),
				}
#: ALL SCREENS IN APP
from .views.main_screen import main_screen
from .views.main_screen_events import *

screens: dict={
				'main_screen': main_screen(),
				}
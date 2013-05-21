#: ALL SCREENS IN APP
from .views.main_screen import main_screen
from .views.main_screen_events import *

from .views.screen_1 import screen_1
from .views.screen_1_events import *

screens: dict={
				'main_screen': main_screen(),
				'screen_1': screen_1(),
				}
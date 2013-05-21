#: ALL SCREENS IN APP
from .views.main_screen import main_screen
from .views.main_screen_events import *

from .views.fata import fata
from .views.fata_events import *

screens: dict={
				'main_screen': main_screen(),
				'fata': fata(),
				}
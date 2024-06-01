import flet as ft
from .app_events_manager import *

from .views.main_screen import CustomPage
# from .views.screen_1 import Screen1
# from .views.screen_2 import Screen2


screens: dict={

		'main_screen': CustomPage(),
        # 'screen_1':    Screen1(),
		# 'screen_2':    Screen2(),
}

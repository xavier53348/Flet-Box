#: THIS MODULE LET YOU MANAGE ALL SCREENS IN APP
#: YOU MAY CHANGE BETWEEN SCREENS TO EASY

# from .views.second_screen import second_screen
# from .views.second_screen_events import *

from .views.main_screen import main_screen
# from .views.main_screen_events import *

# from .views.first_screen import first_screen
# from .views.first_screen_events import *

# from .views.doc_screen import doc_screen
# from .views.doc_screen_events import *

screens: dict={
	'main_screen': main_screen,
	# 'second_screen': second_screen,
	# 'first_screen': first_screen,
	# 'doc_screen': doc_screen,
	# 'main_screen': first_screen(),
	}
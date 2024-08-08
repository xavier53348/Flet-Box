from .flet_box import run_app
#: LEFT DRAGG CONTAINER
from extra_utils.config_container.widget_editor                  import Build_Editor
from extra_utils.drag_container.widget_drag_editor               import Build_Drag_Editor
#: TREEVIEW CONTAINER
from extra_utils.tree_view.tree_view                             import TreeView
from extra_utils.tree_view.tree_view_text_editor                 import TreeViewTextEditor
#: PHONE CONTAINER
from extra_utils.phone_container.widget_phone_editor             import Build_Phone_Editor
#: TAB MENU CONTAINER
from extra_utils.menu_tab_up_phone.widget_menu_tab_editor        import MenuUpContainer
from extra_utils.menu_tab_left_phone.widget_menu_left_editor     import MenuLeftContainer
#: LITE MENU RIGHT PHONE AND DOWN
from extra_utils.lite_menu_bar_right_phone.right_bar_menu_phone  import LiteMenuUpContainer
from extra_utils.lite_menu_bar_down_phone.footer_bar_menu_phone  import LiteMenuDownContainer
from extra_utils.lite_menu_bar_down_phone.selected_widget        import SelectedWidget
#: ICON AND COLOR BROWSER CONTAINER
from extra_utils.icon_browser.icon_browser                       import IconBrowser
from extra_utils.color_browser.color_browser                     import ColorBrowser
from extra_utils.chat_gpt_browser.gpt_browser                    import GptBrowser
#: ABOUT CONTAINER
from extra_utils.about.about                                     import AboutPage
#: CALL GLOBAL VAR  GLOBAL VARS
from extra_utils.settings_var.settings_widget                    import GLOBAL_VAR
#: ALERT DIALOG
from extra_utils.alert.alert_selected                            import AlertSelected
#: SCREEN MANAGER
from extra_utils.screen_manager.screen_manager                   import ScreenManager ,screen_manager

from .config_container.widget_editor                  import Build_Editor
from .drag_container.widget_drag_editor               import Build_Drag_Editor
#: TREEVIEW CONTAINER
from .tree_view.tree_view                             import TreeView
from .tree_view.tree_view_text_editor                 import TreeViewTextEditor
#: PHONE CONTAINER
from .phone_container.widget_phone_editor             import Build_Phone_Editor
#: TAB MENU CONTAINER
from .menu_tab_up_phone.widget_menu_tab_editor        import MenuUpContainer
from .menu_tab_left_phone.widget_menu_left_editor     import MenuLeftContainer
#: LITE MENU RIGHT PHONE AND DOWN
from .lite_menu_bar_right_phone.right_bar_menu_phone  import LiteMenuUpContainer
from .lite_menu_bar_down_phone.footer_bar_menu_phone  import LiteMenuDownContainer
from .lite_menu_bar_down_phone.selected_widget        import SelectedWidget
#: ICON AND COLOR BROWSER CONTAINER
from .icon_browser.icon_browser                       import IconBrowser
from .color_browser.color_browser                     import ColorBrowser
from .chat_gpt_browser.gpt_browser                    import GptBrowser
#: ABOUT CONTAINER
from .about.about                                     import AboutPage
#: CALL GLOBAL VAR  GLOBAL VARS
from .settings_var.settings_widget                    import GLOBAL_VAR
#: ALERT DIALOG
from .alert.alert_selected                            import AlertSelected
#: SCREEN MANAGER
from .screen_manager.screen_manager                   import ScreenManager ,screen_manager
#: PALLETE COLOR
from .color_browser.small_palette_color               import Screen_palette
#: IMAGEN SELECTION
from .config_container.photo_selection                import ScreenPhotoSelection
#: SPONSOR DONATION PAGE
from .sponsonrs.sponsors                              import SponsorPage

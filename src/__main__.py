from src.flet_box import main
import flet as ft

if __name__ == "__main__":
    ft.app(
       # assets_dir   = "assets",
       target         = main,
       # port         = 8082,
       # port         = 8080,
       # view         = ft.AppView.WEB_BROWSER, #view=ft.WEB_BROWSER,
       # web_renderer = ft.WebRenderer.HTML
    )
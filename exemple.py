import flet as ft
from fletbox import FletBox, Builder, Factory

#module with custom components
import flet_material as fm
fm.Theme.set_theme("earth") #whatever theme you want

#factory generates builders
factory = Factory(modules={"fm": fm})

#pass custom factory
fb = FletBox(factory=factory)

#fletbox decorator for routing
@fb.view("/")
def test(page: ft.Page) -> None:
    with page.Container(expand=True, margin=-10, gradient=page.standard_gradient): #can used stored attributes using "page" as a shared storage
        with page.Row() as row: #can be assigned, or not
            row.controls.append(ft.ElevatedButton("FletBox")) #see above
            page.ElevatedButton("FletBox")
            textfield = page.TextField(label="FletBox", text_size=20) #can be assigned, or not - for modification/reads

    @page.postexec #OPTIONAL: postexec decorator - run function after view load
    def postfunc():
        # pass #YOUR_POST_FUNCTION_HERE
        print('hello')
#can define whatever non-view-specific thing you want, passing target is optional
def shared_methods(page: ft.Page):
    page.fonts = {
        "Raleway": "assets/Raleway[wght].ttf"
    }
    page.theme = ft.Theme(color_scheme_seed="pink", visual_density="COMFORTABLE", font_family="Raleway")
    page.standard_gradient = ft.LinearGradient(begin=ft.alignment.bottom_left, end=ft.alignment.top_right, colors=["#F7C35A", "#FBAFAB"])
fb.app()
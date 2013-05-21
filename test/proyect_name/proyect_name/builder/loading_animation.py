import flet
from flet import *
import time
import math


class LoadingAnimation(Stack):
    def __init__(self,colors_bucircles=[
                                        flet.colors.WHITE24 ,
                                        flet.colors.WHITE12 ,
                                        flet.colors.WHITE10 ,
                                        ]):
        self.loading_row = Row(alignment="center", spacing=8,run_spacing=20)
        super().__init__()
        self.colors_bucircles = colors_bucircles

    def animate_loader(self, load=True,time_app=20):
        t = 0

        while load:
            for i, circle in enumerate(self.loading_row.controls):
                y_offset = math.sin(t + i * math.pi / 2)
                circle.offset = transform.Offset(0, y_offset)
                circle.update()
            t += 0.20
            time.sleep(0.02)
            if t >= 4:
                # circle.offset = transform.Offset(0, 0.001)
                for i, circle in enumerate(self.loading_row.controls):
                    circle.offset = transform.Offset(0, 0)
                    circle.update()
                break

    def build(self):
        items: list = [
            Container(
                width=24,
                height=24,
                # margin=2,
                bgcolor=self.colors_bucircles[index],
                shape=BoxShape("circle"),
                offset=transform.Offset(0, 0),
                animate_offset=300,
            )
            for index ,i in enumerate(range(3))
        ]

        self.loading_row.controls = items

        return Container(
            content=self.loading_row,
        )

def main(page: Page):
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"

    loading = LoadingAnimation()
    page.add(loading)

    loading.animate_loader()
    page.update()


if __name__ == "__main__":
    flet.app(target=main)

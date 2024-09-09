import asyncio
import flet as ft

async def main(page: ft.Page) -> None:
    page.title = "Sbot minig app"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "#333333"
    page.window_width = 350
    page.window_height = 650
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    async def score_up(event: ft.ContainerTapEvent) -> None:
        score.data += 1
        score.value = str(score.data)

        image.scale = 0.94
        image.src = 'https://otvet.imgsmail.ru/download/77b000b9869a666caf4585df2e1b4630_i-1105.jpg'
        page.update()
        await asyncio.sleep(0.4)
        image.scale = 1
        image.src="https://cs8.pikabu.ru/post_img/2016/04/04/9/1459780736134836088.jpg"
        page.update()

    score = ft.Text(value="0", size=100, data=0)
    score_counter = ft.Text(
        size=50, animate_opacity=ft.Animation(duration=200, curve=ft.AnimationCurve.BOUNCE_IN)
    )
    
    image = ft.Image(
        src="https://cs8.pikabu.ru/post_img/2016/04/04/9/1459780736134836088.jpg",
        fit=ft.ImageFit.CONTAIN,
        animate_scale=ft.Animation(duration=600, curve=ft.AnimationCurve.EASE)
    )

    page.appbar = ft.AppBar(
        leading_width=60,
        title=ft.Text("Comming soon!"),
        center_title=True,
        bgcolor= '#229ED9',
    )

    page.add(
        score,
        ft.Container(
            content=ft.Stack(controls=[image, score_counter]),
            on_click=score_up,
            margin=ft.Margin(0, 0, 0, 30)
        )
    )

if __name__ == "__main__":
    ft.app(target=main)
import asyncio
import flet as ft
import apscheduler
from apscheduler.schedulers.background import BackgroundScheduler
import sqlite3

def get_conn_c():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    return conn, c

conn, c = get_conn_c()
c.execute("""
CREATE TABLE IF NOT EXISTS clicks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    clcks INTEGER,
    days_in_game INTEGER,
    erg INTEGER DEFAULT 69000
)""")
conn.commit()

async def main(page: ft.Page) -> None:
    page.title = "Sbot app"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "#333333"
    page.window.width = 350
    page.window.height = 650
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    async def score_up(event: ft.ContainerTapEvent) -> None:
        if bscore.data > 0: 
            score.data += 1
            bscore.data -= 1
            bscore.value = str(bscore.data)
            score.value = str(score.data)
            conn, c = get_conn_c()
            c.execute("UPDATE clicks SET clcks = clcks + 1, erg = erg - 1 WHERE user_id = ?", (5394056862,))
            conn.commit()
            image.scale = 0.94
            image.src = 'https://otvet.imgsmail.ru/download/77b000b9869a666caf4585df2e1b4630_i-1105.jpg'
            page.update()
            await asyncio.sleep(0.35)
            image.scale = 1
            image.src="https://cs8.pikabu.ru/post_img/2016/04/04/9/1459780736134836088.jpg"
            page.update()
        elif bscore.data == 0:
            page.open(dia)

    dia = ft.AlertDialog(
        title=ft.Text("Вы потратили всю энергию!", color='#FFFFFF'))
    conn, c = get_conn_c()
    c.execute("SELECT clcks FROM clicks WHERE user_id = ?", (5394056862,))
    clck_db = c.fetchone()[0]
    if clck_db is None:
        clck_db = 0

    score = ft.Text(value=f"{str(clck_db)}", size=100, data=clck_db)
    score_counter = ft.Text(
        size=50, animate_opacity=ft.Animation(duration=200, curve=ft.AnimationCurve.BOUNCE_IN)
    )

    conn, c = get_conn_c()
    c.execute("SELECT erg FROM clicks WHERE user_id = ?", (5394056862,))
    erg_db = c.fetchone()[0]

    bscore = ft.Text(value=f"{str(erg_db)}", size=40, data=erg_db, color='#8C8C8C')
    
    image = ft.Image(
        src="https://cs8.pikabu.ru/post_img/2016/04/04/9/1459780736134836088.jpg",
        fit=ft.ImageFit.CONTAIN,
        animate_scale=ft.Animation(duration=600, curve=ft.AnimationCurve.EASE)
    )

    page.appbar = ft.AppBar(
        leading_width=60,
        title=ft.Text("betatest version 0.1"),
        center_title=True,
        bgcolor= '#0088CC',
    )

    page.add(
        score, bscore,
        ft.Container(
            content=ft.Stack(controls=[image, score_counter]),
            on_click=score_up,
            margin=ft.Margin(0, 0, 0, 30)
        )
    )

async def full_enrg():
    conn, c = get_conn_c()
    c.execute("SELECT user_id FROM clicks")
    user_ids = [row[0] for row in c.fetchall()]

    for user_id in user_ids:
        c.execute("UPDATE clicks SET erg = ? WHERE user_id = ?", (69000, user_id))
        conn.commit()
        
scheduler = BackgroundScheduler()
scheduler.add_job(full_enrg, 'cron', hour=4, minute=12)
scheduler.start()

if __name__ == "__main__":
    ft.app(target=main)

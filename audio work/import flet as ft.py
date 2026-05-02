import flet as ft
import flet_audio as fta

def main(page: ft.Page):

    songs = [
        "audio/Illfollow.mp3",
        "audio/6767.mp3",
        "audio/sickymode.mp3",
        "audio/feeling_Cell.mp3",
        "audio/Loveme.mp3"
    ]

    idk = [0]  

    audio = fta.Audio(src=songs[idk[0]])

    async def play(e):
        await audio.play()
    
    async def pause(e):
        await audio.pause()

    async def resume(e):
        await audio.resume()

    async def next_song(e):
    
        idk[0] = (idk[0] + 1) % len(songs)
        audio.src = songs[idk[0]]
        await audio.play()

    async def prev_song(e):
        idk[0] = (idk[0] - 1) % len(songs)
        audio.src = songs[idk[0]]
        await audio.play()
    


    page.add(   ft.Button("Play", on_click=play),
        ft.Button("pause", on_click=pause),
        ft.Button("resume", on_click=resume),
        ft.Button("Next", on_click=next_song),
        ft.Button("Previous", on_click=prev_song))

ft.run(main, assets_dir="assets")
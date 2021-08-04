from telethon.sync import TelegramClient, events
from picamera import PiCamera
from gpiozero import Button

#¡INTRODUCIR AQUI TU NOMBRE DE USUARIO DE TELEGRAM!
nombre_de_usuario = 'Gt17a'
#¡INTRODUCIR AQUI TU NOMBRE DE USUARIO DE TELEGRAM!


def timbre():

    camera = PiCamera()
    camera.start_preview(alpha=192)
    camera.capture('photo.png')
    camera.stop_preview()
    api_id = 2994597
    api_hash = 'fbf5c705e72df09dfdbb7c7eba51c8f4'

    with TelegramClient('anon', api_id, api_hash) as client:
        client.send_message(nombre_de_usuario, ':bell: ¡ESTAN TOCANDO EL TIMBRE! :bell:')
        client.send_file(nombre_de_usuario, 'photo.png')


button = Button(10)

while True:
    if button.is_pressed:
        timbre()
    else:
        print(0)


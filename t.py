from telethon.sync import TelegramClient


#INTRODUCE TU NOMBRE DE USUARIO
nombre_de_usuario = 'Gt17a'
#INTRODUCE TU NOMBRE DE USUARIO



api_id = 2994597
api_hash = 'fbf5c705e72df09dfdbb7c7eba51c8f4'

with TelegramClient('anon', api_id, api_hash) as client:
    client.send_message(nombre_de_usuario, ':bell: ¡ESTAN TOCANDO EL TIMBRE! :bell:')
    client.send_file(nombre_de_usuario, 'photo.png')
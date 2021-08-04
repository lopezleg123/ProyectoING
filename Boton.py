from gpiozero import Button

button = Button(10)

while True:
    if button.is_pressed:
        print(1)
    else:
        print(0)




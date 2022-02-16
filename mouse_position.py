from pynput.mouse import Controller, Button, Listener


def on_click(x, y, button, pressed):
    if pressed:
        print('Mouse position ({0}, {1})'.format(x, y))


with Listener(on_click=on_click) as listener:
    listener.join()

import qrcode 
import PySimpleGUI as sg
from PIL import Image

layout = [
    [sg.Text('Enter your text:', text_color='black',background_color='purple')],
    [sg.InputText(key='input_text')],
    [sg.Button('Create',button_color='pink')]
]

window = sg.Window('QR Code Generator',layout, background_color='brown')

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Create':
        user_input = values['input_text']
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(user_input)
        qr.make(fit=True)
        img = qr.make_image(fill_color='black', back_color='white')

        img.show()


window.close()  
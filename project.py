import PySimpleGUI as sg
import pyttsx3


tts_engine=pyttsx3.init()
voices = tts_engine.getProperty('voices')

layout = [
    [sg.Text('Enter your text to speak:', text_color='black',background_color='blue')],
    [sg.InputText(key='input_text')],
    [sg.Text('Select a voice:', text_color='black', background_color='orange')],
    [sg.Radio('Male','voice_type',
default=True, key='male_voice', background_color='yellow'),
sg.Radio('Female','voice_type',
default=False, key='female_voice', background_color='purple')],
    [sg.Button('Speak', button_color='pink')]
]

window = sg.Window('Text-to-Speech Project',layout, background_color='indigo')

while True:
    event,values=window.read()
    if event==sg.WIN_CLOSED:
        break
    elif event=='Speak':
        user_input=values['input_text']
        if values['male_voice']:
            tts_engine.setProperty('voice','english+f1')
            tts_engine.say(user_input)
            tts_engine.runAndWait()


window.close()









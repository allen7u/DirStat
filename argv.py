










import sys,os,re,math
from datetime import datetime
from shutil import copy,copytree
import PySimpleGUI as sg


print ('from ps:')
print (sys.argv[1])

layout = [
    [sg.Text('Path')],
    [sg.Input(key='path')],
    [sg.Input(sys.argv[1],key='path')],
    [sg.Button('submit'), sg.Button('cancel')],
    # [sg.Text('输出：'), sg.Text(key='OUTPUT')]
]
window = sg.Window('Tree Maker GUI', layout)
while True:
    event, values = window.read()
    # print(event)
    # print(values)
    if event in (None, 'cancel'):
        break
    else:
        path = values['path']
        # window['OUTPUT'].update(values['INPUT1'])

# input()
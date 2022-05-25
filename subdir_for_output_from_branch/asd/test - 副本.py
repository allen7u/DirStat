import PySimpleGUI as sg
import sys,os,re,math


layout = [
    [sg.Text('Path')],
    [sg.Input(key='path')],
    [sg.Input(key='path',)],
    [sg.Button('submit'), sg.Button('cancel')],
    # [sg.Text('输出：'), sg.Text(key='OUTPUT')]
]
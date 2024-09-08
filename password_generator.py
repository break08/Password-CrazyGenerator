import tkinter as tk
import random
import pyperclip
import os
letters = [
    'a',
    'b',
    'c',
    'd',
    'e',
    'f',
    'g',
    'h',
    'i',
    'j',
    'k',
    'l',
    'm',
    'n',
    'o',
    'p',
    'q',
    'r',
    's',
    't',
    'u',
    'v',
    'w',
    's',
    'y',
    'z'
]
num = [
    '1',
    '2',
    '3',
    '4',
    '5',
    '6',
    '7',
    '8',
    '9',
    '0'
]
sc = [
    '!',
    '@',
    '#',
    '$',
    '%',
    '^',
    '&',
    '*',
    '(',
    ')',
    '-',
    '_'
]
list_all = [letters, num, sc]
def reset ():
    result.config (text = '')
    def generate ():
        result_now = result.cget ("text")
        limit = int(num_cha.get ())
        if len(result_now) < limit:
            random_list = random.choice (list_all)
            random_cha = random.choice (random_list)
            result.config (text = result_now + random_cha)
            root.after (50, generate)
    generate()
def copy ():
    copy = result.cget ("text")
    pyperclip.copy (copy)
    if result.cget ("text") == "":
        file = os.path.join ('announce', 'error_no_num.vbs')
        os.startfile (file)
        
  
root = tk.Tk()
root.title ('Password Generator')
root.geometry ('500x500')
info_1 = tk.Label (root, text = 'Type your number of character here: ')
info_1.place (x = 50, y = 10)
num_cha = tk.Entry (root)
num_cha.place (x = 260, y = 10)
result = tk.Label (root, text = '', bg = 'white', height = 1, width = 50)
result.place (x = 130, y = 30)
info_2 = tk.Label (root, text = 'Password Generated')
info_2.place (x = 50, y = 30)
button = tk.Button (root, text = 'Generate', command = reset)
button.place (x = 250, y = 250)
copy_button = tk.Button (root, text = 'Copy password', command = copy)
copy_button.place (x = 50, y = 250)
root.mainloop()
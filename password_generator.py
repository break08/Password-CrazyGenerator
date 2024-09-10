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
letters_upper = [
    'A',
    'B',
    'C',
    'D',
    'E',
    'F',
    'G',
    'H',
    'I',
    'J',
    'K',
    'L',
    'M',
    'N',
    'O',
    'P',
    'Q',
    'R',
    'S',
    'T',
    'U',
    'V',
    'W',
    'S',
    'Y',
    'Z'
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
emoji = [
    "😀", "😃", "😄", "😁", "😆", "😅", "😂", "🤣", "😊", "😇",
    "😉", "😌", "😍", "🥰", "😘", "😗", "😚", "😋", "🤪", "😜",
    "🥲", "😭", "😤", "😡", "😶", "😱", "😨", "😰", "🤢", "🤮",
    "😷", "🤒", "🤕", "🤠", "🥳", "😎", "🧐", "🤓", "😍", "😭",
    "🐶", "🐱", "🐭", "🐹", "🐰", "🦊", "🐻", "🐼", "🦁", "🐯",
    "🐸", "🐵", "🐔", "🦄", "🦋", "🐝", "🐞", "🦕", "🌵", "🌲",
    "🌸", "🌹", "🌻", "🌼", "🌷", "🌊", "☀️", "🌤", "🌧", "⛈",
    "🍏", "🍎", "🍐", "🍊", "🍋", "🍌", "🍉", "🍇", "🍓", "🥥",
    "🍍", "🥭", "🍑", "🍒", "🍕", "🍔", "🍟", "🌭", "🍿", "🍰",
    "🍺", "🍷", "🍵", "☕", "🥤", "🍫", "🍩", "🍪", "🍭", "🍦",
    "🎉", "🎊", "🎁", "🎈", "🎀", "💎", "🔔", "🎵", "🎶", "🎧",
    "🖥", "📱", "💻", "⌚", "📸", "🎮", "🖊", "📝", "📅", "📚",
    "❤️", "💛", "💚", "💙", "💜", "🖤", "🤍", "🤎", "💔", "❣️",
    "👍", "👎", "👌", "✌️", "🤟", "👏", "🙌", "🙏", "🤝", "💪"
]
list_all = []
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
status_cha = tk.IntVar(value=1)
cha_check = tk.Checkbutton (root, text = 'Include lowercase letters', variable = status_cha)
cha_check.place (x = 50, y = 50)
status_upcha = tk.IntVar(value=1)
upcha_check = tk.Checkbutton (root, text = 'Include upper letters', variable = status_upcha)
upcha_check.place (x = 50, y = 70)
status_num = tk.IntVar(value=1)
num_check = tk.Checkbutton (root, text = 'Include numbers', variable = status_num)
num_check.place (x = 50, y = 90)
status_sc = tk.IntVar(value=1)
sc_check = tk.Checkbutton (root, text = 'Include special characters', variable = status_sc)
sc_check.place (x = 50, y = 110)
status_emo = tk.IntVar(value=0)
emo_check = tk.Checkbutton (root, text = 'Include emoji', variable = status_emo)
emo_check.place (x = 50, y = 150)
def reset ():
    result.config (text = '')
    list_all.clear()
    def generate ():
        if status_cha.get() == 1:
            list_all.append(letters)
        if status_upcha.get() == 1:
            list_all.append(letters_upper)
        if status_num.get() == 1:
            list_all.append(num)
        if status_sc.get() == 1:
            list_all.append(sc)       
        if status_emo.get() == 1:
            list_all.append(emoji)
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
button = tk.Button (root, text = 'Generate Password', command = reset)
button.place (x = 200, y = 250)
copy_button = tk.Button (root, text = 'Copy password', command = copy)
copy_button.place (x = 210, y = 300)
crazy_mode = tk.Label (root, text = 'Crazy Mode (Not recommended)')
crazy_mode.place (x = 50, y = 130)
root.mainloop()
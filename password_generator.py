import tkinter as tk
import random
import pyperclip
from tkinter import messagebox
import subprocess
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
hiragana = [
    ['あ', 'い', 'う', 'え', 'お'],  
    ['か', 'き', 'く', 'け', 'こ'], 
    ['さ', 'し', 'す', 'せ', 'そ'], 
    ['た', 'ち', 'つ', 'て', 'と'], 
    ['な', 'に', 'ぬ', 'ね', 'の'],  
    ['は', 'ひ', 'ふ', 'へ', 'ほ'],  
    ['ま', 'み', 'む', 'め', 'も'],  
    ['や', 'ゆ', 'よ'],  
    ['ら', 'り', 'る', 'れ', 'ろ'], 
    ['わ','を'],     
    ['ん']
]
katakana = [
    ['ア', 'イ', 'ウ', 'エ', 'オ'],  
    ['カ', 'キ', 'ク', 'ケ', 'コ'],  
    ['サ', 'シ', 'ス', 'セ', 'ソ'],  
    ['タ', 'チ', 'ツ', 'テ', 'ト'],  
    ['ナ', 'ニ', 'ヌ', 'ネ', 'ノ'],  
    ['ハ', 'ヒ', 'フ', 'ヘ', 'ホ'],  
    ['マ', 'ミ', 'ム', 'メ', 'モ'],  
    ['ヤ', 'ユ', 'ヨ'],      
    ['ラ', 'リ', 'ル', 'レ', 'ロ'],  
    ['ワ', 'ヲ'],       
    ['ン']                          
]
chinese = [
    '的', '一', '是', '了', '我', '不', '人', '在', '他', '有', 
    '这', '个', '上', '们', '中', '来', '大', '为', '和', '国', 
    '地', '到', '以', '说', '时', '要', '就', '出', '会', '可', 
    '也', '你', '对', '生', '能', '而', '子', '那', '得', '于', 
    '着', '下', '自', '之', '年', '过', '发', '后', '作', '里'
]

list_all = []
root = tk.Tk()
root.title ('Password CrazyGenerator')
icon = tk.PhotoImage(file="icon.png")
root.iconphoto(True, icon)
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
status_hira = tk.IntVar(value=0)
hira_check = tk.Checkbutton (root, text = 'Include Japanese Characters (Hiragana)', variable = status_hira)
hira_check.place (x = 50, y = 170)
status_kata = tk.IntVar(value=0)
ka_check = tk.Checkbutton (root, text = 'Include Japanese Characters (Katakana)', variable = status_kata)
ka_check.place (x = 50, y = 190)
status_chinese = tk.IntVar(value=0)
chinese_check = tk.Checkbutton (root, text = 'Include Chinese Characters', variable = status_chinese)
chinese_check.place (x = 50, y = 210)
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
        if status_hira.get() == 1:
            list_all.append(hiragana)  
        if status_kata.get() == 1:
            list_all.append(katakana)
        if status_chinese.get() == 1:
            list_all.append(chinese)             
        if num_cha.get() == "":
            messagebox.showerror("Error", "Type your number of characters you want in password")
        if status_cha.get() == 0 and status_upcha.get() == 0 and status_num.get() == 0 and status_sc.get() == 0 and status_emo.get() == 0 and status_hira.get() == 0 and status_kata.get() == 0 and status_chinese.get() == 0:
            messagebox.showerror("Error", "Choose your selection, you don't choose any option")
        result_now = result.cget ("text")
        limit = int(num_cha.get ())
        if len(result_now) < limit:
            random_list = random.choice (list_all)
            random_cha = random.choice (random_list)
            if isinstance(random_cha, list):
             random_cha = random.choice(random_cha)
            result.config (text = result_now + random_cha)
            root.after (50, generate)
    generate()
def copy ():
    copy = result.cget ("text")
    if result.cget ("text") == "":
        messagebox.showerror("Error", "Nothing to copy, type the number of characters then click the Generate Button")
    else:
        pyperclip.copy (copy)
    def check_pip():
        try:
            result = subprocess.run(["pip", "--version"], capture_output=True, text=True)
            if result.returncode == 1:
                messagebox.showerror("Error", "Pip is not found, Password Generator need pip to copy")
        except FileNotFoundError:
                messagebox.showerror("Error", "Pip is not found, Password Generator need pip to copy")
    check_pip()
button = tk.Button (root, text = 'Generate Password', command = reset)
button.place (x = 200, y = 250)
copy_button = tk.Button (root, text = 'Copy password', command = copy)
copy_button.place (x = 210, y = 300)
crazy_mode = tk.Label (root, text = 'Crazy Mode (Not recommended)')
crazy_mode.place (x = 50, y = 130)
root.mainloop()
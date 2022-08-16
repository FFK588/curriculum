#! /usr/bin/env python3
import sys
import codecs
import json
import cgi

sys.stdout = codecs.getwriter('utf_8')(sys.stdout.detach())

# ------------- JSONファイルの読み込み  -------------
try:
    with open('chat.txt', 'r') as file:
        chat = json.load(file)
except ValueError:
    chat = []

# ------------- フォームの読み込み  -------------
form  = cgi.FieldStorage()
image = form.getfirst('image')
text  = form.getfirst('text')

# ------------- JSONファイルの保存  -------------
if image and text:
    chat.append({'image': image, 'text': text})
    with open('chat.txt', 'w') as file:
        json.dump(chat, file, indent=4)

print('''
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <title>Python Web Programing</title>
</head>
<body>
    <h2>Pythonチャット</h2>
    <form action="chat.py" method="post">
        <select name="image">
            <option value="python_icon">Python</option>
            <option value="html_icon">HTML</option>
        </select>
        <input type="text" name="text">
        <input type="submit" value="発信">
    </form>
    <hr>
''')

for line in chat:
    print('<p><img src="/{0}.png" alt="image" width="100">{1}</p>'.format(line['image'], line['text']))

print('''
</body>
</html>
''')

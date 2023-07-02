
'''
Name: 
Data: YYYY-MM-DD HH:mm:ss
Input: 
'''
# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。
# coding=utf-8
import os
import requests
from bs4 import BeautifulSoup

def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。
    # 定义要遍历的文件夹路径和HTML文件路径
    folder_path = 'VIDEO\\DS-ISE-CIVIL_ENGINEERING'
    html_file_path = 'index.html'

    # 定义要遍历的文件夹路径和HTML文件路径
      # 创建一个新的HTML文档
    new_html = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <title>XUS-SHARE</title>
    <style>
    body {
    font-family: Arial, sans-serif;
    background-color: #f0f0f0;
    }
    h1 {
    font-size: 24px;
    text-align: center;
    color: #333;
    }
    p {
    font-size: 16px;
    text-align: justify;
    line-height: 1.5;
    }
    </style>
    </head>
    <body>
    <h1>XUS-SHARE</h1>
    <h2>Please click to download the required file.</h2>
    <p>这是一个使用Python和BeautifulSoup创建的HTML页面。</p >

    </body>
    </html>
    '''


    # 打开HTML文件以写入模式
    with open(html_file_path, 'w',encoding='utf-8') as html_file:
        html_file.write(new_html)
        # 遍历文件夹中的所有文件
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            html_file.write('<a href="' + file_path + '"' + ' download=' + '"' +filename + '"' + '>' +  filename + '</a><br/>\n')




def create_html(name):

    # 获取网页内容
    url = 'https://www.example.com'
    response = requests.get(url)
    html_content = response.text

    # 使用BeautifulSoup解析HTML内容
    soup = BeautifulSoup(html_content, 'html.parser')

    # 创建一个新的HTML文档
    new_html = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <title>XUS-SHARE</title>
    <style>
    body {
    font-family: Arial, sans-serif;
    background-color: #f0f0f0;
    }
    h1 {
    font-size: 24px;
    text-align: center;
    color: #333;
    }
    p {
    font-size: 16px;
    text-align: justify;
    line-height: 1.5;
    }
    </style>
    </head>
    <body>
    <h1>Welcome to my file sharing, please click to download the required file.</h1>
    <p>这是一个使用Python和BeautifulSoup创建的HTML页面。</p >
    </body>
    </html>
    '''

    # 将新的HTML内容写入文件中
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_html)


if __name__ == '__main__':
    print_hi('PyCharm')
    # create_html('hello,html')

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助

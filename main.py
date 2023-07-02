
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

def print_hi(name,folder_path,html_file_path):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。
    # 定义要遍历的文件夹路径和HTML文件路径
    # folder_path = 'VIDEO\\CIVIL_ENGINEERING'
    # html_file_path = 'video.html'

  
    # 打开HTML文件以写入模式
    with open(html_file_path, 'w',encoding='utf-8') as html_file:
        # html_file.write(new_html)
        # 遍历文件夹中的所有文件
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            html_file.write('<a href="' + file_path + '"' + ' download=' + '"' +filename + '"' + '>' +  filename + '</a><br/>\n')
            html_file.write('<video controls width ="320" height ="240" > <source src="' + file_path + '" type="video/mp4"></video><br/>\n')



def create_index_html(name):

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
    <h1>AEC VIDEO SHARING PLATFORM</h1>
    <p> Civil Engineering, Building Designer , Visual Scripting </p >
    
    <iframe width ="500" height ="800"  src="civil.html"></iframe>
    <iframe width ="500" height ="800"  src="building.html"></iframe>
    <iframe width ="500" height ="800"  src="GGR.html"></iframe>

    </body>
    </html>
    '''

    # 将新的HTML内容写入文件中
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_html)

if __name__ == '__main__':
    create_index_html('hello,index_html')
    print_hi('civil','VIDEO\\CIVIL_ENGINEERING','civil.html')
    print_hi('building','VIDEO\\CREATIVE_BUILDING','building.html')
    print_hi('GGR','VIDEO\\VISUAL_SCRIPTING','GGR.html')

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助

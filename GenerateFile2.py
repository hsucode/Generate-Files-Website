
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

import os

import os

def traverse_folder(path):
    file_list = []
    for root, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            file_list.append(file_path)
            for dir in dirs:
                dir_path = os.path.join(root, dir)
                traverse_folder(dir_path) # 递归遍历子目录
                return file_list

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
    <p> Civil Engineering, Building Designer , Visual Scripting </p>
    <p> This page is automatically generated, if you find a problem, can not download, please contact song.hsu@outlook.com </p>
    <iframe width ="500" height ="800"  src="civil.html"></iframe>
    <iframe width ="500" height ="800"  src="building.html"></iframe>
    <iframe width ="500" height ="800"  src="GGR.html"></iframe>
    <iframe width ="500" height ="800"  src="story.html"></iframe>
    <iframe width ="500" height ="800"  src="Partner_Work.html"></iframe>


    </body>
    </html>
    '''

    # 将新的HTML内容写入文件中
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_html)



def bianli(html_file_path,folder_path):
    # 打开HTML文件以写入模式
    with open(html_file_path, 'w',encoding='utf-8') as html_file:
        # html_file.write(new_html)
        html_file.write('<h3>' + folder_path + '</h3>')
        path = folder_path  # 替换为你的文件夹路径
        all_files = traverse_folder(path)
        for file in all_files:
            file_path = file
            filename= os.path.basename(file)
            print("name:" + file_path)

            if filename.endswith('.mp4') or filename.endswith('.mkv') or filename.endswith('.wmv') or filename.endswith('.avi'):         
                html_file.write('<a href="' + file_path + '"' + ' download=' + '"' +filename + '"' + '>' +  filename + '</a><br/>\n')
                html_file.write('<video controls width ="320" height ="240" > <source src="' + file_path + '"></video><br/>\n')
            else:
                html_file.write('<a href="' + file_path + '"' + ' download=' + '"' +filename + '"' + '>' +  filename + '</a><br/>\n')


if __name__ == '__main__':
    # create_index_html('hello,index_html')
    # print_hi('civil','VIDEO\\CIVIL_ENGINEERING','civil.html')
    # print_hi('building','VIDEO\\CREATIVE_BUILDING','building.html')
    # print_hi('GGR','VIDEO\\VISUAL_SCRIPTING','GGR.html')
    # print_hi('story','VIDEO\\CUSTOMER_STORY','story.html')
    # print_hi('Partner_Work','DASSAULT_SYSTEMES_Partner_Work','Partner_Work.html')
   
    bianli('Partner_Work.html','DASSAULT_SYSTEMES_Partner_Work')
    bianli('civil.html','VIDEO')


        
#
# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助

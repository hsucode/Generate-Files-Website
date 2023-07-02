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

def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。
    # 定义要遍历的文件夹路径和HTML文件路径
    folder_path = 'D:\\github\\gene-website\\RHINO-evolute'
    html_file_path = 'your_html_file_path.html'

    # 定义要遍历的文件夹路径和HTML文件路径

    # 打开HTML文件以写入模式
    with open(html_file_path, 'w') as html_file:
        # 遍历文件夹中的所有文件
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            html_file.write('<a href="' + file_path + '"' + ' download=' + '"' +filename + '"' + '>' +  filename + '</a><br/>\n')


if __name__ == '__main__':
    print_hi('PyCharm')

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助

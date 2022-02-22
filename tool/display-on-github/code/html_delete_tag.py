import re

express = r'<div style="-aw-headerfooter-type:.*?clear:\bboth">.*?</div>'


def get_html_content(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        content = f.read()
    return content


def get_html_content_list(file_name):
    content = get_html_content(file_name)
    content_list = re.findall(express, content)
    return content_list

def sub_content(content):
    return re.sub(express, '', content)

def main(file_name_full):
    content = get_html_content(file_name_full)
    filter_content = sub_content(content)
    with open(file_name_full, 'w', encoding='utf-8') as f:
        f.write(filter_content)

if __name__ == '__main__':
    file_name = r'F:\Git_WorkSpace\MCU\MCU_C51\SCUT_Experiment2\RES\task\红外发射器课程设计任务书\.hui_pict\pict_word2svg\红外发射器课程设计任务书.html'
    content_list = get_html_content_list(file_name)
    print(content_list)
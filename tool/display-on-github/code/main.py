import ppt_main
import pdf_main
import word_main
import os
import hui_tool
from loguru import logger

file_type = {
    ".pdf": pdf_main.main,
    ".pptx": ppt_main.main,
    ".docx": word_main.main,
    ".doc": word_main.main
}


def check_supported_file(ext):
    if ext in file_type.keys():
        return True
    return False


def file_convert(file_name_full):
    ext = os.path.splitext(file_name_full)[1]
    if check_supported_file(ext):
        logger.info("start convert file %s" % file_name_full)
        file_type[ext](file_name_full, ext)
        logger.info("finish convert file %s" % file_name_full)
    else:
        print("Unsupported file type: %s" % ext)


def test_main():
    # test_file = r"F:\Git_WorkSpace\02notebook\notebook-easy\tool\pdfshow\code\烟雾传感器-MQ_2.pdf"
    # test_file = r"F:\Git_WorkSpace\02notebook\notebook-easy\tool\pptxshow\code\2022.pptx"
    # test_file = r"F:\Git_WorkSpace\02notebook\notebook-easy\tool\word\Document.docx"
    # test_file = r"F:\Git_WorkSpace\02notebook\notebook-easy\tool\word\红外发射器课程设计任务书.doc"
    # file_convert(test_file)
    pass


def main(workspace_path):
    file_name_list = hui_tool.get_file_all(workspace_path)
    for file_name in file_name_list:
        ext = os.path.splitext(file_name)[1]
        if check_supported_file(ext):
            file_convert(file_name)


if __name__ == "__main__":
    # test_main()
    workpath = os.getcwd()
    # workpath = r"F:\Git_WorkSpace\scut\SCUT_3_Forming-Technology-Basics\RES"
    main(workpath)
    print("Done!")

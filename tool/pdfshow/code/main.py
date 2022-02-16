import os
import tool
import hui_readme

pdf2svg_command = "pdf2svg %s --embedimages -o %s"
pdf2svg_folder_name = ".pict_pdf2svg"


def convert_pdf2svg(pdf_file_name, svg_folder_name):
    """
    Convert pdf file to svg file.
    """
    os.system(pdf2svg_command % (pdf_file_name, svg_folder_name))


def deal_work_file(workspace_path, pdf_file_name):
    """
    Deal with the work file.
    """
    temp_pict_folder_name = os.path.join(workspace_path, pdf2svg_folder_name)
    if not tool.check_folder(temp_pict_folder_name):
        return False

    pdf_file_name = os.path.join(workspace_path, pdf_file_name)
    convert_pdf2svg(pdf_file_name, temp_pict_folder_name)

    if not hui_readme.create_readme(workspace_path):
        return False

    return True


def make_pdf2workfolder(workspace_path, pdf_file_name):
    """
    Make a folder for pdf2svg.
    """
    pdf_file_name_without_extension = os.path.splitext(pdf_file_name)[0]
    next_workspace_path = os.path.join(workspace_path,
                                       pdf_file_name_without_extension)
    if not tool.check_folder(next_workspace_path):
        return False
    tool.move_pdf(workspace_path, pdf_file_name, next_workspace_path)
    if not deal_work_file(next_workspace_path, pdf_file_name):
        return False
    return True


def main():
    workpath = os.getcwd()
    # workpath = r"F:\Git_WorkSpace\temp\PDFNetPython3\test"
    file_name_list = tool.get_all_file(workpath, ".pdf")
    if len(file_name_list) == 0:
        print("There is no pdf file in the current folder.")
        exit(0)
    for file_name_full in file_name_list:
        file_name = os.path.basename(file_name_full)
        if make_pdf2workfolder(workpath, file_name):
            # 等一切成功后，再删除源文件
            tool.delete_file(file_name_full)  # Delete the original pdf file.
        else:
            print("Error: %s" % file_name)


def test():
    hui_readme.create_readme(r"F:\Git_WorkSpace\temp\PDFNetPython3\test")


if __name__ == "__main__":
    main()
    # test()
import os

pdf2svg_command = "pdf2svg %s --embedimages --digits 5 -o %s"


def convert_pdf2svg(pdf_file_name, svg_folder_name):
    """
    Convert pdf file to svg file.
    """
    os.system(pdf2svg_command % (pdf_file_name, svg_folder_name))

    return True


def convert(pdf_file_name, svg_folder_name):
    """
    Convert pdf file to svg file.
    """
    return convert_pdf2svg(pdf_file_name, svg_folder_name)

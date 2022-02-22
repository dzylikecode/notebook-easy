import ppt_convert
import hui_tool
import file_frame
import readme_template
import os


class ppt:
    def __init__(self, ext):
        self.pict_folder_name = "pict_ppt2svg"
        self.file_type = ext
        self.relative_path = file_frame.get_relative_path(
            self.pict_folder_name)

    def convert(self, src_file_full, dst_folder_full):
        return ppt_convert.convert(src_file_full, dst_folder_full)

    def create_readme(self, f, store_folder_full):
        file_name_list = hui_tool.get_all_file(store_folder_full, ".svg")
        for i in range(0, len(file_name_list)):
            file_name = os.path.basename(file_name_list[i])
            readme_template.write_svg(i + 1, self.relative_path, file_name, f)


def main(file_name_full, ext):
    file_obj = ppt(ext)
    file_frame.main(file_name_full, file_obj)

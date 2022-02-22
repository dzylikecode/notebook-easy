import hui_tool
import os
from loguru import logger

hide_folder_name = '.hui_pict'


def get_relative_path(file_name):
    """get the relative path of the file"""
    return '%s/%s' % (hide_folder_name, file_name)


def check_converted(workspace_path):
    """check whether the file is converted"""
    # 检查是否已经转换
    flag_file = os.path.join(workspace_path, hide_folder_name, 'README.md')
    if not hui_tool.is_file_exist(flag_file):
        return False
    return True


def flag_converted(workspace_path):
    """flag the file is converted"""
    # 标记已经转换
    flag_file = os.path.join(workspace_path, hide_folder_name, 'README.md')
    hui_tool.check_file(flag_file)


def create_workspace(workspace_path, file_name):
    """create a folder wordspace according to file"""
    file_name_without_extension = os.path.splitext(file_name)[0]
    next_workspace_path = os.path.join(workspace_path,
                                       file_name_without_extension)
    # 创建同名文件夹
    if not hui_tool.check_folder(next_workspace_path):
        next_workspace_path = ''
    # 将文件移动到新文件夹
    if next_workspace_path != '':
        res = hui_tool.copy_file(next_workspace_path, workspace_path,
                                 file_name)
        if not res:
            next_workspace_path = ''
    return next_workspace_path


class work_in_workspace:
    def __init__(self, file_obj):
        self.file_obj = file_obj
        self.store_folder_full = ''

    def main(self, workspace_path, file_name):
        """work in workspace"""
        # 创建 隐藏文件
        hide_folder_name_full = os.path.join(workspace_path, hide_folder_name)
        if not hui_tool.check_folder(hide_folder_name_full):
            return False
        # 调用转化函数, 并且写好readme
        if self.__convert(workspace_path,
                          file_name) and self.__create_readme(workspace_path):
            # 成功后, 标记已经转换
            flag_converted(workspace_path)
            return True
        return False

    def __convert(self, workspace_path, file_name):

        # 创建转化的文件夹
        store_folder_full = os.path.join(workspace_path, hide_folder_name,
                                         self.file_obj.pict_folder_name)
        if not hui_tool.check_folder(store_folder_full):
            return False
        # 调用转化函数
        src_file_full = os.path.join(workspace_path, file_name)
        dst_folder_full = store_folder_full
        if not self.file_obj.convert(src_file_full, dst_folder_full):
            logger.error('%s convert failed' % file_name)
            return False
        self.store_folder_full = store_folder_full
        return True

    def __create_readme(self, workspace_path):
        readme_name = 'README.md'
        readme_full = os.path.join(workspace_path, readme_name)
        if not hui_tool.check_file(readme_full):
            return False
        # 写入readme
        with open(readme_full, 'w', encoding='utf-8') as f:
            self.file_obj.create_readme(f, self.store_folder_full)
        return True


def main(file_name_full, file_obj):
    workspace_path = os.path.split(file_name_full)[0]
    file_name = os.path.split(file_name_full)[1]
    if not check_converted(workspace_path):
        next_workspace_path = create_workspace(workspace_path, file_name)
        res = False
        if next_workspace_path != '':
            obj = work_in_workspace(file_obj)
            res = obj.main(next_workspace_path, file_name)
        else:
            logger.error('file %s create workspace failed!' % file_name_full)
            return False
        if res:
            logger.success("file %s convert successfully!" % file_name_full)
            hui_tool.delete_file(file_name_full)
    else:
        logger.warning('file %s has been converted' % file_name_full)
        return False
    return True

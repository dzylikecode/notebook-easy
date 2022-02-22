import os
import shutil
from loguru import logger


def check_file_folder_template(name, check_func, create_func):
    """
    Check if the folder exists.
    """
    if not check_func(name):
        create_func(name)
        return True
    else:
        logger.warning("The folder %s already exists." % name)
        res = "q"
        while res != "y" and res != "n":
            res = input("Do you want to delete it? (y/n)")
            if res == "y":
                os.system("rm -rf %s" % name)
                create_func(name)
                return True
            elif res == "n":
                logger.info("Please check the folder name.")
                return False


def is_file_exist(file_name):
    """
    Check whether the file exists.
    """
    if os.path.isfile(file_name):
        return True
    else:
        return False


def check_file(file_name):
    def create_file_func(file_name):
        f = open(file_name, "w")
        f.close()

    return check_file_folder_template(file_name, is_file_exist,
                                      create_file_func)


def check_folder(folder_name):
    def check_folder_func(folder_name):
        if os.path.exists(folder_name):
            return True
        else:
            return False

    def create_folder_func(folder_name):
        os.mkdir(folder_name)

    return check_file_folder_template(folder_name, check_folder_func,
                                      create_folder_func)


def copy_file(dst_folder, src_folder, file_name):
    """
    copy file to dest folder.
    """
    src_file_path = os.path.join(src_folder, file_name)
    dst_file_path = os.path.join(dst_folder, file_name)
    if shutil.copy(src_file_path, dst_file_path):
        logger.success("Copy %s to %s successfully." %
                       (src_file_path, dst_file_path))
        return True
    else:
        logger.error("The folder %s does not exist." % src_file_path)
        return False


def delete_file(file_name):
    """
    Delete the file.
    """
    if os.path.isfile(file_name):
        os.remove(file_name)
    else:
        logger.warning("The file %s does not exist." % file_name)
        return False
    return True


def move_file(dst_folder, src_folder, file_name):
    """
    move file to dest folder.
    """
    src_file_path = os.path.join(src_folder, file_name)
    dst_file_path = os.path.join(dst_folder, file_name)
    if shutil.move(src_file_path, dst_file_path):
        logger.success("Move %s to %s successfully." %
                       (src_file_path, dst_file_path))
        return True
    else:
        logger.error("The folder %s does not exist." % src_file_path)
        return False


def get_all_file(path, file_type):
    """
    Get all files in the folder.
    """
    file_list = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(file_type):
                file_list.append(os.path.join(root, file))
    return file_list


def get_file_all(path):
    """
    Get all files in the folder.
    """
    file_list = []
    for root, dirs, files in os.walk(path):
        for file in files:
            file_list.append(os.path.join(root, file))
    return file_list

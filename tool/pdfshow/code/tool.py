import os
import shutil


def check_folder(folder_name):
    """
    Check if the folder exists.
    """
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
        return True
    else:
        print("The folder %s already exists." % folder_name)
        res = "q"
        while res != "y" and res != "n":
            res = input("Do you want to delete it? (y/n)")
            if res == "y":
                os.system("rm -rf %s" % folder_name)
                os.mkdir(folder_name)
                return True
            elif res == "n":
                print("Please check the folder name.")
                return False


def check_file(folder_name):
    """
    Check if the folder exists.
    """
    if not os.path.exists(folder_name):
        f = open(folder_name, "w")
        f.close()
        return True
    else:
        print("The folder %s already exists." % folder_name)
        res = "q"
        while res != "y" and res != "n":
            res = input("Do you want to delete it? (y/n)")
            if res == "y":
                os.system("rm -rf %s" % folder_name)
                f = open(folder_name, "w")
                f.close()
                return True
            elif res == "n":
                print("Please check the folder name.")
                return False


def move_pdf(workspace_path, pdf_file_name, next_workspace_path):
    """
    Move pdf file to workspace.
    """
    pdf_file_name_abs = os.path.join(workspace_path, pdf_file_name)
    pdf_file_name_abs_next = os.path.join(next_workspace_path, pdf_file_name)
    if shutil.copy(pdf_file_name_abs, pdf_file_name_abs_next):
        print("Move %s to %s successfully." %
              (pdf_file_name, next_workspace_path))
    else:
        print("Move %s to %s failed." % (pdf_file_name, next_workspace_path))
        exit(1)


def delete_file(file_path):
    """
    Delete the file.
    """
    if os.path.isfile(file_path):
        os.remove(file_path)
    else:
        print("The file %s does not exist." % file_path)
        exit(1)


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
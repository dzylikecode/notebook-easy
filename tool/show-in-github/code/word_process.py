# pip install Pillow
from PIL import Image
import os
import hui_tool
import shutil

exe_path = os.path.dirname(os.path.realpath(__file__))
flag_pict_path = os.path.join(exe_path, 'src_pict')
flag_pict_full = os.path.join(flag_pict_path, 'flag.png')


def img_equal(src, dst):
    with Image.open(src) as img1:
        with Image.open(dst) as img2:
            if img1.size != img2.size:
                return False
            return img1.histogram() == img2.histogram()


times_count = 0


def img_equal_ex(src, dst):
    global times_count
    if times_count < 2:
        times_count += 1
        return True
    return False


def transparent_color(color):
    color = color[:-1] + (0, )
    return color


def transparent_img(img):
    img = img.convert('RGBA')
    width, height = img.size
    for y in range(height):
        for x in range(width):
            pos = (x, y)
            cur_color = img.getpixel(pos)
            trans_color = transparent_color(cur_color)
            img.putpixel(pos, trans_color)
    return img


def trans_flag_file(temp_file):
    with Image.open(flag_pict_full) as img_flag:
        img_temp = transparent_img(img_flag)
        img_temp.save(temp_file)


def create_img(file_name_full):
    image = Image.new(mode='RGBA', size=(624, 339))
    image.save(file_name_full)


def get_temp_file():
    temp_file = os.path.join(flag_pict_path, 'temp.png')
    if hui_tool.is_file_exist(temp_file):
        return temp_file
    else:
        create_img(temp_file)
    return temp_file


def replace_file(file_name_full):
    temp_file = get_temp_file()
    hui_tool.delete_file(file_name_full)
    shutil.copy(temp_file, file_name_full)


def check_replace_file(file_name_full):
    temp_name = get_temp_file()
    if img_equal_ex(file_name_full, temp_name):
        replace_file(file_name_full)


def main(folder):
    png_list = hui_tool.get_all_file(folder, '.png')
    for png_file in png_list:
        check_replace_file(png_file)


def transparent_png(imgfile, out="out"):
    with Image.open(imgfile) as img:
        img = img.convert('RGBA')
        W, H = img.size
        white_pixel = (255, 255, 255, 255)
        for h in range(W):  ###循环图片的每个像素点
            for l in range(H):
                if img.getpixel((h, l)) == white_pixel:
                    img.putpixel((h, l), (0, 0, 0, 0))
                img.save(out + ".png")


if __name__ == '__main__':
    # get_temp_file()
    # transparent_png(r'flag.png')
    create_img(r'temp.png')
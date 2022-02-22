from loguru import logger
import os

comment = """
<!-- auto created by notebook_easy -->
 """

svg_format = """
<span id="%05d">
<img src="%s/%s">
</span>
"""

html_preview = "http://htmlpreview.github.io/"

html_format = """
[%s](%s%s)
"""
username = ""
project_name = ""
branch_name = "main"
html_address_format = "https://github.com/{0}/{1}/tree/{2}/%s/%s".format(
    username, project_name, branch_name)


def write_svg(id, relative_path, svg_name, file):
    file.write(svg_format % (id, relative_path, svg_name))


def write_html(id, relative_path, file_name, file):
    html_address = html_address_format % (relative_path, file_name)
    file_name_no_ext = os.path.splitext(file_name)[0]
    file.write(html_format % (file_name_no_ext, html_preview, html_address))
    logger.warning("file %s need to add link" % file_name)

import tool
import os

comment = """
<div style="display:none">
created by laDzy
pdfshow:0.0.1
</div>\n
 """

content_format = """
<span id="%d">
<img src=".pict_pdf2svg/%s">
</span>
"""


def write_main_content(workspace_path, file):
    svg_list = tool.get_all_file(workspace_path, ".svg")
    for i in range(0, len(svg_list)):
        svg_name = os.path.basename(svg_list[i])
        file.write(content_format % (i + 1, svg_name))


def create_readme(workspace_path):
    """
    Create README.md file.
    """
    readme_file_name = "README.md"
    readme_file_path = os.path.join(workspace_path, readme_file_name)
    if not tool.check_file(readme_file_path):
        return False

    with open(readme_file_path, "w", encoding="utf-8") as f:
        f.write(comment)
        write_main_content(workspace_path, f)
    return True
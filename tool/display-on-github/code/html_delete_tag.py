import hui_tool

html_express = r'<div style="-aw-headerfooter-type:.*?clear:\bboth">.*?</div>'

svg_express = r'<tspan x="[-+]?[0-9]*\.?[0-9]+" y="[-+]?[0-9]*\.?[0-9]+" textLength="[-+]?[0-9]*\.?[0-9]+" id="tp_[0-9]\d*.*?>.*?</tspan>'


def sub_file_express(file_name, express):
    content = hui_tool.get_file_content(file_name)
    filter_content = hui_tool.sub_content(content, express)
    hui_tool.write_file_content(file_name, filter_content)


def sub_file_html_express(file_name):
    sub_file_express(file_name, html_express)


def sub_file_svg_express(file_name):
    sub_file_express(file_name, svg_express)

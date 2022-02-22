import aspose.slides as slides
import os

svg_name_format = "%s_%05d.svg"


def convert_pptx2svg(pptx_file_name, svg_folder_name):
    """
    Convert pptx file to svg file.
    """
    # Load the presentation
    file_name = os.path.basename(pptx_file_name)
    pptx_file_name_without_extension = os.path.splitext(file_name)[0]
    with slides.Presentation(pptx_file_name) as presentation:
        # Loop through the slides
        for slide in presentation.slides:
            # Export slides to SVG format
            svg_file_name = svg_name_format % (
                pptx_file_name_without_extension, slide.slide_number)
            svg_file_name_full = os.path.join(svg_folder_name, svg_file_name)
            with open(svg_file_name_full, "wb") as file:
                slide.write_as_svg(file)

    return True


def convert(pptx_file_name, svg_folder_name):
    """
    Convert pptx file to svg file.
    """
    return convert_pptx2svg(pptx_file_name, svg_folder_name)

import aspose.words as aw
import os
import word_process


def convert_word2html(word_file_name, html_folder_name):
    """
    Convert word file to html file.
    """
    file_name = os.path.basename(word_file_name)
    word_file_name_without_extension = os.path.splitext(file_name)[0]
    # Load the document from disk
    doc = aw.Document(word_file_name)
    # Enable export of fonts
    options = aw.saving.HtmlSaveOptions()
    options.export_font_resources = True

    html_file_name = word_file_name_without_extension + ".html"
    html_file_name_full = os.path.join(html_folder_name, html_file_name)

    # Save the document as HTML
    doc.save(html_file_name_full, options)

    word_process.main(html_folder_name)

    return True


def convert(word_file_name, html_folder_name):
    """
    Convert word file to html file.
    """
    return convert_word2html(word_file_name, html_folder_name)

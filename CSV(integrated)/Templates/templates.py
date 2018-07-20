import os

def get_template_path(path):
    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), path)
    if not os.path.isfile(file_path):
        raise Exception("There is no file {path_dir}".format(path_dir=path))
    return file_path


def get_template(path):
    template_path = get_template_path(path)
    return open(template_path).read()


def render_template(template, context):
    return template.format(**context)


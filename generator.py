import time
import os
import jinja2
from pylatex import Document, NoEscape


latex_jinja_env = jinja2.Environment(
    block_start_string='\BLOCK{',
    block_end_string='}',
    variable_start_string='\VAR{',
    variable_end_string='}',
    comment_start_string='\#{',
    comment_end_string='}',
    line_statement_prefix='%%',
    line_comment_prefix='%#',
    trim_blocks=True,
    autoescape=False,
    loader=jinja2.FileSystemLoader(os.path.abspath('.'))
)


def generate(vars_dict):
    timestamp = str(time.time())
    tmp_path = ''.join(['tmp/', timestamp])
    data = render(vars_dict, latex_jinja_env)
    document = Document(default_filepath=tmp_path, data=NoEscape(data))
    document.generate_pdf()


def render(vars_dict, latex_jinja_env):
    template = latex_jinja_env.get_template('template.j2')
    return template.render(vars_dict)


if __name__ == '__main__':
    dict = {
        'first_name': 'Etienne',
        'last_name': 'Soucy',
        'schools': [
            {
                'name': 'École Polytechnique de Montréal',
                'start_year': '2009',
                'end_year': '2011'
            },
            {
                'name': 'Université de Montréal',
                'start_year': '2011',
                'end_year': '2012'
            }
        ]
    }
    generate(dict)

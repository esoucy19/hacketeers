import time
import os
import jinja2


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


def generate(vars_dict, latex_jinja_env):
    timestamp = str(time.time())
    data = render(vars_dict, latex_jinja_env)
    pwd = os.path.abspath('.')
    print(pwd)
    tmpdir = ''.join([
        'tmp/',
        timestamp
    ])
    print(tmpdir)
    tmptex = ''.join([
        tmpdir,
        '/template.tex'
    ])
    command = ''.join([
        'latexmk --pdf --interaction=nonstopmode -outdir=',
        tmpdir,
        ' ',
        tmpdir,
        '/template.tex'
    ])
    dir = ''.join([pwd, '/', tmpdir])
    print(dir)
    if not os.path.exists(dir):
        os.makedirs(dir)
    with open(tmptex, 'w') as tmp_file:
        tmp_file.write(data)
    os.system(command)


def render(vars_dict, latex_jinja_env):
    template = latex_jinja_env.get_template('template.tex')
    return template.render(vars_dict)


if __name__ == '__main__':
    dict = {
        'first_name': 'Etienne',
        'last_name': 'Soucy',
        'address_line_1': '1050 Amesbury #930',
        'address_line_2': 'Montreal, Canada, H9J 1G6',
        'phone_number': '514-690-3373',
        'email': 'monagz@gmail.com',
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
    generate(dict, latex_jinja_env)

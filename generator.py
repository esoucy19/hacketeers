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


def generate(vars_dict, latex_jinja_env=latex_jinja_env):
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
    return ''.join([dir, '/template.pdf'])


def render(vars_dict, latex_jinja_env):
    template = latex_jinja_env.get_template('template.tex')
    return template.render(vars_dict)


if __name__ == '__main__':
    dict = {
        'first_name': 'Etienne',
        'last_name': 'Soucy',
        'address_line_1': '1050 Amesbury apt. 930',
        'address_line_2': 'Montreal, Canada, H9J 1G6',
        'phone_number': '514-690-3373',
        'email': 'test@mail.com',
        'schools': [
            {
                'name': 'École Polytechnique de Montréal',
                'start_year': '2009',
                'end_year': '2011',
                'degree': 'Masters',
                'department': 'Computer Science'
            }, {
                'name': 'Université de Montréal',
                'start_year': '2011',
                'end_year': '2012',
                'degree': 'Bachelor\'s',
                'department': 'Chemical Engineering'
            }
        ],
        'languages': [
            'French',
            'English'
        ],
        'technical_skills': [
            'Microsoft Office (Word, Excel, Outlook)',
            'Programming languages: Python, Java, Perl',
            'Databases: Mysql, Oracle'
        ],
        'jobs': [
            {
                'position': 'QA specialist',
                'start_date': '2017',
                'end_date': 'present',
                'institution': 'peerio',
                'tasks': [
                    'Wrote documentation',
                    'Pushed to dev',
                    'Tested all the code'
                ]
            }, {
                'position': 'IT support technician',
                'start_date': '2015',
                'end_date': '2017',
                'institution': 'LCPC Informatique',
                'tasks': [
                    'End user support',
                    'Troubleshooting',
                    'Assembly and installation of computer equipment'
                ]
            }
        ],
        'awards': [
            {
                'award': 'Meritas student prize',
                'date': '2017',
                'institution': 'McGill University'
            }, {
                'award': 'Examplary implication',
                'date': '2015',
                'institution': 'École Polytechnique de Montréal'
            }
        ],
        'volunteer_experiences': [
            {
                'date': '2012, 2013, 2014',
                'institution': 'Food Against Fascism',
                'role': 'Distributed food to guests'
            },
            {
                'date': '2015, 2016',
                'institution': 'People\'s Potato',
                'role': 'Cooking, plunger, cleaning'
            }
        ]
    }
    generate(dict, latex_jinja_env)

import pathlib
import os


def parse_directory_into_string(directory: pathlib.Path, indent=1):
    strings = []
    for file in directory.iterdir():
        if file.is_dir():
            result = parse_directory_into_string(file, indent+1)
            string = f'\u2570-- {file.name}/\n' + '|   ' * indent + f'{result}'
        else:
            string = f'\u2570-- {file.name}'
        strings.append(string)

    return '\n'.join(strings)


project_dir = pathlib.Path(os.path.dirname(__file__))
templates = project_dir / 'src' / 'templates'
templates_md = project_dir / 'doc' / 'source' / 'templates_.md'

sections = []
for t in templates.iterdir():
    if t.is_dir():
        title = f'## {t.name}'
        s = parse_directory_into_string(t)
        section = f'{title}\n\n```\n{s}\n```\n\n'
        sections.append(section)

doc = '\n'.join(sections)
with open(templates_md, 'w', encoding='utf-8') as f:
    f.write(doc)

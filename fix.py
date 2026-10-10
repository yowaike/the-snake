from pathlib import Path

p = Path('tests/conftest.py')
text = p.read_text(encoding='utf-8')

old = "            f'Убедитесь, что в модуле `the_snake` определен класс `{class_name}`.'"
new = (
    "            'Убедитесь, что в модуле `the_snake` определен '\n"
    "            f'класс `{class_name}`.'"
)

if old in text:
    p.write_text(text.replace(old, new), encoding='utf-8')
    print('Fixed')
else:
    print('Not found')

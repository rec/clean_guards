import sys


def clean_guards(lines, filename):
    while lines and not lines[0].strip():
        lines.pop(0)
    while lines and not lines[-1].strip():
        lines.pop()

    conditions = (lines[0].startswith('#ifndef'), lines[1].startswith('#define'),
                lines[-1].startswith('#endif'))
    if all(conditions):
        return ['#pragma once\n'] + lines[2:-1]

    print(filename, 'could not be cleaned!', conditions)


def read_clean_write(*files):
    for filename in files:
        lines = open(filename).readlines()
        lines = clean_guards(lines, filename)

        lines and open(filename, 'w').writelines(lines)


if __name__ == '__main__':
    read_clean_write(*sys.argv[1:])

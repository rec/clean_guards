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
    if not lines[0].startswith('#pragma'):
        print(filename, 'could not be cleaned!', conditions)


def read_clean_write(*files):
    count = 0
    for filename in files:
        lines = open(filename).readlines()
        lines = clean_guards(lines, filename)
        if lines:
            open(filename, 'w').writelines(lines)
            count += 1
    return count


if __name__ == '__main__':
    print(read_clean_write(*sys.argv[1:]), 'files cleaned')

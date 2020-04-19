from zipfile import ZipFile

INTERNAL_FILE = 'internal.txt'


def write_zipfile(filename, content):

    with ZipFile(filename, 'w') as zipfile:
        zipfile.writestr(INTERNAL_FILE, content)


def read_zipfile(filename):
    with ZipFile(filename, 'r') as zipfile:
        with zipfile.open(INTERNAL_FILE) as intfile:
            content = intfile.read()

    return content.decode('utf8')

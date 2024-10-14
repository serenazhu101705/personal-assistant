from module import file


f = file() if 'delete' not in ask else file(delete = True)
f.open_or_del()

from emaillistapp import model
# import sys
# import os
# try:
#     sys.path.append(os.getcwd())
# except ImportError:
#     raise ImportError('Import Fail')


def run_list():
    results = model.findall() # dict 형태임
    for index, result in enumerate(results):
        print(f'{index+1}:{result["first_name"]}{result["last_name"]}:{result["email"]}')


def run_add():
    firstname = input('first name: ')
    lastname = input('last name: ')
    email = input('email: ')

    model.insert(firstname, lastname, email)

    run_list()


def run_delete():
    email = input('email: ')
    model.deletebyemail(email)

    run_list()


def main():
    while True:
        cmd = input('(l)ist, (a)dd, (d)elete, (q)uit >')
        if cmd == 'q':
            break
        elif cmd == 'l':
            run_list()
        elif cmd == 'a':
            run_add()
        elif cmd == 'd':
            run_delete()


if __name__ == '__main__':
    main()

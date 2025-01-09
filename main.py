from auth import login, register, logout


def login_response():
    username = input('Username: ')
    password = input('Password: ')
    response = login(username, password)
    print(response.message)


def register_response():
    username = input('Username: ')
    password = input('Password: ')
    response = register(username, password)
    print(response.message)


def logout_response():
    response = logout()
    print(response.message)


def menu():
    print('1. Login')
    print('2. Register')
    print('3. Logout')
    print('q. Exit')
    return input('?: ')


def run():
    while True:
        choice = menu()
        if choice == '1':
            login_response()
        elif choice == '2':
            register_response()
        elif choice == '3':
            logout_response()
        elif choice == 'q':
            break


if __name__ == '__main__':
    run()

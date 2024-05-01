# Робота з файлами
# Написати програму для зберігання та керування списком покупок.
# Основна ідея полягає в тому, щоб програма зберігала дані про список продуктів та їх кількість у текстовому файлі.
# Кожен рядок в файлі містить інформацію про один продукт та його кількість у форматі "назва продукту, кількість".
# Після запуску програми користувач може додавати нові продукти до списку та їх кількість, переглядати список, редагувати наявну інформацію,
# видаляти продукти зі списку та зберігати зміни у файлі.
def view_shopping_list(file_path):
    pass

def edit_product(file_path):
    pass

def delete_product(file_path):
    pass

def add_product(file_path):
    pass

def main():
    while True:
        print("""
        1 - show
        2 - add
        3 - remove
        4 - edit
        5 - exit
        """)
        answer = input("What do you want to do?")
        if answer == "1":
            view_shopping_list("data.txt")
        if answer == "2":
            add_product("data.txt")
        if answer == "3":
            delete_product("data.txt")
        if answer == "4":
            edit_product("data.txt")
        if answer == "5":
            break

            
        
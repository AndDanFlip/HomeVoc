import os

os.system('cls')

in_key=input("Введите значение ключа(name или account):  ")
n_word='name'
a_word='account'
user1 = {'name':'Иван','age':20,'account':'account1'}
user2 = {'name':'Петр','age':25,'account':'account2'}
user3 = {'name':'Ольга','age':18,'account':'account3'}
user4 = {'name':'Анна','age':27,'account':'account4'}
user_list = [user1, user2, user3, user4]

account1 = {'login':'ivan', 'password':'q1'}
account2 = {'login':'petr', 'password':'q2'}
account3 = {'login':'olga', 'password':'q3'}
account4 = {'login':'anna', 'password':'q4'}
accounts = [account1, account2, account3, account3]

length_usr = len(user_list)
length_accs = len(accounts)

if in_key.lower()==n_word:
     print(f"Значение ключа name для юзера 1: {user_list[0]['name']}")
     print(f"Значение ключа name для юзера 2: {user_list[1]['name']}")
     print(f"Значение ключа name для юзера 3: {user_list[2]['name']}")
     print(f"Значение ключа name для юзера 4: {user_list[3]['name']}")
else: 
    if in_key.lower()==a_word:
     print(f"Значение ключа account для юзера 1: {user_list[0]['account']}")
     print(f"Значение ключа account для юзера 2: {user_list[1]['account']}")
     print(f"Значение ключа account для юзера 3: {user_list[2]['account']}")
     print(f"Значение ключа account для юзера 4: {user_list[3]['account']}")
    else:
         print("Введенный ключ не найден")

num=input("Введите порядковый номер:")
if int(num) > length_usr and int(num) > length_accs:
     print("Пользователь с указанным номером не найден")
else:     
    print("Данные по юзеру №" + str(num) + ":" )
    print(f"Имя:{user_list[int(num)-1]['name']}")
    print(f"Возраст:{user_list[int(num)-1]['age']}")
    print(f"Логин:{accounts[int(num)-1]['login']}")
    print(f"Пароль:{accounts[int(num)-1]['password']}")

inse=input("Введите номер пользователя, которого нужно переместить в конец: ")

print("Список до изменения: ", user_list)

print(f"Пользователь с именем {user_list[int(inse)-1]['name']} перемещен в конец.")

def swapPos(list, posX, posY):
     list[posX], list[posY] = list[posY], list[posX]
     return list

posX=int(length_usr)-1
posY=int(inse)-1 

print("Список после замены:", swapPos(user_list,posX,posY))


sum_age=sum(sub['age'] for sub in user_list)
average_age=sum_age/(int(length_usr))
print("Средний возраст всех юзеров:", average_age)
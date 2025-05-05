# Напишите программу, которая получает на вход строку чисел, разделенных пробелами, и формирует словарь,
#  в котором ключами служат числа, а значениями – слово "четное" или "нечетное".
my_dict={}
a = list(map(int,input().split()))
for i in a:
    if i%2==0:
        mydict = {i:"Четное"}
        my_dict.update(mydict)
    else:
        mydict = {i: "Нечетное"}
        my_dict.update(mydict)
print(my_dict)

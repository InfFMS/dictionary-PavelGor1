# Создайте программу-переводчик, которая хранит перевод
#  слов с русского языка на английский.
# После запуска программа выводит список слов в словаре
# и предлагает пользователю ввести слово для перевода.
# Если введенного слова нет в словаре выводится сообщение "нет такого слова".
# Используйте словари для словаря:)
word = input()
my_dict = {"Россия":'Russia',"люблю":"love","Паша":"Pasha"}
if word in my_dict:
    word = my_dict[word]
    print(word)
elif word not in my_dict:
    print("Введите слово с переводом, каждое слово отдельно")

new_word = input()
new_word2 = input()
if new_word not in my_dict:
    my_dict2 = {new_word:new_word2}
    my_dict.update(my_dict2)
    print("Слово добавлено")
print(my_dict)

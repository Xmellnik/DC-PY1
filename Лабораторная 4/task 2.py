def get_count_char(str_):  # первая функция
    letter_count = {}
    str_ = str_.lower()  # перевод строки в нижний регистр
    for i in range(len(str_)):
        if str_[i].isalpha():  # проверка на принадлежность символа к буквам
            if not letter_count.keys().__contains__(str_[i]):
                letter_count[str_[i]] = 0
            letter_count[str_[i]] += 1
    return letter_count  # возвращает словарь с частотой использования каждого символа

def new_dict_char(letter_count):  # вторая функция
    percent = {}
    total_count = 0
    letter_count_keys = letter_count.keys()
    for a in letter_count_keys:
        total_count += letter_count[a]
    for a in letter_count_keys:
        letter_count[a] = (letter_count[a] / total_count) * 100  # считаем процентное содержание каждого символа
    return percent  # возвращается словарь, где количество символа заменено на процентное содержание

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""

print(get_count_char(main_str))


#Напишите функцию get_most_frequent_word, которая на вход принимает текст (только английские слова и пробелы), и возвращает самое часто встречающееся слово. Если таких слов несколько - верните любое.
an=input('write a text    ')
def get_most_frequent_word(a):
    b = a.split()
    new_dict = {}
    for i in b:
        if i in new_dict:
            new_dict[i]+=1
        else:
            new_dict[i]=1


    most_frequent_word = max(new_dict, key=new_dict.get)
    return most_frequent_word

print ( get_most_frequent_word(an))


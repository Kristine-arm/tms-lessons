an=input('write a text    ')
def get_longest_word(a):
    b = a.split()
    c=''
    for i in b:
        if len(i)>len(c):
            c = i
#            print(c)
    return c


print(get_longest_word(an))




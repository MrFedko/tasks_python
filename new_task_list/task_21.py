# Определить, позицию второго вхождения строки в списке либо сообщить, что его нет.

my_string = ['13', 'sfd3', 'sdfeq5', '13', 'sd831sd']

def search(any, what_search):
    if any.count(what_search) == 1:
        return 'эта строка уникальна'
    elif any.count(what_search) == 0:
        return 'этой строки нет в списке'
    else: 
        return any.index(what_search, any.index(what_search) + 1 , len(any))
    
print(search(my_string, '13'))


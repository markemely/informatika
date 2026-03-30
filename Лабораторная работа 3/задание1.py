def find_index(items,item): #находим в предложенном списке нужный нам обьект и выписываем его индекс
    for index, given_item in enumerate(items): #создаем соотношение индексов к товарам
        if given_item == item:
            return index #если искомый товар совпадает с товаром  в списке, то как раз выводим его индекс, как предполагалось изначально
items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = find_index(items_list,find_item)
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")

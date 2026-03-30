def count_letters(letters):
    all_letters = {}
    down_letters = letters.lower()
    for letter in down_letters:
        if letter.isalpha():
            if letter in all_letters:
                all_letters[letter]  += 1
            else:
                all_letters[letter] = 1
    return all_letters
def calculate_frequency(dictionary):
    number_of_letters = 0
    for number in dictionary.values():
        number_of_letters = number + number_of_letters
    repetition_rate = {}
    for item, number in dictionary.items():
        rate = number / number_of_letters
        repetition_rate[item] = round(rate, 2)
    return repetition_rate

main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

counting = count_letters(main_str)
selection = calculate_frequency(counting)
for item, rate in selection.items():
    print(f"{item}: {rate:.2f}")

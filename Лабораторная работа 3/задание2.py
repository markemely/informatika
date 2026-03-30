def find_common_participants(participants_first, participants_second, sep=','): #рассматриваем два списка с участниками и разделяем запятой
    firstlist = participants_first.split(sep)
    secondlist = participants_second.split(sep)
    firstset = set(firstlist) #преобразуем в множество(чтобы найти общих участников)
    secondset = set(secondlist)
    common = firstset.intersection(secondset) #нахождение общих участников
    commonparticipants = list(common)
    commonparticipants.sort()
    return commonparticipants
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
all_participants = find_common_participants(participants_first_group, participants_second_group, "|")
print("Общие участники:", all_participants)



def find_common_participants(participant1, participant2, argument=","):
    participant1 = participant1.split(argument)
    participant2 = participant2.split(argument)
    result = list(set(participant1) & set(participant2))
    return sorted(result)

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

result = find_common_participants(participants_first_group, participants_first_group, "|")
print(result)


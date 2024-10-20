# Использование %:
team1_num = 5
team2_num = 6
print('В команде Мастера кода участников: %s !' % team1_num)

print('В команде Мастера кода участников: %(team1_num)s и %(team2_num)s !' % {'team1_num': team1_num,
                                                                              'team2_num': team2_num})
# Использование format():

print('Команда Волшебники данных решила задач: 4{score_2} !'.format(score_2=2))

print('Волшебники данных решили задачи за {team1_time} с !'.format(team1_time=18015.2))

# Использование f-строк:
score_1 = 40
score_2 = 42
print(f'Команды решили {score_1} и {score_2} задач.')

challenge_result = 'Мастера'
print(f'Результат битвы: победа команды {challenge_result} кода!')

tasks_total = 82
time_avg = 350.4
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!.')

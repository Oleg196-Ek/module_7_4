team1_num = 'Мастера кода'
team2_num = 'Волшебники данных'
team1_count = 5
team2_count = 6
team1_time = 1552.512
team2_time = 2153.31451
score_1 = 40
score_2 = 42
tasks_total = score_1 + score_2
time_total = team1_time + team2_time
time_avg = 45.2

if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    result = 'Победа команды Волшебники Данных!'
else:
    result = 'Ничья!'

# %
print('В команде %(name)s участников: %(count)x' % {'name': team1_num, 'count': team1_count})
print('Итого сегодня в командах участников: %(first)x и %(second)x !' % {'first': team1_count,'second': team2_count})

# format()
print('Команда {} решила: {} задач'.format(team2_num, score_2))
print('{} решили задачи за {} c !'.format(team2_num, team1_time))

# f-строки
print(f'Команды решили {score_1} и {score_2} задач.')
print(f'Сегодня было решено {tasks_total} в среднем по {time_avg} секунды на задачу!')
print(f'Результаты битвы: {result}')



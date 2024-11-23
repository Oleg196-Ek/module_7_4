team1_num = int(input())
team2_num = int(input())
print('В команде Мастера кода участников:%s!' % '5')
print( "Итого сегодня в командах участников:%s и %s!" % (5,6))

score_2 = int(input())
team1_time = float(input())
print('Команда Волшебники данных решила задач: {}!'.format(score_2))
print( 'Волшебники данных решили задачи за {}c!'.format(team1_time))

score_1 = int(input())
print(f'Команды решили {score_1} и {score_2} задач')
team2_time = float(input())
task_total = score_1 + score_2
time_total = team1_time + team2_time
time_avg = time_total / task_total
print(f'Сегодня было решено {task_total} задач, в среднем по {time_avg} секунды за задачу')
if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    print(f'Победа команды Мастера кода!')
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    print(f'Победа команды Волшебники Данных!')
else:
    print(f'Ничья!')


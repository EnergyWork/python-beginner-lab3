"""
Дан список подобных кортежей:
    hotel_rooms = [(‘Ann’, 400), (‘Elizabeth’, 103), (‘Mr. McMullen’, 202), (‘Mrs. Smith", 200)]
Вывести на экран последовательность сообщений вида: 
    Hello, Ann! Your room is 400.
Для тех, кто указан как мистер Mr. / миссис Mrs. / мисс Miss| Ms. сообщение должно выглядеть так:
    Good morning, Mr. McMullen! Your room is 202.
"""

hotel_rooms = [('Ann', 400), ('Elizabeth', 103), ('Mr. McMullen', 202), ('Mrs. Smith', 200)]
for room in hotel_rooms:
    print(('Good morning' if room[0].split()[0] in ['Mr.', 'Mrs.', 'Miss', 'Ms.'] else 'Hello') + \
        ', {human}! Your room is {room_number}.'.format(human=room[0], room_number=room[1]))

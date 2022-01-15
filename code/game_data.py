mangolia_1 = {
    'лошади': '../maps/mongolia/mongolian_horse.csv',
    'animation_forest': '../maps/mongolia/mongolian_forest.csv',
    'animation_water_left_bottom': '../maps/mongolia/mongolian_anim water_1.csv',
    'animation_water_right_bottom': '../maps/mongolia/mongolian_anim water_2.csv',
    'animation_water_left_up': '../maps/mongolia/mongolian_anim water_3.csv',
    'animation_water_right_up': '../maps/mongolia/mongolian_anim_water_4.csv',
    'people': '../maps/mongolia/mongolian_npc.csv'
}

dialogs_pos = [[-9060, -9450]]
dialogs = {0: ['Житель: \n'
               'Приветствую тебя, воин! \n C какой целью ты пожаловал к нам со свои войском?',
               'Хан: \n'
               'Я хочу объединить наш народ и для этого мне нужны воины.\n'
               'Позволь мне забрать юношь и обучить их \nнашему воинскому ремеслу,\n'
               'а я в свою очередь щедро награжу тебя.']}


def get_dialog(pos):
    for p in range(len(dialogs_pos)):
        if dialogs_pos[p][0] - 20 <= pos[0] <= dialogs_pos[p][0] + 20 \
                and dialogs_pos[p][1] - 20 <= pos[1] <= dialogs_pos[p][1] + 20:
            return p

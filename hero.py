class Hero:

    hp = 0
    power = 0
    name = ''
    words = ''

    def fight(self,enemy_hp,enemy_power):

        my_hp = self.hp-enemy_power
        enemy_hp = enemy_hp - self.power

        if my_hp > enemy_hp:
            print(f'{self.name}赢了')
        elif my_hp < enemy_hp:
            print('敌人赢了')
        else:
            print('我们打平了')

    def speak_line(self):

        print(self.words)

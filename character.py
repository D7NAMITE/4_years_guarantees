import math


class Gauge:
    def __init__(self, mag: float, highest: float, cap: float = 20):
        self.__mag = mag
        self.__highest = highest
        self.__cap = cap

    def gauge_calculate(self):
        if 0 <= self.__mag <= self.__highest:
            return (self.__mag / self.__highest) * self.__cap
        elif self.__mag > self.__highest:
            return self.__cap
        elif self.__mag < 0:
            return 0

    @property
    def mag(self):
        return self.__mag

    @mag.setter
    def mag(self, new_mag):
        if 0 <= new_mag <= self.__highest:
            self.__mag = new_mag
        elif self.__mag > self.__highest:
            self.__mag = self.__highest
        elif self.__mag < 0:
            self.__mag = 0

    @property
    def highest(self):
        return self.__highest

    @highest.setter
    def highest(self, new_highest):
        self.__highest = new_highest

    @property
    def cap(self):
        return self.__cap

    @cap.setter
    def cap(self, new_line_cap):
        self.__cap = new_line_cap

    def __str__(self):
        return f'[{"■" * math.ceil(self.gauge_calculate()) + ("□" * math.ceil(self.__cap - self.gauge_calculate()))}]'


class Player:
    def __init__(self, name: str = 'Unknown Player', hp: float = 100, highest_hp: float = 100,
                 atk: float = 10, coin: float = 0, year: str = 0, item=None):
        self.__name = name
        self.__hp = hp
        self.__atk = atk
        self.__highest_hp = highest_hp
        self.__coin = coin
        self.__hp_gauge = Gauge(self.__hp, self.__highest_hp)
        self.__year = year

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @property
    def hp(self):
        return self.__hp

    @hp.setter
    def hp(self, new_hp):
        if new_hp < 0:
            self.__hp = 0
            self.__hp_gauge = Gauge(self.__hp, self.__highest_hp)
        elif new_hp > self.__highest_hp:
            self.__hp = self.__highest_hp
            self.__hp_gauge = Gauge(self.__hp, self.__highest_hp)
        elif 0 <= new_hp <= self.__highest_hp:
            self.__hp = new_hp
            self.__hp_gauge = Gauge(self.__hp, self.__highest_hp)

    @property
    def atk(self):
        return self.__atk

    @atk.setter
    def atk(self, new_atk):
        if new_atk < 0:
            self.__atk = 0
        else:
            self.__atk = new_atk

    @property
    def highest_hp(self):
        self.__hp_gauge = Gauge(self.__hp, self.__highest_hp)
        return self.__highest_hp

    @highest_hp.setter
    def highest_hp(self, new_highest_hp):
        if new_highest_hp < self.__hp:
            self.__highest_hp = self.__hp
        elif new_highest_hp < 0:
            pass
        else:
            self.__highest_hp = new_highest_hp

    @property
    def coin(self):
        return self.__coin

    @coin.setter
    def coin(self, new_coin):
        self.__coin = new_coin

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, new_year):
        self.__year = new_year

    def __str__(self):
        return f'Name : {self.__name}\n' \
               f'Year : {self.__year}\n' \
               f' >> Intelligent Damage : {self.__atk}\n' \
               f' >> Mental Stability :{self.__hp}/{self.__highest_hp}\n' \
               f'    {self.__hp_gauge}\n' \
               f' >> Skill Points : {self.__coin}'


class Enemy:
    def __init__(self, name: str = 'Unknown Hostile', hp: float = 100, highest_hp: float = 100,
                 atk: float = 10, year: str = 0):
        self.__name = name
        self.__hp = hp
        self.__atk = atk
        self.__highest_hp = highest_hp
        self.__hp_gauge = Gauge(self.__hp, self.__highest_hp)
        self.__year = year

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @property
    def hp(self):
        return self.__hp

    @hp.setter
    def hp(self, new_hp):
        if new_hp < 0:
            self.__hp = 0
            self.__hp_gauge = Gauge(self.__hp, self.__highest_hp)
        elif new_hp > self.__highest_hp:
            self.__hp = self.__highest_hp
            self.__hp_gauge = Gauge(self.__hp, self.__highest_hp)
        elif 0 <= new_hp <= self.__highest_hp:
            self.__hp = new_hp
            self.__hp_gauge = Gauge(self.__hp, self.__highest_hp)

    @property
    def atk(self):
        return self.__atk

    @atk.setter
    def atk(self, new_atk):
        if new_atk < 0:
            self.__atk = 0
        else:
            self.__atk = new_atk

    @property
    def highest_hp(self):
        return self.__highest_hp

    @highest_hp.setter
    def highest_hp(self, new_highest_hp):
        if new_highest_hp < self.__hp:
            self.__highest_hp = self.__hp
        elif new_highest_hp < 0:
            pass
        else:
            self.__highest_hp = new_highest_hp

    def __str__(self):
        return f'Name : {self.__name}\n' \
               f' >> Intelligent Damage : {self.__atk}\n' \
               f' >> Mental Stability :\n' \
               f'   {self.__hp_gauge} {self.__hp}/{self.__highest_hp}\n'

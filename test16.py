"""
게임 캐릭터 시스템을 만드세요.
- Warrior 클래스: 전사 기본 능력
- Mage 클래스: 마법사 기본 능력
- Paladin 클래스: Warrior와 Mage를 다중상속받는 성기사 클래스

각 클래스는 고유의 능력치와 스킬을 가지며, Paladin은 양쪽의 능력을 모두 사용할 수 있어야 합니다.

테스트 코드:
paladin = Paladin("아서스", 100)
paladin.warrior_attack()
paladin.cast_spell()
paladin.display_info()
"""

class Warrior:
    def __init__(self, strength):
        self.strenght = strength

    def warrior_attack(self):
        print(f"전사 공격! 데미지 : {self.strenght}")

    def display_warrior_info(self):
        print(f"전사 힘: {self.strenght}")

class Mage:
    def __init__(self, magic):
        self.magic = magic

    def cast_spell(self):
        print(f"마법 공격! 데미지 : {self.magic}")
    
    def display_mage_info(self):
        print(f"마법사 마력 : {self.magic}")

class Paladin(Warrior, Mage):
    def __init__(self, name, power):
        Warrior.__init__(self, power)
        Mage.__init__(self, power * 0.8)
        self.name = name

    def display_info(self):
        print(f"캐릭터 이름 : {self.name}")
        self.display_warrior_info()
        self.display_mage_info

paladin = Paladin("아서스", 100)
paladin.warrior_attack()
paladin.cast_spell()
paladin.display_info()
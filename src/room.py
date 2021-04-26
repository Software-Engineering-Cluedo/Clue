from src.card import Card
from src.weapontoken import WeaponToken


class Room(Card):
    weapon_token = None


    def __init__(self, name, card_id, symbol):
        super().__init__(name, card_id, symbol)


    def set_weapon_token(self, weapon_token):
        self.weapon_token = weapon_token


    def get_weapon_token(self):
        return self.weapon_token


    def contains_weapon(self):
        return type(self.weapon_token) is WeaponToken

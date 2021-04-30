from src.card import Card
from src.weapontoken import WeaponToken


class Room(Card):
    weapon_token = None

    def __init__(self, name, card_id, symbol):
        super().__init__(name, card_id, symbol)


    def set_weapon_token(self, weapon_token):
        """Sets the weapon for the current room"""
        self.weapon_token = weapon_token


    def get_weapon_token(self):
        """Returns the weapon for the current room 
            Returns: 
            weapon_token: the weapon in the room 
        """
        return self.weapon_token


    def contains_weapon(self):
        """Checks if room contains a weapon
            Returns: 
            boolean: true if it contains a weapon, false otherwise.
        """
        return type(self.weapon_token) is WeaponToken

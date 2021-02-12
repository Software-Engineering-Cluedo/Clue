class Solution:
    def __init__(self, people, weapons, rooms):
        self.perpetrator = people.random()
        self.weapon = weapons.random()
        self.room = rooms.random()

    def get_person(self):
        return self.perpetrator
    
    def get_weapon(self):
        return self.weapon

    def get_room(self):
        return self.room
    
    def get_solution(self):
        return tuple(self.perpetrator, self.weapon, self.room)

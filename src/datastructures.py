
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = [{
            "id":self._generateId(),
            "first_name":"Jhon",
            "last_name":self.last_name,
            "age":33,
            "lucky_numbers":[7,5,4]
        },{
            "id":self._generateId(),
            "first_name":"Jane ",
            "last_name":self.last_name,
            "age":33,
            "lucky_numbers":[10,14,3]
        },{
            "id":self._generateId(),
            "first_name":"Jimmy ",
            "last_name":self.last_name,
            "age":33,
            "lucky_numbers":[1]
        }
        ]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        member_id = {
            'id': member.get('id', self._generate_id()),
            'last_name': self.last_name
        }
        member.update(member_id)
        self._members.append(member)
        return member

    def delete_member(self, member_id):
        for member in self._members:
            if member['id'] == member_id:
                self._members.remove(member)
                return {'message': f'Miembro con ID {member_id} eliminado exitosamente'}
        return None

    def get_member(self, member_id):
        for member in self._members:
            if member['id'] == member_id:
                return member
        return None

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members

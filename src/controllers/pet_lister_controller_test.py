from src.models.sqlite.entities.pets import PetsTable
from .pet_list_controller import PetListerController

class MockTestRepository:
    def list_pets(self):
        return [
            PetsTable(name="Flutty", type="Cat", id=4),
            PetsTable(name="Buddy", type="Dog", id=47),
        ]
    
def test_list_pets():
    controller = PetListerController(MockTestRepository())
    response = controller.list()

    expected_response = {
        "data":{
            "type": "Pets",
            "count": 2,
            "attributes": [
                {"name": "Flutty", "id": 4, "type": "Cat"},
                {"name": "Buddy", "id": 47, "type": "Dog"},
            ]
        }

        
    } 

    assert response == expected_response

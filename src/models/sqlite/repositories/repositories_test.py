import pytest
from src.models.sqlite.settings.connection import db_connection_handler
from .pets_repository import PetsRepository
from .people_repository import PeopleRepository

db_connection_handler.connect_to_db()

@pytest.mark.skip(reason="interacao com o banco")
def test_list_pets():
    repo = PetsRepository(db_connection_handler)
    response = repo.list_pets()
    # print()
    print(response)

@pytest.mark.skip(reason="interacao com o banco")
def test_delete_pet():
    name = 'shrek'
    repo = PetsRepository(db_connection=db_connection_handler)
    repo.delete_pets(name=name)

@pytest.mark.skip(reason="interacao com o banco")
def test_insert_person():
    first_name = "test_name"
    last_name = "test_last"
    age = 77
    pet_id = 2    

    repo = PeopleRepository(db_connection_handler)
    repo.insert_person(first_name=first_name,
                       last_name=last_name,
                       age=age,
                       pet_id=pet_id)


@pytest.mark.skip(reason="insercao no banco de dados")
def test_get_person():
    person_id = 1
    
    repo = PeopleRepository(db_connection=db_connection_handler)
    response = repo.get_person(person_id=person_id) 
    print()
    print(response)
    print()
    print(response.pet_name)
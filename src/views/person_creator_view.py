from src.controllers.person_creator_controller import PersonCreatorController
from src.validators.person_creator_validator import person_creator_validator
from .interfaces.view_interface import ViewInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse

class PersonCreatorView(ViewInterface):
    def __init__(self, controller: PersonCreatorController) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        person_creator_validator(http_request)
        person_info = http_request.body
        body_response = self.__controller.create(person_info)

        return HttpResponse(status_code=201, body=body_response) 
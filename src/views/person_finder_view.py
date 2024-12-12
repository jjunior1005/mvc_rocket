from src.controllers.interfaces.person_finder_controller import PersonFinderControllerInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from .interfaces.view_interface import ViewInterface

class PersonFinderView(ViewInterface):
    def __init__(self, controller: PersonFinderControllerInterface):
        self.__controller = controller
    
    def handle(self, http_request: HttpRequest) -> HttpResponse:
        person_id = http_request.param["person_id"]
        body_respose = self.__controller.find(person_id)

        return HttpResponse(status_code=200, body=body_respose)
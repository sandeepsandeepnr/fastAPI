import imp
from fastapi import APIRouter
from fastapi import HTTPException

from api.authAPI import AuthAPI,User
from api.employee import Employee
from api.analytics import Analytics


class Router:
    def __init__(self, auth_api: AuthAPI,employee:Employee,analytics:Analytics ) -> None:
        self.__auth_api = auth_api
        self.__employee = employee
        self.__analytics = analytics

    @property
    def router(self):
        api_router = APIRouter(prefix='/api', tags=['api'])
        
        @api_router.get('/')
        def index_route():
            return 'Hello! Welcome to api  route'

        @api_router.post('/register/')
        def create_user(user: User):
            return self.__auth_api.post_register_user(user)
        
        @api_router.post('/employee')
        def create_employee():
            return self.__employee.create_employee()

        @api_router.get('/employee') 
        def get_employee():
            return self.__employee.get_employee()  

        @api_router.get('/all_employee')     
        def get_all_employee():
            return self.__employee.get_all_employee()  

        @api_router.post('/employee')
        def create_analytics():
            return self.__analytics.create_analytics()    

        return api_router
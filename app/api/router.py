import imp
from fastapi import APIRouter
from fastapi import HTTPException

from api.authAPI import AuthAPI,Login
from api.employee import Employee,EmployeeModel
from api.analytics import Analytics,AnalyticsModel,UpdateAnalytics


class Router:
    def __init__(self, auth_api: AuthAPI,employee:Employee,analytics:Analytics ) -> None:
        self.__auth_api = auth_api
        self.__employee = employee,
        self.__analytics = analytics

    @property
    def router(self):
        api_router = APIRouter(prefix='/api', tags=['api'])
        
        @api_router.get('/login')
        def create_login(login: Login):
            return self.__auth_api.post_login_user(login)

        @api_router.post('/employee')
        def create_employee(employee: EmployeeModel):
            return self.__employee.create_employee(employee)

        @api_router.get('/employee') 
        def get_employee():
            return self.__employee.get_employee()  

        @api_router.get('/all_employee')     
        def get_all_employee():
            return self.__employee.get_all_employee()  

        @api_router.post('/analytics')
        def create_analytics(analytics:AnalyticsModel):
            return self.__analytics.create_analytics()    

        @api_router.put('/analytics')
        def update_analytics(updateAnalytics:UpdateAnalytics):
            return self.__analytics.update_analytics()



        return api_router
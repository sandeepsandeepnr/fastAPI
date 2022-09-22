
class User(BaseModel):
    name: str
    email: str 
    password: str
    age: int | None = None

class Employee:


    def get_employee(self):
        return 'get  employee details '

    def get_all_employee(self):
        return 'get  all employee details '

    def create_employee(self):
        return 'create employee details  '

    def update_employee(self):
        return 'update employee details  '

    def delete_employee(self):
        return 'delete employee'
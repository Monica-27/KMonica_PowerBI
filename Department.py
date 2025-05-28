#which has dept id dept naem loction of the dept and head of the dept through the constructor intialize the dept attributes create a ammethod to dispaly the dept info then dipaly total depts in your organisation
#display all dept info, add a fucn to search dept by name
class Department:
    count=0
    all_departments = []
    def __init__(self,id,deptname,location,hod):
        self.id=id
        self.deptname=deptname
        self.location=location
        self.hod=hod
        Department.count+=1
        Department.all_departments.append(self)

    def display_dept_info(self):
        print("Department Information:")
        print("----------")
        print(f"Dept Id: {self.id}")
        print(f"Dept Name: {self.deptname}")
        print(f"Location: {self.location}")
        print(f"Hod : {self.hod}")

    @classmethod
    def get_total_dept(cls):
        return cls.count
    
departments = [
Department(100, "CSE", "SMB", "Sreevani"),
Department(200, "IT", "Perl", "Aruna"),
Department(300, "ECE", "Delta", "Srinivas")
]

for dept in departments:
    dept.display_dept_info()

search_name = input("Enter department name: ")

found = False
for dept in departments:
    if dept.deptname== search_name: 
        print("Found")
        dept.display_dept_info()
        found = True
        break

if not found:
    print("Not Present")

print(f"Total departments: {Department.get_total_dept()}")




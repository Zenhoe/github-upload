class EmployeeEmailSlicer:
    def __init__(self, Email):

        self.Email = Email
        

    def EmailSlicer(self):
        Name = self.Email[: self.Email.index("@")]
        Domain = self.Email[ self.Email.index("@") + 1:]
        print("The name is {} and the domain is {}".format(Name, Domain))

emp1 = EmployeeEmailSlicer(Email = "MarcelNeu@gmail.ca")
emp2 = EmployeeEmailSlicer(Email = "JimNeu@hotmail.com")

emp1.EmailSlicer()
emp2.EmailSlicer()
        
        


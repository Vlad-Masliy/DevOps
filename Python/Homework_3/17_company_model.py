import abc


# Implement all methods where `NotImplementedError` is raised


class Company(object):
    """ Represents a company """

    def __init__(self, name, address=None):
        self.name = name
        self.address = address
        self.employees = list()
        self.__money = 1000

    def add_employee(self, employee):
        # make sure employee is an instance of Engineer or Manager
        # make sure he is not employed already
        if employee.is_employed:
            print(f'Employee {employee.name} is already employed')
            return
        if not (isinstance(employee, Manager) or isinstance(employee, Engineer)):
            print(f'Company {self.name} only hires managers or engineers')
            return
        self.employees.append(employee)

    def dismiss_employee(self, employee):
        """
        Dismisses an employee. Employee must be a company member.
        Company should notify employee that he/she was dismissed
        """
        print(f'Employee {employee.name} dismissed from the company {self.name}')

    def notify_im_leaving(self, employee):
        """ En employee should call this method when leaving a company """
        print(f'Employee {employee.name} leaves from the company {self.name}')

    def do_tasks(self, employee):
        """
        Engineer should call this method when he is working.
        Company should withdraw 10 money from a personal account and return
        them to engineer. That will be a payment
        :rtype: int
        """
        # make sure engineer is employed to this company
        # check employee is Engineer
        if employee not in self.employees:
            print(f'Employee {employee.name} does not work at company {self.name}')
            return
        if not isinstance(employee, Engineer):
            print(f'Employee {employee.name} is not Engineer')
            return
        self.__money -= 10
        employee.put_money_into_my_wallet(10)
        return


    def write_reports(self, employee):
        """
        Manager should call this method when he is working.
        Company should withdraw 12 money from a personal account and return
        them to manager. That will be a payment
        :rtype: int
        """
        # make sure manager is employed to this company
        # check employee is Manager
        employees = self.employees
        if employee not in employees:
            print(f'Employee {employee.name} does not work in company {self.name}')
            return
        if not isinstance(employee, Manager):
            print(f'Employee {employee.name} is not Manager')
            return
        self.__money -= 12
        employee.put_money_into_my_wallet(12)


    def make_a_party(self):
        """ Party time! All employees get 5 money """
        # make sure a company is not a bankrupt before and after the party
        # call employee.bonus_to_salary()
        if self.is_bankrupt:
            print(f'Party can not take place, because company {self.name} is bankrupt')
            return
        for employee in self.employees:
            employee.bonus_to_salary(self, 5)
            self.__money -= 5
        if self.is_bankrupt:
            print(f'Company {self.name} is bankrupt')
            self.go_bankrupt()


    def show_money(self):
        """ Displays amount of money that company has """
        print(f'Company {self.name} has {(self.__money)} dolars')

    def go_bankrupt(self):
        """
        Declare bankruptcy. Company money are drop to 0.
        All employees become unemployed.
        """
        for employee in self.employees:
            self.dismiss_employee(employee)
            employee.become_unemployed()
        self.__money = 0

    @property
    def is_bankrupt(self):
        """ returns True or False """
        return self.__money <= 0

    def __repr__(self):
        return 'Company (%s)' % self.name

        
class Person(object):
    """ Represents any person """

    def __init__(self, name, age, sex=None, address=None):
        self.name = name
        self.age = age
        self.sex = sex if sex is not None else '<not specified>'
        self.address = address

    def __repr__(self):
        return '%s, %s years old' % (self.name, self.age)


class Employee(Person):
    __metaclass__ = abc.ABCMeta

    def __init__(self, name, age, sex=None, address=None):
        super(Employee, self).__init__(name, age, sex, address)
        self.company = None
        self.__money = 0

    def join_company(self, company):
        # make sure that this person is not employed already
        # employees = company.employees
        # employees.append(self)
        if self.is_employed:
            print(f'Employee {self.name} already employed')
            return
        company.add_employee(self)
        self.company = company
        print(f'Employee {self.name} hired to company {company.name}')

    def become_unemployed(self):
        """ Leave current company """
        employees = self.company.employees
        if self not in employees:
            print(f'Employee {self.name} does not work at company {self.company.name}')
            return
        self.company.dismiss_employee(self)
        employees.remove(self)
        self.company = None


    def notify_dismissed(self):
        """ Company should call this method when dismissing an employee """
        print(f'Employee {self.name} dismissed at {self.company.name}')

    def bonus_to_salary(self, company, reward=5):
        """
        Company should call this method on each employee when having a party
        """
        # make sure person is employed to same company
        # money + 5
        if self in company.employees: 
            self.__money += reward
        else:
            print(f'Employee {self.name} does not work at company {company.name}')
        return
       
    @property
    def is_employed(self):
        """ returns True or False """
        return self.company is not None

    def put_money_into_my_wallet(self, amount):
        """ Adds the indicated amount of money to persons budget """
        # Engineer and Manager will have to use this method to store their
        # salary, because __money is a private attribute
        self.__money += amount
        return

    def show_money(self):
        """ Shows how much money person has earned """
        print(f'Employee {self.name} has {self.__money} dolars')

    @abc.abstractmethod
    def do_work(self):
        """ This method requires re-implementation """
        print(f'Employee {self.name} do work')

    def __repr__(self):
        if self.is_employed:
            return '%s works at %s' % (self.name, self.company)
        return '%s, unemployed'


class Engineer(Employee):


    def do_work(self):
        self.company.do_tasks(self)


class Manager(Employee):

    def do_work(self):
        self.company.write_reports(self)





def check_yourself():
    """ Now let's operate on objects """

    # create first company
    fruits_company = Company('Fruits', address='Ocean street, 1')
    print(fruits_company)

    # add some employees
    alex = Engineer('Alex', 55)
    alex.join_company(fruits_company)
    alex.do_work()
    alex.show_money()

    # add second company
    doors_company = Company('Windows and doors', address='Mountain ave. 10')
    print(doors_company)

    # Alex wants to work for doors
    alex.join_company(doors_company)
    # ups, already haired
    alex.become_unemployed()
    alex.join_company(doors_company)
    alex.do_work()

    # Bill also wants to work for doors
    bill = Engineer('Bill', 20)
    bill.join_company(doors_company)
    bill.do_work()

    # Jane is a very good manager. She wants to work for fruits
    jane = Manager('Jane', 30)
    jane.join_company(fruits_company)
    # Jane works pretty hard. She writes lots of reports
    jane.do_work()
    jane.do_work()

    # Bill wants Jane to be his manager, he leaves doors and joins fruits
    bill.become_unemployed()
    bill.join_company(fruits_company)

    # doors becomes a bankrupt
    doors_company.go_bankrupt()

    # alex becomes unemployed and goes to fruits
    alex.join_company(fruits_company)

    # fruits company has a celebration party
    fruits_company.make_a_party()

    # results
    fruits_company.show_money()
    doors_company.show_money()
    alex.show_money()
    bill.show_money()
    jane.show_money()


if __name__ == '__main__':
    check_yourself()

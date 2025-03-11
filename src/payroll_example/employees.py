
from abc import ABC, abstractmethod


class Employee(ABC):
    def __init__(self, name: str,
                 id: int) -> None:
        '''Initialises object by assigning unique employee ID and name

        Inputs:
            name [str]      - Name of employee
            id [int]        - Unique ID number of employee

        Returns:
            None
        '''
        self.__id = id
        self.__name = name

    @property
    def id(self) -> str:
        '''Returns non-changable ID in hex-string format
        '''
        return self.__id

    @property
    def name(self) -> str:
        '''Returns name of employee
        '''
        return self.__name

    @abstractmethod
    def calculate_payroll(self) -> float:
        '''Calculate the total amount of money due to employee
        at the end of the month'''
        pass


class SalaryEmployee(Employee):
    def __init__(self, name: str,
                 id: int,
                 monthly_wage: float) -> None:
        '''Initialises object by assigning unique employee ID,
        name and monthly wage.

        Inputs:
            name [str]              - Name of employee
            id [int]                - Unique ID number of employee
            monthly_wage [float]    - Monthly salary

        Returns:
            None
        '''
        super().__init__(name, id)

        # Define monthly wage
        self.__monthly_wage = monthly_wage

    def __repr__(self) -> str:
        '''Repr of Hourly employee object
        '''
        mg = f'SalaryEmployee({self.name}, {self.id}, {self.monthly_wage})'
        return mg

    def __str__(self) -> str:
        '''Readable representation of object
        '''
        mg = f'{self.name} is an salaried employee earning £{self.monthly_wage:,.2f} per month'  # noqa: E501
        return mg

    @property
    def monthly_wage(self) -> float:
        '''Non-changable property that returns the monthly salary
        '''
        return self.__monthly_wage

    def calculate_payroll(self) -> float:
        '''Calculate amount to be paid to to employee at end of month.

        Inputs:
            None

        Returns:
            payroll_amount [float]  - Amount to be paid to employee
        '''
        return self.__monthly_wage


class HourlyEmployee(Employee):
    def __init__(self, name: str,
                 id: int,
                 hourly_rate: float) -> None:
        '''Initialises hourly-paid employee by assigning unique employee ID,
        name and hourly rate.

        Inputs:
            name [str]              - Name of employee
            id [int]                - Unique ID number of employee
            hourly_rate [float]     - Hourly pay rate of employee

        Returns:
            None
        '''
        super().__init__(name, id)
        self.__hourly_rate = hourly_rate
        self.__hours_worked = 0

    def __repr__(self) -> str:
        '''Repr of Hourly employee object
        '''
        mg = f'HourlyEmployee({self.name}, {self.id}, {self.hourly_rate})'
        return mg

    def __str__(self) -> str:
        '''Readable representation of object
        '''
        mg = f'{self.name} is an Hourly-paid employee earning £{self.hourly_rate:0.2f} per hour'  # noqa: E501
        return mg

    @property
    def hourly_rate(self) -> float:
        '''Getter for hourly rate. Can't be changed.
        '''
        return self.__hourly_rate

    @property
    def hours_worked(self) -> int:
        '''How many hours has the employee worked?
        '''
        return self.__hours_worked

    def add_work(self, hours: int) -> None:
        '''Adds hours of work when hourly employee has done a shift.

        Inputs:
            hours [int]             - Number of (whole) hours done in shift.

        Returns:
            None
        '''
        # Hours should be strictly positive
        if hours >= 0:
            self.__hours_worked += hours
        else:
            raise ValueError('Hours should be positive')

    def calculate_payroll(self) -> float:
        '''Calculate amount to be paid to to employee at end of month.

        Inputs:
            None

        Returns:
            payroll_amount [float]  - Amount to be paid to employee
        '''
        pay = self.hours_worked * self.hourly_rate
        return pay

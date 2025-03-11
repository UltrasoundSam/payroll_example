# Payroll-Example
<!--
- These are examples. See https://shields.io for others or to customize this set of shields. You might want to include dependencies, project status and licence info here -
![GitHub repo size](https://img.shields.io/github/repo-size/scottydocs/README-template.md)
![GitHub contributors](https://img.shields.io/github/contributors/scottydocs/README-template.md)
![GitHub stars](https://img.shields.io/github/stars/scottydocs/README-template.md?style=social)
![GitHub forks](https://img.shields.io/github/forks/scottydocs/README-template.md?style=social)
![Twitter Follow](https://img.shields.io/twitter/follow/scottydocs?style=social) -->

Payroll-example is a tool that allows the finance team to calculate the amount owed to each employee.

This project allows our finance team to assign a role to every member of staff, whether they are a salaried employee, or whether they are paid by the hour. The advance
of this package is that the calculations are abstracted away from the end-user through a user-friendly interface, allowing them to calculate payroll in a more streamlined,
time efficient manner, reducing errors by 5 %.

## Prerequisites

Before you begin, ensure you have met the following requirements:
<!--- These are just example requirements. Add, duplicate or remove as required --->
* You have installed the latest version of `python` with a version greater than 3.12
* You have a `<Windows/Linux/Mac>` machine - package is cross platform across all major OSs.
* It is also advised that have jupyter notebooks installed (```python -m pip install juypter```) to allow for interactive programming.
<!-- * You have read `<guide/link/documentation_related_to_project>`.  -->


## Installing Payroll-Example

To install Payroll-Example, follow these steps:


```bash
python -m pip install /path/to/this/folder
```

## Using Payroll-Example

To use Payroll-Example, follow these steps:

```python
import uuid
from random import randrange

# Generate some random employees
JohnSmith = HourlyEmployee(name='John Smith',
                           id=uuid.uuid4().int,
                           hourly_rate=17.50)

ErikaMustermann = SalaryEmployee(name='Erika Mustermann',
                                 id=uuid.uuid4().int,
                                 monthly_wage=2780)

IonPopescu = SalaryEmployee(name='Ion Popescu',
                            id=uuid.uuid4().int,
                            monthly_wage=3110.5)

AgatheDupont = HourlyEmployee(name='Agathe Dupont',
                              id=uuid.uuid4().int,
                              hourly_rate=20.12)

# For the hourly employees, let's randomly assign hours worked
days_worked = randrange(11, 21)     # Choose how many days they worked this month
for _ in range(days_worked):
    # For each day, they might have a variable number of hours worked
    JohnSmith.add_work(randrange(3, 8))
    AgatheDupont.add_work(randrange(4, 8))


# We can now create out list of employees, iterating through to calculate their individual payrolls
total_payroll = 0
employees = (JohnSmith, ErikaMustermann, IonPopescu, AgatheDupont)

# We can iterate through the employees and calculate their individual payrolls
for employee in employees:
    total_payroll += employee.calculate_payroll()

print(f'The company will pay out a total of £{total_payroll:,.2f} this month')
```

## Contributing to Payroll-Example
<!--- If your README is long or you have some specific process or steps you want contributors to follow, consider creating a separate CONTRIBUTING.md file--->
To contribute to Payroll-Example, follow these steps:

1. Fork this repository.
2. Create a branch: `git checkout -b <branch_name>`.
3. Make your changes and commit them: `git commit -m '<commit_message>'`
4. Push to the original branch: `git push origin Payroll-Example/<location>`
5. Create the pull request.

Alternatively see the GitHub documentation on [creating a pull request](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).

## Contact

If you want to contact me you can reach me at <s.hill@yorksj.ac.uk>.

## License
<!--- If you're not sure which open license to use see https://choosealicense.com/--->

This project uses the following license: [License](./LICENSE).
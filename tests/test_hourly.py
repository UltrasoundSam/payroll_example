# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 2025 15:46

@author: samhill

Tests the hourly-paid employee class
"""
import pytest
import uuid

from payroll_example import HourlyEmployee

# Define some useful constants
HOURLY_NAME = 'John Smith'
HOURLY_RATE = 17.50
HOURLY_ID = uuid.uuid4().int


@pytest.fixture
def john_employee() -> HourlyEmployee:
    John = HourlyEmployee(name=HOURLY_NAME,
                          id=HOURLY_ID,
                          hourly_rate=HOURLY_RATE)
    return John


def test_rate_property(john_employee):
    '''Tests that hourly pay rate is set properly
    '''
    john_employee = HourlyEmployee(name=HOURLY_NAME,
                                   id=HOURLY_ID,
                                   hourly_rate=HOURLY_RATE)
    assert john_employee.hourly_rate == HOURLY_RATE


def test_rate_private(john_employee):
    '''Tests that the hourly rate is a private attribute that cannot be altered
    '''
    john_employee = HourlyEmployee(name=HOURLY_NAME,
                                   id=HOURLY_ID,
                                   hourly_rate=HOURLY_RATE)

    with pytest.raises(AttributeError):
        john_employee.hourly_rate = 50


def test_add_hours(john_employee):
    '''Tests that hours can be added when employee has done
    a shift
    '''
    # Add 10 hours to john's hours worked
    hours = 10
    john_employee.add_work(hours)
    assert john_employee.hours_worked == hours


def test_add_incorrect_hours(john_employee):
    '''Makes sures negative hours that are added are rejected
    '''
    # Add negative hours! This shouldn't work, and should through an exception
    with pytest.raises(ValueError):
        john_employee.add_work(-25)


@pytest.mark.parametrize("hours, expected",
                         [(0, 0),
                          (1, HOURLY_RATE),
                          (25.54, 25.54*HOURLY_RATE),
                          (1e-3, 1e-3*HOURLY_RATE)])
def test_calculate_payroll(john_employee, hours, expected):
    '''Makes sure pay is calculated correctly
    '''
    john_employee.add_work(hours)
    assert john_employee.calculate_payroll() == pytest.approx(expected)

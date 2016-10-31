# tests.test_vehicles
# test module to evaluate the classes in the vehicles module
#
# for a list of available asserts:
# https://docs.python.org/2/library/unittest.html#assert-methods
#
# to execute tests, run the following command from project root:
#   nosetests -v --with-coverage --cover-package=motorsports \
#   --cover-inclusive --cover-erase tests
#
# Author:   Allen Leis <allen.leis@georgetown.edu>
# Created:  Fri Sep 11 23:22:32 2015 -0400
#
# Copyright (C) 2015 georgetown.edu
# For license information, see LICENSE.txt
#
# ID: test_vehicles.py [] allen.leis@georgetown.edu $

"""
Test cases for vehicles module
"""

##########################################################################
## Imports
##########################################################################

import unittest
from unittest import skip
from motorsports.buildings import Car, BaseVehicle

##########################################################################
## Tests
##########################################################################

class VehicleTests(unittest.TestCase):

    def test_description(self):
        """
        Ensure the car description return a string of: "color, make model"
        """
        c = Car(color='blue',make='honda',model='civic')
        d = c.description
        try:
            self.assertEqual(d, '{} {} {}'.format(c.color, c.make, c.model))
        except AssertionError:
            self.fail("Was not able to return a string of: color, make model")


    def test_initial_state_is_stopped(self):
        """
        Ensure the a car's initial state is "stopped"
        """
        c = Car(color='blue',make='honda',model='civic')
        try:
            self.assertEqual(c.state, 'stopped')
        except AssertionError:
            self.fail("Was not able to return an initial state of stopped")


    def test_state_after_start(self):
        """
        Ensure the car's state is "started" after using start method
        """
        c = Car(color='blue',make='honda',model='civic')
        c.start()
        try:
            self.assertEqual(c.state, 'started')
        except AssertionError:
            self.fail("Was not able to return the car's state as started after using start method")

    def test_state_after_stop(self):
        """
        Ensure the car's state is "stopped" after using shutdown method
        """
        c = Car(color='blue',make='honda',model='civic')
        c.start()
        c.shutdown()
        try:
            self.assertEqual(c.state, 'stopped')
        except AssertionError:
            self.fail("Was not able to return the car's state as stopped after using shutdown method")

    def test_str_builtin(self):
        """
        Ensure the car evaluates to a string of
        "I am a <car color>, <car make>, <car model>."
        """
        c = Car(color='blue',make='honda',model='civic')
        try:
            self.assertEqual(str(c), 'I am a blue honda civic.')
        except AssertionError:
            self.fail("Was not able to ensure the car evaluates to a string of 'I am a <car color> <car make> <car model>'.")

    def test_color_requirement(self):
        """
        Ensure the car requires a color argument during instantiation
        """
        try:
            c = Car(make='honda',model='civic')
        except TypeError as e:
            try:
                self.assertEqual(str(e), "__init__() missing 1 required positional argument: 'color'")
            except AssertionError:
                self.fail("Was not able to ensure the car requires a color argument during instantiation.")



    def test_make_requirement(self):
        """
        Ensure the car requires a make argument during instantiation
        """
        try:
            c = Car(color= 'blue', model='civic')
        except TypeError as e:
            try:
                self.assertEqual(str(e), "__init__() missing 1 required positional argument: 'make'")
            except AssertionError:
                self.fail("Was not able to ensure the car requires a make argument during instantiation.")


    def test_model_requirement(self):
        """
        Ensure the car requires a model argument during instantiation
        """
        try:
            c = Car(color= 'blue', make='honda')
        except TypeError as e:
            try:
                self.assertEqual(str(e), "__init__() missing 1 required positional argument: 'model'")
            except AssertionError:
                self.fail("Was not able to ensure the car requires a model argument during instantiation.")


    def test_state_read_only(self):
        """
        Ensure the car state attribute is read only and throws
        AttributeError if someone tries to assign a value directly
        """
        c = Car(color= 'blue', make='honda', model='civic')
        try:
            try:
                c.state = 'test'
            except AttributeError as a:
                self.assertEqual(str(a), "can't set attribute")
        except AssertionError:
            self.fail("Was not able to ensure he car state attribute is read only and throws AttributeError if someone tries to assign a value directly")


    def test_car_is_a_vehicle(self):
        """
        Ensure a car object is also an instance of BaseVehicle
        """
        c = Car(color= 'blue', make='honda', model='civic')
        try:
            self.assertEqual(isinstance(c, BaseVehicle),True)
        except AssertionError:
            self.fail("Was not able to ensure a car object is also an instance of BaseVehicle")


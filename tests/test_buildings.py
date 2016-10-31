# tests.test_buildings
# test module to evaluate the classes in the buildings module
#
# to execute tests, run the following command from project root:
#   nosetests -v --with-coverage --cover-package=motorsports \
#   --cover-inclusive --cover-erase tests
#
# for a list of available asserts:
# https://docs.python.org/2/library/unittest.html#assert-methods
#
# Author:   Allen Leis <allen.leis@georgetown.edu>
# Created:  Fri Sep 11 23:22:32 2015 -0400
#
# Copyright (C) 2015 georgetown.edu
# For license information, see LICENSE.txt
#
# ID: test_buildings.py [] allen.leis@georgetown.edu $

"""
Test cases for buildings module
"""

##########################################################################
## Imports
##########################################################################

import unittest
from unittest import skip
from motorsports.buildings import Garage
from motorsports.buildings import Car

##########################################################################
## Tests
##########################################################################

class GarageTests(unittest.TestCase):

    def test_has_name(self):
        """
        Ensure the garage returns the name provided at creation
        """
        name = 'Bob\'s Garage'
        g = Garage(name)
        self.assertEqual(name, g.name)

    def test_allows_cars_to_enter(self):
        """
        Ensure the garage allows Car object to enter
        """
        c = Car(color= 'yellow', make='honda', model='civic')
        g = Garage(name='test_garage')
        g.enter(c)


    def test_ensure_cars_enter_fully(self):
        """
        Ensure vehicle is in garage after it enters (eg: vehicle in garage == True)
        """
        d = Car(color= 'yellow', make='honda', model='civic')
        g = Garage(name='test_garage')
        g.enter(d)
        self.assertEqual(d in g.vehicles, True)

    def test_only_allows_cars_to_enter(self):
        """
        Ensure the garage raises TypeError if non vehicle attempts to enter
        """
        f = 'Frank'
        g = Garage(name='test_garage')
        try:
            g.enter(f)
        except TypeError as e:
            try:
                self.assertEqual("Only vehicles are allowed in garages", str(e))
            except AssertionError:
                self.fail('Could not raise TypeError on non-vehicle entering')



    def test_only_allows_cars_to_exit(self):
        """
        Ensure the garage raises TypeError if non vehicle attempts to exit
        """
        f = 'Frank'
        g = Garage(name='test_garage')
        try:
            g.exit(f)
        except TypeError as e:
            try:
                self.assertEqual("Only vehicles are allowed in garages.", str(e))
            except AssertionError:
                self.fail('Could not raise TypeError on non-vehicle entering')

    def test_allows_cars_to_exit(self):
        """
        Ensure vehicles can leave the garage
        """
        d = Car(color= 'yellow', make='honda', model='civic')
        g = Garage(name='test_garage')
        g.enter(d)
        g.exit(d)


    def test_ensure_cars_exit_fully(self):
        """
        Vehicle is not in garage after it exits
        """
        d = Car(color= 'yellow', make='honda', model='civic')
        g = Garage(name='test_garage')
        g.enter(d)
        g.exit(d)

        try:
            self.assertEqual(d in g.vehicles,False)
        except AssertionError:
            self.fail('Could not ensure vehicle is not in garage after it exits')

    def test_raise_lookup_error_on_exit(self):
        """
        Ensure that garage raises LookupError if vehicle attempts
        to exit but was never in garage.
        """
        d = Car(color= 'yellow', make='honda', model='civic')
        g = Garage(name='test_garage')
        try:
            g.exit(d)
        except LookupError as e:
            try:
                self.assertEqual(str(e),"That vehicle is not in test_garage.")
            except AssertionError:
                self.fail('Could not ensure that garage raises LookupError if vehicle attempts to exit but was never in garage.')

    def test_iter_builtin(self):
        """
        Ensure we can iterate over garage vehicles by trying to
        iterate over the garage itself
        """
        gg = Garage(name='test_garage')
        a = Car(color= 'red', make='honda', model='civic')
        b = Car(color= 'white', make='honda', model='civic')
        c = Car(color= 'green', make='honda', model='civic')
        gg.enter(a)
        gg.enter(b)
        gg.enter(c)

        manual_list = [a,b,c]
        garage_test_list = [v for v in gg]

        try:
            self.assertEqual(garage_test_list, manual_list)
        except AssertionError:
            self.fail('Could not ensure we can iterate over garage vehicles by trying to iterate over the garage itself')

    def test_len_builtin(self):
        """
        Ensure that the length of the garage matches the number
        of vehicles parked in it
        """
        g = Garage(name='test_garage')
        a = Car(color= 'red', make='honda', model='civic')
        b = Car(color= 'white', make='honda', model='civic')
        c = Car(color= 'blue', make='honda', model='civic')
        g.enter(a)
        g.enter(b)
        g.enter(c)

        manual_list = len([a,b,c])
        garage_test_list = len([v for v in g])

        try:
            self.assertEqual(garage_test_list, manual_list)
        except AssertionError:
            self.fail('Could not ensure we can iterate over garage vehicles by trying to iterate over the garage itself.')


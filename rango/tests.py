# 
# Tango with Django 2 Progress Tests
# By Leif Azzopardi and David Maxwell
# With assistance from Enzo Roiz (https://github.com/enzoroiz)
# 
# Chapter 3 -- Django Basics
# Last updated October 3rd, 2019
# Revising Author: David Maxwell
# 

#
# In order to run these tests, copy this module to your tango_with_django_project/rango/ directory.
# Once this is complete, run $ python manage.py test rango.tests_chapter3
# 
# The tests will then be run, and the output displayed -- do you pass them all?
# 
# Once you are done with the tests, delete the module. You don't need to put it in your Git repository!
#

import os
import importlib
from django.urls import reverse
from django.test import TestCase
from django.conf import settings


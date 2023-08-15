#!/usr/bin/python3
"""
Defines tests for command interpreter
"""
import unittest
from unittest.mock import patch
from io import StringIO
import pep8
import os
import json
import console
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage


class TestConsole(unittest.TestCase):

    """
    Unittest module for command interpreter
    """
    @classmethod
    def setUpClass(self):
        """
        Set up test class before any test
        """
        self.command = console.HBNBCommand()
        if os.path.exists("file.json"):
            os.remove("file.json")

    @classmethod
    def tearDownClass(self):
        """
        Clear the test class before next tests
        """
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_documentation_console(self):
        """
        Test module documentation
        """
        self.assertGreater(len(console.__doc__), 3)
        self.assertGreater(len(self.__doc__), 3)

    def test_emptyline(self):
        """Test emptyline command"""
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.command.onecmd("\n")
            self.assertEqual(fake_output.getvalue(), '')

    def test_create(self):
        """Test create command"""
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.command.onecmd("create")
            self.assertEqual("** class name missing **\n",
                             fake_output.getvalue())

        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.command.onecmd("create MyModel")
            self.assertEqual("** class doesn't exist **\n",
                             fake_output.getvalue())

        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.command.onecmd("create User")

        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.command.onecmd("User.all()")
            self.assertEqual('["[User]',
                             fake_output.getvalue()[:8])

    def test_all(self):
        """Test all command"""
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.command.onecmd("all MyModel")
            self.assertEqual("** class doesn't exist **\n",
                             fake_output.getvalue())

        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.command.onecmd("all City")
            self.assertEqual("[]\n", fake_output.getvalue())

    def test_destroy(self):
        """Test destroy command"""
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.command.onecmd("destroy")
            self.assertEqual("** class name missing **\n",
                             fake_output.getvalue())

        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.command.onecmd("destroy TheWorld")
            self.assertEqual("** class doesn't exist **\n",
                             fake_output.getvalue())

        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.command.onecmd("destroy BaseModel")
            self.assertEqual("** instance id missing **\n",
                             fake_output.getvalue())

        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.command.onecmd("destroy BaseModel 12345 12345")
            self.assertEqual("** no instance found **\n",
                             fake_output.getvalue())

    def test_update(self):
        """Test update command"""
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.command.onecmd("update")
            self.assertEqual("** class name missing **\n",
                             fake_output.getvalue())

        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.command.onecmd("update MyModel")
            self.assertEqual("** class doesn't exist **\n",
                             fake_output.getvalue())

        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.command.onecmd("update User")
            self.assertEqual("** instance id missing **\n",
                             fake_output.getvalue())

        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.command.onecmd("update BaseModel 12345")
            self.assertEqual("** attribute name missing **\n",
                             fake_output.getvalue())

    def test_show(self):
        """Test show command"""
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.command.onecmd("show")
            self.assertEqual("** class name missing **\n",
                             fake_output.getvalue())

        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.command.onecmd("show BaseModel")
            self.assertEqual("** instance id missing **\n",
                             fake_output.getvalue())

    def test_default(self):
        """Test <class>.<cmd>"""
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.command.onecmd("User.count()")
            self.assertEqual(int, type(eval(fake_output.getvalue())))

    def test_pep8_console(self):
        """
        Pep8 compliance in console.py
        """
        style = pep8.StyleGuide(quiet=False)
        errors = 0
        file = (["console.py"])
        errors += style.check_files(file).total_errors
        self.assertEqual(errors, 0, 'Need to fix Pep8')

    def test_pep8_test_console(self):
        """
        Pep8 compliance in test_console.py
        """
        style = pep8.StyleGuide(quiet=False)
        errors = 0
        file = (["tests/test_console.py"])
        errors += style.check_files(file).total_errors
        self.assertEqual(errors, 0, 'Need to fix Pep8')


if __name__ == "__main__":
    unittest.main()

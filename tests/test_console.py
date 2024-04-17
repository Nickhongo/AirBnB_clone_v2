import unittest
from unittest.moxk import patch
from io import StringIo
from console import HBNBCommand
from models import storage
from models.state import State

class TestHBNBConsole(unittest.TestCase):
    def test_create_with_params(self):
        with patch("sys.stdout", new=StringIo()) as mock_stdout:
            HBNBCommand().onecmd('create State name="Arizona"')

            result = mock_stdout.getValue().strip()

            self.assertEqual(len(result), 36)
            state_id = result
            state_obj = storage.all()["State.{}".format(state_id)]
            self.assertIsInstance(state_obj, State)
            self.assertEqual(state_obj.name, "Arizona")

if __name__ == "__main__":
    unittest.main()

import unittest
import subprocess
import echo


class TestEcho(unittest.TestCase):
    def setUp(self):

    # def test_help(self):
    #     """ Running the program without arguments should show usage. """

    #     # Run the command `python ./echo.py -h` in a separate process, then
    #     # collect it's output.
    #     process = subprocess.Popen(
    #         ["python", "./echo.py", "-h"],
    #         stdout=subprocess.PIPE)
    #     stdout, _ = process.communicate()
    #     usage = open("./USAGE", "r").read()

    #     self.assertEquals(stdout, usage)

    def test_upper(self):
        pass
    def test_lower(self):
        pass

    def test_title(self):
        pass


if __name__ == "__main__":
    unittest.main()
import unittest
from utils import system_cmd
from system import LinuxX
from stats import pretty_dur


class TestUtils(unittest.TestCase):

    def test_system_cmd_stdout(self):
        exit_code, std_out, std_err = system_cmd("echo hei")
        self.assertEqual(std_out, "hei\n")

    def test_system_cmd_exit_code_okay(self):
        exit_code, std_out, std_err = system_cmd("uptime")
        self.assertEqual(exit_code, 0)
        self.assertIsInstance(exit_code, int)

    def test_system_cmd_exit_code_fail(self):
        exit_code, std_out, std_err = system_cmd("command-should-not-be-found")
        self.assertNotEqual(exit_code, 0)


class TestSystem(unittest.TestCase):

    def test_active_window(self):
        interface = LinuxX()
        active_window = interface.active_window()
        self.assertNotEqual(active_window, None)

    def test_idle_sec(self):
        interface = LinuxX()
        idle_sec = interface.idle_sec()
        self.assertNotEqual(idle_sec, None)
        self.assertIsInstance(idle_sec, int)

class TestStats(unittest.TestCase):

    def test_pretty_dur(self):
        self.assertEqual(pretty_dur(60), "1h00m")
        self.assertEqual(pretty_dur(0), "0h00m")
        self.assertEqual(pretty_dur(121), "2h01m")
        self.assertEqual(pretty_dur(70), "1h10m")

if __name__ == '__main__':
    unittest.main()
"""
Tests for string .isIPv4() method.
"""

from silk.interpreter import Interpreter


class TestStringIsIPv4:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_isIPv4_valid(self):
        output = self._run('print("192.168.1.1".isIPv4())')
        assert output[-1] == "true"

    def test_isIPv4_localhost(self):
        output = self._run('print("127.0.0.1".isIPv4())')
        assert output[-1] == "true"

    def test_isIPv4_invalid(self):
        output = self._run('print("256.0.0.1".isIPv4())')
        assert output[-1] == "false"

    def test_isIPv4_not_ip(self):
        output = self._run('print("hello".isIPv4())')
        assert output[-1] == "false"

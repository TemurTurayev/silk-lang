"""
Tests for string .isAnagram(other) method.
"""

from silk.interpreter import Interpreter


class TestStringIsAnagram:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_isAnagram_true(self):
        output = self._run('print("listen".isAnagram("silent"))')
        assert output[-1] == "true"

    def test_isAnagram_false(self):
        output = self._run('print("hello".isAnagram("world"))')
        assert output[-1] == "false"

    def test_isAnagram_case_insensitive(self):
        output = self._run('print("Astronomer".isAnagram("Moon starer"))')
        assert output[-1] == "true"

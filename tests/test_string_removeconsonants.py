"""
Tests for string .removeConsonants() method.
"""

from silk.interpreter import Interpreter


class TestStringRemoveConsonants:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_removeConsonants_basic(self):
        output = self._run('print("hello".removeConsonants())')
        assert output[-1] == "eo"

    def test_removeConsonants_all_consonants(self):
        output = self._run('print("xyz".removeConsonants())')
        assert output[-1] == ""

"""
Tests for string .toPhonetic() method - convert to International Phonetic Alphabet representation.
"""

from silk.interpreter import Interpreter


class TestStringToPhonetic:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toPhonetic_hello(self):
        output = self._run('print("hello".toPhonetic())')
        assert output[-1] == "h-e-l-l-o"

    def test_toPhonetic_abc(self):
        output = self._run('print("abc".toPhonetic())')
        assert output[-1] == "a-b-c"

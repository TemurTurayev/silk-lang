"""
Tests for array .frequencies() method.
"""

from silk.interpreter import Interpreter


class TestArrayFrequencies:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_frequencies_basic(self):
        output = self._run('''
let result = ["a", "b", "a", "c", "b", "a"].frequencies()
print(result.get("a"))
print(result.get("b"))
print(result.get("c"))
''')
        assert output[-3] == "3"
        assert output[-2] == "2"
        assert output[-1] == "1"

    def test_frequencies_numbers(self):
        output = self._run('''
let result = [1, 2, 2, 3, 3, 3].frequencies()
print(result.get(1))
print(result.get(3))
''')
        assert output[-2] == "1"
        assert output[-1] == "3"

    def test_frequencies_single(self):
        output = self._run('''
let result = [5].frequencies()
print(result.get(5))
''')
        assert output[-1] == "1"

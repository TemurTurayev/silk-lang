"""
Tests for array .without() method.
"""

from silk.interpreter import Interpreter


class TestArrayWithout:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_without_basic(self):
        output = self._run('''
print([1, 2, 3, 4, 5].without([2, 4]))
''')
        assert output[-1] == "[1, 3, 5]"

    def test_without_no_match(self):
        output = self._run('''
print([1, 2, 3].without([99]))
''')
        assert output[-1] == "[1, 2, 3]"

    def test_without_all(self):
        output = self._run('''
print([1, 1, 1].without([1]))
''')
        assert output[-1] == "[]"

    def test_without_strings(self):
        output = self._run('''
print(["a", "b", "c"].without(["b"]))
''')
        assert output[-1] == "[a, c]"

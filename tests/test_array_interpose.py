"""
Tests for array .interpose(separator) method.
"""

from silk.interpreter import Interpreter


class TestArrayInterpose:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_interpose_basic(self):
        output = self._run('''
print([1, 2, 3].interpose(0))
''')
        assert output[-1] == "[1, 0, 2, 0, 3]"

    def test_interpose_strings(self):
        output = self._run('''
print(["a", "b", "c"].interpose("-"))
''')
        assert output[-1] == "[a, -, b, -, c]"

    def test_interpose_single(self):
        output = self._run('''
print([1].interpose(0))
''')
        assert output[-1] == "[1]"

    def test_interpose_empty(self):
        output = self._run('''
print([].interpose(0))
''')
        assert output[-1] == "[]"

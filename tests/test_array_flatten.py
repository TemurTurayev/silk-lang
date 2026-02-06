"""
Tests for array .flatten(depth) - recursive flatten with depth control.
"""

from silk.interpreter import Interpreter


class TestArrayFlatten:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_flatten_one_level(self):
        output = self._run('''
print([[1, 2], [3, 4]].flatten(1))
''')
        assert output[-1] == "[1, 2, 3, 4]"

    def test_flatten_nested(self):
        output = self._run('''
print([[1, [2, 3]], [4]].flatten(2))
''')
        assert output[-1] == "[1, 2, 3, 4]"

    def test_flatten_zero_depth(self):
        output = self._run('''
print([[1, 2], [3]].flatten(0))
''')
        assert output[-1] == "[[1, 2], [3]]"

    def test_flatten_mixed(self):
        output = self._run('''
print([1, [2, 3], 4].flatten(1))
''')
        assert output[-1] == "[1, 2, 3, 4]"

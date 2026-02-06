"""
Tests for array .takeWhile() and .skipWhile() methods.
"""

from silk.interpreter import Interpreter


class TestArrayTakeWhile:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_takeWhile_basic(self):
        output = self._run('''
print([1, 2, 3, 4, 5].takeWhile(|x| x < 4))
''')
        assert output[-1] == "[1, 2, 3]"

    def test_takeWhile_all(self):
        output = self._run('''
print([1, 2, 3].takeWhile(|x| x < 10))
''')
        assert output[-1] == "[1, 2, 3]"

    def test_takeWhile_none(self):
        output = self._run('''
print([5, 6, 7].takeWhile(|x| x < 3))
''')
        assert output[-1] == "[]"

    def test_skipWhile_basic(self):
        output = self._run('''
print([1, 2, 3, 4, 5].skipWhile(|x| x < 3))
''')
        assert output[-1] == "[3, 4, 5]"

    def test_skipWhile_all(self):
        output = self._run('''
print([1, 2, 3].skipWhile(|x| x < 10))
''')
        assert output[-1] == "[]"

    def test_skipWhile_none(self):
        output = self._run('''
print([5, 6, 7].skipWhile(|x| x > 10))
''')
        assert output[-1] == "[5, 6, 7]"

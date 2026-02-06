"""
Tests for array .head(), .tail(), .reject() methods.
"""

from silk.interpreter import Interpreter


class TestArrayHeadTail:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_head_basic(self):
        output = self._run('''
print([1, 2, 3, 4, 5].head(3))
''')
        assert output[-1] == "[1, 2, 3]"

    def test_head_larger_than_array(self):
        output = self._run('''
print([1, 2].head(10))
''')
        assert output[-1] == "[1, 2]"

    def test_tail_basic(self):
        output = self._run('''
print([1, 2, 3, 4, 5].tail(2))
''')
        assert output[-1] == "[4, 5]"

    def test_tail_larger_than_array(self):
        output = self._run('''
print([1, 2].tail(10))
''')
        assert output[-1] == "[1, 2]"


class TestArrayReject:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_reject_basic(self):
        output = self._run('''
print([1, 2, 3, 4, 5].reject(|x| x % 2 == 0))
''')
        assert output[-1] == "[1, 3, 5]"

    def test_reject_none(self):
        output = self._run('''
print([1, 2, 3].reject(|x| x > 10))
''')
        assert output[-1] == "[1, 2, 3]"

    def test_reject_all(self):
        output = self._run('''
print([2, 4, 6].reject(|x| x % 2 == 0))
''')
        assert output[-1] == "[]"

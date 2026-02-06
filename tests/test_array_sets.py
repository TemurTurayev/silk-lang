"""
Tests for array .intersection() and .union() methods.
"""

from silk.interpreter import Interpreter


class TestArrayIntersection:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_intersection_basic(self):
        output = self._run('''
print([1, 2, 3, 4].intersection([3, 4, 5, 6]))
''')
        assert output[-1] == "[3, 4]"

    def test_intersection_empty(self):
        output = self._run('''
print([1, 2].intersection([3, 4]))
''')
        assert output[-1] == "[]"

    def test_intersection_same(self):
        output = self._run('''
print([1, 2, 3].intersection([1, 2, 3]))
''')
        assert output[-1] == "[1, 2, 3]"


class TestArrayUnion:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_union_basic(self):
        output = self._run('''
print([1, 2, 3].union([3, 4, 5]))
''')
        assert output[-1] == "[1, 2, 3, 4, 5]"

    def test_union_no_overlap(self):
        output = self._run('''
print([1, 2].union([3, 4]))
''')
        assert output[-1] == "[1, 2, 3, 4]"

    def test_union_duplicates(self):
        output = self._run('''
print([1, 1, 2].union([2, 3, 3]))
''')
        assert output[-1] == "[1, 2, 3]"

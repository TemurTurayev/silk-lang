"""
Tests for array .any() and .all() aliases.
"""

from silk.interpreter import Interpreter


class TestArrayAny:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_any_true(self):
        output = self._run('''
print([1, 2, 3].any(|x| x > 2))
''')
        assert output[-1] == "true"

    def test_any_false(self):
        output = self._run('''
print([1, 2, 3].any(|x| x > 10))
''')
        assert output[-1] == "false"

    def test_any_empty(self):
        output = self._run('''
print([].any(|x| x > 0))
''')
        assert output[-1] == "false"


class TestArrayAll:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_all_true(self):
        output = self._run('''
print([1, 2, 3].all(|x| x > 0))
''')
        assert output[-1] == "true"

    def test_all_false(self):
        output = self._run('''
print([1, 2, 3].all(|x| x > 1))
''')
        assert output[-1] == "false"

    def test_all_empty(self):
        output = self._run('''
print([].all(|x| x > 0))
''')
        assert output[-1] == "true"

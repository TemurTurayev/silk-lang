"""
Tests for array .mapIntersperse(val) method - insert value between elements.
"""

from silk.interpreter import Interpreter


class TestArrayMapIntersperse:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapIntersperse_zero(self):
        output = self._run('''
let result = [1, 2, 3].mapIntersperse(0)
print(result)
''')
        assert output[-1] == "[1, 0, 2, 0, 3]"

    def test_mapIntersperse_single(self):
        output = self._run('''
let result = [5].mapIntersperse(0)
print(result)
''')
        assert output[-1] == "[5]"

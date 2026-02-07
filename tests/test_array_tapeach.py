"""
Tests for array .tapEach(fn) method - calls fn on each element, returns original array.
"""

from silk.interpreter import Interpreter


class TestArrayTapEach:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_tapEach_returns_original(self):
        output = self._run('''
let side = []
let result = [1, 2, 3].tapEach(|x| side.push(x * 10))
print(result)
''')
        assert output[-1] == "[1, 2, 3]"

    def test_tapEach_side_effect(self):
        output = self._run('''
let side = []
[1, 2, 3].tapEach(|x| side.push(x * 10))
print(side)
''')
        assert output[-1] == "[10, 20, 30]"

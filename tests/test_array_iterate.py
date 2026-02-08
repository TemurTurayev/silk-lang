"""
Tests for array .iterate(seed, fn, count) - generate array by repeatedly applying fn.
Similar to unfold but always applies fn starting from seed.
"""

from silk.interpreter import Interpreter


class TestArrayIterate:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_iterate_doubles(self):
        output = self._run('''
let result = [].iterate(2, |x| x * 2, 4)
print(result)
''')
        assert output[-1] == "[2, 4, 8, 16]"

    def test_iterate_increment(self):
        output = self._run('''
let result = [].iterate(0, |x| x + 5, 3)
print(result)
''')
        assert output[-1] == "[0, 5, 10]"

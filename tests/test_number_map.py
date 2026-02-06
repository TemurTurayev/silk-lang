"""
Tests for number .map() method.
"""

from silk.interpreter import Interpreter


class TestNumberMap:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_map_double(self):
        output = self._run('''
print(5.map(|x| x * 2))
''')
        assert output[-1] == "10"

    def test_map_negate(self):
        output = self._run('''
print(3.map(|x| -x))
''')
        assert output[-1] == "-3"

    def test_map_chain(self):
        output = self._run('''
print(10.map(|x| x + 5).map(|x| x * 2))
''')
        assert output[-1] == "30"

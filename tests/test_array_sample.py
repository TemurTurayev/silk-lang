"""
Tests for array .sample() and .shuffle() methods.
"""

from silk.interpreter import Interpreter


class TestArraySample:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_sample_length(self):
        output = self._run('''
let s = [1, 2, 3, 4, 5].sample(3)
print(s.length)
''')
        assert output[-1] == "3"

    def test_sample_one(self):
        output = self._run('''
let s = [10, 20, 30].sample(1)
print(s.length)
''')
        assert output[-1] == "1"

    def test_sample_all(self):
        output = self._run('''
let s = [1, 2, 3].sample(3)
print(s.length)
''')
        assert output[-1] == "3"

    def test_shuffle_length(self):
        output = self._run('''
let s = [1, 2, 3, 4, 5].shuffle()
print(s.length)
''')
        assert output[-1] == "5"

"""
Tests for array .juxtapose(fns) method - apply multiple functions.
"""

from silk.interpreter import Interpreter


class TestArrayJuxtapose:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_juxtapose_basic(self):
        output = self._run('''
let fns = [|x| x * 2, |x| x + 1]
print([1, 2, 3].juxtapose(fns))
''')
        assert output[-1] == "[[2, 2], [4, 3], [6, 4]]"

    def test_juxtapose_single_fn(self):
        output = self._run('''
print([5].juxtapose([|x| x * x]))
''')
        assert output[-1] == "[[25]]"

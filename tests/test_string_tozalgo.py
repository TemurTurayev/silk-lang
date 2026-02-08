"""
Tests for string .toZalgo() method - Zalgo text generation.
"""

from silk.interpreter import Interpreter


class TestStringToZalgo:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toZalgo_length(self):
        output = self._run('print("hi".toZalgo().length)')
        # Zalgo adds combining characters, so length > original
        assert int(output[-1]) > 2

    def test_toZalgo_contains_original(self):
        output = self._run('''
let z = "a".toZalgo()
print(z.contains("a"))
''')
        assert output[-1] == "true"

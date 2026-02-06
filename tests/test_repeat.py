"""
Tests for repeat n { body } statement.
"""

from silk.interpreter import Interpreter


class TestRepeat:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_repeat_basic(self):
        output = self._run('''
let mut count = 0
repeat 3 {
    count += 1
}
print(count)
''')
        assert output[-1] == "3"

    def test_repeat_zero(self):
        output = self._run('''
let mut count = 0
repeat 0 {
    count += 1
}
print(count)
''')
        assert output[-1] == "0"

    def test_repeat_with_expression(self):
        output = self._run('''
let n = 4
let mut sum = 0
repeat n + 1 {
    sum += 2
}
print(sum)
''')
        assert output[-1] == "10"

    def test_repeat_nested(self):
        output = self._run('''
let mut count = 0
repeat 3 {
    repeat 2 {
        count += 1
    }
}
print(count)
''')
        assert output[-1] == "6"

    def test_repeat_with_break(self):
        output = self._run('''
let mut count = 0
repeat 10 {
    count += 1
    if count == 3 {
        break
    }
}
print(count)
''')
        assert output[-1] == "3"

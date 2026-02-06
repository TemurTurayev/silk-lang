"""
Tests for loop { } (infinite loop with break).
"""

from silk.interpreter import Interpreter


class TestLoop:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_loop_with_break(self):
        output = self._run('''
let mut i = 0
loop {
    i += 1
    if i == 5 {
        break
    }
}
print(i)
''')
        assert output[-1] == "5"

    def test_loop_with_continue(self):
        output = self._run('''
let mut sum = 0
let mut i = 0
loop {
    i += 1
    if i > 5 {
        break
    }
    if i % 2 == 0 {
        continue
    }
    sum += i
}
print(sum)
''')
        assert output[-1] == "9"

    def test_loop_nested(self):
        output = self._run('''
let mut count = 0
let mut outer = 0
loop {
    outer += 1
    if outer > 3 {
        break
    }
    let mut inner = 0
    loop {
        inner += 1
        if inner > 2 {
            break
        }
        count += 1
    }
}
print(count)
''')
        assert output[-1] == "6"

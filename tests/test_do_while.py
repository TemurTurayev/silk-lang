"""
Tests for do..while loop (executes body at least once).
"""

from silk.interpreter import Interpreter


class TestDoWhile:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_basic_do_while(self):
        output = self._run('''
let mut i = 0
do {
    i += 1
} while i < 3
print(i)
''')
        assert output[-1] == "3"

    def test_do_while_runs_once(self):
        """Body runs at least once even if condition is false."""
        output = self._run('''
let mut count = 0
do {
    count += 1
} while false
print(count)
''')
        assert output[-1] == "1"

    def test_do_while_with_break(self):
        output = self._run('''
let mut i = 0
do {
    i += 1
    if i == 5 { break }
} while i < 100
print(i)
''')
        assert output[-1] == "5"

    def test_do_while_with_continue(self):
        output = self._run('''
let mut i = 0
let mut sum = 0
do {
    i += 1
    if i % 2 == 0 { continue }
    sum += i
} while i < 6
print(sum)
''')
        assert output[-1] == "9"

    def test_do_while_counter(self):
        output = self._run('''
let mut n = 100
let mut digits = 0
do {
    digits += 1
    n = n / 10
} while n >= 1
print(digits)
''')
        assert output[-1] == "3"

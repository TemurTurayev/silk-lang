"""
Tests for lambda shorthand syntax.

Syntax: |params| expr
"""

from silk.interpreter import Interpreter


class TestLambda:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_lambda_single_param(self):
        output = self._run('''
let double = |x| x * 2
print(double(5))
''')
        assert output[-1] == "10"

    def test_lambda_in_map(self):
        output = self._run('''
let arr = [1, 2, 3]
let result = arr.map(|x| x * x)
print(result)
''')
        assert output[-1] == "[1, 4, 9]"

    def test_lambda_in_filter(self):
        output = self._run('''
let arr = [1, 2, 3, 4, 5, 6]
let evens = arr.filter(|x| x % 2 == 0)
print(evens)
''')
        assert output[-1] == "[2, 4, 6]"

    def test_lambda_two_params(self):
        output = self._run('''
let add = |a, b| a + b
print(add(3, 4))
''')
        assert output[-1] == "7"

    def test_lambda_in_reduce(self):
        output = self._run('''
let sum = [1, 2, 3, 4].reduce(|acc, x| acc + x, 0)
print(sum)
''')
        assert output[-1] == "10"

    def test_lambda_no_params(self):
        output = self._run('''
let greet = || "hello"
print(greet())
''')
        assert output[-1] == "hello"

    def test_lambda_in_sort_every(self):
        output = self._run('''
let all_pos = [1, 2, 3].every(|x| x > 0)
print(all_pos)
''')
        assert output[-1] == "true"

    def test_lambda_chained(self):
        output = self._run('''
let result = (1..6).filter(|x| x % 2 == 0).map(|x| x * 10)
print(result)
''')
        assert output[-1] == "[20, 40]"

    def test_lambda_with_find(self):
        output = self._run('''
let found = [10, 20, 30].find(|x| x > 15)
print(found)
''')
        assert output[-1] == "20"

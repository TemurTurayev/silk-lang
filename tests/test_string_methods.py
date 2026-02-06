"""
Tests for additional string methods: indexOf, substring, padStart, padEnd.
"""

from silk.interpreter import Interpreter


class TestStringMethods:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_indexOf_found(self):
        output = self._run('print("hello world".indexOf("world"))')
        assert output[-1] == "6"

    def test_indexOf_not_found(self):
        output = self._run('print("hello".indexOf("xyz"))')
        assert output[-1] == "-1"

    def test_indexOf_empty(self):
        output = self._run('print("hello".indexOf(""))')
        assert output[-1] == "0"

    def test_substring_two_args(self):
        output = self._run('print("hello world".substring(0, 5))')
        assert output[-1] == "hello"

    def test_substring_one_arg(self):
        output = self._run('print("hello world".substring(6))')
        assert output[-1] == "world"

    def test_substring_middle(self):
        output = self._run('print("abcdef".substring(2, 4))')
        assert output[-1] == "cd"

    def test_repeat(self):
        output = self._run('print("ha".repeat(3))')
        assert output[-1] == "hahaha"

    def test_repeat_zero(self):
        output = self._run('print("ha".repeat(0))')
        assert output[-1] == ""

    def test_padStart(self):
        output = self._run('print("42".padStart(5, "0"))')
        assert output[-1] == "00042"

    def test_padEnd(self):
        output = self._run('print("hi".padEnd(5, "."))')
        assert output[-1] == "hi..."

    def test_chained_methods(self):
        output = self._run('''
let result = "  Hello World  ".trim().lower()
print(result)
''')
        assert output[-1] == "hello world"

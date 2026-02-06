"""
Tests for string .title() and .capitalize() methods.
"""

from silk.interpreter import Interpreter


class TestStringCase:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_title(self):
        output = self._run('''
print("hello world".title())
''')
        assert output[-1] == "Hello World"

    def test_title_mixed(self):
        output = self._run('''
print("the quick brown FOX".title())
''')
        assert output[-1] == "The Quick Brown Fox"

    def test_capitalize(self):
        output = self._run('''
print("hello world".capitalize())
''')
        assert output[-1] == "Hello world"

    def test_capitalize_already(self):
        output = self._run('''
print("Hello".capitalize())
''')
        assert output[-1] == "Hello"

    def test_words(self):
        output = self._run('''
let w = "hello world foo".words()
print(w.length)
''')
        assert output[-1] == "3"

    def test_words_result(self):
        output = self._run('''
print("one two three".words())
''')
        assert output[-1] == "[one, two, three]"

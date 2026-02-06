"""
Tests for string .kebabCase() and .titleCase() methods.
"""

from silk.interpreter import Interpreter


class TestStringKebabTitle:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_kebabCase_from_camel(self):
        output = self._run('''
print("helloWorld".kebabCase())
''')
        assert output[-1] == "hello-world"

    def test_kebabCase_from_snake(self):
        output = self._run('''
print("hello_world".kebabCase())
''')
        assert output[-1] == "hello-world"

    def test_kebabCase_from_spaces(self):
        output = self._run('''
print("Hello World".kebabCase())
''')
        assert output[-1] == "hello-world"

    def test_titleCase_basic(self):
        output = self._run('''
print("hello world".titleCase())
''')
        assert output[-1] == "Hello World"

    def test_titleCase_from_snake(self):
        output = self._run('''
print("hello_world".titleCase())
''')
        assert output[-1] == "Hello World"

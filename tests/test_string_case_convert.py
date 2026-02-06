"""
Tests for string .camelCase() and .snakeCase() methods.
"""

from silk.interpreter import Interpreter


class TestStringCaseConvert:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_camelCase_from_snake(self):
        output = self._run('''
print("hello_world".camelCase())
''')
        assert output[-1] == "helloWorld"

    def test_camelCase_from_spaces(self):
        output = self._run('''
print("hello world".camelCase())
''')
        assert output[-1] == "helloWorld"

    def test_camelCase_from_kebab(self):
        output = self._run('''
print("get-user-name".camelCase())
''')
        assert output[-1] == "getUserName"

    def test_snakeCase_from_camel(self):
        output = self._run('''
print("helloWorld".snakeCase())
''')
        assert output[-1] == "hello_world"

    def test_snakeCase_from_spaces(self):
        output = self._run('''
print("Hello World".snakeCase())
''')
        assert output[-1] == "hello_world"

    def test_snakeCase_from_kebab(self):
        output = self._run('''
print("get-user-name".snakeCase())
''')
        assert output[-1] == "get_user_name"

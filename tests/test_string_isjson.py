"""
Tests for string .isJSON() method.
"""

from silk.interpreter import Interpreter


class TestStringIsJSON:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_isJSON_object(self):
        output = self._run("""print('{"a": 1}'.isJSON())""")
        assert output[-1] == "true"

    def test_isJSON_array(self):
        output = self._run("""print('[1, 2, 3]'.isJSON())""")
        assert output[-1] == "true"

    def test_isJSON_invalid(self):
        output = self._run('print("not json".isJSON())')
        assert output[-1] == "false"

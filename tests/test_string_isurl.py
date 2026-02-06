"""
Tests for string .isUrl() method.
"""

from silk.interpreter import Interpreter


class TestStringIsUrl:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_isUrl_valid_https(self):
        output = self._run('print("https://example.com".isUrl())')
        assert output[-1] == "true"

    def test_isUrl_valid_http(self):
        output = self._run('print("http://test.org/path".isUrl())')
        assert output[-1] == "true"

    def test_isUrl_invalid(self):
        output = self._run('print("not a url".isUrl())')
        assert output[-1] == "false"

    def test_isUrl_no_scheme(self):
        output = self._run('print("example.com".isUrl())')
        assert output[-1] == "false"

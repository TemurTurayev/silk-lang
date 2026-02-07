"""
Tests for string .extractUrls() method.
"""

from silk.interpreter import Interpreter


class TestStringExtractUrls:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_extractUrls_basic(self):
        output = self._run('print("visit https://example.com and http://test.org".extractUrls())')
        assert output[-1] == "[https://example.com, http://test.org]"

    def test_extractUrls_none(self):
        output = self._run('print("no urls here".extractUrls())')
        assert output[-1] == "[]"

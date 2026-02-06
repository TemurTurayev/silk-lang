"""
Tests for dict .mapKeys() method.
"""

from silk.interpreter import Interpreter


class TestDictMapKeys:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_mapKeys_upper(self):
        output = self._run('''
let m = {"hello": 1, "world": 2}
let result = m.mapKeys(|k| k.toUpper())
print(result.get("HELLO"))
print(result.get("WORLD"))
''')
        assert output[-2] == "1"
        assert output[-1] == "2"

    def test_mapKeys_prefix(self):
        output = self._run('''
let m = {"name": "silk", "version": "1.0"}
let result = m.mapKeys(|k| "app_" + k)
print(result.has("app_name"))
print(result.has("app_version"))
''')
        assert output[-2] == "true"
        assert output[-1] == "true"

    def test_mapKeys_length(self):
        output = self._run('''
let m = {"a": 1, "b": 2}
print(m.mapKeys(|k| k.toUpper()).length)
''')
        assert output[-1] == "2"

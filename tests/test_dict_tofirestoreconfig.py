"""
Tests for dict .toFirestoreConfig() method - Firestore config format.
"""

from silk.interpreter import Interpreter


class TestDictToFirestoreConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toFirestoreConfig_basic(self):
        output = self._run('print({"port": 8080}.toFirestoreConfig())')
        assert output[-1] == "port = 8080"

    def test_toFirestoreConfig_string(self):
        output = self._run('print({"project": "myapp"}.toFirestoreConfig())')
        assert output[-1] == "project = myapp"

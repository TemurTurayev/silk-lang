"""
Tests for dict .toSQLiteConfig() method - SQLite PRAGMA config format.
"""

from silk.interpreter import Interpreter


class TestDictToSQLiteConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toSQLiteConfig_basic(self):
        output = self._run('''
let d = {"journal_mode": "wal"}
print(d.toSQLiteConfig())
''')
        assert output[-1] == 'PRAGMA journal_mode = wal;'

    def test_toSQLiteConfig_number(self):
        output = self._run('''
let d = {"cache_size": 10000}
print(d.toSQLiteConfig())
''')
        assert output[-1] == 'PRAGMA cache_size = 10000;'

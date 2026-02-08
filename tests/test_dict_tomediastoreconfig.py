"""
Tests for dict .toMediaStoreConfig() method - format as AWS MediaStore config.
"""

from silk.interpreter import Interpreter


class TestDictToMediaStoreConfig:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_toMediaStoreConfig_basic(self):
        output = self._run('print({"container": "videos"}.toMediaStoreConfig())')
        assert output[-1] == "container = videos"

    def test_toMediaStoreConfig_multi(self):
        output = self._run('print({"container": "videos", "policy": "public"}.toMediaStoreConfig())')
        assert "container = videos" in output[-1]

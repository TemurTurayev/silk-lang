"""
Tests for map .entries(), .merge(), .forEach() methods.
"""

from silk.interpreter import Interpreter


class TestMapEntries:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_entries_basic(self):
        output = self._run('''
let m = {"a": 1, "b": 2}
let e = m.entries()
print(e.length)
''')
        assert output[-1] == "2"

    def test_entries_iterate(self):
        output = self._run('''
let m = {"x": 10}
for entry in m.entries() {
    let [k, v] = entry
    print(f"{k}={v}")
}
''')
        assert output[-1] == "x=10"


class TestMapMerge:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_merge_basic(self):
        output = self._run('''
let a = {"x": 1}
let b = {"y": 2}
let c = a.merge(b)
print(c.keys().sort())
''')
        assert output[-1] == "[x, y]"

    def test_merge_override(self):
        output = self._run('''
let a = {"x": 1, "y": 2}
let b = {"y": 99}
let c = a.merge(b)
print(c["y"])
''')
        assert output[-1] == "99"

    def test_merge_does_not_mutate(self):
        output = self._run('''
let a = {"x": 1}
let b = {"y": 2}
let c = a.merge(b)
print(a.keys().length)
''')
        assert output[-1] == "1"


class TestMapForEach:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_forEach_basic(self):
        output = self._run('''
let m = {"a": 1}
m.forEach(fn(k, v) {
    print(f"{k} -> {v}")
})
''')
        assert output[-1] == "a -> 1"

    def test_forEach_empty(self):
        output = self._run('''
let m = {:}
m.forEach(fn(k, v) { print("nope") })
print("done")
''')
        assert output[-1] == "done"

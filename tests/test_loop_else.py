"""
Tests for while..else and for..else loops.

The else block runs only if the loop completes without breaking.
"""

from silk.interpreter import Interpreter


class TestWhileElse:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_while_else_no_break(self):
        output = self._run('''
let mut i = 0
while i < 3 {
    i += 1
} else {
    print("completed")
}
''')
        assert output[-1] == "completed"

    def test_while_else_with_break(self):
        output = self._run('''
let mut i = 0
while i < 10 {
    if i == 3 { break }
    i += 1
} else {
    print("completed")
}
print("done")
''')
        assert output[-1] == "done"
        assert "completed" not in output

    def test_while_else_false_condition(self):
        output = self._run('''
while false {
    print("never")
} else {
    print("else ran")
}
''')
        assert output[-1] == "else ran"


class TestForElse:

    def _run(self, source):
        interp = Interpreter()
        interp.run(source)
        return interp.output_lines

    def test_for_else_no_break(self):
        output = self._run('''
for x in [1, 2, 3] {
    print(x)
} else {
    print("completed")
}
''')
        assert output[-1] == "completed"

    def test_for_else_with_break(self):
        output = self._run('''
for x in [1, 2, 3, 4, 5] {
    if x == 3 { break }
} else {
    print("completed")
}
print("done")
''')
        assert output[-1] == "done"
        assert "completed" not in output

    def test_for_else_empty_iterable(self):
        output = self._run('''
for x in [] {
    print("never")
} else {
    print("empty done")
}
''')
        assert output[-1] == "empty done"

    def test_for_else_search_pattern(self):
        """Classic use case: search and report if not found."""
        output = self._run('''
let items = [1, 2, 3, 4, 5]
let mut found = false
for x in items {
    if x == 3 {
        found = true
        break
    }
} else {
    print("not found")
}
if found { print("found 3") }
''')
        assert output[-1] == "found 3"
        assert "not found" not in output

# p6_Steinberg_Jacob.py
# Jacob Steinberg
# z23812823
# COP 4045 - Python Programming
# Homework 3 - Problem 6

from __future__ import annotations


class Entry:
    def __init__(self, name: str, parent: Entry | None = None) -> None:
        self.name = name
        self._parent = parent

    def parent(self) -> Entry | None:
        return self._parent

    def size(self) -> int:
        raise NotImplementedError("Subclasses must implement size().")

    def absolute_path(self) -> list[Entry]:
        parent = self.parent()
        if parent is None:
            return [self]
        return [self] + parent.absolute_path()


class File(Entry):
    def __init__(
        self, name: str, bytes_used: int, parent: Entry | None = None
    ) -> None:
        super().__init__(name, parent)

        if bytes_used < 0:
            raise ValueError("bytes_used cannot be negative")

        self.bytes_used = bytes_used

    def size(self) -> int:
        return self.bytes_used


class Folder(Entry):

    def __init__(self, name: str, parent: Entry | None = None) -> None:
        super().__init__(name, parent)
        self._children: list[Entry] = []

    def add(self, entry: Entry) -> None:
        self._children.append(entry)
        entry._parent = self

    def children(self) -> tuple[Entry, ...]:
        return tuple(self._children)

    def size(self) -> int:
        return sum(child.size() for child in self._children)


def find_large_files(entry: Entry, minimum_size: int) -> list[File]:

    if isinstance(entry, File):
        if entry.size() >= minimum_size:
            return [entry]
        return []

    if isinstance(entry, Folder):
        matches: list[File] = []

        for child in entry.children():
            matches.extend(find_large_files(child, minimum_size))

        return matches

    return []

def test_file_system() -> None:
    """Test folder sizes, parent paths, and recursive file searching."""
    root = Folder("root")
    documents = Folder("documents")
    small_file = File("notes.txt", 100)
    large_file = File("report.pdf", 500)

    root.add(documents)
    root.add(small_file)
    documents.add(large_file)

    assert small_file.size() == 100
    assert documents.size() == 500
    assert root.size() == 600
    assert large_file.parent() is documents
    assert documents.children() == (large_file,)
    assert large_file.absolute_path() == [large_file, documents, root]
    assert find_large_files(root, 300) == [large_file]
    assert find_large_files(root, 600) == []

    print("All tests passed!")


if __name__ == "__main__":
    test_file_system()


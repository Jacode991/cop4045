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

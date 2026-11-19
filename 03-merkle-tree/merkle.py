"""A tiny Merkle tree: commit to a list, then prove one item is in it."""
from hashlib import sha256


def h(*parts: bytes) -> bytes:
    return sha256(b"".join(parts)).digest()


def build(leaves: list[bytes]) -> list[list[bytes]]:
    """Return every level of the tree, leaves first, root last."""
    level = [h(leaf) for leaf in leaves]
    levels = [level]
    while len(level) > 1:
        if len(level) % 2:                      # odd count: duplicate the last node
            level = level + [level[-1]]
        level = [h(level[i], level[i + 1]) for i in range(0, len(level), 2)]
        levels.append(level)
    return levels


def prove(levels: list[list[bytes]], index: int) -> list[tuple[bytes, bool]]:
    """Collect the sibling at each level. The bool says 'sibling is on the right'."""
    path = []
    for level in levels[:-1]:
        if len(level) % 2:
            level = level + [level[-1]]
        sibling = index ^ 1                     # flip the last bit: 4<->5, 6<->7
        path.append((level[sibling], sibling > index))
        index //= 2
    return path


def verify(root: bytes, leaf: bytes, path: list[tuple[bytes, bool]]) -> bool:
    node = h(leaf)
    for sibling, sibling_on_right in path:
        node = h(node, sibling) if sibling_on_right else h(sibling, node)
    return node == root


if __name__ == "__main__":
    fruits = [b"apple", b"banana", b"cherry", b"date", b"elderberry"]
    levels = build(fruits)
    root = levels[-1][0]
    print("root:", root.hex())

    proof = prove(levels, 2)                    # prove "cherry" is in the list
    print("proof size:", len(proof), "hashes for", len(fruits), "leaves")
    assert verify(root, b"cherry", proof)
    assert not verify(root, b"durian", proof)   # wrong leaf -> fails
    print("all checks passed")

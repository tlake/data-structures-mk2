# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import pytest
from structures.hash_table import HashTable


@pytest.fixture
def words_table():
    ht = HashTable(10 ** 6)

    with open('/usr/share/dict/words', 'r') as fh:
        for line in fh:
            ht.set(line.strip(), line.strip())

    return ht


def test_init():
    ht = HashTable(1024)
    assert len(ht.table_list) == 1024


def test_hash():
    ht = HashTable(4)

    assert ht._hash('a') == 1
    assert ht._hash('d') == 0
    assert ht._hash('e') == 1

    ht = HashTable(8)

    assert ht._hash('a') == 1
    assert ht._hash('d') == 4
    assert ht._hash('e') == 5
    assert ht._hash('h') == 0


def test_set():
    ht = HashTable(4)
    ht.set('pterodactyl', 'pterodactyl')
    ht.set

    assert ht.table_list[3] == [('pterodactyl', 'pterodactyl')]

    ht.set('c', 'c')
    assert ht.table_list[3] == [('pterodactyl', 'pterodactyl'), ('c', 'c')]

    ht.set('a', 'a')
    assert ht.table_list[1] == [('a', 'a')]

    with pytest.raises(TypeError):
        ht.set(1, 2)


def test_get(words_table):
    ht = words_table

    with open('/usr/share/dict/words', 'r') as fh:
        for line in fh:
            assert ht.get(line.strip()) == line.strip()

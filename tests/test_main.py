import os, io, json, math, re, importlib
import pytest
mod = importlib.import_module('main')


def test_version_orden():
    a = mod.Version("1.2.10")
    b = mod.Version("1.3.0")
    c = mod.Version("1.2.10")
    assert a < b
    assert a == c
    assert repr(a).startswith("Version(")

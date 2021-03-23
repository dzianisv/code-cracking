#!/usr/bin/env python3

import pytest
import subprocess

@pytest.yield_fixture
def proc_fixture():
    proc = subprocess.Popen(["/usr/bin/echo", "hello world"])
    yield proc
    proc.terminate()
    try:
        proc.wait(timeout=3)
    except subprocess.TimeoutExpired:
        proc.kill()
        proc.wait()

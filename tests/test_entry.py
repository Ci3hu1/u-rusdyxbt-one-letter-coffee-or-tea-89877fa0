"""Tests for the One Letter: Coffee or Tea entry.

Run: python3 -m unittest discover -s tests -v
"""

import os
import stat
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from main import LETTER  # noqa: E402


class TestEntry(unittest.TestCase):
    def test_letter_is_exactly_one_char(self):
        """The gate demands exactly 1 character, not whitespace-only."""
        self.assertEqual(len(LETTER), 1)
        self.assertIn(LETTER, ("A", "B"))
        self.assertTrue(LETTER.strip(), "letter must not be whitespace")

    def test_program_writes_exactly_one_byte(self):
        """main.py writes exactly LETTER with no trailing newline."""
        with tempfile.TemporaryDirectory() as tmp:
            env = dict(os.environ, ENTRY_OUTPUT_DIR=tmp)
            result = subprocess.run(
                [sys.executable, str(ROOT / "main.py")],
                env=env,
                capture_output=True,
                text=True,
                timeout=30,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            out = Path(tmp) / "entry.txt"
            self.assertTrue(out.is_file())
            data = out.read_bytes()
            self.assertEqual(data, LETTER.encode("utf-8"))
            self.assertEqual(len(data), 1, "gate: exactly 1 character")
            self.assertEqual(data.decode("utf-8"), "A")
            mode = stat.S_IMODE(out.stat().st_mode)
            self.assertEqual(mode, 0o644, "output must be world-readable")


if __name__ == "__main__":
    unittest.main()

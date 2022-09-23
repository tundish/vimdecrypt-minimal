#!/usr/bin/env python3
# encoding: utf-8

# Tool for decrypting vim (blowfish2) encrypted files.
# Copyright (C) 2020 Gertjan van Zwieten

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

import unittest

from vimdecrypt import decrypt


class Test(unittest.TestCase):
  def test(self):
    import io
    f = io.BytesIO(b'VimCrypt~03!\xff\xcf\xe2R\x9b\xe0\xa9\x85\xa20\xf4S\x95)18A\xaa,\x11\x83\x98\xfb}i\xfa\xff\xf1\xc6|,')
    self.assertEqual(decrypt(f, 'my password'), 'my secret text\n')
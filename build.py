"""Builds photo-booth.min.js from photo-booth.js.

Edit photo-booth.js, bump VERSION, run this, then upload both files to GitHub
and publish a release tagged with the same version.

Needs the rjsmin package (pip install rjsmin).
"""
from pathlib import Path

import rjsmin

VERSION = '2.2.0'

HERE = Path(__file__).parent
BANNER = '/*! Postcard Photo Booth v' + VERSION + ' · Tides Studio · tidesstudio.com */\n'

source = (HERE / 'photo-booth.js').read_text(encoding='utf-8')
(HERE / 'photo-booth.min.js').write_text(BANNER + rjsmin.jsmin(source).strip() + '\n', encoding='utf-8')
print('Built photo-booth.min.js', VERSION)

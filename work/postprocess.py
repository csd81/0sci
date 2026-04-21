#!/usr/bin/env python3
"""Post-process marker output for Heath's Scientific Computing.

Removes page-break artifacts (running headers/page numbers that leaked into
prose). Two safe patterns only:

  1. Header embedded inside a word hyphenated across a page break, e.g.
     "...sophisticated perxvi Preface\n\nspective, however..."
     We detect this because the header is sandwiched between \w fragments
     with a paragraph break after it — a very specific signature.

  2. Standalone running headers that ended up as their own paragraph, i.e.
     sandwiched between \n\n on both sides.

We deliberately do NOT try to remove "inline" headers inside running prose
because the matcher cannot distinguish them from ordinary phrasing like
"from Chapter 4 to Chapter 3" or "the computer exercises in the book".
"""
import re
import sys
import shutil
from pathlib import Path

SRC_ROOT = Path('/home/rama/Desktop/0sci/chapters_md')
DST_ROOT = Path('/home/rama/Desktop/0sci/chapters')

# Header keywords that appear in this book's running headers.
# Only tokens that are rare/absent in prose context — we dropped
# "Exercises" and single words that are ambiguous.
HDR = (r'(?:Preface(?:\s+to\s+the\s+Classics\s+Edition)?'
       r'|Notation'
       r'|Contents'
       r'|Bibliography'
       r'|Index'
       r'|Computer\s+Problems'
       r'|Review\s+Questions'
       r'|Chapter\s+\d+(?:[:.]\s+[^\n]{1,60})?'
       r'|\d+\.\d+\s+[^\n]{1,60})')
PAGENUM = r'(?:\d{1,4}|[ivxlcdm]{2,6})'   # multi-char roman only — avoid bare "i"/"m"
HDR_PAIR = (r'(?:' + PAGENUM + r'\s+' + HDR +
            r'|' + HDR + r'\s+' + PAGENUM + r')')

# Case A: header fragment embedded mid-word across a line break.
# Anchored by \n\n (paragraph break) between header and the word tail —
# that's the signature of a page-break hyphenation.
EMBED = re.compile(
    r'(\w+?)'                          # left fragment
    r'\s*' + HDR_PAIR + r'\s*\n\n'     # header + paragraph break
    r'(\w+)',                          # right fragment
    re.IGNORECASE,
)

# Case B: running header as its own paragraph.
STANDALONE = re.compile(
    r'\n\n\s*' + HDR_PAIR + r'\s*\n\n',
    re.IGNORECASE,
)

# Lone page number on its own line (rare but seen).
LONE_PAGENUM = re.compile(r'(?m)^\s*' + PAGENUM + r'\s*$')

# HTML sup/sub outside math — normalize to markdown-ish superscripts since
# marker leaves them in for typographic (not mathematical) use.
SUP_RE = re.compile(r'<sup>(.*?)</sup>', re.DOTALL)
SUB_RE = re.compile(r'<sub>(.*?)</sub>', re.DOTALL)


def glue_embedded_headers(text: str) -> tuple[str, int]:
    n = 0

    def _glue(m):
        nonlocal n
        n += 1
        return m.group(1) + m.group(m.lastindex)

    return EMBED.sub(_glue, text), n


def drop_standalone_headers(text: str) -> tuple[str, int]:
    new, n1 = STANDALONE.subn('\n\n', text)
    new, n2 = LONE_PAGENUM.subn('', new)
    new = re.sub(r'\n{3,}', '\n\n', new)
    return new, n1 + n2


def normalize_html_supsub(text: str) -> tuple[str, int]:
    n = 0

    def _sup(m):
        nonlocal n
        n += 1
        inner = m.group(1).strip()
        return f'^{{{inner}}}' if len(inner) > 1 else f'^{inner}'

    def _sub(m):
        nonlocal n
        n += 1
        inner = m.group(1).strip()
        return f'_{{{inner}}}' if len(inner) > 1 else f'_{inner}'

    new = SUP_RE.sub(_sup, text)
    new = SUB_RE.sub(_sub, new)
    return new, n


def process_file(src: Path, dst: Path) -> dict:
    text = src.read_text(encoding='utf-8')
    stats = {'file': dst.name, 'orig_chars': len(text)}
    text, stats['glued'] = glue_embedded_headers(text)
    text, stats['standalone_hdrs'] = drop_standalone_headers(text)
    text, stats['html_supsub'] = normalize_html_supsub(text)
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(text.rstrip() + '\n', encoding='utf-8')
    stats['final_chars'] = len(text)
    return stats


def copy_assets(src_dir: Path, dst_assets_dir: Path) -> int:
    count = 0
    for ext in ('*.png', '*.jpg', '*.jpeg'):
        for p in src_dir.glob(ext):
            dst_assets_dir.mkdir(parents=True, exist_ok=True)
            shutil.copy2(p, dst_assets_dir / p.name)
            count += 1
    return count


def main() -> int:
    if not SRC_ROOT.exists():
        print(f'Source dir not found: {SRC_ROOT}', file=sys.stderr)
        return 1
    DST_ROOT.mkdir(parents=True, exist_ok=True)

    results = []
    for chapter_dir in sorted(SRC_ROOT.iterdir()):
        if not chapter_dir.is_dir():
            continue
        md = chapter_dir / f'{chapter_dir.name}.md'
        if not md.exists():
            continue
        dst_md = DST_ROOT / f'{chapter_dir.name}.md'
        assets = DST_ROOT / f'{chapter_dir.name}_assets'
        stats = process_file(md, dst_md)
        stats['images'] = copy_assets(chapter_dir, assets)
        if stats['images'] == 0 and assets.exists():
            try: assets.rmdir()
            except OSError: pass
        results.append(stats)

    print(f'{"file":42} {"glued":>6} {"stdalone":>9} {"sup/sub":>8} {"imgs":>5}')
    for s in results:
        print(f'{s["file"]:42} {s["glued"]:>6} {s["standalone_hdrs"]:>9} '
              f'{s["html_supsub"]:>8} {s["images"]:>5}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

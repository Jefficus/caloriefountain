# -*- coding: utf-8 -*-

# Copyright © 2023 Jefferson Smith, Roberto Alsina et al.

# Permission is hereby granted, free of charge, to any
# person obtaining a copy of this software and associated
# documentation files (the "Software"), to deal in the
# Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the
# Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice
# shall be included in all copies or substantial portions of
# the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY
# KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
# WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR
# PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS
# OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR
# OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
# OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

"""Markdown Extension for Nikola.

- Specific post-processing.
- Strikethrough inline patterns.
"""

import re

from nikola.plugin_categories import MarkdownExtension

try:
    from markdown.postprocessors import Postprocessor
    from markdown.inlinepatterns import SimpleTagPattern
    from markdown.extensions import Extension
except ImportError:
    # No need to catch this, if you try to use this without Markdown,
    # the markdown compiler will fail first
    Postprocessor = SimpleTagPattern = Extension = object


CODERE = re.compile('<reference>(.*?)</reference>', flags=re.MULTILINE | re.DOTALL)
OBSLINK_RE = r"(\[{2})(.+?)(\]{2})"  # [[pagelink]]


class ObsidianPostProcessor(Postprocessor):
    """Obsidian-specific post-processing for Markdown."""

    def run(self, text):
        """Run the postprocessor."""
        output = text

        # python-markdown's highlighter uses <div class="codehilite"><pre>
        # for code.  We switch it to reST's <pre class="code">.
        # TODO: monkey-patch for CodeHilite that uses nikola.utils.NikolaPygmentsHTML
        # output = CODERE.sub('<pre class="code literal-block">\\1</pre>', output)
        output = CODERE.sub('<a href="/posts/\\1.md">\\1</a>', output)
        return output


class ObsidianExtension(MarkdownExtension, Extension):
    """Obsidian Markdown extensions."""

    def _add_obslink_post_processor(self, md):
        """Extend Markdown with the postprocessor."""
        pp = ObsidianPostProcessor()
        md.postprocessors.register(pp, 'obsidian_post_processor', 1)

    def _add_obslink_inline_pattern(self, md):
        """Support PHP-Markdown style strikethrough, for example: ``[[page link]]``."""
        pattern = SimpleTagPattern(OBSLINK_RE, 'reference')
        md.inlinePatterns.register(pattern, 'reference', 175)

    def extendMarkdown(self, md, md_globals=None):
        """Extend markdown to Obsidian flavoured page links."""
        self._add_obslink_post_processor(md)
        self._add_obslink_inline_pattern(md)
        md.registerExtension(self)


def makeExtension(configs=None):  # pragma: no cover
    """Make extension."""
    return ObsidianExtension(configs)

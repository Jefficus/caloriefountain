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
- Reveal teaser split as visible mark
- This is only being done as a Markdown Extension
- because I already know how to do that. :-)
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


TEASERPAT = '<!-- TEASER_END -->'
REVEALHTML = "<hr class='teaserbreak'>"


class TeaserSplitPostProcessor(Postprocessor):
    """Teaser post-processing for Markdown."""

    def run(self, text):
        """Run the postprocessor."""
        output = text

        # Find the teaser pattern if it's there and 
        # insert an HR tag after it. We can't remove
        # the teaser tag itself, because templates use
        # that to figure out where to stop rendering
        # the teaser preview.
        output = re.sub(TEASERPAT, 
                        f"{TEASERPAT}\n{REVEALHTML}", 
                        output)
        return output


class TeaserSplitExtension(MarkdownExtension, Extension):
    """Teaser Markdown extensions."""

    def _add_teasersplit_post_processor(self, md):
        """Extend Markdown with the postprocessor."""
        pp = TeaserSplitPostProcessor()
        md.postprocessors.register(pp, 'teasersplit_post_processor', 1)

    # def _add_teasersplit_inline_pattern(self, md):
    #     """Support PHP-Markdown style strikethrough, for example: ``[[page link]]``."""
    #     pattern = SimpleTagPattern(TEASERPAT, 'entity')
    #     md.inlinePatterns.register(pattern, 'entity', 75)

    def extendMarkdown(self, md, md_globals=None):
        """Extend markdown to Obsidian flavoured page links."""
        self._add_teasersplit_post_processor(md)
        # self._add_teasersplit_inline_pattern(md)
        md.registerExtension(self)


def makeExtension(configs=None):  # pragma: no cover
    """Make extension."""
    return TeaserSplitExtension(configs)

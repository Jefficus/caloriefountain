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
- Obsidian links don't render properly in python markdown
- so fix the generated HTML.
"""

import re
import os

from nikola.plugin_categories import MarkdownExtension

try:
    from markdown.postprocessors import Postprocessor
    from markdown.inlinepatterns import SimpleTagPattern
    from markdown.extensions import Extension
except ImportError:
    # No need to catch this, if you try to use this without Markdown,
    # the markdown compiler will fail first
    Postprocessor = SimpleTagPattern = Extension = object


IMAGELINKPAT = '!<img class="float-right blogthumb" src="(.*?)">'


class ObsidianHTMLImageLinkPostProcessor(Postprocessor):
    """Converter for image links generated from Obsidian markdown."""


    def run(self, text):
        """Run the postprocessor."""
        output = text

        def replacer(m):
            oldlink = m.group(1)
            # ensure image is accessing thumbnail of image
            # rather than full image
            # if not '.thumbnail' in oldlink:
            #     path,ext = os.path.splitext(oldlink)
            #     oldlink = path + ".thumbnail" + ext
            newurl = f"/posts/images{oldlink}"
            newhtml = f'<img class="float-right blogthumb" src="{newurl}">'
            return newhtml

        # Find the already-process img link pattern (if there) 
        # and modify it to use approp Nikola paths.
        output = re.sub(IMAGELINKPAT, replacer, output)
        
        return output


class ObsidianLinkConverterExtension(MarkdownExtension, Extension):
    """Obsidian image link converter Markdown extensions."""

    def _add_imglink_post_processor(self, md):
        """Extend Markdown with the postprocessor."""
        pp = ObsidianHTMLImageLinkPostProcessor()
        md.postprocessors.register(pp, 'obsidian_link_converter_extension', 1)

    def extendMarkdown(self, md, md_globals=None):
        """Extend markdown to Obsidian flavoured page links."""
        self._add_imglink_post_processor(md)
        md.registerExtension(self)


def makeExtension(configs=None):  # pragma: no cover
    """Make extension."""
    return ObsidianLinkConverterExtension(configs)

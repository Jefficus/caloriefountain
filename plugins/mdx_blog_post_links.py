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
- Obsidian blog post links don't contain a /posts prefix
- so give them one.
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


BLOGPOSTLINKPAT = '<a class="bloglink" href="(.*?)">'


class ObsidianHTMLBlogPostLinkProcessor(Postprocessor):
    """Converter for blog post links generated from Obsidian markdown."""


    def run(self, text):
        """Run the postprocessor."""
        output = text

        def replacer(m):
            oldlink = m.group(1)
            # ensure link is referencing /posts
            if "/posts/" in oldlink:
                newurl = oldlink
            else:
                newurl = f"/posts/{oldlink}"
            newhtml = f'<a class="bloglink obsidian" href="{newurl}">'
            return newhtml

        # Find the already-processed blog link pattern (if there) 
        # and modify it to use approp Nikola paths.
        output = re.sub(BLOGPOSTLINKPAT, replacer, output)
        
        return output


class ObsidianBlogLinkConverterExtension(MarkdownExtension, Extension):
    """Obsidian blog link converter Markdown extensions."""

    def _add_bloglink_post_processor(self, md):
        """Extend Markdown with the postprocessor."""
        pp = ObsidianHTMLBlogPostLinkProcessor()
        md.postprocessors.register(pp, 'obsidian_blog_link_converter_extension', 1)

    def extendMarkdown(self, md, md_globals=None):
        """Extend markdown to Obsidian flavoured page links."""
        self._add_bloglink_post_processor(md)
        md.registerExtension(self)


def makeExtension(configs=None):  # pragma: no cover
    """Make extension."""
    return ObsidianBlogLinkConverterExtension(configs)

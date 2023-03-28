# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1680021607.290228
_enable_loop = True
_template_filename = 'themes/caloriefountain/templates/index.tmpl'
_template_uri = 'index.tmpl'
_source_encoding = 'utf-8'
_exports = ['extra_head', 'content', 'content_header', 'before_content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('helper', context._clean_inheritance_tokens(), templateuri='index_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'helper')] = ns

    ns = runtime.TemplateNamespace('math', context._clean_inheritance_tokens(), templateuri='math_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'math')] = ns

    ns = runtime.TemplateNamespace('comments', context._clean_inheritance_tokens(), templateuri='comments_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'comments')] = ns

    ns = runtime.TemplateNamespace('pagination', context._clean_inheritance_tokens(), templateuri='pagination_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'pagination')] = ns

    ns = runtime.TemplateNamespace('feeds_translations', context._clean_inheritance_tokens(), templateuri='feeds_translations_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'feeds_translations')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, 'feeds_translations')._populate(_import_ns, ['*'])
        posts = _import_ns.get('posts', context.get('posts', UNDEFINED))
        multiple_authors_per_post = _import_ns.get('multiple_authors_per_post', context.get('multiple_authors_per_post', UNDEFINED))
        featured = _import_ns.get('featured', context.get('featured', UNDEFINED))
        feeds_translations = _mako_get_namespace(context, 'feeds_translations')
        sorted = _import_ns.get('sorted', context.get('sorted', UNDEFINED))
        def before_content():
            return render_before_content(context._locals(__M_locals))
        comments = _mako_get_namespace(context, 'comments')
        def content():
            return render_content(context._locals(__M_locals))
        page_links = _import_ns.get('page_links', context.get('page_links', UNDEFINED))
        prev_next_links_reversed = _import_ns.get('prev_next_links_reversed', context.get('prev_next_links_reversed', UNDEFINED))
        kind = _import_ns.get('kind', context.get('kind', UNDEFINED))
        prevlink = _import_ns.get('prevlink', context.get('prevlink', UNDEFINED))
        def content_header():
            return render_content_header(context._locals(__M_locals))
        set = _import_ns.get('set', context.get('set', UNDEFINED))
        permalink = _import_ns.get('permalink', context.get('permalink', UNDEFINED))
        list = _import_ns.get('list', context.get('list', UNDEFINED))
        index_file = _import_ns.get('index_file', context.get('index_file', UNDEFINED))
        pagekind = _import_ns.get('pagekind', context.get('pagekind', UNDEFINED))
        is_frontmost_index = _import_ns.get('is_frontmost_index', context.get('is_frontmost_index', UNDEFINED))
        front_index_header = _import_ns.get('front_index_header', context.get('front_index_header', UNDEFINED))
        theme_config = _import_ns.get('theme_config', context.get('theme_config', UNDEFINED))
        _link = _import_ns.get('_link', context.get('_link', UNDEFINED))
        current_page = _import_ns.get('current_page', context.get('current_page', UNDEFINED))
        author_pages_generated = _import_ns.get('author_pages_generated', context.get('author_pages_generated', UNDEFINED))
        site_has_comments = _import_ns.get('site_has_comments', context.get('site_has_comments', UNDEFINED))
        nextlink = _import_ns.get('nextlink', context.get('nextlink', UNDEFINED))
        math = _mako_get_namespace(context, 'math')
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        date_format = _import_ns.get('date_format', context.get('date_format', UNDEFINED))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        index_teasers = _import_ns.get('index_teasers', context.get('index_teasers', UNDEFINED))
        pagination = _mako_get_namespace(context, 'pagination')
        helper = _mako_get_namespace(context, 'helper')
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'before_content'):
            context['self'].before_content(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'feeds_translations')._populate(_import_ns, ['*'])
        index_file = _import_ns.get('index_file', context.get('index_file', UNDEFINED))
        posts = _import_ns.get('posts', context.get('posts', UNDEFINED))
        math = _mako_get_namespace(context, 'math')
        def extra_head():
            return render_extra_head(context)
        permalink = _import_ns.get('permalink', context.get('permalink', UNDEFINED))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n    ')
        __M_writer(str(parent.extra_head()))
        __M_writer('\n')
        if posts and (permalink == '/' or permalink == '/' + index_file):
            __M_writer('        <link rel="prefetch" href="')
            __M_writer(str(posts[0].permalink()))
            __M_writer('" type="text/html">\n')
        __M_writer('    ')
        __M_writer(str(math.math_styles_ifposts(posts)))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'feeds_translations')._populate(_import_ns, ['*'])
        posts = _import_ns.get('posts', context.get('posts', UNDEFINED))
        multiple_authors_per_post = _import_ns.get('multiple_authors_per_post', context.get('multiple_authors_per_post', UNDEFINED))
        feeds_translations = _mako_get_namespace(context, 'feeds_translations')
        sorted = _import_ns.get('sorted', context.get('sorted', UNDEFINED))
        _link = _import_ns.get('_link', context.get('_link', UNDEFINED))
        comments = _mako_get_namespace(context, 'comments')
        current_page = _import_ns.get('current_page', context.get('current_page', UNDEFINED))
        author_pages_generated = _import_ns.get('author_pages_generated', context.get('author_pages_generated', UNDEFINED))
        def content():
            return render_content(context)
        page_links = _import_ns.get('page_links', context.get('page_links', UNDEFINED))
        prev_next_links_reversed = _import_ns.get('prev_next_links_reversed', context.get('prev_next_links_reversed', UNDEFINED))
        kind = _import_ns.get('kind', context.get('kind', UNDEFINED))
        prevlink = _import_ns.get('prevlink', context.get('prevlink', UNDEFINED))
        site_has_comments = _import_ns.get('site_has_comments', context.get('site_has_comments', UNDEFINED))
        nextlink = _import_ns.get('nextlink', context.get('nextlink', UNDEFINED))
        def content_header():
            return render_content_header(context)
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        math = _mako_get_namespace(context, 'math')
        set = _import_ns.get('set', context.get('set', UNDEFINED))
        date_format = _import_ns.get('date_format', context.get('date_format', UNDEFINED))
        permalink = _import_ns.get('permalink', context.get('permalink', UNDEFINED))
        list = _import_ns.get('list', context.get('list', UNDEFINED))
        pagekind = _import_ns.get('pagekind', context.get('pagekind', UNDEFINED))
        front_index_header = _import_ns.get('front_index_header', context.get('front_index_header', UNDEFINED))
        index_teasers = _import_ns.get('index_teasers', context.get('index_teasers', UNDEFINED))
        pagination = _mako_get_namespace(context, 'pagination')
        helper = _mako_get_namespace(context, 'helper')
        __M_writer = context.writer()
        __M_writer('\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content_header'):
            context['self'].content_header(**pageargs)
        

        __M_writer('\n')
        if not 'targets' in permalink:
            if 'main_index' in pagekind:
                __M_writer('            ')
                __M_writer(str(front_index_header))
                __M_writer('\n')
            if page_links:
                __M_writer('            ')
                __M_writer(str(pagination.page_navigation(current_page, page_links, prevlink, nextlink, prev_next_links_reversed)))
                __M_writer('\n')
            __M_writer('        <div class="postindex">\n')
            for post in posts:
                __M_writer('                <article class="h-entry post-')
                __M_writer(str(post.meta('type')))
                __M_writer('" itemscope="itemscope" itemtype="http://schema.org/Article">\n                <header>\n                    <h1 class="p-name entry-title"><a href="')
                __M_writer(str(post.permalink()))
                __M_writer('" class="u-url">')
                __M_writer(filters.html_escape(str(post.title())))
                __M_writer('</a></h1>\n                    <div class="metadata">\n                        <p class="byline author vcard"><span class="byline-name fn" itemprop="author">\n')
                if author_pages_generated and multiple_authors_per_post:
                    for author in post.authors():
                        __M_writer('                                <a href="')
                        __M_writer(str(_link('author', author)))
                        __M_writer('">')
                        __M_writer(filters.html_escape(str(author)))
                        __M_writer('</a>\n')
                elif author_pages_generated:
                    __M_writer('                            <a href="')
                    __M_writer(str(_link('author', post.author())))
                    __M_writer('">')
                    __M_writer(filters.html_escape(str(post.author())))
                    __M_writer('</a>\n')
                else:
                    __M_writer('                            ')
                    __M_writer(filters.html_escape(str(post.author())))
                    __M_writer('\n')
                __M_writer('                        </span></p>\n                <p class="dateline">\n                <a href="')
                __M_writer(str(post.permalink()))
                __M_writer('" rel="bookmark">\n                <time class="published dt-published" datetime="')
                __M_writer(str(post.formatted_date('webiso')))
                __M_writer('" itemprop="datePublished" title="')
                __M_writer(filters.html_escape(str(post.formatted_date(date_format))))
                __M_writer('">')
                __M_writer(filters.html_escape(str(post.formatted_date(date_format))))
                __M_writer('</time>\n')
                if post.updated and post.updated != post.date:
                    __M_writer('                    <span class="updated"> (')
                    __M_writer(str(messages("updated")))
                    __M_writer('\n                        <time class="dt-updated" datetime="')
                    __M_writer(str(post.formatted_updated('webiso')))
                    __M_writer('" itemprop="dateUpdated" title="')
                    __M_writer(filters.html_escape(str(post.formatted_updated(date_format))))
                    __M_writer('">')
                    __M_writer(filters.html_escape(str(post.formatted_updated(date_format))))
                    __M_writer('</time>)</span>\n')
                __M_writer('                </a>\n                </p>\n')
                if not post.meta('nocomments') and site_has_comments:
                    __M_writer('                            <p class="commentline">')
                    __M_writer(str(comments.comment_link(post.permalink(), post._base_path)))
                    __M_writer('\n')
                __M_writer('                    </div>\n                </header>\n')
                if index_teasers:
                    __M_writer('                    <div class="p-summary entry-summary">\n                        ')
                    __M_writer(str(post.text(teaser_only=True)))
                    __M_writer('\n                    </div>\n')
                else:
                    __M_writer('                    <div class="e-content entry-content">\n                        ')
                    __M_writer(str(post.text(teaser_only=False)))
                    __M_writer('\n                    </div>\n')
                __M_writer('                </article>\n')
            __M_writer('        </div>\n')
        else:
            __M_writer('        <!-- Dashboard -->\n        <div class="postindex">\n            <table id="mytab" class="table sortable">\n            <thead>\n            <tr>\n                <th scope="col">Status</th>\n                <th scope="col">Target Name</th>\n                <th scope="col">Started</th>\n                <th scope="col">Goal</th>\n            </tr>\n            </thead>\n            <tbody>\n')
            for post in sorted(posts,reverse=True,key=lambda x:list(set(['today','thisweek','completed','unsuccessful']).intersection(set(x.tags)))):
                __M_writer('                    <tr>\n                    <td>\n')
                if 'today' in post.tags or 'thisweek' in post.tags:
                    __M_writer('                            <img src="/images/active_solid.svg" class="flagicon">\n                            <span style="display:none">1</span>\n')
                elif 'unsuccessful' in post.tags:
                    __M_writer('                            <img src="/images/failure_hollow.svg" class="flagicon">\n                            <span style="display:none">4</span>\n')
                elif 'completed' in post.tags:
                    __M_writer('                            <img src="/images/success_hollow.svg" class="flagicon">\n                            <span style="display:none">3</span>\n')
                else:
                    __M_writer('                            <img src="/images/paused_solid.svg" class="flagicon">\n                            <span style="display:none">2</span>\n')
                __M_writer('                    </td>\n                    <td><a href="')
                __M_writer(str(post.permalink()))
                __M_writer('" class="u-url bloglink">\n                        ')
                __M_writer(filters.html_escape(str(' '.join(post.title().split()[1:]))))
                __M_writer('\n                        </a>\n                    </td>\n                    <td class="text-nowrap">\n                        ')
                __M_writer(filters.html_escape(str(post.formatted_date('yyyy-MM-dd'))))
                __M_writer('\n                    </td>\n                    <td>')
                __M_writer(str(' '.join(post.text(teaser_only=True,show_read_more_link=True).split()[1:])))
                __M_writer('</td>\n                    </tr>\n')
            __M_writer('            </tbody>\n            </table>\n        </div>\n')
        __M_writer('\n    ')
        __M_writer(str(helper.html_pager()))
        __M_writer('\n    ')
        __M_writer(str(comments.comment_link_script()))
        __M_writer('\n    ')
        __M_writer(str(math.math_scripts_ifposts(posts)))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_header(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'feeds_translations')._populate(_import_ns, ['*'])
        def content_header():
            return render_content_header(context)
        feeds_translations = _mako_get_namespace(context, 'feeds_translations')
        kind = _import_ns.get('kind', context.get('kind', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n        ')
        __M_writer(str(feeds_translations.translation_link(kind)))
        __M_writer('\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_before_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'feeds_translations')._populate(_import_ns, ['*'])
        pagekind = _import_ns.get('pagekind', context.get('pagekind', UNDEFINED))
        featured = _import_ns.get('featured', context.get('featured', UNDEFINED))
        is_frontmost_index = _import_ns.get('is_frontmost_index', context.get('is_frontmost_index', UNDEFINED))
        theme_config = _import_ns.get('theme_config', context.get('theme_config', UNDEFINED))
        def before_content():
            return render_before_content(context)
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n')
        if 'main_index' in pagekind and is_frontmost_index and featured and (theme_config.get('featured_large') or theme_config.get('featured_small')):
            if theme_config.get('featured_on_mobile'):
                __M_writer('            <div class="d-block">\n')
            else:
                __M_writer('            <div class="d-none d-md-block">\n')
            if featured and theme_config.get('featured_large'):
                __M_writer('        <div class="jumbotron p-0 text-white rounded bg-dark">\n            <div class="row bootblog4-featured-jumbotron-row">\n                <div class="col-md-6 p-3 p-md-4 pr-0 h-md-250 bootblog4-featured-text">\n                    <h1 class="display-4 font-italic"><a class="text-white" href="')
                __M_writer(str(featured[0].permalink()))
                __M_writer('">')
                __M_writer(str(featured[0].title()))
                __M_writer('</a></h1>\n')
                if featured[0].previewimage:
                    __M_writer('                            <div class="lead my-3 mb-0">')
                    __M_writer(str(featured[0].text(teaser_only=True, strip_html=theme_config.get('featured_strip_html', True))))
                    __M_writer('</div>\n                        </div>\n')
                    if theme_config.get('featured_large_image_on_mobile'):
                        __M_writer('                        <div class="col-md-6 p-0 h-md-250 text-right">\n')
                    else:
                        __M_writer('                        <div class="col-md-6 p-0 h-md-250 text-right d-none d-md-block">\n')
                    __M_writer('                            <img class="bootblog4-featured-large-image" src="')
                    __M_writer(str(featured[0].previewimage))
                    __M_writer('" alt="')
                    __M_writer(str(featured.pop(0).title()))
                    __M_writer('">\n                        </div>\n')
                else:
                    __M_writer('                        <div class="lead my-3 mb-0">')
                    __M_writer(str(featured.pop(0).text(teaser_only=True, strip_html=theme_config.get('featured_strip_html', True))))
                    __M_writer('</div>\n                        </div>\n')
                __M_writer('            </div>\n        </div>\n')
            __M_writer('\n')
            if featured and theme_config.get('featured_small'):
                __M_writer('            <div class="row mb-2">\n')
                if len(featured) == 1:
                    __M_writer('                <div class="col-md-12">\n')
                else:
                    __M_writer('                <div class="col-md-6">\n')
                __M_writer('                    <div class="card flex-md-row mb-4 box-shadow h-md-250">\n                       <div class="card-body d-flex flex-column align-items-start">\n                           <h3 class="mb-0">\n                               <a class="text-dark" href="')
                __M_writer(str(featured[0].permalink()))
                __M_writer('">')
                __M_writer(str(featured[0].title()))
                __M_writer('</a>\n                           </h3>\n')
                if featured[0].previewimage:
                    __M_writer('                               <div class="card-text mb-auto bootblog4-featured-text">')
                    __M_writer(str(featured[0].text(teaser_only=True, strip_html=theme_config.get('featured_strip_html', True))))
                    __M_writer('</div>\n                               </div>\n                               <img class="card-img-right flex-auto d-none d-lg-block" src="')
                    __M_writer(str(featured[0].previewimage))
                    __M_writer('" alt="')
                    __M_writer(str(featured.pop(0).title()))
                    __M_writer('">\n')
                else:
                    __M_writer('                           <div class="card-text mb-auto bootblog4-featured-text">')
                    __M_writer(str(featured.pop(0).text(teaser_only=True, strip_html=theme_config.get('featured_strip_html', True))))
                    __M_writer('</div>\n                           </div>\n')
                __M_writer('                    </div>\n                </div>\n\n')
                if featured:
                    __M_writer('               <div class="col-md-6">\n                    <div class="card flex-md-row mb-4 box-shadow h-md-250">\n                       <div class="card-body d-flex flex-column align-items-start">\n                           <h3 class="mb-0">\n                               <a class="text-dark" href="')
                    __M_writer(str(featured[0].permalink()))
                    __M_writer('">')
                    __M_writer(str(featured[0].title()))
                    __M_writer('</a>\n                           </h3>\n')
                    if featured[0].previewimage:
                        __M_writer('                               <div class="card-text mb-auto bootblog4-featured-text">')
                        __M_writer(str(featured[0].text(teaser_only=True, strip_html=theme_config.get('featured_strip_html', True))))
                        __M_writer('</div>\n                               </div>\n                               <img class="card-img-right flex-auto d-none d-lg-block" src="')
                        __M_writer(str(featured[0].previewimage))
                        __M_writer('" alt="')
                        __M_writer(str(featured.pop(0).title()))
                        __M_writer('">\n')
                    else:
                        __M_writer('                           <div class="card-text mb-auto bootblog4-featured-text">')
                        __M_writer(str(featured.pop(0).text(teaser_only=True, strip_html=theme_config.get('featured_strip_html', True))))
                        __M_writer('</div>\n                           </div>\n')
                    __M_writer('                    </div>\n                </div>\n')
                __M_writer('       </div>\n')
            __M_writer('    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "themes/caloriefountain/templates/index.tmpl", "uri": "index.tmpl", "source_encoding": "utf-8", "line_map": {"23": 2, "26": 3, "29": 4, "32": 5, "35": 6, "41": 0, "87": 2, "88": 3, "89": 4, "90": 5, "91": 6, "92": 7, "97": 15, "102": 119, "107": 196, "113": 9, "126": 9, "127": 10, "128": 10, "129": 11, "130": 12, "131": 12, "132": 12, "133": 14, "134": 14, "135": 14, "141": 17, "176": 17, "181": 20, "182": 21, "183": 22, "184": 23, "185": 23, "186": 23, "187": 25, "188": 26, "189": 26, "190": 26, "191": 28, "192": 29, "193": 30, "194": 30, "195": 30, "196": 32, "197": 32, "198": 32, "199": 32, "200": 35, "201": 36, "202": 37, "203": 37, "204": 37, "205": 37, "206": 37, "207": 39, "208": 40, "209": 40, "210": 40, "211": 40, "212": 40, "213": 41, "214": 42, "215": 42, "216": 42, "217": 44, "218": 46, "219": 46, "220": 47, "221": 47, "222": 47, "223": 47, "224": 47, "225": 47, "226": 48, "227": 49, "228": 49, "229": 49, "230": 50, "231": 50, "232": 50, "233": 50, "234": 50, "235": 50, "236": 52, "237": 54, "238": 55, "239": 55, "240": 55, "241": 57, "242": 59, "243": 60, "244": 61, "245": 61, "246": 63, "247": 64, "248": 65, "249": 65, "250": 68, "251": 70, "252": 71, "253": 72, "254": 84, "255": 85, "256": 87, "257": 88, "258": 90, "259": 91, "260": 93, "261": 94, "262": 96, "263": 97, "264": 100, "265": 101, "266": 101, "267": 102, "268": 102, "269": 106, "270": 106, "271": 108, "272": 108, "273": 111, "274": 115, "275": 116, "276": 116, "277": 117, "278": 117, "279": 118, "280": 118, "286": 18, "296": 18, "297": 19, "298": 19, "304": 121, "317": 121, "318": 122, "319": 123, "320": 124, "321": 125, "322": 126, "323": 128, "324": 129, "325": 132, "326": 132, "327": 132, "328": 132, "329": 133, "330": 134, "331": 134, "332": 134, "333": 136, "334": 137, "335": 138, "336": 139, "337": 141, "338": 141, "339": 141, "340": 141, "341": 141, "342": 143, "343": 144, "344": 144, "345": 144, "346": 147, "347": 150, "348": 151, "349": 152, "350": 153, "351": 154, "352": 155, "353": 156, "354": 158, "355": 161, "356": 161, "357": 161, "358": 161, "359": 163, "360": 164, "361": 164, "362": 164, "363": 166, "364": 166, "365": 166, "366": 166, "367": 167, "368": 168, "369": 168, "370": 168, "371": 171, "372": 174, "373": 175, "374": 179, "375": 179, "376": 179, "377": 179, "378": 181, "379": 182, "380": 182, "381": 182, "382": 184, "383": 184, "384": 184, "385": 184, "386": 185, "387": 186, "388": 186, "389": 186, "390": 189, "391": 192, "392": 194, "398": 392}}
__M_END_METADATA
"""

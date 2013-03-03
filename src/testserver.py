#! /usr/bin/python -tt
# -*- coding: utf-8 -*-

import flask


app = flask.Flask(__name__)


@app.route('/<doctype>/', defaults={'page': 1})
@app.route('/<doctype>/page/<int:page>')
def doctype_paging(doctype, page):
    valid_types = ['html5', 'xhtml5', 'html4.01', 'xhtml1.1']
    if page < 1:
        flask.abort(404)
    if doctype not in valid_types:
        flask.abort(404)
    is_xhtml = doctype.startswith('xhtml')
    tmpl_name = '{0}.tmpl'.format(doctype)
    next_page = flask.url_for('doctype_paging', doctype=doctype, page=page+1)
    content = flask.render_template(tmpl_name,
                                    next_page=next_page,
                                    page_num=page)
    response = flask.make_response(content)
    if is_xhtml:
        response.headers['Content-Type'] = 'application/xhtml+xml; charset=UTF-8'
    return response


if __name__ == '__main__':
    app.run(debug=True)

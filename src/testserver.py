#! /usr/bin/python -tt
# -*- coding: utf-8 -*-

import flask


app = flask.Flask(__name__)


@app.route('/<html_type>/', defaults={'page': 1})
@app.route('/<html_type>/page/<int:page>')
def html5_paging(html_type, page):
    if page < 1:
        flask.abort(404)
    is_xhtml = 'xhtml' in html_type
    content = flask.render_template('html5.html',
                                    is_xhtml=is_xhtml,
                                    next_page=flask.url_for('html5_paging',
                                                            html_type=html_type,
                                                            page=page+1),

                                    page_num=page)
    response = flask.make_response(content)
    if is_xhtml:
        response.headers['Content-Type'] = 'application/xhtml+xml; charset=UTF-8'
    return response


if __name__ == '__main__':
    app.run(debug=True)

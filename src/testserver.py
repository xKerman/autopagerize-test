#! /usr/bin/python -tt
# -*- coding: utf-8 -*-

import flask


app = flask.Flask(__name__)


@app.route('/html5/', defaults={'page': 1})
@app.route('/html5/page/<int:page>')
def html5_paging(page):
    if page < 1:
        flask.abort(404)
    return flask.render_template('html5.html',
                                 next_page=flask.url_for('html5_paging', page=page+1),
                                 page_num=page)


if __name__ == '__main__':
    app.run(debug=True)

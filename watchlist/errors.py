from flask import render_template

from watchlist import app


@app.errorhandler(404)
def page_not_found(e):
    # user = User.query.first()
    return render_template('404.html'), 404  # 返回模板和状态码
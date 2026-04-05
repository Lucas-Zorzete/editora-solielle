import os
from flask import Flask, render_template, jsonify
from flask_cors import CORS
from database import db_session, init_db
from models import Book, Author, Post, Launch, Recommendation, Article

app = Flask(__name__)
CORS(app)

with app.app_context():
    init_db()

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/novidades')
def novidades():
    books = Book.query.all()
    authors = Author.query.all()
    posts = Post.query.all()
    launches = Launch.query.all()
    recommendations = Recommendation.query.all()
    articles = Article.query.all()

    everything = []

    for b in books:
        everything.append({
            "tipo": "book",
            "titulo": b.title,
            "data": b.created_at.isoformat()
        })
    for a in authors:
        everything.append({
            "tipo": "author",
            "titulo": a.name,
            "data": a.created_at.isoformat()
        })
    for p in posts:
        everything.append({
            "tipo": "post",
            "titulo": p.title,
            "data": p.created_at.isoformat()
        })
    for l in launches:
        everything.append({
            "tipo": "launch",
            "titulo": l.title,
            "data": l.created_at.isoformat()
        })
    for r in recommendations:
        everything.append({
            "tipo": "recommendation",
            "titulo": r.title,
            "data": r.created_at.isoformat()
        })
    for a in articles:
        everything.append({
            "tipo": "article",
            "titulo": a.caption,
            "data": a.created_at.isoformat()
        })

    # do mais novo para o mais velho
    everything.sort(key=lambda x: x['data'], reverse=True)

    return(jsonify(everything))


@app.route('/api/books')
def get_books():
    books = Book.query.all()
    return jsonify([{
        "id": b.id, "title": b.title, "author": b.author,
        "genre": b.genre, "sinopse": b.synopsis,
        "price": b.price, "cover": b.cover, "link": b.link
    } for b in books])

@app.route('/api/authors')
def get_authors():
    authors = Author.query.all()
    return jsonify([{
        "name": a.name, "avatar": a.avatar, "pet": a.pet, "width": a.width,
        "emoji": a.emoji, "bio": a.bio, "account": a.account, "link": a.link 
    } for a in authors])

@app.route('/api/posts')
def get_posts():
    posts = Post.query.all()
    return jsonify([{
        "id": p.id, "title": p.title, 
        "excerpt": p.excerpt, "cover": p.cover
    } for p in posts])

@app.route('/api/launches')
def get_launches():
    launches = Launch.query.all()
    return jsonify([{
        "id": l.id, "title": l.title, "author": l.author,
        "genre": l.genre, "cover": l.cover, "bio": l.bio
    } for l in launches])

@app.route('/api/recommendations')
def get_recommendations():
    recommendations = Recommendation.query.all()
    return jsonify([{
        "id": r.id, "title": r.title, "text": r.text
    } for r in recommendations])

@app.route('/api/articles')
def get_articles():
    articles = Article.query.all()
    return jsonify([{
        "id": a.id, "img": a.img, "caption": a.caption
    } for a in articles])

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
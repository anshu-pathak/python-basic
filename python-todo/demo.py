from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, validate, ValidationError

app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///demo.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://padmin:anshu@1403@localhost/crud'
app.secret_key = 'many random bytes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# this is our database model


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.String(200))
    author = db.Column(db.String(50))

    def __init__(self, title, description, author):
        self.title = title
        self.description = description
        self.author = author

# schema with required field validation.


class PostSchema(Schema):

    title = fields.Str(required=True)
    description = fields.Str(required=True)
    author = fields.Str(required=True)

    class Meta:
        fields = ("id", "title", "author", "description")
        ordered = True
        exclude = ["id"]


post_schema = PostSchema()
posts_schema = PostSchema(many=True)

# for adding a new post.


@app.route('/post', methods=['POST'])
def add_post():
    # checking the response data.
    json_input = request.get_json()
    try:
        data = post_schema.load(json_input)
    except ValidationError as err:
        return {"errors": err.messages}, 422

    title = request.json['title']
    if title == "":
        return 'The title field have not any values'

    description = request.json['description']
    if description == "":
        return 'The description field have not any values'

    author = request.json['author']
    if author == "":
        return 'The author field have not any values'
    my_posts = Post(title, description, author)

    db.session.add(my_posts)
    db.session.commit()

    return get_post()

# getting posts


@app.route('/get', methods=['GET'])
def get_post():
    all_posts = Post.query.all()
    result = posts_schema.dump(all_posts)

    return jsonify(result)

# getting particular post


@app.route('/post_details/<id>/', methods=['GET'])
def post_details(id):
    post = Post.query.get(id)
    return post_schema.jsonify(post)


# updating post
@app.route('/post_update/<id>/', methods=['PUT'])
def post_update(id):
    post = Post.query.get(id)

    title = request.json['title']
    description = request.json['description']
    author = request.json['author']

    post.title = title
    post.description = description
    post.author = author

    db.session.commit()
    return post_schema.jsonify(post)


# deleting post
@app.route('/post_delete/<id>/', methods=['DELETE'])
def post_delete(id):
    post = Post.query.get(id)
    db.session.delete(post)
    db.session.commit()

    return post_schema.jsonify(post)


@app.route('/post_delete/all', methods=['DELETE'])
def post_deleteall():

    # delete all the data in one time
    db.session.query(Post).delete()
    db.session.commit()

    return 'Deleted all data successfully'


if __name__ == "__main__":
    app.run(port=7000, debug=True)

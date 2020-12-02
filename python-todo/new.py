from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields


# initliazing our flask app, SQLAlchemy and Marshmallow
app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://padmin:anshu@1403@localhost/todo'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///demo.db'
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


class PostSchema(Schema):

    title = fields.Str(
        required=True, error_messages={"required": "Please provide a title."}
    )
    description = fields.Str(
        required=True, error_messages={"required": "Please provide a description."}
    )
    author = fields.Str(
        required=True, error_messages={"required": "Please provide a author."}
    )

    class Meta:
        fields = ("id", "title", "author", "description")
        # order = True
        # exclude = ("id", "author")


post_schema = PostSchema()
posts_schema = PostSchema(many=True)


# adding a post


@app.route('/post', methods=['POST'])
def add_post():
    data = request.get_json(force=True)
    title = request.json['title']
    description = request.json['description']
    author = request.json['author']
    my_posts = Post(title, description, author)
    result = posts_schema.load(my_posts).data
    print(result)
    # errors = post_schema.validate(result)

    # if errors:
    #     return {
    #         "message": errors
    #     }, 500
    # else:

    db.session.add(my_posts)
    db.session.commit()

    # return {"message": "Activity successfully created"}, 202

    return post_schema.jsonify(my_posts)


# getting posts
@app.route('/get', methods=['GET'])
def get_post():
    all_posts = Post.query.all()
    # categories_schema.dump(categories).
    result = posts_schema.dump(all_posts).data

    return jsonify(result)


if __name__ == "__main__":
    app.run(port=3001)

import datetime

from flask import Response, stream_with_context

from app import app
from redis_provider.Message import Message


@app.route('/')
@app.route('/index')
def index():
    return 'Hello world!'


def stream_template(template_name, **context):
    t = app.jinja_env.get_template(template_name)
    rv = t.stream(context)
    rv.disable_buffering()
    return rv


def random_call(messages):
    msg = Message('lenovo', 'sample text', datetime.datetime.now())
    messages.append(msg)
    return msg


def get_messages():
    import time
    messages = []
    while True:
        yield random_call(messages)
        time.sleep(5)


@app.route('/posts')
def posts():
    messages = get_messages()
    return Response(stream_with_context(stream_template('messages_page.html', messages=messages)))

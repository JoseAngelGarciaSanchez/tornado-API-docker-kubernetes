# app.py
import tornado.ioloop
import tornado.web
import json


class PreprocessHandler(tornado.web.RequestHandler):
    async def post(self):
        data = json.loads(self.request.body.decode("utf-8"))
        # TODO: Add preprocessing logic
        preprocessed_data = data
        self.write(json.dumps(preprocessed_data))


def make_app():
    return tornado.web.Application(
        [
            (r"/preprocess", PreprocessHandler),
        ]
    )


if __name__ == "__main__":
    app = make_app()
    app.listen(8888, address="0.0.0.0")
    tornado.ioloop.IOLoop.current().start()

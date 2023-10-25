import tornado.ioloop
import tornado.web
import tornado.httpclient
import json

TF_SERVING_URL = "http://tf-serving-service:443/v1/models/my_model:predict"


class PreprocessHandler(tornado.web.RequestHandler):
    async def post(self):
        data = json.loads(self.request.body.decode("utf-8"))
        # TODO: Add preprocessing logic
        preprocessed_data = {"instances": [data]}

        # Send data to TensorFlow Serving for prediction
        response = await self.forward_request(TF_SERVING_URL, preprocessed_data)

        self.write(response.body)

    async def forward_request(self, url, data):
        http_client = tornado.httpclient.AsyncHTTPClient()
        request = tornado.httpclient.HTTPRequest(
            url=url,
            method="POST",
            body=json.dumps(data),
            headers={"Content-Type": "application/json"},
        )
        response = await http_client.fetch(request)
        return response


def make_app():
    return tornado.web.Application(
        [
            (r"/predict", PreprocessHandler),
        ]
    )


if __name__ == "__main__":
    app = make_app()
    app.listen(8888, address="0.0.0.0")
    tornado.ioloop.IOLoop.current().start()

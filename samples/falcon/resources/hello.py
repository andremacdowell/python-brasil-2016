# encoding: utf-8
import falcon
import json
from authentication import authenticate


class Hello:

    @falcon.before(authenticate)
    def on_get(self, request, response):
        response.status = falcon.HTTP_200
        response.body = json.dumps({"success": True})

    @falcon.before(authenticate)
    def on_post(self, request, response):
        body = request.stream.read()

        if not body:
            raise falcon.HTTPBadRequest("Empty POST body",
                                        "A JSON body is required.")

        try:
            json_data = json.loads(body)
        except ValueError:
            raise falcon.HTTPUnprocessableEntity(
                "Invalid POST body", "A valid JSON body is required.")

        data = {
            "success": True,
            "data": json_data
        }

        response.status = falcon.HTTP_202
        response.body = json.dumps(data)

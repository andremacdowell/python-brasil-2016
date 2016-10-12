# encoding: utf-8
import requests
import flask_restful as restful

external_route = "http://httpbin.org/get"
api = restful.Api()


class Hello(restful.Resource):

    def get(self):
        response = requests.get(external_route)

        result = {
            "data": None,
            "success": False
        }
        status = response.status_code

        if status == 200:
            result["data"] = response.json()
            result["success"] = True

        return api.make_response(result, status)

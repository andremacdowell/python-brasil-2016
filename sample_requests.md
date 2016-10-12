### FALCON
- POST
curl -H "token: python-brasil-2016" -H "Content-Type: application/json" -X POST -d '{"test": 1, "test2": "2"}' http://localhost:5000/api/v1/hello

- GET
curl -H "token: python-brasil-2016" http://localhost:5000/api/v1/hello 


### FLASK
- GET
curl http://localhost:5000/api/v1/hello


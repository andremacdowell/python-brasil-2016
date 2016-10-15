source /usr/local/bin/virtualenvwrapper.sh

workon python-brasil-2016-falcon
py.test --cov-report html:cov-falcon --cov=samples/falcon samples/falcon/
firefox cov-falcon/index.html 

workon python-brasil-2016-flask
py.test --cov-report html:cov-flask --cov=samples/flask samples/flask/
firefox cov-flask/index.html 

workon python-brasil-2016-pymssql
py.test --cov-report html:cov-pymssql --cov=samples/pymssql samples/pymssql/
firefox cov-pymssql/index.html 

workon python-brasil-2016-rabbitmq
py.test --cov-report html:cov-rabbitmq --cov=samples/rabbitmq samples/rabbitmq/
firefox cov-rabbitmq/index.html 

workon python-brasil-2016-redis
py.test --cov-report html:cov-redis --cov=samples/redis samples/redis/
firefox cov-redis/index.html 

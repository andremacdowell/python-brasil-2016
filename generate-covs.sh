source /usr/local/bin/virtualenvwrapper.sh

listVar="falcon flask pymssql rabbitmq redis"
for i in $listVar; do
    sample="$i"
    workon python-brasil-2016-$sample
    py.test --cov-report html:cov-$sample --cov=samples/$sample samples/$sample/
    firefox cov-$sample/index.html 
done

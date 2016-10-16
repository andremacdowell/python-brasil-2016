# Mock Away! - Uma análise de escrita de testes de unidade e mocks para algumas ferramentas e frameworks conhecidos

Neste repositório encontra-se a apresentação feita na Python Brasil 2016, assim como os sample-projects usados nos exemplos.

### Apresentação

A apresentação foi feita com a ferramenta [Marp](https://yhatt.github.io/marp/) pelos seguintes motivos:

1- Eu gosto de **Markdown** :cupid:

2- Eu não gosto de LaTex :thumbsdown:

### Samples

Coloquei aqui samples de testes para usos dos seguintes frameworks:

- [Flask](https://github.com/pallets/flask)
- [Falcon](	https://github.com/falconry/falcon)
- [pymssql](https://github.com/pymssql/pymssql)
- [pika (RabbitMQ)](https://github.com/pika/pika)
- [Redis](https://github.com/andymccurdy/redis-py)

### Executando os testes

Para executar os testes e gerar os coverage reports, criei um shell script (*generate-covs.sh* na raiz do repositório) que abre o browser com os htmls gerados. Para executa-lo você precisa de:
- virtualenv & virtualenvwrapper
- Um virtual-env para cada sample no formato *python-brasil-2016-$SAMPLENAME* (com o *requirements* instalado)
- Firefox! (para abrir o browser com os reports, pode remover caso não queiram!)

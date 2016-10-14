<!-- $theme: gaia -->

Mock Away!
===

# ![75%](images/cheating-at-cards.png)

##### Uma análise de escrita de testes de unidade e mocks para algumas ferramentas e frameworks conhecidos

###### Por André Mac Dowell ([@andremacdowell](https://twitter.com/andremacdowell))

---

<!-- page_number: true -->

# Índice

- Quem sou eu 
- Testes de unidade em Python
- Mocks em Python
- Chamadas a APIs
- Conectores de banco de dados
- Mensageria
- Provedores de Cache
- Discussão

---

# Quem sou eu
# ![](images/crop1.jpg)

---

<!-- footer: Quem sou eu -->
### Quem sou eu?
- Trabalho com Python a +- 1 ano (antes Java por ~4 anos)
- [Dojo](https://github.com/amdowell/dojo_monty_python) bacaninha com temática Monty Python
- Alguns projetos entregues usando *Falcon, Flask, Django, pymssql, pymongo, grequests, pika, redis, Celery* e outras coisas legais
###### (e outras nem tanto, olhando para você pywin32 :rage:)

---

##### :exclamation: Eu vim do meio acadêmico, então me interrompam se eu estiver sendo chato/prolixo/lerdo :exclamation:

---

<!-- footer: -->
# Testes de unidade em Python
#### (a.k.a. introdução)

---

<!-- footer: Testes de unidade em Python -->
### Testes de unidade em Python
- Testes de unidade testam funções
	- Pense em uma unidade mínima
</br>
- Testes de integração testam fluxos ou funcionalidades
	- A integração entre multiplas unidades!

---

- Modulo padrão: **unittest**

Em um arquivo *test_something.py*:
```python
import unittest

class TestSomething(unittest.TestCase):
    def setUp(self):
        sets_up_something()
    
    def test_something(self):
        ...
        self.assertTrue(...)
    
    def test_something_else(self):
        ...
```  

---

<!-- footer: -->
# Mocks em Python
#### (o que "mockar" e o que não "mockar"?)

---

<!-- footer: o que "mockar" e o que não "mockar"? -->
### Mocks em Python
- Mocks são objetos ou chamadas de função que "substituem" as verdadeiras
</br>
- "Development is about making things, while mocking is about faking things.", Mike Lin - 2016

---

### Mocks :heart: Testes unitários

---

### Mocks :heart: Testes unitários
- Se **A** é auto-contido, não precisa
- Se **A** chama **B**, para testar **A** unitariamente, precisamos mockar **B**
- Se queremos testar a funcionalidade **A** por completo, queremos um *teste de integração* (não precisamos mockar).

---

```python
# Em resources.A (classe)
def function_a(self, b):
    return b.deal_with_stuff(something)

# Teste de B
def test_b(self):
    b = B()
    self.assertEqual(b.deal_with_stuff(something_else),
                     expected_b)

# Teste de A
def fake_function(*args):
    return expected_fake

def test_a(self):
    a = A()
    b = B()
    b.deal_with_stuff = fake_function #monkey_patch!!
    self.assertEqual(a.function_a(b), expected_fake)

```

---

```python
# Mesmo teste de A, com mock
@mock.patch("B.deal_with_stuff")
def test_a(self, mock_b):
    a = A()
    mock_b.return_value = expected_fake
    self.assertEqual(a.function_a(mock.MagicMock()),
                     expected_fake)
```

- python 2.7:
  ```python
  import mock # pip install mock
  ```

- python 3.5
  ```python
  import unittest.mock # nativo
  ```
---

<!-- footer: -->
# "Mockando" chamadas à APIs
#### (flask e falcon: criando e mockando end-points)

---

<!-- footer: flask e falcon: criando e mockando end-points -->

---

<!-- footer: -->
# Conectores de banco de dados
#### (pymssql amado)

---

<!-- footer: Conectores de banco de dados -->

---

<!-- footer: -->
# Mensageria
#### (mock aqui mock ali)

---

<!-- footer: Mensageria -->

---

<!-- footer: -->
# Provedores de cache
#### (redis salvando a minha vida)

---

<!-- footer: Provedores de cache-->

---

<!-- footer: -->
# acabou

---

# acabou
#### (discussão/dúvidas)

---

### Bibliografia

- Fonte da imagem de capa: <a href="https://www.christart.com/">christart</a>
- Fala maneira sobre testes: [Mike Lin](https://blog.fugue.co/2016-02-11-python-mocking-101.html) (ótimo artigo)
</br>
- Outras fontes legais sobre Testes e Mocking:
    - [Guia](http://docs.python-guide.org/en/latest/writing/tests/) de escrita de testes
	- [Artigo](https://www.toptal.com/python/an-introduction-to-mocking-in-python) do Naftuli Tzvi Kay
	- [Artigo](http://alexmarandon.com/articles/python_mock_gotchas/) do Alex Marandon
	- [Artigo](http://www.drdobbs.com/testing/using-mocks-in-python/240168251) do José R.C. Cruz

---

## Valeu galera! :+1:

##### https://github.com/amdowell/python-brasil-2016
###### (Escrito em **Markdown** graças ao [Marp](https://yhatt.github.io/marp/))

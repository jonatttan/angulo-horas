# Projeto ângulo de horas :clock1230:

### Objetivo:

Obter a medida do ângulo em graus entre o ponteiro de hora em relação ao de minutos.



### Requisitos do projeto:

1. Computador com Python e navegador instalado e atualizado;

2. Bibliotecas utilizadas no projeto estão listadas no arquivo nomeado requirements.txt;

3. Base de dados do PostgreSQL (de preferência).

   

### Procedimentos para rodar:

1. Realize o clone do projeto (ou baixe via .zip);

2. Baixe as bibliotecas necessárias, descritas no arquivo requirements.txt;

3. Navegue até o repositório clonado;

4. Alimente o arquivo secrets.json de acordo com as configurações de sua base de dados;

5. Rode com o comando "python manage.py runserver";

6. Acesse por navegador de sua referência no endereço http://localhost:8000/v1/rest/clock/ (deverá ser apresentada a API do Django REST framework em Angulo List com os cadastros).

   

### Modo de usar:

1. Abra o navegador no endereço http://localhost:8000/v1/rest/clock/6/0/ (6/0/ representa 6:00, altere conforme desejar);
2. Quando digitado os dados na barra de endereço, é realizado primeiramente uma consulta, se os dados existirem na base, estes são apresentados. Caso não exista, será calculado e cadastrado, bastando atualizar a página para consultar novamente;
3. Para realizar a consulta de todos os dados, digite http://localhost:8000/v1/rest/clock/.





Críticas, dúvidas e/ ou sugestões: jonattan.sousa@gmail.com
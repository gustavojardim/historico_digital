# Histórico Digital (Digital History)

Este projeto é um protótipo de uma blockchain para armazenar dados relacionados a manutenção de automóveis e seu ciclo de vida. Foi desenvolvido para compor o meu trabalho de conclusão do curso de graduação em Análise e Desenvolvimento de Sistemas pela Universidade do Vale do Rio dos Sinos (UNISINOS)

O protótipo está implementado em Python, utilizando trê bibliotecas principas: Django, Flask e SQLAlchemy. O Flask é responsável tornar possível que o código seja executado 24 horas por dia como uma API Rest, ou seja, mapeando métodos e suas lógicas para rotas de GET e POST; enquanto o SQLAlchemy realiza a conexão com banco de dados off-chain para registrar usuários, fornecedores, e dados básicos de um serviço registrado na blockchain. A plataforma web é alicerçada nos frameworks Django, para Python e Bootstrap para o código HMTL (Linguagem de Marcação de HiperTexto). O site consome e registra dados através da API Rest que utiliza o Flask. Neste cenário, o Django foi utilizado implementando o padrão de desenvolvimento web chamado Model-View-Template (MVT). Além disso, este framework conta com dois pontos positivos determinantes para a escolha do mesmo: rápida configuração e deploy de um site e uma suave curva de aprendizagem. Além deste framework, é utilizado o Bootstrap, que disponibiliza componentes de layout para construção do design do site. Este não necessita de nenhum tipo de instalação, sendo necessária somente a referência para o servidor do framework no código HTML que o site se encarrega de carregar os componentes no momento do carregamento das páginas do site. As características determinantes para escolher o Bootstrap foram as seguintes:
·     Simples e rápida utilização;
·     Prover componentes com layouts prontos que permitem que o desenvolvedor foque nas regras de negócio da aplicação;
·     Seus componentes são responsivos, isto é, se adequam ao dispositivo em que o site está sendo consumindo, garantindo uma boa usabilidade e experiência ao usuário.

## What is blockchain? How it is implemented? And how it works?

Please read the [step-by-step implementation tutorial](https://www.ibm.com/developerworks/cloud/library/cl-develop-blockchain-app-in-python/index.html) to get your answers :)

## Instructions to run

Clone (or fork) the project,

```sh
$ git clone git@github.com:gustavojardim/historico_digital.git
```

Create a SQL database to be your off-chain storage and configure it on **application_setup.py**,

Install the dependencies,

```sh
$ cd historico_digital
$ pipenv install
```

Run the application,

```sh
$ python app.py
```

The application should be up and running at [http://localhost:5000](http://localhost:5000).

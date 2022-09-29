# Analysis Tool for Undergrad Students

[![discord](https://img.shields.io/badge/Discord-7289DA?style=for-the-badge&logo=discord&logoColor=white)](https://discord.gg/ZwbuRG7GBx)

- [Analysis Tool for Undergrad Students](#analysis-tool-for-undergrad-students)
  - [O que é?](#o-que-é)
  - [Como obter a ferramenta?](#como-obter-a-ferramenta)
  - [Como contribuir?](#como-contribuir)
  - [Licença](#licença)

## O que é?

**Analysis Tool for Undergrad Students** é um software que fornece ferramentas para análise de dados, criação e customização de gráficos etc. Surgiu inicialmente como uma aplicação desktop, mas agora, para termos de portabilidade e facilidade de distribuição, decidimos desenvolver uma versão web.

## Como obter a ferramenta?

A ferramenta é online e pode ser acessada pelo link: <https://www.atusweb.xyz>

Caso queira rodar o software localmente para **desenvolvimento**, será necessário seguir alguns passos:

- Clone do repositório
- Definir as variáveis de ambiente (arquivo .env na pasta do repositório)
  - MYSQL_ROOT_PASSWORD
  - DJANGO_SECRET_KEY
  - DJANGO_EMAIL_HOST_USER
  - DJANGO_EMAIL_HOST_PASSWORD
- Instalação do [Docker](https://www.docker.com/)
- ```docker compose -f ./dev.yml```

## Como contribuir?

Qualquer contribuição, reporte de bugs, correção de bugs, melhorias na documentação e ideias são bem-vindas!

As contribuções ao código podem ser feitas via PRs, reporte de bugs ou ideias podem ser enviadas via e-mail ou via issues.

E-mail para contato: atusdevs@gmail.com

## Licença

[MIT License](https://github.com/git/git-scm.com/blob/main/MIT-LICENSE.txt)

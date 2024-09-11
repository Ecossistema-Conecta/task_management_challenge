
# Sistema de Gestão de Tarefas com Funcionalidades Avançadas

Desenvolver uma aplicação web para gerenciar tarefas e projetos, permitindo que os usuários criem, organizem e acompanhem tarefas de forma colaborativa. A aplicação suportará múltiplos projetos, atribuição de tarefas a diferentes usuários e fornecerá relatórios e notificações para manter todos atualizados sobre o progresso.



## Instalação

Instale as dependencias do projeto com docker

```bash
  docker compose build --no-cache
```
    
## Deploy

Para fazer o deploy desse projeto rode

```bash
  docker compose up
```


## Uso/Exemplos

Crie um usuario superuser para o primeiro login no sistema
```bash
docker compose run task-manager-web python manage.py createsuperuser
```

E acesse a [página inicial](http//:127.0.0.1:8001/)




## Roadmap

- Autenticação e Autorização de Usuários

- CRUD de Projetos e Tarefas

- Gerenciamento de Tarefas

- Sistema de Notificações

- Relatórios e Estatísticas

- Funcionalidades de Colaboração

- Interface de Usuário

- Configurações e Personalização

Para mais detalhes acesse o arquivo README.md
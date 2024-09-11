# Sistema de Gestão de Tarefas com Funcionalidades Avançadas



## Objetivo do Projeto



Desenvolver uma aplicação web para gerenciar tarefas e projetos, permitindo que os usuários criem, organizem e acompanhem tarefas de forma colaborativa. A aplicação suportará múltiplos projetos, atribuição de tarefas a diferentes usuários e fornecerá relatórios e notificações para manter todos atualizados sobre o progresso.

# Para instalar acesse o arquivo INSTALL.md e siga o passo a passo


## Funcionalidades Principais



### 1. Autenticação e Autorização de Usuários



- **Cadastro e Login**: Permitir que os usuários se registrem e façam login na aplicação. Veja a [documentação Django sobre Autenticação](https://docs.djangoproject.com/en/stable/topics/auth/) para detalhes sobre como configurar e personalizar o sistema de autenticação, em todas as telas o usuário deve estar autenticado para conseguir navegar.
- **Gerenciamento de Sessão**: Manter a sessão do usuário ativa e permitir logout. Consulte [Django Sessions](https://docs.djangoproject.com/en/stable/topics/http/sessions/) para gerenciamento de sessões.
- **Papéis e Permissões**: Diferenciar entre tipos de usuários, como administradores e usuários regulares, com diferentes permissões. Veja [Django Permissions Templates](https://docs.djangoproject.com/en/stable/topics/auth/default/#permissions) para gerenciar permissões e limitar acesso a telas. Veja [Django Permissions View]( https://docs.djangoproject.com/en/5.1/topics/auth/default/#django.contrib.auth.decorators.permission_required).



### 2. CRUD de Projetos e Tarefas

- **O django possui class based views que facilitam a criação de CRUDs, veja [Django Class Based Views](https://docs.djangoproject.com/en/stable/topics/class-based-views/) para mais informações.**

- **Criar e Editar Projetos**: Permitir que os usuários criem e editem projetos, adicionando informações como nome, descrição e data de conclusão. Consulte [Django Models](https://docs.djangoproject.com/en/stable/topics/db/models/) para criar e gerenciar modelos e [Django Create View](https://docs.djangoproject.com/en/stable/ref/class-based-views/generic-editing/#django.views.generic.edit.CreateView).
- **Listar e Excluir Projetos**: Listar todos os projetos e permitir a exclusão de projetos que não são mais necessários. Veja [Django QuerySet API](https://docs.djangoproject.com/en/stable/topics/db/queries/) para listar e manipular objetos, views [Django Update View](https://docs.djangoproject.com/en/stable/ref/class-based-views/generic-editing/#django.views.generic.edit.UpdateView) e [Django Delete View](https://docs.djangoproject.com/en/stable/ref/class-based-views/generic-editing/#django.views.generic.edit.DeleteView).
- **Criar e Editar Tarefas**: Permitir que os usuários criem e editem tarefas dentro dos projetos, definindo detalhes como título, descrição, prioridade e prazo. Consulte [Django Forms](https://docs.djangoproject.com/en/stable/topics/forms/) para criar formulários, form view [Django Form View](https://docs.djangoproject.com/en/stable/ref/class-based-views/generic-editing/#django.views.generic.edit.FormView), view [Django Create View](https://docs.djangoproject.com/en/stable/ref/class-based-views/generic-editing/#django.views.generic.edit.CreateView) e [Django Update View](https://docs.djangoproject.com/en/stable/ref/class-based-views/generic-editing/#django.views.generic.edit.UpdateView).
- **Listar e Excluir Tarefas**: Listar todas as tarefas dentro de um projeto e permitir a exclusão de tarefas completadas ou desnecessárias. Veja [Django QuerySet API](https://docs.djangoproject.com/en/stable/topics/db/queries/) para trabalhar com consultas e exclusão, views [Django List View](https://docs.djangoproject.com/en/stable/ref/class-based-views/generic-display/#listview) e [Django Delete View](https://docs.djangoproject.com/en/stable/ref/class-based-views/generic-editing/#django.views.generic.edit.DeleteView).



### 3. Gerenciamento de Tarefas



- **Status da Tarefa**: Permitir que as tarefas sejam marcadas como pendentes, em progresso ou concluídas. Utilize [Django Models](https://docs.djangoproject.com/en/stable/topics/db/models/) para definir campos e status.
- **Atribuição de Tarefas**: Permitir que os usuários atribuam tarefas a si mesmos ou a outros membros do projeto. Veja [Django ForeignKey](https://docs.djangoproject.com/en/stable/topics/db/models/#relationships) para relacionar usuários e tarefas.
- **Prioridade e Prazo**: Definir a prioridade (alta, média, baixa) e a data de conclusão esperada para cada tarefa. Consulte [Django Forms](https://docs.djangoproject.com/en/stable/topics/forms/) para campos de formulário.
- **Tags e Categorias**: Adicionar tags ou categorias às tarefas para facilitar a organização e a busca. Veja [Django ManyToManyField](https://docs.djangoproject.com/en/stable/topics/db/models/#many-to-many-relationships) para relacionar tags e categorias.



### 4. Sistema de Notificações



- **Notificações por Email**: Enviar notificações por email para atualizações importantes, como quando uma tarefa é atribuída ou uma tarefa está prestes a vencer. Consulte [Django Email](https://docs.djangoproject.com/en/stable/topics/email/) para configuração e envio de emails e aqui tem um exemplo de como usar smtp free [Gmail SMTP free](https://medium.com/django-unleashed/configuring-smtp-server-in-django-a-comprehensive-guide-91810a2bca3f).
- **Notificações In-App**: Mostrar notificações dentro da aplicação para atualizações em tempo real, como novos comentários ou mudanças de status. Veja [Django Signals](https://docs.djangoproject.com/en/stable/topics/signals/) para implementar notificações em tempo real.



### 5. Relatórios e Estatísticas



- **Visão Geral do Projeto**: Oferecer uma visão geral do progresso do projeto, incluindo o número de tarefas concluídas e pendentes. Utilize [Django QuerySet API](https://docs.djangoproject.com/en/stable/topics/db/queries/) para gerar relatórios.
- **Relatórios de Desempenho**: Gerar relatórios sobre o desempenho das tarefas, como a quantidade de tarefas concluídas dentro do prazo e a carga de trabalho dos usuários. Veja [Django QuerySet API](https://docs.djangoproject.com/en/stable/topics/db/queries/) e [Django Aggregation](https://docs.djangoproject.com/en/stable/topics/db/aggregation/) para criar relatórios.
- **Gráficos e Diagramas**: Exibir gráficos de progresso, como gráficos de Gantt ou diagramas de burndown. Para isso, você pode usar bibliotecas JavaScript externas como [Chart.js](https://www.chartjs.org/docs/latest/) ou [D3.js](https://d3js.org/).



### 6. Funcionalidades de Colaboração



- **Comentários nas Tarefas**: Permitir que os usuários adicionem comentários nas tarefas para discussões e atualizações. Crie um modelo para comentários e use relacionamentos. Veja [Django Relationships](https://docs.djangoproject.com/en/stable/topics/db/models/#relationships).
- **Atribuição de Responsabilidades**: Gerenciar quem é responsável por cada tarefa e atualizar os usuários sobre suas responsabilidades. Veja [Django ForeignKey](https://docs.djangoproject.com/en/stable/topics/db/models/#relationships) para atribuições.
- **Histórico de Atividades**: Manter um histórico das atividades realizadas, como alterações de status e comentários, para rastreamento e auditoria. Use [Django Signals](https://docs.djangoproject.com/en/stable/topics/signals/) para registrar atividades.



### 7. Interface de Usuário



- **Design Responsivo**: Garantir que a aplicação funcione bem em diferentes dispositivos e tamanhos de tela. Utilize [Bootstrap](https://getbootstrap.com/docs/5.2/getting-started/introduction/) para um design responsivo.
- **Experiência do Usuário (UX)**: Criar uma interface intuitiva e fácil de usar, com navegação clara e feedback visual apropriado. Veja [Django Templates](https://docs.djangoproject.com/en/stable/topics/templates/) para criar e gerenciar templates.
- **Dashboard**: Fornecer um painel inicial onde os usuários possam visualizar os projetos ativos, tarefas pendentes e notificações recentes. Consulte [Chartjs](https://www.chartjs.org/) para construir dashboards.



### 8. Configurações e Personalização



- **Preferências de Notificação**: Permitir que os usuários personalizem suas preferências de notificação. Veja [Django Settings](https://docs.djangoproject.com/en/stable/topics/settings/) para configurar preferências.
- **Temas e Layouts**: Oferecer opções para personalizar o tema e o layout da interface de usuário. Utilize [Bootstrap](https://getbootstrap.com/docs/5.2/getting-started/introduction/) para personalizar o design.



## Outros Recursos Úteis



- **Django REST Framework** (se você planeja criar uma API para o projeto): [Django REST Framework](https://www.django-rest-framework.org/)
- **Documentação sobre Deploy com Django**: [Deploy Django](https://docs.djangoproject.com/en/stable/howto/deployment/)
- **Documentação sobre Django**: [Django Girls](https://tutorial.djangogirls.org/en/)

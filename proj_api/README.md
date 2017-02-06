# API

Utilizei o Django REST Framework para a criação da API, por ser uma ferramenta amplamente 
utilizada e testada para este fim. Primeiro, defini os modelos a serem criados, conforme 
especificado no email. Para os serviços, utilizei linhas de serviços que definiriam o 
produto usado, seu custo e sua quantidade em cada serviço.

Depois disso, criei os serializers e configurei as opções de cada um, como campos "somente 
leitura", atualização do custo do serviço, etc.

A API permite criar, deletar e atualizar produtos, safras, serviços e linhas de serviços:

* produtos - (acessível em /produtos ou /produtos/id) - Possuem nome e preço médio. Na API, o 
preço médio é um campo somente para leitura. Este campo é atualizável através de uma view, que 
atualiza todos os produtos baseados em linhas de serviços que tiveram sua data de fim no mês 
anterior.

* safras - (acessível em /safras ou /safras/id) - Possuem nome, data de início e fim. Sua criação 
é bem simples.

* servicos - (acessível em /servicos ou /servicos/id) - Possuem nome, data de início e fim, safra 
a qual estão associados e um custo total. Este custo total, na API, é um campo somente leitura. 
Sua atualização é feita na criação de uma linha de serviço associada a este serviço.

* linhas de serviços - (acessível em /linhas_servicos ou /linhas_servicos/id) - Linhas de serviços 
definem a quantidade e o custo de produtos utilizados em um serviço. Possuem o serviço e o 
produto a que estão associados, além do custo e da quantidade.

## Ideias possíveis

* Validação de dados em campos como data início e fim (início tem que ser anterior ao fim)
* Implementação de autenticação e autorização para criação e leitura (Django REST Framework 
permite essa funcionalidade)
* Associação do script de atualização do preço médio dos produtos a um CRON job, para que a 
atualização não precise ser "disparada" pelo usuário
# Data-Driven API Tests

## Descrição
Este projeto tem como objetivo realizar testes automatizados em APIs públicas utilizando **Postman** e **Newman**, 
com análise dos resultados em **Python**. A ideia é transformar a execução dos testes em **insights estratégicos**, 
através de gráficos e métricas que apoiam decisões sobre qualidade de software.

## Ferramentas utilizadas
- [Postman](https://www.postman.com/) → criação e execução de coleções de testes.
- [Newman](https://www.npmjs.com/package/newman) → execução automatizada das coleções via CLI.
- [Python](https://www.python.org/) → análise dos relatórios (Pandas, Matplotlib, Seaborn).
- [ReqRes API](https://reqres.in/) → API pública usada para os testes.

## Estrutura do projeto
data-driven-api-tests/ 
│ 
├── postman/ # Coleções e ambientes do Postman 
├── reports/ # Resultados exportados (CSV/JSON via Newman) 
├── analysis/ # Scripts Python para análise 
└── README.md # Documentação do projeto

## Como rodar
1. Clone este repositório.
2. Instale o Newman:
   ```bash
   npm install -g newman
3. Execute a coleção:
   newman run postman/collection.json -r json,html
4. Analise os relatórios com python:
   jupyter notebook analysis/analysis.ipynb
   
## Resultados esperados
-> Gráficos de sucesso vs falha.

-> Tempo médio de resposta por endpoint.

-> Distribuição de status codes.

## Licença
Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

# Data-Driven API Tests

# Descrição
Este projeto tem como objetivo realizar testes automatizados em APIs públicas utilizando Postman e Newman, com integração contínua via GitHub Actions e análise dos resultados em Python. A proposta é transformar a execução dos testes em insights estratégicos, através de gráficos e métricas que apoiam decisões sobre qualidade de software.

# Ferramentas utilizadas

Postman → criação e execução de coleções de testes
Newman → execução automatizada das coleções via CLI
GitHub Actions → automação do fluxo de testes e análise
Python → análise dos relatórios (Pandas, Matplotlib)
JSONPlaceholder API → API pública usada para os testes

# Estrutura do projeto

data-driven-api-tests/                         
.github/workflows/ newman-analysis.yml e newman_tests.yml                                      
postman/ jsonplaceholder_tests.postman_collection.json               
README.md      
analyze_report.py                 


# Como rodar

* Clone o repositório:
git clone https://github.com/Bomjardimraquel/data-driven-api-tests.git
cd data-driven-api-tests

* Instale o Newman:
npm install -g newman

* Execute a coleção:
newman run postman/jsonplaceholder_tests.postman_collection.json -r json,html

* Analise os relatórios com Python:
python analyze_report.py

## Resultados esperados

-> Gráficos de sucesso vs falha

-> Tempo médio de resposta por endpoint

-> Distribuição de status codes

-> Taxa de sucesso por requisição

## Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

# Avaliação N3 - Documentação

Este projeto é focado no gerenciamento pessoal de medicamentos, com o objetivo de melhorar a organização, saúde e bem-estar dos usuários. A plataforma permite o controle de três áreas principais para facilitar a administração de medicamentos:

### 1. Perfil do Usuário
- A criação de um perfil que armazena dados pessoais e informações relevantes sobre o usuário, como condições de saúde e histórico de medicamentos.

### 2. Estoque de Medicamentos
- Um sistema de cadastro e monitoramento do estoque de medicamentos, onde o usuário pode registrar medicamentos prescritos por médicos e/ou de uso contínuo pessoal. O sistema acompanha quantidades, datas de validade, dosagens e categorias dos remédios, garantindo que nunca falte um medicamento essencial.

### 3. Notas Personalizadas
- O sistema permite criar notas para agendamentos personalizados para alertar o usuário sobre o horário de cada medicação, além de atualizar o estoque automaticamente a cada dose tomada.

A aplicação é ideal para pessoas com rotinas agitadas, idosos ou qualquer pessoa que precise de um apoio adicional para manter a disciplina no uso de medicações. Ao reduzir o risco de esquecimento e melhorar o controle do estoque, o sistema contribui para um bem-estar maior, promovendo saúde e segurança com um acompanhamento preciso das medicações necessárias.

## Executando

Para executar o projeto:

1. Modifique o arquivo `.env.example` para `.env` e preencha as variáveis de ambiente, ou defina diretamente pelo terminal.
3. Rode o comando `docker compose up -d` na raiz do projeto.

## Tecnologias Utilizadas
[![My Skills](https://skillicons.dev/icons?i=py,flask,docker,mysql)](https://skillicons.dev)

## Recursos

1. Usuário
2. Medicamentos 
3. Notas

## Regras de Negócio

* As sementes com data de validade expirada não podem ser registradas em novos plantios;
* O tempo de germinação de uma semente deve ser entre 1 e 999 dias;
* A data de expiração da semente não pode estar no passado no momento do cadastro;
* Os tipos de semente devem ser: `Fruta`, `Legume` ou `Cereal`.
* As operações de criação e atualização devem validar a quantidade mínima de sementes necessária para um plantio;

## Rotas

### Sementes

#### `GET /sementes[?tipo=:tipo]`
Lista todas as sementes disponíveis. Filtra pela `tipo` se for informado.

Resposta:
````json
[
  {
    "id": 1,
    "nome": "Semente 1",
    "tipo": "Semente 1",
    "tempoGerminacao": 10,
    "dataExpiracao": "2021-01-01",
  }
]
````

Respostas de erro:
* `400` - `tipo` inválido;
* `204` - nenhuma semente encontrada;

#### `GET /sementes/{id}`
Lista uma semente específica pelo `id`.

Resposta:
````json
{
  "id": 1,
  "nome": "Semente 1",
  "tipo": "Semente 1",
  "tempoGerminacao": 10,
  "dataExpiracao": "2021-01-01",
}
````

Respostas de erro:
* `400` - `id` inválido;
* `404` - semente não encontrada;

#### `POST /sementes`

Cadastra uma nova semente.

Corpo da Requisição:
````json
{
  "nome": "Tomate",
  "tipo": "Fruta",
  "tempoGerminacao": 10,
}
````

Corpo da Resposta:
````json
[
  {
    "id": 1,
    "nome": "Tomate",
    "tipo": "Fruta",
    "tempoGerminacao": 10,
  }
]
````

Respostas de erro:
* `400` - data de expiração inválida;
* `400` - tempo de germinação inválido;
* `400` - tipo inválido;
* `404` - semente não encontrada;
* `409` - semente já cadastrada;

#### `PATCH /sementes/{id}`

Atualiza as informações de uma semente específica pelo `id`.

Corpo da Requisição:
````json
{
  "tempoGerminacao": 12,
}
````

Corpo da Resposta:
````json
[
  {
    "id": 1,
    "nome": "Tomate",
    "tipo": "Fruta",
    "tempoGerminacao": 12,
  }
]
````

Respostas de erro:
* `400` - `id` inválido;
* `400` - data de expiração inválida;
* `400` - tempo de germinação inválido;
* `400` - tipo inválido;
* `404` - semente não encontrada;

#### `DELETE /sementes/{id}`

Deleta uma semente específica pelo `id`.

Corpo da Resposta:
````json
[
  {
    "id": 1,
    "nome": "Tomate",
    "tipo": "Fruta",
    "tempoGerminacao": 12,
  }
]
````

Respostas de erro:
* `400` - `id` inválido;
* `404` - semente não encontrada;
* `409` - semente em uso;

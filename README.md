# Avaliação N3 - Documentação :page_facing_up:

Este projeto é focado no gerenciamento pessoal de medicamentos, com o objetivo de melhorar a organização, saúde e bem-estar dos usuários. A plataforma permite o controle de três áreas principais para facilitar a administração de medicamentos:

#### 1. Perfil do Usuário
>- A criação de um perfil que armazena dados pessoais e informações relevantes sobre o usuário, como condições de saúde e histórico de medicamentos.

#### 2. Estoque de Medicamentos
>- Um sistema de cadastro e monitoramento do estoque de medicamentos, onde o usuário pode registrar medicamentos prescritos por médicos e/ou de uso contínuo pessoal. O sistema acompanha quantidades, datas de validade, dosagens e categorias dos remédios, garantindo que nunca falte um medicamento essencial.

#### 3. Notas Personalizadas
>- O sistema permite criar notas para agendamentos personalizados para alertar o usuário sobre o horário de cada medicação, além de atualizar o estoque automaticamente a cada dose tomada.

A aplicação é ideal para pessoas com rotinas agitadas, idosos ou qualquer pessoa que precise de um apoio adicional para manter a disciplina no uso de medicações. Ao reduzir o risco de esquecimento e melhorar o controle do estoque, o sistema contribui para um bem-estar maior, promovendo saúde e segurança com um acompanhamento preciso das medicações necessárias.

## Executando :hammer:

Para executar o projeto:

1. Modifique o arquivo `.env.example` para `.env` e preencha as variáveis de ambiente, ou defina diretamente pelo terminal.
3. Rode o comando `docker compose up -d` na raiz do projeto.

## Tecnologias Utilizadas
[![My Skills](https://skillicons.dev/icons?i=py,flask,docker,mysql&theme=light)](https://skillicons.dev)

## Recursos

1. Usuário
2. Medicamentos 
3. Notas

## Regras de Negócio :briefcase:

#### 1. Cadastro de Usuário
> * Cada usuário deve ter um perfil único no sistema.
> * O usuário precisa preencher informações básicas, como nome, idade e condições de saúde relevantes, no cadastro.

#### 2. Controle de Estoque de Medicamentos
> * O sistema deve permitir o cadastro de medicamentos com nome, descrição, tipo e quantidade inicial.
> * Ao registrar uma nova dose tomada, a quantidade no estoque deve ser atualizada automaticamente.
> * Quando a quantidade de um medicamento atingir um valor mínimo (configurável), o sistema deve enviar uma notificação de alerta para o usuário.

#### 3. Lembretes de Medicamento
> * O sistema deve enviar notificações no horário configurado para lembrar o usuário de tomar a medicação.
> * Se o usuário não marcar a dose como tomada até um certo tempo após o lembrete, o sistema pode enviar uma notificação de atraso.

#### 4. Validade dos Medicamentos
> * Ao cadastrar um medicamento, o usuário deve inserir a data de validade do produto.
> * O sistema deve alertar o usuário quando o medicamento estiver próximo de vencer.

#### 5. Controle de Quantidade por Dose
> * Ao criar um lembrete, o usuário deve definir a quantidade de medicamento a ser tomada em cada dose.
> * Cada vez que uma dose é marcada como tomada, essa quantidade deve ser subtraída automaticamente do estoque.

## Rotas :milky_way:

### Usuarios

#### `GET /usuarios`
Lista todos os usuários disponíveis.

#### Resposta:
```json
{
  "success": true,
  "usuarios": [
    {
      "id": 1,
      "first_name": "João",
      "last_name": "Silva",
      "age": 30,
      "password": "senha123"
    }
  ]
}
```

#### Respostas de erro:
- `404` - Nenhum usuário encontrado;
- `500` - Erro interno do servidor;

---

### `GET /usuarios/{id}`
Lista um usuário específico pelo `id`.

#### Resposta:
```json
{
  "success": true,
  "usuario": {
    "id": 1,
    "first_name": "João",
    "last_name": "Silva",
    "age": 30,
    "password": "senha123"
  }
}
```

#### Respostas de erro:
- `400` - `id` inválido;
- `404` - Usuário não encontrado;
- `500` - Erro interno do servidor;

---

### `GET /usuarios?first_name=:first_name`
Busca usuários pelo nome.

#### Resposta:
```json
{
  "success": true,
  "usuario": {
    "id": 1,
    "first_name": "João",
    "last_name": "Silva",
    "age": 30,
    "password": "senha123"
  }
}
```

#### Respostas de erro:
- `404` - Usuário não encontrado;
- `500` - Erro interno do servidor;

---

### `POST /usuarios`
Cadastra um novo usuário.

#### Corpo da Requisição:
```json
{
  "first_name": "Maria",
  "last_name": "Oliveira",
  "age": 25,
  "password": "senha123"
}
```

#### Corpo da Resposta:
```json
{
  "success": true,
  "message": "Usuário criado com sucesso"
}
```

#### Respostas de erro:
- `400` - Dados inválidos;
- `500` - Erro interno do servidor;

---

### `PATCH /usuarios/{id}`
Atualiza as informações de um usuário específico pelo `id`.

#### Corpo da Requisição:
```json
{
  "first_name": "Maria",
  "last_name": "Oliveira",
  "age": 26,
  "password": "novaSenha"
}
```

#### Corpo da Resposta:
```json
{
  "success": true,
  "message": "Usuário atualizado com sucesso"
}
```

#### Respostas de erro:
- `400` - `id` inválido;
- `404` - Usuário não encontrado;
- `500` - Erro interno do servidor;

---

### `DELETE /usuarios/{id}`
Deleta um usuário específico pelo `id`.

#### Corpo da Resposta:
```json
{
  "success": true,
  "message": "Usuário deletado com sucesso"
}
```

#### Respostas de erro:
- `400` - `id` inválido;
- `404` - Usuário não encontrado;
- `500` - Erro interno do servidor;


### Medicamentos

### `GET /meds_stock`
Lista todo o estoque de medicamentos.

#### Resposta:
```json
{
  "success": true,
  "meds_stock": [
    {
      "id": 1,
      "med_name": "Paracetamol",
      "med_qtd": 100,
      "med_val": "2023-11-01",
      "med_desc": "Medicamento para dor e febre",
      "med_type": "Analgésico",
      "user_id": 2
    }
  ]
}
```

#### Respostas de erro:
- `404` - Estoque de medicamentos não encontrado;
- `500` - Erro interno do servidor;

---

### `GET /meds_stock/{id}`
Busca um medicamento específico no estoque pelo `id`.

#### Resposta:
```json
{
  "success": true,
  "meds_stock": {
    "id": 1,
    "med_name": "Paracetamol",
    "med_qtd": 100,
    "med_val": "2023-11-01",
    "med_desc": "Medicamento para dor e febre",
    "med_type": "Analgésico",
    "user_id": 2
  }
}
```

#### Respostas de erro:
- `404` - Medicamento não encontrado;
- `500` - Erro interno do servidor;

---

### `POST /meds_stock`
Adiciona um novo medicamento ao estoque.

#### Corpo da Requisição:
```json
{
  "med_name": "Ibuprofeno",
  "med_qtd": 200,
  "med_val": "2024-05-01",
  "med_desc": "Medicamento anti-inflamatório",
  "med_type": "Anti-inflamatório",
  "user_id": 1
}
```

#### Corpo da Resposta:
```json
{
  "success": true,
  "message": "Medicamento adicionado ao estoque"
}
```

#### Respostas de erro:
- `500` - Erro interno do servidor;

---

### `PATCH /meds_stock/{id}`
Atualiza as informações de um medicamento no estoque.

#### Corpo da Requisição:
```json
{
  "med_name": "Ibuprofeno",
  "med_qtd": 150,
  "med_val": "2024-06-01",
  "med_desc": "Anti-inflamatório atualizado",
  "med_type": "Anti-inflamatório",
  "user_id": 1
}
```

#### Corpo da Resposta:
```json
{
  "success": true,
  "message": "Medicamento atualizado"
}
```

#### Respostas de erro:
- `404` - Medicamento não encontrado;
- `500` - Erro interno do servidor;

---

### `DELETE /meds_stock/{id}`
Remove um medicamento do estoque.

#### Corpo da Resposta:
```json
{
  "success": true,
  "message": "Medicamento deletado"
}
```

#### Respostas de erro:
- `404` - Medicamento não encontrado;
- `500` - Erro interno do servidor;


### Notebook


### `GET /notebooks`
Lista todas as notas cadastradas.

#### Resposta:
```json
{
  "success": true,
  "notebooks": [
    {
      "id": 1,
      "note_title": "Nota de Paracetamol",
      "med_stock_id": 10,
      "note_desc": "Instruções para uso de Paracetamol",
      "med_method": "Oral",
      "med_type": "Analgésico",
      "med_freq": "8h",
      "qtd_taken": 2,
      "qtd_total": 10,
      "init_schedule": "2024-01-10",
      "end_schedule": "2024-01-20",
      "status": "Ativo",
      "obs": "Tomar após as refeições",
      "user_id": 2
    }
  ]
}
```

#### Respostas de erro:
- `404` - Nenhuma nota encontrada;
- `500` - Erro interno do servidor;

---

### `GET /notebooks/{id}`
Busca uma nota específica pelo `id`.

#### Resposta:
```json
{
  "success": true,
  "notebook": {
    "id": 1,
    "note_title": "Nota de Paracetamol",
    "med_stock_id": 10,
    "note_desc": "Instruções para uso de Paracetamol",
    "med_method": "Oral",
    "med_type": "Analgésico",
    "med_freq": "8h",
    "qtd_taken": 2,
    "qtd_total": 10,
    "init_schedule": "2024-01-10",
    "end_schedule": "2024-01-20",
    "status": "Ativo",
    "obs": "Tomar após as refeições",
    "user_id": 2
  }
}
```

#### Respostas de erro:
- `404` - Nota não encontrada;
- `500` - Erro interno do servidor;

---

### `POST /notebooks`
Adiciona uma nova nota.

#### Corpo da Requisição:
```json
{
  "note_title": "Nota de Ibuprofeno",
  "med_stock_id": 15,
  "note_desc": "Instruções para uso de Ibuprofeno",
  "med_method": "Oral",
  "med_type": "Anti-inflamatório",
  "med_freq": "12h",
  "qtd_taken": 1,
  "qtd_total": 20,
  "init_schedule": "2024-02-01",
  "end_schedule": "2024-02-15",
  "status": "Ativo",
  "obs": "Tomar com água",
  "user_id": 1
}
```

#### Corpo da Resposta:
```json
{
  "success": true,
  "message": "Nota criada com sucesso"
}
```

#### Respostas de erro:
- `500` - Erro interno do servidor;

---

### `PATCH /notebooks/{id}`
Atualiza as informações de uma nota.

#### Corpo da Requisição:
```json
{
  "note_title": "Nota atualizada de Ibuprofeno",
  "med_stock_id": 15,
  "note_desc": "Instruções atualizadas para uso de Ibuprofeno",
  "med_method": "Oral",
  "med_type": "Anti-inflamatório",
  "med_freq": "12h",
  "qtd_taken": 1,
  "qtd_total": 20,
  "init_schedule": "2024-02-01",
  "end_schedule": "2024-02-15",
  "status": "Ativo",
  "obs": "Tomar com água",
  "user_id": 1
}
```

#### Corpo da Resposta:
```json
{
  "success": true,
  "message": "Nota atualizada com sucesso"
}
```

#### Respostas de erro:
- `404` - Nota não encontrada;
- `500` - Erro interno do servidor;

---

### `DELETE /notebooks/{id}`
Remove uma nota específica pelo `id`.

#### Corpo da Resposta:
```json
{
  "success": true,
  "message": "Nota deletada com sucesso"
}
```

#### Respostas de erro:
- `404` - Nota não encontrada;
- `500` - Erro interno do servidor;



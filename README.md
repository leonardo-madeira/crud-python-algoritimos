# Sistema de Cadastro de Clientes (CRUD em Python)

## 📋 Descrição do Projeto

Este projeto consiste em um sistema simples de cadastro de clientes, desenvolvido em Python, utilizando apenas recursos nativos da linguagem. Ele implementa um CRUD (Create, Read, Update, Delete) funcional, onde é possível cadastrar, listar, atualizar e deletar clientes e, com base no CPF que atua como identificador único, recuperar dados do cliente.

O sistema é totalmente interativo via terminal, voltado para aprendizado e prática de lógica de programação, manipulação de listas, estrutura de repetição e validações básicas de entrada de dados.

---

## 🚀 Funcionalidades

- **Cadastrar cliente:** Insere um novo cliente na lista após validação dos dados.
- **Listar clientes:** Exibe todos os clientes cadastrados com CPF e telefone formatados.
- **Atualizar cliente:** Permite substituir os dados de um cliente existente, buscando pelo CPF.
- **Deletar cliente:** Remove um cliente do sistema com confirmação do usuário.
- **Sair do sistema:** Finaliza a execução do programa.

---
## 🧠 Desenvolvimento e Estrutura

O projeto foi dividido em funções para modularizar as tarefas:

- `voltar_menu()`: Pergunta ao usuário se deseja retornar ao menu principal.
- `cadastrar_atualizar_cliente()`: Coleta dados do cliente e valida entrada.
- `listar_clientes(banco_de_dados)`: Formata e exibe os dados dos clientes.
- A lógica principal roda dentro de um `while True`, apresentando o menu de opções.

A estrutura de dados usada foi uma lista de listas, onde cada sublista representa um cliente.

---

## ❗ Validações Implementadas

- **CPF:** Deve conter 11 dígitos numéricos.
- **Telefone:** Deve conter 11 dígitos (DDD + número).
- **Email:** Deve conter "@" e ".".
- **Evita duplicação incorreta:** Utiliza o CPF como chave única para atualizar ou remover clientes.

---

## 💡 Desafios Encontrados

### 1. **Organização da estrutura de dados**
Inicialmente foi desafiador decidir como armazenar os dados dos clientes. A solução adotada foi usar uma lista onde cada cliente é representado por uma sublista com 5 campos fixos, invés do uso de dicionários.

### 2. **Validação de dados**
Outra dificuldade foi garantir que o sistema não aceitasse entradas inválidas. Foram implementadas validações simples porém eficazes para e-mail, CPF e telefone.

### 3. **Formatação de saída**
A apresentação dos dados do cliente exigiu a implementação de máscaras para CPF e telefone, o que foi resolvido com slicing de strings e formatação por índices.

### 4. **Atualização e deleção seguras**
Era necessário garantir que as operações de alteração e exclusão fossem feitas no cliente certo. Isso foi feito utilizando o CPF como identificador, evitando alterações equivocadas.

### 5. **Fluxo de navegação**
Garantir que o usuário pudesse retornar ao menu principal após cada operação foi fundamental. A função `voltar_menu()` foi criada para controlar esse comportamento.

---
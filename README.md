# Words API

Uma API simples para contar vogais em palavras e ordenar palavras.

## Endpoints

### 1. POST /vowel_count

Conta o número de vogais em uma lista de palavras.

**Parâmetros:**

- `words` (Obrigatório): Uma lista (array) com as palavras para o cálculo das vogais de cada uma.

**Exemplo de Requisição:**

```json
{
  "words": ["Darth Vader", "Han Solo", "Mestre Yoda", "Obi-Wan Kenobi"]
}
```

**Exemplo de Resposta:**

```json
{
  "Darth Vader": 3,
  "Han Solo": 3,
  "Mestre Yoda": 4,
  "Obi-Wan Kenobi": 6
}
```

### 2. POST /sort

Ordena uma lista de palavras em ordem crescente ou decrescente.

**Parâmetros:**

- `words` (Obrigatório): Uma lista (array) com as palavras para a ordenação.
- `order` (Obrigatório): Usar asc para ordenação crescente ou desc para a ordenação decrescente.

**Exemplo de Requisição:**

```json
{
  "words": ["Darth Vader", "Han Solo", "Mestre Yoda", "Obi-Wan Kenobi"],
  "order": "asc"
}
```

**Exemplo de Resposta:**

```json
[
  "Darth Vader",
  "Han Solo",
  "Mestre Yoda",
  "Obi-Wan Kenobi"
]
```

## Instalação e Execução

1. **Clonar o repositório:**

   ```bash
   git clone https://github.com/Lmicael/Words-API

2. **Instalar as dependências:**

    ```bash
    pip install -r requirements.txt

3. **Execução**

    ```bash
    cd src
    python app.py

A aplicação estará disponível em **http://127.0.0.1:5000**.

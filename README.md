# 📘 Atividade Prática: Test Driven Development (TDD)

> **Disciplina:** Engenharia de Software III  
> **Professor:** Willyams Saraiva  
> **Alunos:** Ananias Carlos, Davi Carreiro, Michel Jr, Sidney Nascimento
> **Tecnologia:** Python + PyTest

![Python](https://img.shields.io/badge/Python-3.11+-blue?style=for-the-badge&logo=python)
![TDD](https://img.shields.io/badge/Metodologia-TDD-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Concluído-brightgreen?style=for-the-badge)

---

## 🎯 Sobre o Projeto

Este projeto consiste no desenvolvimento de um módulo de calculadora utilizando estritamente a metodologia **TDD (Test Driven Development)**. [cite_start]O objetivo foi aplicar o ciclo **Red → Green → Refactor** para garantir a confiabilidade e qualidade do código desde a primeira linha[cite: 10, 13, 21].

O sistema inclui operações matemáticas básicas, validações de regras de negócio (como divisão por zero e paridade de inteiros) e uma interface de linha de comando (CLI) para demonstração.

---

## 📝 Relatório da Aplicação do TDD

[cite_start]Conforme solicitado nos critérios de avaliação, segue o resumo da experiência:

### [cite_start]1. O que é TDD? [cite: 67]
O *Test Driven Development* (Desenvolvimento Orientado a Testes) é uma prática de engenharia de software onde os testes automatizados são escritos **antes** do código de produção. Ele inverte a ordem tradicional de desenvolvimento, focando primeiro no comportamento desejado e depois na implementação.

### [cite_start]2. Como o TDD foi aplicado? [cite: 69]
Seguimos rigorosamente o ciclo de 3 passos:
1.  🔴 **RED:** Escrevemos um teste falho no `test_calculadora.py` para uma nova funcionalidade (ex: `somar`).
2.  🟢 **GREEN:** Implementamos o código mínimo em `calculadora_service.py` para fazer o teste passar.
3.  🔵 **REFACTOR:** Melhoramos o código (adicionando *Type Hints* e tratamento de erros) sem alterar o comportamento, garantido pelos testes que continuaram passando.

### [cite_start]3. Dificuldades e Benefícios [cite: 70, 71]
* **Dificuldade:** A principal dificuldade foi a mudança de mentalidade de não escrever a lógica imediatamente. Foi necessário "segurar a ansiedade" para escrever o teste primeiro. Também houve o desafio de definir regras matemáticas estritas (ex: paridade apenas para inteiros).
* **Benefícios:** O código nasceu testado e documentado. Quando precisamos alterar a lógica do `isPar` para rejeitar decimais, os testes existentes garantiram que nada mais quebrasse. A confiança na entrega é muito maior.

---

## 🛠️ Funcionalidades Implementadas

[cite_start]A classe `CalculadoraService` atende aos seguintes requisitos[cite: 27]:

* ✅ **Somar:** Soma de positivos, negativos e zeros.
* ✅ **Subtrair:** Subtração com suporte a resultados negativos.
* ✅ **Multiplicar:** Regra de sinais e multiplicação por zero.
* [cite_start]✅ **Dividir:** Suporte a decimais e bloqueio de **Divisão por Zero** (`ZeroDivisionError`)[cite: 50].
* ✅ **Verificar Paridade (`isPar`):** Validação estrita (apenas números inteiros). Lança erro se receber float (ex: `4.5`).
* ✅ **Validar Positivo:** Retorna `False` para zero e negativos.

---

## 📂 Estrutura do Projeto

```text
projeto_tdd_pytest/
│
├── calculadora_service.py   # Lógica de Negócio (Backend)
├── test_calculadora.py      # Testes Unitários (PyTest)
├── app.py                   # Interface Interativa (CLI)
└── README.md                # Documentação
```
---

## 🚀 Como Executar o Projeto

Siga os passos abaixo para rodar a aplicação em sua máquina.

### Pré-requisitos
* Python 3.8 ou superior instalado.

### 1. Instalação
Clone o repositório e instale a única dependência (PyTest):

```bash
# Clone o projeto
git clone [https://github.com/seu-usuario/projeto_tdd_pytest.git](https://github.com/seu-usuario/projeto_tdd_pytest.git)
cd projeto_tdd_pytest

# Crie um ambiente virtual (Opcional, mas recomendado)
python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Instale o PyTest
pip install pytest
```

### 2. Rodando os Testes (Prova do TDD)
Para verificar se todos os requisitos foram atendidos e ver os testes passando:

```bash
pytest -v
```

### 3. Rodando a Aplicação (Demo)
Para testar a calculadora manualmente através do menu interativo no terminal:

```bash
python app.py
```
---

Desenvolvido para a disciplina de Engenharia de Software III.
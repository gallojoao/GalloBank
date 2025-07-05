# 💰 Gallo Bank

Sistema simples de gerenciamento bancário feito em Python, como parte de um **desafio prático da plataforma [DIO](https://www.dio.me/)**.

Este projeto simula um banco com funcionalidades básicas como depósitos, saques e visualização de extrato, registrando cada transação com identificador único e data/hora.

---

## 🧾 Funcionalidades

- ✅ Realizar **depósitos** com limite de valor e quantidade
- ✅ Realizar **saques**, com verificação de saldo
- ✅ Consultar **extrato completo** com:
  - Tipo de transação (Depósito ou Saque)
  - Valor
  - Data e hora
  - ID único da transação

---

## 📌 Regras do Sistema

- Cada depósito deve ser de no máximo **R$ 500,00**
- O usuário pode realizar **até 3 depósitos**
- Saques são permitidos somente se houver saldo suficiente
- Cada operação é registrada no extrato com:
  - `ID único`
  - `Tipo`
  - `Valor`
  - `Data e Hora`

---

## 🧠 Tecnologias Usadas

- [Python 3](https://www.python.org/)
- Módulo `uuid` para gerar identificadores únicos
- Módulo `datetime` para registrar data e hora

---

## ▶️ Como Executar

1. Clone o repositório ou copie o arquivo `banco.py`
2. Execute o script com Python:

```bash
python banco.py 
```
3. Siga as instruções do menu interativo:
```
1 - Depositar
2 - Sacar
3 - Extrato
4 - Sair
```
## 📋 Exemplo de Extrato
```
===== EXTRATO =====
2025-07-05 14:33:12 | Depósito   | R$ 200.00 | ID: 4a9e2f0a
2025-07-05 14:45:09 | Saque      | R$ 100.00 | ID: b7d3ae11
===================
```
## 👨‍💻 Autor
Desenvolvido por João Gallo, como parte do desafio da [Digital Innovation One (DIO)](dio.me), com foco em prática de lógica e fundamentos de Python.


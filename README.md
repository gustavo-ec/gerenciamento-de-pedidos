# Sistema de Gerenciamento de Pedidos - Bubble Tea

Sistema em Python para gerenciamento de pedidos personalizados de **Bubble Tea**(https://en.wikipedia.org/wiki/Bubble_tea). Usa POO, JSON para persistência e modularização. Projeto acadêmico UEFS.

## 👤 Autor

- **Gustavo Silva Ribeiro**
- **Bacharelando em Engenharia da Computação – UEFS**
- **Email: gustavosr.comp@gmail.com** | **+55(75)99116-3924**

## Descrição

Permite que clientes montem sua bebida escolhendo:
- **Base** (leite, maracujá, rosa ou manga)
- **Complementos** (boba, lichia, geleia, taro, chia — quantos quiser)

Funcionalidades principais:
- Descontos por categoria de cliente:
  - Estudante (E): 25% de desconto
  - Professor/Funcionário (T): R$ 1,00 de desconto fixo
  - Comum (C): sem desconto
- Cashback de **10%** sobre o valor do pedido
- Opção de utilizar saldo de cashback acumulado em compras futuras
- Persistência de dados em arquivos JSON (`clientes.txt` e `pedidos.txt`)
- Histórico de pedidos consultável

## Tecnologias Utilizadas

- Python 3.13.4
- Programação Orientada a Objetos (POO)
- Biblioteca `json` para persistência
- Modularização (separação entre lógica de negócio e interface)

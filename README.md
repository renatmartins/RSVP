# 🐍 Código Python - Exemplos e Aplicação

Este repositório contém código Python demonstrando conceitos fundamentais e uma aplicação prática de gerenciamento de tarefas.

## 📁 Arquivos

### `exemplos_basicos.py`
Demonstra conceitos fundamentais do Python:
- ✅ Variáveis e tipos de dados
- ✅ Estruturas de dados (listas, tuplas, dicionários, sets)
- ✅ Estruturas de controle (if/else, loops)
- ✅ Funções
- ✅ Manipulação de listas e strings
- ✅ Tratamento de exceções
- ✅ Exemplo prático de análise de dados

### `main.py`
Aplicação completa de gerenciamento de tarefas com:
- ✅ Interface de menu interativo
- ✅ Adicionar, listar, completar e remover tarefas
- ✅ Sistema de prioridades
- ✅ Persistência de dados em JSON
- ✅ Funções matemáticas (Fibonacci, estatísticas)
- ✅ Tratamento robusto de erros

## 🚀 Como Executar

### Pré-requisitos
- Python 3.6 ou superior
- Sistema operacional: Linux, macOS ou Windows

### Executando os Exemplos Básicos
```bash
python3 exemplos_basicos.py
```

### Executando o Gerenciador de Tarefas
```bash
python3 main.py
```

## 📖 Funcionalidades do Gerenciador de Tarefas

### Menu Principal
1. **➕ Adicionar tarefa** - Cria uma nova tarefa com título, descrição e prioridade
2. **📋 Listar todas as tarefas** - Mostra todas as tarefas cadastradas
3. **⏳ Listar tarefas pendentes** - Exibe apenas tarefas não concluídas
4. **✅ Marcar tarefa como concluída** - Marca uma tarefa específica como finalizada
5. **🗑️ Remover tarefa** - Remove uma tarefa da lista
6. **📊 Demonstrar funções matemáticas** - Exemplos de Fibonacci e estatísticas
7. **🚪 Sair** - Encerra o programa

### Recursos Avançados
- **Persistência**: Dados salvos automaticamente em `tarefas.json`
- **Prioridades**: Sistema de cores (🔴 Alta, 🟡 Média, 🟢 Baixa)
- **Timestamps**: Registro da data de criação de cada tarefa
- **Validação**: Entrada de dados com tratamento de erros
- **Interface visual**: Uso de emojis para melhor experiência

## 🎯 Conceitos Python Demonstrados

### Programação Orientada a Objetos
- Classes e métodos
- Atributos de instância
- Encapsulamento

### Manipulação de Dados
- Listas e dicionários
- Serialização JSON
- Type hints

### Controle de Fluxo
- Estruturas condicionais
- Loops `for` e `while`
- List comprehensions

### Tratamento de Erros
- Blocos `try/except`
- Exceções específicas
- Recuperação graceful

### Funções Avançadas
- Parâmetros opcionais
- Documentação com docstrings
- Retorno de múltiplos tipos

## 📊 Exemplo de Uso

```python
# Criando instância do gerenciador
gerenciador = GerenciadorTarefas()

# Adicionando uma tarefa
gerenciador.adicionar_tarefa(
    titulo="Estudar Python",
    descricao="Revisar conceitos de POO",
    prioridade="alta"
)

# Listando tarefas
gerenciador.listar_tarefas()
```

## 🔧 Customização

Você pode personalizar o código modificando:

- **Arquivo de dados**: Altere `self.arquivo` na classe `GerenciadorTarefas`
- **Prioridades**: Adicione novos níveis no dicionário `prioridade_emoji`
- **Funções matemáticas**: Implemente novos algoritmos no menu opção 6

## 📝 Estrutura dos Dados

As tarefas são armazenadas no formato JSON:

```json
{
  "id": 1,
  "titulo": "Exemplo de tarefa",
  "descricao": "Descrição detalhada",
  "prioridade": "alta",
  "concluida": false,
  "data_criacao": "2024-01-15T10:30:00"
}
```

## 🐛 Tratamento de Erros

O código inclui tratamento para:
- ❌ Divisão por zero
- ❌ Tipos de dados inválidos
- ❌ Arquivos não encontrados
- ❌ IDs de tarefas inexistentes
- ❌ Interrupção pelo usuário (Ctrl+C)

## 📚 Aprendizado

Este código é ideal para:
- 🎓 Estudantes iniciantes em Python
- 👩‍💻 Desenvolvedores aprendendo POO
- 📖 Demonstração de boas práticas
- 🛠️ Base para projetos maiores

## 🤝 Contribuições

Sinta-se à vontade para:
- Adicionar novas funcionalidades
- Melhorar a interface
- Implementar novos algoritmos
- Corrigir bugs ou melhorar o código

---

**Desenvolvido com ❤️ em Python 🐍**
# Calculadora de Testes de Hipóteses

## Contribuições para o Projeto

Obrigado pelo interesse em contribuir! Este guia ajudará você a começar.

### Configurando o Ambiente de Desenvolvimento

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/seu-usuario/calculadora-testes-hipoteses.git
   cd calculadora-testes-hipoteses
   ```

2. **Crie um ambiente virtual**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Linux/Mac
   # ou
   .venv\Scripts\activate     # Windows
   ```

3. **Instale as dependências**:
   ```bash
   pip install -r requirements.txt
   ```

### Executando o Projeto

```bash
python hypothesis_calc.py
```

### Estrutura do Código

- **`hypothesis_calc.py`**: Código principal modular (versão atual)
- **`calculadora_testes_hipoteses.py`**: Versão anterior (para referência)
- **`fórmulas_principais.md`**: Documentação das fórmulas estatísticas
- **`pyproject.toml`**: Configurações do projeto e dependências

### Características do Código Atual

- **Modularidade**: Cada teste em função separada
- **Type Hints**: Anotações de tipo completas
- **Flexibilidade**: Suporte a entrada resumida ou completa
- **Validação**: Verificações robustas de parâmetros
- **Clareza**: Interface numerada e intuitiva

### Diretrizes de Contribuição

1. **Mantenha o código simples e educacional**
2. **Adicione docstrings em todas as funções**
3. **Use apenas NumPy e SciPy (sem pandas ou statsmodels)**
4. **Mantenha a interface de console interativa**
5. **Documente as fórmulas utilizadas**

### Reportando Bugs

Use as Issues do GitHub para reportar bugs, incluindo:
- Versão do Python
- Sistema operacional
- Passos para reproduzir o problema
- Saída esperada vs. atual

### Sugestões de Melhorias

- [ ] Interface gráfica (GUI)
- [ ] Exportação de resultados
- [ ] Mais tipos de testes
- [ ] Visualizações gráficas
- [ ] Testes unitários
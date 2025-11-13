# 📊 Calculadora Auxiliar de Testes de Hipóteses

Uma calculadora estatística interativa desenvolvida para auxiliar no cálculo de métricas intermediárias de diversos tipos de testes de hipóteses estatísticos.

## 🎯 Objetivo

Este projeto foi desenvolvido como parte dos estudos de **Análise Inferencial** e tem como objetivo fornecer uma ferramenta prática para:

- Calcular estatísticas de teste para diferentes tipos de testes de hipóteses
- Determinar valores críticos e p-valores
- Auxiliar na compreensão dos conceitos estatísticos
- Servir como material de apoio educacional

## ✨ Funcionalidades

A calculadora suporta os seguintes tipos de testes:

### 🔍 Testes para Média
- **Teste Z** (variância populacional conhecida)
- **Teste t** (variância populacional desconhecida)
- **Teste t pareado** (amostras dependentes)

### 📊 Testes para Proporção
- **Teste Z para proporção** (uma amostra)
- **Teste Z para diferença de proporções** (duas amostras)

### 📏 Testes para Variância
- **Teste Qui-quadrado** (uma amostra)
- **Teste F** (comparação de variâncias)

### 🔄 Testes de Comparação
- **Teste t para duas amostras independentes**
- **Teste t de Welch** (variâncias desiguais)
- **Teste Z para duas amostras** (variâncias conhecidas)

## 🛠️ Tecnologias Utilizadas

- **Python 3.13+**
- **NumPy** - Computação numérica
- **SciPy** - Distribuições estatísticas

## 📦 Instalação

### Pré-requisitos
- Python 3.13 ou superior
- pip (gerenciador de pacotes Python)

### Clonando o Repositório
```bash
git clone https://github.com/seu-usuario/calculadora-testes-hipoteses.git
cd calculadora-testes-hipoteses
```

### Instalando Dependências

#### Opção 1: Usando pip
```bash
pip install -r requirements.txt
```

#### Opção 2: Usando Poetry
```bash
poetry install
poetry shell
```

## 🚀 Como Usar

### Executando a Calculadora
```bash
python calculadora_testes_hipoteses.py
```

### Interface Interativa
A calculadora apresenta um menu interativo onde você pode escolher o tipo de teste desejado:

```
=== CALCULADORA DE TESTES DE HIPÓTESES ===

1. Teste Z (média, σ² conhecida)
2. Teste t (média, σ² desconhecida)
3. Teste t pareado (amostras dependentes)
4. Teste Z (proporção)
5. Teste Qui-quadrado (variância)
...
```

### Exemplo de Uso
```python
# Para um teste t de uma amostra
# Digite os valores quando solicitado:
# - Média amostral: 15.2
# - Média populacional (H0): 14.5
# - Desvio padrão amostral: 2.3
# - Tamanho da amostra: 25
# - Nível de significância: 0.05
```

## 📚 Documentação Adicional

- **[Fórmulas Principais](fórmulas_principais.md)** - Referência completa das fórmulas utilizadas
- Documentação inline no código fonte

## 🧮 Estrutura do Projeto

```
├── calculadora_testes_hipoteses.py  # Código principal
├── fórmulas_principais.md           # Documentação das fórmulas
├── pyproject.toml                   # Configuração do Poetry
├── requirements.txt                 # Dependências pip
├── README.md                       # Este arquivo
├── LICENSE                         # Licença do projeto
└── .gitignore                      # Arquivos ignorados pelo Git
```

## 🤝 Contribuindo

Contribuições são bem-vindas! Para contribuir:

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📝 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## 👨‍💻 Autor

**Arthur Garcia**
- Email: arturgarcia046@gmail.com
- GitHub: [@arturgarcia13](https://github.com/arturgarcia13)

## 🎓 Contexto Acadêmico

Este projeto foi desenvolvido como parte dos estudos de **Análise Inferencial** na faculdade, com foco em:
- Aplicação prática de conceitos estatísticos
- Desenvolvimento de ferramentas educacionais
- Programação científica em Python

## 📊 Status do Projeto

- ✅ Implementação dos principais testes de hipóteses
- ✅ Interface interativa de console
- ✅ Validação de entrada de dados
- ✅ Documentação das fórmulas
- 🔄 Em desenvolvimento: Interface gráfica (GUI)
- 🔄 Planejado: Exportação de relatórios

---

**📌 Nota**: Este é um projeto educacional desenvolvido para fins acadêmicos. Para análises estatísticas profissionais, considere usar bibliotecas especializadas como `statsmodels` ou `scikit-learn`.
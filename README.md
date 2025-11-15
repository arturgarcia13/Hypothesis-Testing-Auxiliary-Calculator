# 📊 Calculadora Estatística para Testes de Hipóteses

Uma calculadora estatística interativa desenvolvida para auxiliar no cálculo de métricas intermediárias de diversos tipos de testes de hipóteses estatísticos, **sem interpretação automática dos resultados**.

## 🎯 Objetivo

Este projeto foi desenvolvido como parte dos estudos de **Análise Inferencial** e tem como objetivo fornecer uma ferramenta prática e educacional para:

- Calcular estatísticas de teste e valores críticos
- Permitir entrada de dados tanto resumidos quanto amostras completas
- Implementar fórmulas manualmente (sem bibliotecas de alto nível)
- Auxiliar na compreensão dos conceitos estatísticos fundamentais
- Servir como material de apoio para estudos acadêmicos

## ✨ Funcionalidades

A calculadora implementa **9 tipos diferentes de testes estatísticos** com entrada flexível de dados:

### 🔍 Testes para Média
1. **Teste t para Média** (variância desconhecida)
2. **Teste Z para Média** (variância conhecida)

### 🔄 Testes de Comparação entre Amostras
3. **Diferença entre Médias** (variâncias desconhecidas e iguais)
4. **Teste t de Welch** (variâncias desconhecidas e diferentes)
5. **Amostras Emparelhadas** (teste t pareado)
6. **Diferença entre Médias** (variâncias conhecidas)

### 📊 Testes para Proporção
7. **Teste Z para Proporção** (uma amostra)
8. **Diferença entre Proporções** (teste Z)

### 📏 Testes para Variância
9. **Teste Qui-quadrado** (uma variância)
10. **Teste F** (diferença entre variâncias)

### 🎛️ Modos de Entrada
- **Valores Resumidos**: Insira diretamente média, desvio padrão, tamanho da amostra
- **Amostra Completa**: Digite todos os valores e as estatísticas serão calculadas automaticamente

## 🛠️ Tecnologias Utilizadas

- **Python 3.13+**
- **NumPy** - Operações matemáticas básicas (sqrt, etc.)
- **SciPy** - Distribuições estatísticas (t, F, chi², Normal)
- **Typing** - Anotações de tipo para maior clareza do código

## 🏗️ Características Técnicas

- ✅ **Implementação Manual**: Todas as fórmulas implementadas do zero
- ✅ **Entrada Flexível**: Suporte a valores resumidos ou amostras completas
- ✅ **Validação Robusta**: Verificação de entradas e tratamento de erros
- ✅ **Código Modular**: Funções separadas para cada tipo de teste
- ✅ **Type Hints**: Anotações de tipo para melhor documentação
- ✅ **Interface Intuitiva**: Menu interativo numerado e claro
- ❌ **Sem Pandas/Statsmodels**: Conforme especificação do projeto

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
python hypothesis_calc.py
```

### Interface Interativa
A calculadora apresenta um menu interativo numerado onde você pode escolher o tipo de teste desejado:

```
TIPOS DE TESTES DISPONÍVEIS
==============================
[1] Média com variância desconhecida (Teste t)
[2] Diferença entre médias (variâncias desconhecidas e iguais)
[3] Diferença entre médias (variâncias desconhecidas e diferentes - Welch)
[4] Amostras emparelhadas (Teste t pareado)
[5] Média com variância conhecida (Teste Z)
[6] Proporção (Teste Z)
[7] Variância (Teste Chi-quadrado)
[8] Diferença entre proporções (Teste Z)
[9] Diferença entre variâncias (Teste F)
```

### Exemplo de Uso

#### Opção 1: Valores Resumidos
```
x̄ (média amostral): 15.2
S (desvio padrão amostral): 2.3
n (tamanho da amostra): 25
μ₀ (média sob H₀): 14.5
α (nível de significância): 0.05
```

#### Opção 2: Amostra Completa
```
Digite os valores da amostra (separados por espaço): 12.5 15.2 14.8 16.1 13.9 15.5
μ₀ (média sob H₀): 14.5
α (nível de significância): 0.05
```

## 📚 Documentação Adicional

- **[Fórmulas Principais](fórmulas_principais.md)** - Referência completa das fórmulas utilizadas
- Documentação inline no código fonte

## 🧮 Estrutura do Projeto

```
├── hypothesis_calc.py              # 🎯 Código principal (NOVO)
├── calculadora_testes_hipoteses.py # Versão anterior (para referência)
├── fórmulas_principais.md          # Documentação das fórmulas
├── pyproject.toml                  # Configuração do Poetry
├── requirements.txt                # Dependências pip
├── setup.py                        # Script de configuração
├── README.md                      # Este arquivo
├── LICENSE                        # Licença do projeto
├── CHANGELOG.md                   # Histórico de versões
├── CONTRIBUTING.md                # Guia para contribuições
├── GITHUB_GUIDE.md               # Guia de publicação no GitHub
└── .gitignore                     # Arquivos ignorados pelo Git
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
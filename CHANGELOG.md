# Changelog

Todas as mudanças notáveis deste projeto serão documentadas neste arquivo.

O formato é baseado em [Keep a Changelog](https://keepachangelog.com/pt-BR/1.0.0/),
e este projeto segue [Semantic Versioning](https://semver.org/lang/pt-BR/).

## [0.1.0] - 2024-11-13

### Adicionado
- 🎉 Primeira versão da calculadora de testes de hipóteses
- ✨ Interface interativa de console
- 📊 Implementação completa dos principais testes estatísticos:
  - Teste Z para média (variância conhecida)
  - Teste t para média (variância desconhecida)
  - Teste t pareado (amostras dependentes)
  - Teste Z para proporção
  - Teste Qui-quadrado para variância
  - Teste t para diferença entre médias (variâncias iguais)
  - Teste t de Welch (variâncias diferentes)
  - Teste Z para diferença entre médias (variâncias conhecidas)
  - Teste Z para diferença entre proporções
  - Teste F para diferença entre variâncias
- 🔍 Validação robusta de entrada de dados
- 📋 Documentação das fórmulas principais em Markdown
- 🛡️ Tratamento de erros e exceções
- 📝 Docstrings detalhadas em todas as funções
- 🎯 Resultados formatados e organizados

### Detalhes Técnicos
- Python 3.13+ como requisito mínimo
- Dependências: NumPy (>=2.3.4) e SciPy (>=1.16.3)
- Arquitetura modular com funções específicas para cada teste
- Interface de console interativa com menu de seleção
- Validação de parâmetros estatísticos (tamanho de amostra, nível de significância, etc.)

### Contexto Acadêmico
- Desenvolvido para a disciplina de Análise Inferencial
- Foco educacional sem interpretação automática de resultados
- Proibido o uso de pandas e statsmodels conforme especificações

---

**Legenda:**
- 🎉 Nova funcionalidade principal
- ✨ Melhoria ou nova feature
- 🐛 Correção de bug
- 📚 Documentação
- 🔒 Segurança
- ⚡ Performance
- 🛠️ Manutenção
- 📊 Análise/Estatística
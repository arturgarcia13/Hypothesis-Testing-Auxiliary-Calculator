# Changelog

Todas as mudanças notáveis deste projeto serão documentadas neste arquivo.

O formato é baseado em [Keep a Changelog](https://keepachangelog.com/pt-BR/1.0.0/),
e este projeto segue [Semantic Versioning](https://semver.org/lang/pt-BR/).

## [0.2.0] - 2024-11-15

### Adicionado
- 🎉 **Nova versão modular** com código completamente refatorado (`hypothesis_calc.py`)
- ✨ **Entrada flexível de dados**: Valores resumidos OU amostra completa
- 📊 **9 testes estatísticos** implementados com fórmulas manuais:
  1. Teste t para média (variância desconhecida)
  2. Diferença entre médias (variâncias desconhecidas e iguais)
  3. Teste t de Welch (variâncias desconhecidas e diferentes)
  4. Amostras emparelhadas (teste t pareado)
  5. Teste Z para média (variância conhecida)
  6. Teste Z para proporção
  7. Teste Qui-quadrado para variância
  8. Teste Z para diferença entre proporções
  9. Teste F para diferença entre variâncias
- 🔧 **Type hints** completas para melhor documentação do código
- 🎛️ **Interface aprimorada** com menu numerado mais intuitivo
- 📈 **Cálculo automático** de estatísticas quando amostra completa é fornecida
- 🛡️ **Validação robusta** com mensagens de erro claras
- 📋 **Resultados padronizados** em formato de dicionário

### Melhorias Técnicas
- Arquitetura mais limpa com funções modulares independentes
- Separação clara entre lógica de cálculo e interface
- Suporte a ambos os tipos de entrada (resumidos/completos)
- Validação específica para cada tipo de parâmetro
- Tratamento de exceções mais robusto

### Compatibilidade
- Mantém `calculadora_testes_hipoteses.py` como referência
- Mesmas dependências: NumPy e SciPy
- Python 3.13+ como requisito

## [0.1.0] - 2024-11-13

### Adicionado
- 🎉 Primeira versão da calculadora de testes de hipóteses
- ✨ Interface interativa de console
- 📊 Implementação completa dos principais testes estatísticos
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
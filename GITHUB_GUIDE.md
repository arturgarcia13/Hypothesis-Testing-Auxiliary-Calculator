# Guia de Publicação no GitHub

## 📋 Pré-requisitos

Antes de publicar, certifique-se de ter:
- [x] Conta no GitHub criada
- [x] Git instalado localmente
- [x] Projeto finalizado e testado

## 🚀 Passos para Publicação

### 1. Inicializar Repositório Git Local

Abra o terminal na pasta do projeto e execute:

```bash
# Inicializar repositório Git
git init

# Adicionar todos os arquivos
git add .

# Fazer o primeiro commit
git commit -m "feat: implementação inicial da calculadora de testes de hipóteses

- Adiciona interface interativa de console
- Implementa 10 tipos diferentes de testes estatísticos
- Inclui validação robusta de entrada de dados
- Adiciona documentação completa das fórmulas
- Configura estrutura do projeto para publicação"
```

### 2. Criar Repositório no GitHub

1. Acesse [GitHub](https://github.com)
2. Clique em **"New repository"**
3. Configure:
   - **Repository name**: `calculadora-testes-hipoteses`
   - **Description**: `🧮 Calculadora estatística interativa para testes de hipóteses desenvolvida em Python`
   - **Visibility**: Public (ou Private se preferir)
   - **NÃO** marque "Initialize with README" (já temos um)

### 3. Conectar e Enviar para o GitHub

```bash
# Adicionar repositório remoto (substituir SEU_USUARIO pelo seu username do GitHub)
git remote add origin https://github.com/SEU_USUARIO/calculadora-testes-hipoteses.git

# Definir branch principal
git branch -M main

# Enviar para o GitHub
git push -u origin main
```

### 4. Configurar o Repositório no GitHub

Após o upload, configure no GitHub:

#### Topics/Tags
Adicione as tags no repositório:
- `python`
- `estatistica`
- `testes-hipoteses`
- `analise-inferencial`
- `educacao`
- `numpy`
- `scipy`
- `faculdade`

#### About Section
- **Description**: Calculadora estatística interativa para testes de hipóteses
- **Website**: Deixe em branco ou adicione um link se tiver
- **Topics**: Use as tags acima

#### Settings Recomendadas
- **Issues**: ✅ Habilitado
- **Wiki**: ⬜ Opcional
- **Discussions**: ⬜ Opcional
- **Projects**: ⬜ Opcional

### 5. Criar Release (Opcional)

Para criar a primeira release:

1. Vá para **Releases** no repositório
2. Clique em **"Create a new release"**
3. Configure:
   - **Tag version**: `v0.1.0`
   - **Release title**: `🎉 Primeira Versão - Calculadora de Testes de Hipóteses v0.1.0`
   - **Description**: Copie o conteúdo da seção [0.1.0] do CHANGELOG.md

## 🔧 Comandos Úteis para Manutenção

### Atualizações Futuras
```bash
# Adicionar mudanças
git add .

# Commit com mensagem descritiva
git commit -m "tipo: descrição das mudanças"

# Enviar para o GitHub
git push
```

### Tipos de Commit Recomendados
- `feat:` - Nova funcionalidade
- `fix:` - Correção de bug
- `docs:` - Mudanças na documentação
- `style:` - Formatação, sem mudança de funcionalidade
- `refactor:` - Refatoração de código
- `test:` - Adição de testes
- `chore:` - Manutenção geral

## 📋 Checklist Final

Antes de publicar, verifique:
- [x] README.md completo e informativo
- [x] .gitignore configurado adequadamente
- [x] LICENSE incluída
- [x] requirements.txt atualizado
- [x] pyproject.toml configurado
- [x] CHANGELOG.md documentado
- [x] Código testado e funcionando
- [x] Documentação das fórmulas incluída
- [x] Setup.py para instalação fácil

## 🌟 Próximos Passos

Após a publicação, considere:
1. Adicionar badges no README (build status, license, etc.)
2. Configurar GitHub Actions para testes automatizados
3. Criar issues para melhorias futuras
4. Convidar colaboradores se necessário
5. Divulgar o projeto em redes acadêmicas

---

**Dica**: Mantenha o repositório atualizado regularmente e documente todas as mudanças no CHANGELOG.md!
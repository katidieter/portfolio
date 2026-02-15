# Portfolio Streamlit

Um portfólio pessoal interativo desenvolvido com Streamlit, com suporte a múltiplos idiomas (Português e Inglês).

## Características

- 🌐 Suporte a múltiplos idiomas (PT/EN)
- 📱 Design responsivo
- 🎨 Interface moderna e profissional
- 📊 Seções: Sobre, Projetos, Mentoria, Recomendações, Conteúdos e Contato

## Estrutura do Projeto

```
portfolio-streamlit/
├── app.py                 # Aplicação principal
├── components/            # Componentes customizados
│   ├── buttons.py        # Botões HTML customizados
│   └── cards.py          # Cards de projetos
├── data/                  # Dados e traduções
│   ├── translations.py   # Dicionários de tradução
│   ├── projects.py       # Dados dos projetos
│   ├── mentorship.py     # Dados de mentoria
│   ├── recommendations.py # Recomendações
│   └── content.py        # Conteúdos publicados
├── assets/               # Recursos estáticos
│   └── profile.jpg       # Imagem de perfil
├── requirements.txt      # Dependências Python
└── README.md            # Este arquivo
```

## Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)
- Git (para clonar o repositório)

## Instalação

### 1. Clone o repositório

```bash
git clone <repository-url>
cd portfolio-streamlit
```

### 2. Crie um ambiente virtual (recomendado)

**No Linux/macOS:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**No Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure seus dados pessoais

Edite os arquivos em `data/` para adicionar suas informações:
- `data/about.py` - Suas informações pessoais e profissionais
- `data/projects.py` - Seus projetos
- `data/mentorship.py` - Informações sobre mentoria (se aplicável)
- `data/recommendations.py` - Suas recomendações de livros, cursos e ferramentas
- `data/content.py` - Seus artigos, vídeos e outros conteúdos

### 5. Adicione sua foto de perfil

Substitua o arquivo `assets/profile.jpg` pela sua foto de perfil.

## Execução Local

### Iniciar a aplicação

Execute o seguinte comando no diretório raiz do projeto:

```bash
streamlit run app.py
```

A aplicação estará disponível em `http://localhost:8501`

### Parar a aplicação

Pressione `Ctrl+C` no terminal onde a aplicação está rodando.

### Visualizar em outro dispositivo na mesma rede

Quando você inicia a aplicação, o Streamlit exibe dois URLs:
- **Local URL**: `http://localhost:8501` (apenas no seu computador)
- **Network URL**: `http://192.168.x.x:8501` (acessível de outros dispositivos na mesma rede)

Use o Network URL para testar em dispositivos móveis na mesma rede Wi-Fi.

## Testes

### Executar testes unitários

```bash
pytest
```

### Executar testes com cobertura

```bash
pytest --cov=. --cov-report=html
```

O relatório de cobertura será gerado em `htmlcov/index.html`.

### Executar testes de propriedades (Property-Based Tests)

```bash
pytest -v -k property
```

## Deployment no Streamlit Cloud

O Streamlit Cloud oferece hospedagem gratuita para aplicações Streamlit. Siga os passos abaixo:

### 1. Prepare seu repositório

Certifique-se de que seu código está em um repositório GitHub público ou privado.

**Arquivos necessários:**
- `app.py` - Arquivo principal da aplicação
- `requirements.txt` - Dependências Python
- `.streamlit/config.toml` - Configurações de tema (opcional)
- Todos os arquivos em `components/`, `data/` e `assets/`

### 2. Acesse o Streamlit Cloud

1. Vá para [share.streamlit.io](https://share.streamlit.io)
2. Faça login com sua conta GitHub

### 3. Deploy da aplicação

1. Clique em "New app"
2. Selecione seu repositório GitHub
3. Escolha o branch (geralmente `main` ou `master`)
4. Defina o caminho do arquivo principal: `app.py`
5. (Opcional) Configure variáveis de ambiente em "Advanced settings"
6. Clique em "Deploy!"

### 4. Aguarde o deployment

O Streamlit Cloud irá:
- Instalar as dependências do `requirements.txt`
- Executar sua aplicação
- Fornecer uma URL pública (ex: `https://seu-usuario-portfolio.streamlit.app`)

O processo geralmente leva 2-5 minutos.

### 5. Atualizações automáticas

Sempre que você fizer push de novas alterações para o branch configurado, o Streamlit Cloud automaticamente:
- Detecta as mudanças
- Reconstrói a aplicação
- Atualiza o deployment

### Troubleshooting no Streamlit Cloud

**Erro de dependências:**
- Verifique se todas as bibliotecas estão listadas em `requirements.txt`
- Use versões específicas (ex: `streamlit==1.28.0`) para evitar incompatibilidades

**Erro de arquivo não encontrado:**
- Certifique-se de que todos os arquivos necessários estão no repositório
- Verifique os caminhos relativos no código

**Aplicação não inicia:**
- Verifique os logs no painel do Streamlit Cloud
- Teste localmente antes de fazer deploy

### Gerenciar sua aplicação

No painel do Streamlit Cloud você pode:
- Ver logs em tempo real
- Reiniciar a aplicação
- Alterar configurações
- Excluir o deployment

## Personalização

### Alterar o tema

Edite `.streamlit/config.toml` para personalizar cores e aparência:

```toml
[theme]
primaryColor = "#0066cc"        # Cor primária (botões, links)
backgroundColor = "#ffffff"      # Cor de fundo
secondaryBackgroundColor = "#f0f2f6"  # Cor de fundo secundária
textColor = "#262730"           # Cor do texto
font = "sans serif"             # Fonte
```

### Adicionar novas seções

1. Crie um novo módulo de dados em `data/`
2. Adicione traduções em `data/translations.py`
3. Crie uma função de renderização em `app.py`
4. Adicione a seção ao menu no `render_sidebar()`

## Estrutura de Dados

### Formato de Projetos

```python
{
    "title": {"pt": "Título PT", "en": "Title EN"},
    "description": {"pt": "Descrição PT", "en": "Description EN"},
    "technologies": ["Python", "Streamlit", "Pandas"],
    "url": "https://github.com/user/project"
}
```

### Formato de Recomendações

```python
{
    "title": {"pt": "Título PT", "en": "Title EN"},
    "category": "book",  # book, course, tool, article
    "description": {"pt": "Descrição PT", "en": "Description EN"},
    "author_creator": "Nome do Autor",
    "url": "https://link-to-resource.com",
    "reason": {"pt": "Por que recomendo PT", "en": "Why I recommend EN"}
}
```

## Desenvolvimento

Este projeto segue a metodologia de desenvolvimento orientado por especificações. Consulte os documentos em `.kiro/specs/portfolio-streamlit/` para mais detalhes sobre requisitos, design e tarefas de implementação.

## Licença

[Adicione sua licença aqui]

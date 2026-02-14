# Plano de Implementação: Portfolio Streamlit

## Visão Geral

Este plano implementa um portfólio pessoal com Streamlit, incluindo seis seções principais (Sobre, Projetos, Mentoria, Recomendações, Conteúdos e Contato), suporte a múltiplos idiomas (Português e Inglês), e componentes customizados para uma apresentação profissional.

## Tarefas

- [x] 1. Configurar estrutura inicial do projeto
  - Criar estrutura de diretórios (components/, data/, assets/)
  - Criar arquivo requirements.txt com dependências (streamlit, hypothesis, pytest, pytest-cov)
  - Criar arquivo README.md com instruções básicas
  - _Requisitos: 10.1, 10.3_

- [x] 2. Implementar módulo de traduções
  - [x] 2.1 Criar data/translations.py com dicionário de traduções
    - Implementar TRANSLATIONS com chaves para todas as seções
    - Incluir traduções para PT e EN
    - Implementar função get_translation(key, language)
    - _Requisitos: 3.1, 3.4, 8.1_
  
  - [ ]* 2.2 Escrever teste de propriedade para completude de traduções
    - **Propriedade 3: Completude de traduções**
    - **Valida: Requisitos 3.2, 3.4**

- [x] 3. Implementar módulos de dados
  - [x] 3.1 Criar data/projects.py com dados de projetos
    - Implementar lista PROJECTS com estrutura de dados definida
    - Implementar função get_projects()
    - _Requisitos: 5.1, 8.2_
  
  - [x] 3.2 Criar data/mentorship.py com informações de mentoria
    - Implementar dicionário MENTORSHIP_INFO
    - Implementar função get_mentorship_info()
    - _Requisitos: 8.2_
  
  - [x] 3.3 Criar data/recommendations.py com recomendações do profissional
    - Implementar lista RECOMMENDATIONS com livros, cursos, ferramentas recomendados
    - Implementar função get_recommendations(category)
    - _Requisitos: 7.1, 7.2, 7.3, 9.2_
  
  - [x] 3.4 Criar data/content.py com conteúdos publicados
    - Implementar lista CONTENTS
    - Implementar função get_contents(content_type)
    - _Requisitos: 8.2_
  
  - [ ]* 3.5 Escrever teste de propriedade para integridade de dados de projetos
    - **Propriedade 4: Integridade de dados de projetos**
    - **Valida: Requisitos 5.2, 5.3**

- [x] 4. Implementar componentes customizados
  - [x] 4.1 Criar components/buttons.py com botões HTML customizados
    - Implementar função create_custom_button(text, url, background_color, text_color, border_radius)
    - Usar streamlit.components.html para renderizar HTML customizado
    - _Requisitos: 6.1, 6.2, 6.3_
  
  - [ ]* 4.2 Escrever teste de propriedade para customização de botões
    - **Propriedade 6: Customização de botões**
    - **Valida: Requisitos 6.1, 6.3**
  
  - [ ]* 4.3 Escrever teste de propriedade para URLs de botões
    - **Propriedade 7: Botões abrem URLs corretas**
    - **Valida: Requisitos 6.2, 7.4**
  
  - [x] 4.4 Criar components/cards.py com cards de projetos
    - Implementar função render_project_card(title, description, technologies, url, language)
    - Implementar função render_projects_grid(projects, language)
    - _Requisitos: 5.2, 5.3, 5.4_
  
  - [ ]* 4.5 Escrever teste de propriedade para layout de múltiplos projetos
    - **Propriedade 5: Layout organizado de múltiplos projetos**
    - **Valida: Requisitos 5.4**

- [x] 5. Implementar aplicação principal
  - [x] 5.1 Criar app.py com configuração inicial
    - Implementar função setup_page() para configurar título, ícone e layout
    - Implementar função initialize_session_state() para inicializar language e current_section
    - _Requisitos: 1.1, 1.2, 1.3, 2.4, 3.3_
  
  - [ ]* 5.2 Escrever testes unitários para configuração da página
    - Verificar que page_config é chamado com parâmetros corretos
    - Verificar que session_state é inicializado corretamente
    - _Requisitos: 1.1, 1.2, 1.3_
  
  - [ ]* 5.3 Escrever teste de propriedade para persistência de estado
    - **Propriedade 2: Persistência de estado da sessão**
    - **Valida: Requisitos 2.4, 3.3**

- [x] 6. Implementar sidebar e navegação
  - [x] 6.1 Criar função render_sidebar() em app.py
    - Implementar seletor de idioma
    - Implementar menu de navegação com todas as seções
    - Retornar seção selecionada
    - _Requisitos: 2.1, 2.2, 2.3, 3.1_
  
  - [ ]* 6.2 Escrever teste de propriedade para navegação
    - **Propriedade 1: Navegação exibe conteúdo correspondente**
    - **Valida: Requisitos 2.2**
  
  - [ ]* 6.3 Escrever testes unitários para seções obrigatórias
    - Verificar que About, Projects, Mentorship, Recommendations, Content e Contact estão disponíveis
    - Verificar que idiomas PT e EN estão disponíveis
    - _Requisitos: 2.3, 3.1_

- [x] 7. Implementar seção Sobre
  - [x] 7.1 Criar função render_about_section(language) em app.py
    - Exibir foto de perfil
    - Exibir introdução profissional traduzida
    - Exibir skills e tecnologias
    - Exibir resumo profissional
    - _Requisitos: 4.1, 4.2, 4.3, 4.4_
  
  - [ ]* 7.2 Escrever testes unitários para seção Sobre
    - Verificar que todos os elementos são exibidos
    - _Requisitos: 4.1, 4.2, 4.3, 4.4_

- [ ] 8. Implementar seção Projetos
  - [x] 8.1 Criar função render_projects_section(language) em app.py
    - Carregar projetos de data/projects.py
    - Usar render_projects_grid para exibir projetos
    - _Requisitos: 5.1, 5.4_
  
  - [ ]* 8.2 Escrever testes unitários para seção Projetos
    - Verificar que projetos são exibidos
    - _Requisitos: 5.1_

- [x] 9. Implementar seção Mentoria
  - [x] 9.1 Criar função render_mentorship_section(language) em app.py
    - Carregar informações de data/mentorship.py
    - Exibir descrição, áreas e disponibilidade
    - Incluir botão para agendamento
    - _Requisitos: 8.2_
  
  - [ ]* 9.2 Escrever testes unitários para seção Mentoria
    - Verificar que informações de mentoria são exibidas
    - _Requisitos: 8.2_

- [x] 10. Implementar seção Recomendações
  - [x] 10.1 Criar função render_recommendations_section(language) em app.py
    - Carregar recomendações de data/recommendations.py
    - Exibir cada recomendação com título, categoria, descrição, autor/criador e motivo
    - Incluir filtro opcional por categoria (livros, cursos, ferramentas, etc.)
    - Incluir botão/link para acessar o recurso recomendado
    - _Requisitos: 7.1, 7.2, 7.3, 7.4_
  
  - [ ]* 10.2 Escrever testes unitários para seção Recomendações
    - Verificar que recomendações são exibidas corretamente
    - Verificar que filtro por categoria funciona
    - _Requisitos: 7.1, 7.2, 7.3_

- [x] 11. Implementar seção Conteúdos
  - [x] 11.1 Criar função render_content_section(language) em app.py
    - Carregar conteúdos de data/content.py
    - Exibir conteúdos com título, descrição, tipo e tags
    - Incluir filtro opcional por tipo de conteúdo
    - _Requisitos: 8.2_
  
  - [ ]* 11.2 Escrever testes unitários para seção Conteúdos
    - Verificar que conteúdos são exibidos
    - _Requisitos: 8.2_
  
  - [ ]* 11.3 Escrever teste de propriedade para atualização dinâmica de conteúdo
    - **Propriedade 9: Atualização dinâmica de conteúdo**
    - **Valida: Requisitos 8.4**

- [x] 12. Implementar seção Contato
  - [x] 12.1 Criar função render_contact_section(language) em app.py
    - Exibir botões para email e LinkedIn
    - Incluir botões para redes sociais adicionais (GitHub e Medium.)
    - Usar create_custom_button para todos os botões
    - _Requisitos: 7.1, 7.2, 7.3_
  
  - [ ]* 12.2 Escrever testes unitários para seção Contato
    - Verificar que botões de contato são exibidos
    - _Requisitos: 7.1, 7.2_
  
  - [ ]* 12.3 Escrever teste de propriedade para suporte a links de redes sociais
    - **Propriedade 8: Suporte a links de redes sociais**
    - **Valida: Requisitos 7.3**

- [x] 13. Implementar função principal e coordenação
  - [x] 13.1 Criar função render_content(section, language) em app.py
    - Implementar switch/match para renderizar seção apropriada
    - Chamar função de renderização correspondente para cada seção
    - _Requisitos: 2.2_
  
  - [x] 13.2 Criar função main() em app.py
    - Chamar setup_page()
    - Chamar initialize_session_state()
    - Chamar render_sidebar() e obter seção selecionada
    - Chamar render_content() com seção e idioma
    - _Requisitos: 1.1, 2.2_
  
  - [x] 13.3 Adicionar ponto de entrada if __name__ == "__main__"
    - Chamar main()

- [ ] 14. Checkpoint - Garantir que todos os testes passam
  - Executar pytest para testes unitários
  - Executar testes de propriedades com Hypothesis
  - Verificar cobertura de código (mínimo 80%)
  - Perguntar ao usuário se há dúvidas

- [x] 15. Adicionar responsividade e layout
  - [x] 15.1 Implementar uso de colunas do Streamlit
    - Usar st.columns() para organizar conteúdo em seções apropriadas
    - Garantir layout responsivo
    - _Requisitos: 9.1, 9.3_
  
  - [ ]* 15.2 Escrever testes unitários para componentes de layout
    - Verificar que colunas são usadas apropriadamente
    - _Requisitos: 9.1, 9.3_

- [ ] 16. Adicionar tratamento de erros
  - [ ] 16.1 Implementar tratamento de chaves de tradução ausentes
    - Adicionar fallback para chave original
    - Adicionar logging de avisos
    - _Requisitos: 3.2_
  
  - [ ] 16.2 Implementar validação de dados de projetos
    - Validar campos obrigatórios antes de renderizar
    - Exibir mensagem de erro para dados incompletos
    - _Requisitos: 5.2_
  
  - [ ] 16.3 Implementar validação de URLs
    - Validar formato de URLs antes de criar botões
    - Desabilitar botões com URLs inválidas
    - _Requisitos: 6.2_
  
  - [ ]* 16.4 Escrever testes unitários para tratamento de erros
    - Testar comportamento com dados inválidos
    - Testar fallbacks

- [ ] 17. Adicionar assets e conteúdo real
  - [ ] 17.1 Adicionar imagem de perfil em assets/
    - Adicionar foto de perfil ou avatar
    - _Requisitos: 4.2_
  
  - [ ] 17.2 Preencher dados reais nos módulos de dados
    - Adicionar projetos reais em data/projects.py
    - Adicionar informações de mentoria em data/mentorship.py
    - Adicionar suas recomendações de livros, cursos e ferramentas em data/recommendations.py
    - Adicionar conteúdos em data/content.py
    - _Requisitos: 9.2_

- [x] 18. Configurar para deployment
  - [x] 18.1 Criar arquivo .streamlit/config.toml
    - Configurar tema e aparência
    - _Requisitos: 10.4_
  
  - [x] 18.2 Atualizar README.md com instruções completas
    - Adicionar instruções de instalação
    - Adicionar instruções de execução local
    - Adicionar instruções de deployment no Streamlit Cloud
    - _Requisitos: 10.3_
  
  - [x] 18.3 Verificar compatibilidade com Streamlit Cloud
    - Testar que requirements.txt está completo
    - Verificar que não há dependências de sistema
    - _Requisitos: 10.2, 10.4_

- [ ] 19. Checkpoint final - Validação completa
  - Executar aplicação localmente e testar todas as seções
  - Verificar alternância de idiomas
  - Verificar todos os links e botões
  - Garantir que todos os testes passam
  - Perguntar ao usuário se há ajustes necessários

## Notas

- Tarefas marcadas com `*` são opcionais e podem ser puladas para um MVP mais rápido
- Cada tarefa referencia requisitos específicos para rastreabilidade
- Checkpoints garantem validação incremental
- Testes de propriedades validam propriedades universais de corretude
- Testes unitários validam exemplos específicos e casos extremos

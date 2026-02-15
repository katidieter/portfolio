"""
Componente de cards de projetos para o portfólio Streamlit.

Este módulo fornece funções para renderizar cards de projetos e organizar
múltiplos projetos em um layout de grid.
"""

import streamlit as st
from data.translations import get_translation


def render_project_card(
    title: str,
    description: str,
    technologies: list[str],
    url: str,
    language: str
) -> None:
    """
    Renderiza um card de projeto com informações formatadas.
    
    Args:
        title: Título do projeto
        description: Descrição do projeto
        technologies: Lista de tecnologias utilizadas
        url: Link para o projeto
        language: Idioma atual para tradução de labels
    """
    with st.container():
        st.markdown(f"### {title}")
        st.write(description)
        
        # Exibir tecnologias
        if technologies:
            tech_label = get_translation("projects_technologies", language)
            tech_badges = " • ".join([f"`{tech}`" for tech in technologies])
            st.markdown(f"**{tech_label}:** {tech_badges}")
        
        # Botão para ver projeto
        view_text = get_translation("projects_view", language)
        st.markdown(
            f'<a href="{url}" target="_blank" style="'
            'display: inline-block; '
            'padding: 0.5rem 1rem; '
            'background-color: #0066cc; '
            'color: white; '
            'text-decoration: none; '
            'border-radius: 5px; '
            'margin-top: 0.5rem; '
            'font-weight: 500;">'
            f'{view_text}</a>',
            unsafe_allow_html=True
        )
        
        st.markdown("---")


def render_projects_grid(projects: list[dict], language: str) -> None:
    """
    Renderiza múltiplos projetos em layout de grid responsivo.
    
    Args:
        projects: Lista de dicionários com dados dos projetos
        language: Idioma atual
    """
    if not projects:
        empty_message = get_translation("projects_empty", language)
        st.info(empty_message)
        return
    
    # Renderizar projetos em colunas responsivas (2 por linha)
    # Usar gap entre colunas para melhor espaçamento
    for i in range(0, len(projects), 2):
        cols = st.columns(2, gap="large")
        
        # Primeiro projeto da linha
        with cols[0]:
            project = projects[i]
            title = project["title"].get(language, project["title"].get("pt", ""))
            description = project["description"].get(language, project["description"].get("pt", ""))
            
            render_project_card(
                title=title,
                description=description,
                technologies=project.get("technologies", []),
                url=project.get("url", "#"),
                language=language
            )
        
        # Segundo projeto da linha (se existir)
        if i + 1 < len(projects):
            with cols[1]:
                project = projects[i + 1]
                title = project["title"].get(language, project["title"].get("pt", ""))
                description = project["description"].get(language, project["description"].get("pt", ""))
                
                render_project_card(
                    title=title,
                    description=description,
                    technologies=project.get("technologies", []),
                    url=project.get("url", "#"),
                    language=language
                )
        else:
            # Se houver número ímpar de projetos, deixar a segunda coluna vazia
            # mas manter o layout consistente
            with cols[1]:
                st.empty()

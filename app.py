"""
Portfolio Streamlit Application

Main application file for the personal portfolio built with Streamlit.
Supports multiple languages (Portuguese and English) and multiple sections.
"""

import streamlit as st
from data.translations import get_translation
from data.about import get_about_info
from data.projects import get_projects
from data.mentorship import get_mentorship_info
from data.recommendations import get_recommendations
from data.content import get_contents
from components.cards import render_projects_grid
from components.buttons import create_custom_button
import os


def setup_page() -> None:
    """
    Configura as propriedades da página Streamlit.
    
    Configura título, ícone e layout da página conforme requisitos 1.1, 1.2, 1.3.
    """
    st.set_page_config(
        page_title="Portfolio",
        page_icon="👨‍💻",
        layout="wide",
        initial_sidebar_state="expanded"
    )


def initialize_session_state() -> None:
    """
    Inicializa variáveis de estado da sessão.
    
    Inicializa language (idioma padrão: português) e current_section (seção padrão: about)
    conforme requisitos 2.4 e 3.3.
    """
    if "language" not in st.session_state:
        st.session_state.language = "pt"
    
    if "current_section" not in st.session_state:
        st.session_state.current_section = "about"


def render_about_section(language: str) -> None:
    """
    Renderiza a seção Sobre com informações profissionais.
    
    Exibe:
    - Foto de perfil
    - Introdução profissional traduzida
    - Skills e tecnologias
    - Resumo profissional
    
    Args:
        language: Código do idioma ('pt' ou 'en')
    
    Requisitos: 4.1, 4.2, 4.3, 4.4
    """
    about_info = get_about_info()
    
    # Título da seção
    st.title(get_translation("about_title", language))
    
    # Layout com colunas para foto e introdução
    col1, col2 = st.columns([1, 2])
    
    with col1:
        # Exibir foto de perfil se existir, caso contrário usar emoji
        profile_image_path = about_info.get("profile_image", "")
        if profile_image_path and os.path.exists(profile_image_path):
            st.image(profile_image_path, width=250)
        else:
            # Usar emoji como avatar padrão se imagem não existir
            st.markdown("## 👨‍💻")
            st.caption("Foto de perfil")
    
    with col2:
        # Nome
        st.header(about_info.get("name", ""))
        
        # Introdução profissional traduzida
        introduction = about_info.get("introduction", {}).get(language, "")
        if introduction:
            st.markdown(introduction)
    
    st.divider()
    
    # Skills e Tecnologias em colunas
    col_skills, col_tech = st.columns(2)
    
    with col_skills:
        st.subheader(get_translation("about_skills", language))
        skills = about_info.get("skills", [])
        if skills:
            # Exibir skills como badges/pills
            for skill in skills:
                st.markdown(f"- {skill}")
        else:
            st.info("Nenhuma habilidade cadastrada.")
    
    with col_tech:
        st.subheader(get_translation("about_technologies", language))
        technologies = about_info.get("technologies", [])
        if technologies:
            # Exibir tecnologias como badges/pills
            for tech in technologies:
                st.markdown(f"- {tech}")
        else:
            st.info("Nenhuma tecnologia cadastrada.")
    
    st.divider()
    
    # Resumo profissional
    st.subheader(get_translation("about_summary", language))
    summary = about_info.get("summary", {}).get(language, "")
    if summary:
        st.markdown(summary)
    else:
        st.info("Resumo profissional não disponível.")


def render_projects_section(language: str) -> None:
    """
    Renderiza a seção de Projetos com lista de projetos.
    
    Carrega projetos de data/projects.py e usa render_projects_grid
    para exibir em layout organizado.
    
    Args:
        language: Código do idioma ('pt' ou 'en')
    
    Requisitos: 5.1, 5.4
    """
    # Título da seção
    st.title(get_translation("nav_projects", language))
    
    # Carregar projetos
    projects = get_projects()
    
    # Renderizar projetos usando o grid
    render_projects_grid(projects, language)


def render_mentorship_section(language: str) -> None:
    """
    Renderiza a seção de Mentoria com informações sobre serviços de mentoria.
    
    Carrega informações de data/mentorship.py e exibe:
    - Descrição dos serviços de mentoria
    - Áreas de mentoria oferecidas
    - Disponibilidade
    - Botão para agendamento
    
    Args:
        language: Código do idioma ('pt' ou 'en')
    
    Requisitos: 8.2
    """
    # Título da seção
    st.title(get_translation("nav_mentorship", language))
    
    # Carregar informações de mentoria
    mentorship_info = get_mentorship_info()
    
    # Descrição
    st.subheader(get_translation("mentorship_description", language))
    description = mentorship_info.get("description", {}).get(language, "")
    if description:
        st.markdown(description)
    else:
        st.info("Descrição não disponível.")
    
    st.divider()
    
    # Layout responsivo com colunas para áreas e disponibilidade
    col_areas, col_availability = st.columns([3, 2])
    
    with col_areas:
        # Áreas de mentoria
        st.subheader(get_translation("mentorship_areas", language))
        areas = mentorship_info.get("areas", [])
        if areas:
            for area in areas:
                area_text = area.get(language, "")
                if area_text:
                    st.markdown(f"- {area_text}")
        else:
            st.info("Áreas de mentoria não disponíveis.")
    
    with col_availability:
        # Disponibilidade
        st.subheader(get_translation("mentorship_availability", language))
        availability = mentorship_info.get("availability", {}).get(language, "")
        if availability:
            st.markdown(availability)
        else:
            st.info("Informação de disponibilidade não disponível.")
    
    st.divider()
    
    # Botão para agendamento - centralizado
    contact_url = mentorship_info.get("contact_url", "")
    if contact_url:
        st.subheader(get_translation("mentorship_schedule", language))
        # Usar colunas para centralizar o botão
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            create_custom_button(
                text=get_translation("mentorship_schedule", language),
                url=contact_url,
                background_color="#0066cc",
                text_color="#ffffff"
            )
    else:
        st.warning("Link de agendamento não disponível.")


def render_recommendations_section(language: str) -> None:
    """
    Renderiza a seção de Recomendações com lista de recursos recomendados.
    
    Carrega recomendações de data/recommendations.py e exibe:
    - Título, categoria, descrição, autor/criador e motivo de cada recomendação
    - Filtro opcional por categoria (livros, cursos, ferramentas, etc.)
    - Botão/link para acessar o recurso recomendado
    
    Args:
        language: Código do idioma ('pt' ou 'en')
    
    Requisitos: 7.1, 7.2, 7.3, 7.4
    """
    # Título da seção
    st.title(get_translation("recommendations_title", language))
    
    # Layout responsivo para filtro - usar colunas para melhor organização
    col_filter, col_spacer = st.columns([2, 3])
    
    with col_filter:
        # Filtro por categoria
        st.subheader(get_translation("recommendations_filter", language))
        
        # Opções de filtro
        filter_options = {
            None: get_translation("recommendations_all", language),
            "book": get_translation("recommendations_book", language),
            "course": get_translation("recommendations_course", language),
            "tool": get_translation("recommendations_tool", language),
            "article": get_translation("recommendations_article", language)
        }
        
        # Selectbox para filtro
        selected_filter = st.selectbox(
            label="",
            options=list(filter_options.keys()),
            format_func=lambda x: filter_options[x],
            key="recommendations_filter_selector"
        )
    
    st.divider()
    
    # Carregar recomendações com filtro aplicado
    recommendations = get_recommendations(category=selected_filter)
    
    # Verificar se há recomendações
    if not recommendations:
        st.info(get_translation("recommendations_empty", language))
        return
    
    # Exibir cada recomendação em layout responsivo
    for recommendation in recommendations:
        # Obter dados traduzidos
        title = recommendation.get("title", {}).get(language, "")
        category = recommendation.get("category", "")
        description = recommendation.get("description", {}).get(language, "")
        author_creator = recommendation.get("author_creator", "")
        url = recommendation.get("url", "")
        reason = recommendation.get("reason", {}).get(language, "")
        
        # Container para cada recomendação
        with st.container():
            # Título da recomendação
            st.subheader(title)
            
            # Categoria e autor em colunas responsivas
            col1, col2 = st.columns([1, 3])
            with col1:
                # Badge para categoria
                category_label = filter_options.get(category, category)
                st.markdown(f"**{category_label}**")
            with col2:
                # Autor/Criador
                if author_creator:
                    st.caption(f"{get_translation('recommendations_by', language)} {author_creator}")
            
            # Descrição
            if description:
                st.markdown(description)
            
            # Motivo da recomendação
            if reason:
                st.markdown(f"**{get_translation('recommendations_why', language)}:** {reason}")
            
            # Botão para acessar recurso
            if url:
                create_custom_button(
                    text=get_translation("recommendations_access", language),
                    url=url,
                    background_color="#0066cc",
                    text_color="#ffffff"
                )
            
            st.divider()


def render_content_section(language: str) -> None:
    """
    Renderiza a seção de Conteúdos com lista de conteúdos publicados.
    
    Carrega conteúdos de data/content.py e exibe:
    - Título, descrição, tipo e tags de cada conteúdo
    - Filtro opcional por tipo de conteúdo
    - Botão para visualizar cada conteúdo
    
    Args:
        language: Código do idioma ('pt' ou 'en')
    
    Requisitos: 8.2
    """
    # Título da seção
    st.title(get_translation("content_title", language))
    
    # Layout responsivo para filtro - usar colunas para melhor organização
    col_filter, col_spacer = st.columns([2, 3])
    
    with col_filter:
        # Filtro por tipo de conteúdo
        st.subheader(get_translation("content_filter", language))
        
        # Opções de filtro
        filter_options = {
            None: get_translation("content_all", language),
            "article": get_translation("content_article", language),
            "video": get_translation("content_video", language),
            "podcast": get_translation("content_podcast", language),
            "tutorial": get_translation("content_tutorial", language)
        }
        
        # Selectbox para filtro
        selected_filter = st.selectbox(
            label="",
            options=list(filter_options.keys()),
            format_func=lambda x: filter_options[x],
            key="content_filter_selector"
        )
    
    st.divider()
    
    # Carregar conteúdos com filtro aplicado
    contents = get_contents(content_type=selected_filter)
    
    # Verificar se há conteúdos
    if not contents:
        st.info(get_translation("content_empty", language))
        return
    
    # Exibir cada conteúdo em layout responsivo
    for content in contents:
        # Obter dados traduzidos
        title = content.get("title", {}).get(language, "")
        description = content.get("description", {}).get(language, "")
        content_type = content.get("type", "")
        url = content.get("url", "")
        date = content.get("date", "")
        tags = content.get("tags", [])
        
        # Container para cada conteúdo
        with st.container():
            # Título do conteúdo
            st.subheader(title)
            
            # Tipo e data em colunas responsivas
            col1, col2 = st.columns([1, 3])
            with col1:
                # Badge para tipo de conteúdo
                type_label = filter_options.get(content_type, content_type)
                st.markdown(f"**{type_label}**")
            with col2:
                # Data de publicação
                if date:
                    st.caption(f"📅 {date}")
            
            # Descrição
            if description:
                st.markdown(description)
            
            # Tags
            if tags:
                tags_text = " • ".join([f"`{tag}`" for tag in tags])
                st.markdown(f"{get_translation('content_tags', language)}: {tags_text}")
            
            # Botão para visualizar conteúdo
            if url:
                create_custom_button(
                    text=get_translation("content_view", language),
                    url=url,
                    background_color="#0066cc",
                    text_color="#ffffff"
                )
            
            st.divider()


def render_sidebar() -> str:
    """
    Renderiza o menu lateral com seletor de idioma e navegação.
    
    Implementa:
    - Seletor de idioma (PT/EN)
    - Menu de navegação com todas as seções
    - Atualiza session_state com seleções do usuário
    
    Returns:
        str: Seção selecionada pelo usuário
    
    Requisitos: 2.1, 2.2, 2.3, 3.1
    """
    with st.sidebar:
        # Seletor de idioma
        st.subheader(get_translation("language_selector", st.session_state.language))
        
        # Criar opções de idioma
        language_options = {
            "pt": get_translation("language_pt", st.session_state.language),
            "en": get_translation("language_en", st.session_state.language)
        }
        
        # Selectbox para idioma
        selected_language = st.selectbox(
            label="",
            options=list(language_options.keys()),
            format_func=lambda x: language_options[x],
            index=0 if st.session_state.language == "pt" else 1,
            key="language_selector"
        )
        
        # Atualizar idioma no session_state se mudou
        if selected_language != st.session_state.language:
            st.session_state.language = selected_language
            st.rerun()
        
        st.divider()
        
        # Menu de navegação
        st.subheader("Menu")
        
        # Definir todas as seções disponíveis
        sections = {
            "about": get_translation("nav_about", st.session_state.language),
            "projects": get_translation("nav_projects", st.session_state.language),
            "mentorship": get_translation("nav_mentorship", st.session_state.language),
            "recommendations": get_translation("nav_recommendations", st.session_state.language),
            "content": get_translation("nav_content", st.session_state.language),
            "contact": get_translation("nav_contact", st.session_state.language)
        }
        
        # Radio buttons para navegação
        selected_section = st.radio(
            label="",
            options=list(sections.keys()),
            format_func=lambda x: sections[x],
            index=list(sections.keys()).index(st.session_state.current_section),
            key="section_selector"
        )
        
        # Atualizar seção no session_state
        if selected_section != st.session_state.current_section:
            st.session_state.current_section = selected_section
        
        return selected_section


def render_contact_section(language: str) -> None:
    """
    Renderiza a seção de Contato com botões para redes sociais e email.
    
    Exibe botões customizados para:
    - Email
    - LinkedIn
    - GitHub
    - Medium
    
    Args:
        language: Código do idioma ('pt' ou 'en')
    
    Requisitos: 7.1, 7.2, 7.3
    """
    # Título da seção
    st.title(get_translation("contact_title", language))
    
    # Descrição introdutória
    st.markdown(get_translation("contact_intro", language))
    
    st.divider()
    
    # Informações de contato - substituir com dados reais
    contact_info = {
        "linkedin": "https://www.linkedin.com/in/katieli-dieter/",
        "github": "https://github.com/katidieter",
        "medium": "https://medium.com/@katielidieter"
    }
    
    # Layout em colunas para organizar os botões
    col1, col2 = st.columns(2)
    
    with col1:        
        # Botão do GitHub
        st.subheader(get_translation("contact_github", language))
        create_custom_button(
            text=get_translation("contact_follow", language),
            url=contact_info['github'],
            background_color="#333333",
            text_color="#ffffff"
        )
    
        # Botão do LinkedIn
        st.subheader(get_translation("contact_linkedin", language))
        create_custom_button(
            text=get_translation("contact_connect", language),
            url=contact_info['linkedin'],
            background_color="#0077B5",
            text_color="#ffffff"
        )
        
        st.markdown("")  # Espaçamento
        
        # Botão do Medium
        st.subheader("Medium")
        create_custom_button(
            text=get_translation("contact_follow", language),
            url=contact_info['medium'],
            background_color="#000000",
            text_color="#ffffff"
        )


def render_content(section: str, language: str) -> None:
    """
    Renderiza o conteúdo da seção selecionada no idioma escolhido.
    
    Implementa switch/match para renderizar seção apropriada e chama
    a função de renderização correspondente para cada seção.
    
    Args:
        section: Seção a ser renderizada ('about', 'projects', 'mentorship', 
                 'recommendations', 'content', 'contact')
        language: Código do idioma ('pt' ou 'en')
    
    Requisitos: 2.2
    """
    # Switch/match para renderizar seção apropriada
    match section:
        case "about":
            render_about_section(language)
        case "projects":
            render_projects_section(language)
        case "mentorship":
            render_mentorship_section(language)
        case "recommendations":
            render_recommendations_section(language)
        case "content":
            render_content_section(language)
        case "contact":
            render_contact_section(language)
        case _:
            # Fallback para seções não reconhecidas
            st.title(get_translation(f"nav_{section}", language))
            st.warning(f"Seção '{section}' não implementada.")


def main() -> None:
    """
    Função principal que inicializa e executa a aplicação.
    
    Coordena a execução da aplicação:
    - Configura a página
    - Inicializa o estado da sessão
    - Renderiza o sidebar e obtém a seção selecionada
    - Renderiza o conteúdo da seção no idioma selecionado
    
    Requisitos: 1.1, 2.2
    """
    # Configurar página
    setup_page()
    
    # Inicializar estado da sessão
    initialize_session_state()
    
    # Renderizar sidebar e obter seção selecionada
    selected_section = render_sidebar()
    
    # Renderizar conteúdo com seção e idioma
    render_content(selected_section, st.session_state.language)


if __name__ == "__main__":
    main()

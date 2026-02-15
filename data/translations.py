"""
Módulo de traduções para o portfólio Streamlit.

Este módulo contém todas as strings traduzidas para suporte a múltiplos idiomas.
"""

TRANSLATIONS = {
    "pt": {
        # Navegação
        "nav_about": "Sobre",
        "nav_projects": "Projetos",
        "nav_mentorship": "Mentoria",
        "nav_recommendations": "Recomendações",
        "nav_content": "Conteúdos",
        "nav_contact": "Contato",
        
        # Seletor de idioma
        "language_selector": "Idioma",
        "language_pt": "Português",
        "language_en": "English",
        
        # Seção Sobre
        "about_title": "Sobre Mim",
        "about_skills": "Habilidades",
        "about_technologies": "Tecnologias",
        "about_summary": "Resumo Profissional",
        
        # Seção Projetos
        "projects_title": "Meus Projetos",
        "projects_view": "Ver Projeto",
        "projects_technologies": "Tecnologias",
        "projects_empty": "Nenhum projeto disponível no momento.",
        
        # Seção Mentoria
        "mentorship_title": "Mentoria",
        "mentorship_description": "Descrição",
        "mentorship_areas": "Áreas de Mentoria",
        "mentorship_availability": "Disponibilidade",
        "mentorship_schedule": "Agendar Sessão",
        
        # Seção Recomendações
        "recommendations_title": "Recomendações",
        "recommendations_filter": "Filtrar por categoria",
        "recommendations_all": "Todas",
        "recommendations_book": "Livros",
        "recommendations_course": "Cursos",
        "recommendations_tool": "Ferramentas",
        "recommendations_article": "Artigos",
        "recommendations_by": "por",
        "recommendations_why": "Por que recomendo",
        "recommendations_access": "Acessar Recurso",
        "recommendations_empty": "Nenhuma recomendação disponível no momento.",
        
        # Seção Conteúdos
        "content_title": "Conteúdos",
        "content_filter": "Filtrar por tipo",
        "content_all": "Todos",
        "content_article": "Artigos",
        "content_video": "Vídeos",
        "content_podcast": "Podcasts",
        "content_tutorial": "Tutoriais",
        "content_view": "Ver Conteúdo",
        "content_tags": "Tags",
        "content_empty": "Nenhum conteúdo disponível no momento.",
        
        # Seção Contato
        "contact_title": "Entre em Contato",
        "contact_intro": "Conecte-se comigo através das seguintes plataformas:",
        "contact_email": "Email",
        "contact_linkedin": "LinkedIn",
        "contact_github": "GitHub",
        "contact_twitter": "Twitter",
        "contact_send_email": "Enviar Email",
        "contact_connect": "Conectar",
        "contact_follow": "Seguir",
        
        # Botões gerais
        "button_view": "Ver",
        "button_learn_more": "Saiba Mais",
        "button_back": "Voltar",
        
        # Mensagens de erro
        "error_translation_missing": "Tradução não encontrada",
        "error_data_incomplete": "Dados incompletos",
        "error_invalid_url": "URL inválida",
        "error_loading": "Erro ao carregar",
    },
    "en": {
        # Navigation
        "nav_about": "About",
        "nav_projects": "Projects",
        "nav_mentorship": "Mentorship",
        "nav_recommendations": "Recommendations",
        "nav_content": "Content",
        "nav_contact": "Contact",
        
        # Language selector
        "language_selector": "Language",
        "language_pt": "Português",
        "language_en": "English",
        
        # About section
        "about_title": "About Me",
        "about_skills": "Skills",
        "about_technologies": "Technologies",
        "about_summary": "Professional Summary",
        
        # Projects section
        "projects_title": "My Projects",
        "projects_view": "View Project",
        "projects_technologies": "Technologies",
        "projects_empty": "No projects available at the moment.",
        
        # Mentorship section
        "mentorship_title": "Mentorship",
        "mentorship_description": "Description",
        "mentorship_areas": "Mentorship Areas",
        "mentorship_availability": "Availability",
        "mentorship_schedule": "Schedule Session",
        
        # Recommendations section
        "recommendations_title": "Recommendations",
        "recommendations_filter": "Filter by category",
        "recommendations_all": "All",
        "recommendations_book": "Books",
        "recommendations_course": "Courses",
        "recommendations_tool": "Tools",
        "recommendations_article": "Articles",
        "recommendations_by": "by",
        "recommendations_why": "Why I recommend",
        "recommendations_access": "Access Resource",
        "recommendations_empty": "No recommendations available at the moment.",
        
        # Content section
        "content_title": "Content",
        "content_filter": "Filter by type",
        "content_all": "All",
        "content_article": "Articles",
        "content_video": "Videos",
        "content_podcast": "Podcasts",
        "content_tutorial": "Tutorials",
        "content_view": "View Content",
        "content_tags": "Tags",
        "content_empty": "No content available at the moment.",
        
        # Contact section
        "contact_title": "Get in Touch",
        "contact_intro": "Connect with me through the following platforms:",
        "contact_email": "Email",
        "contact_linkedin": "LinkedIn",
        "contact_github": "GitHub",
        "contact_twitter": "Twitter",
        "contact_send_email": "Send Email",
        "contact_connect": "Connect",
        "contact_follow": "Follow",
        
        # General buttons
        "button_view": "View",
        "button_learn_more": "Learn More",
        "button_back": "Back",
        
        # Error messages
        "error_translation_missing": "Translation not found",
        "error_data_incomplete": "Incomplete data",
        "error_invalid_url": "Invalid URL",
        "error_loading": "Error loading",
    }
}


def get_translation(key: str, language: str) -> str:
    """
    Retorna a tradução para uma chave no idioma especificado.
    
    Args:
        key: Chave da tradução
        language: Código do idioma ('pt' ou 'en')
    
    Returns:
        String traduzida ou chave original se não encontrada
    
    Examples:
        >>> get_translation("nav_about", "pt")
        'Sobre'
        >>> get_translation("nav_about", "en")
        'About'
        >>> get_translation("nonexistent_key", "pt")
        'nonexistent_key'
    """
    # Validar idioma suportado, usar 'pt' como padrão
    if language not in TRANSLATIONS:
        language = "pt"
    
    # Retornar tradução ou chave original como fallback
    return TRANSLATIONS[language].get(key, key)

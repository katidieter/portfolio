"""
Módulo de dados de projetos do portfólio.

Este módulo contém a lista de projetos e funções para acessá-los.
"""

PROJECTS = [
    {
        "title": {
            "pt": "Portfólio Streamlit",
            "en": "Streamlit Portfolio"
        },
        "description": {
            "pt": "Aplicação web de portfólio pessoal desenvolvida com Streamlit, com suporte a múltiplos idiomas e design responsivo.",
            "en": "Personal portfolio web application built with Streamlit, featuring multi-language support and responsive design."
        },
        "technologies": ["Python", "Streamlit"],
        "url": "https://github.com/katidieter/portfolio"
    },
]


def get_projects():
    """
    Retorna a lista de todos os projetos.
    
    Returns:
        list[dict]: Lista de dicionários contendo dados dos projetos.
                   Cada projeto contém title, description, technologies e url.
    """
    return PROJECTS

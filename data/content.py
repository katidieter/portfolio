"""
Módulo de dados de conteúdos publicados do portfólio.

Este módulo contém links para artigos, vídeos e outros conteúdos criados.
"""

CONTENTS = [
    {
        "title": {
            "pt": "Ainda vale a pena aprender a programar na era do Vibe Code?",
            "en": "Is It Still Worth Learning to Code in the Vibe Coding Era?"
        },
        "description": {
            "pt": "Uma reflexão sobre porquê ainda vale a pena aprender a programar na era do Vibe Code",
            "en": "A deep reflextion about you should learn to program in Vibe Coding Era"
        },
        "type": "article",
        "url": "https://medium.com/@katielidieter/is-it-still-worth-learning-to-code-in-the-vibe-coding-era-6b3d29895340",
        "date": "2025-12-30",
        "tags": ["Python", "Programming", "Vibe Coding"]
    },
    {
        "title": {
            "pt": "O que eu faria se estivesse começando carreira em dados hoje",
            "en": "What I would do if I were starting in data today"
        },
        "description": {
            "pt": "Dicas práticas do que eu faria se estivesse começando na área de dados hoje",
            "en": "Practical tips of what I would do if I were starting in data now. "
        },
        "type": "article",
        "url": "https://medium.com/@katielidieter/o-que-eu-faria-se-estivesse-come%C3%A7ando-carreira-em-dados-hoje-1676c39359b4",
        "date": "2024-09-11",
        "tags": ["Data", "Career", "Mentor"]
    },
    {
        "title": {
            "pt": "[SCTEC] Despertar - O poder de decidir: O valor dos dados]",
            "en": "[SCTEC] Wake - The power of decide: The value of data"
        },
        "description": {
            "pt": "Apresentação sobre a àrea de dados e painel de discussão sobre oportunidades na insdustria.",
            "en": "Talking about data industry and participating of a panel about it."
        },
        "type": "video",
        "url": "https://www.youtube.com/live/FZgP06sjLa4",
        "date": "2026-02-04",
        "tags": ["Data", "Career", "Education"]
    },
]


def get_contents(content_type=None):
    """
    Retorna lista de conteúdos, opcionalmente filtrados por tipo.
    
    Args:
        content_type (str, optional): Tipo de conteúdo para filtrar 
                                     (article, video, podcast, tutorial).
                                     Se None, retorna todos os conteúdos.
    
    Returns:
        list[dict]: Lista de dicionários contendo conteúdos.
                   Cada conteúdo contém title, description, type, url, date e tags.
    """
    if content_type is None:
        return CONTENTS
    
    return [content for content in CONTENTS if content["type"] == content_type]

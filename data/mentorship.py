"""
Módulo de dados de mentoria do portfólio.

Este módulo contém informações sobre serviços de mentoria oferecidos.
"""

MENTORSHIP_INFO = {
    "description": {
        "pt": "Ofereço sessões de mentoria personalizadas para profissionais que desejam iniciar ou avançar em suas carreiras em dados. Com mais de 12 anos de experiência em técnologia e ciência de dados, posso ajudá-lo a alcançar seus objetivos profissionais.",
        "en": "I offer personalized mentorship sessions for professionals looking to advance their careers in data. With more than 12 years of experience in tech and data science, I can help you achieve your professional goals."
    },
    "areas": [
        {
            "pt": "Ciência de Dados e Machine Learning",
            "en": "Data Science and Machine Learning"
        },
        {
            "pt": "Consultas SQL",
            "en": "SQL queries"
        },
        {
            "pt": "Transição de carreira",
            "en": "Career transition"
        },
        {
            "pt": "Programação",
            "en": "Programming"
        },
    ],
    "availability": {
        "pt": "Disponível para sessões semanais ou quinzenais",
        "en": "Available for weekly or bi-weekly sessions"
    },
    "contact_url": "https://app.ementor.com.br/mentor/katielidieter/"
}


def get_mentorship_info():
    """
    Retorna informações sobre serviços de mentoria.
    
    Returns:
        dict: Dicionário contendo description, areas, availability e contact_url.
    """
    return MENTORSHIP_INFO

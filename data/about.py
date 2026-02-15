"""
Módulo de dados da seção Sobre do portfólio.

Este módulo contém informações pessoais e profissionais para a seção About.
"""

ABOUT_INFO = {
    "name": "Seu Nome",
    "profile_image": "assets/profile.jpg",  
    "introduction": {
        "pt": "Olá! Sou uma Cientista de Dados focada em Projetos de Antifraude.",
        "en": "Hey! I am a Senior Data Scientist focused on antifraud projects."
    },
    "skills": [
        "Python",
        "Data Science",
        "Machine Learning",
        "Problem Solving",
        "Cloud",
        "Programming",
        "Automation"
    ],
    "technologies": [
        "Python",
        "Streamlit",
        "Pandas",
        "NumPy",
        "Scikit-learn",
        "Git",
        "Docker",
        "SQL",
        "PySpark"
    ],
    "summary": {
        "pt": "Cientista de dados com experiência em projectos de antifraude, logística e marketing. "
              "Especializada em modelar soluções inovadoras usando Python e Ferramentas de Machine Learning. "
              "Apaixonada por aprendizado contínuo e compartilhamento de conhecimento.",
        "en": "Data Scientist with experience in antifraud, logistics and marketing projects. "
              "Specialized in modeling innovative solutions using Python and Machine Learning tools. "
              "Passionate about continuous learning and knowledge sharing."
    }
}


def get_about_info():
    """
    Retorna informações da seção Sobre.
    
    Returns:
        dict: Dicionário contendo informações pessoais e profissionais.
              Inclui name, profile_image, introduction, skills, technologies e summary.
    """
    return ABOUT_INFO


import random
from datetime import datetime, timedelta

# Configurações
random.seed(42)  # Para resultados reproduzíveis (remova para total aleatoriedade)
total_posts = 1000
start_date = datetime.now() - timedelta(days=730)

# Opções para campos
tipos_conteudo = ["Foto", "Vídeo", "Enquete", "Texto", "Link", "Clip", "Transmissão"]
publicos_alvo = ["Homens_18-25", "Homens_25-35", "Mulheres_18-25", "Mulheres_25-35", "Unissex"]
temas = {
    "Masculinidade": ["Fitness", "Carros", "Finanças", "Sucesso", "Motivação"],
    "Juventude Feminina": ["Moda", "Beleza", "Relacionamentos", "Empoderamento"],
    "Esperança": ["Histórias Inspiradoras", "Superação", "Filantropia"],
    "Entretenimento": ["Memes", "Hobbies", "Viagens", "Celebridades"]
}

# SQL de criação
sql_output = """-- Tabela de posts VK com dados estratégicos
CREATE TABLE vk_posts (
    post_id INT PRIMARY KEY,
    data_post DATE,
    hora_post TIME,
    dia_semana VARCHAR(10),
    likes INT,
    intervalo_anterior_horas DECIMAL(5,2),
    tipo_conteudo VARCHAR(15),
    publico_alvo VARCHAR(15),
    tema_engajamento VARCHAR(30),
    palavras_chave TEXT
);

-- Inserts
"""

for i in range(1, total_posts + 1):
    # Data/hora aleatória
    data_post = start_date + timedelta(
        days=random.randint(0, 730),
        hours=random.randint(0, 23),
        minutes=random.randint(0, 59)
    )

    # Metadados
    tipo = random.choice(tipos_conteudo)
    publico = random.choice(publicos_alvo)

    # Tema coerente com público
    if "Homens" in publico:
        tema_categoria = "Masculinidade"
    elif "Mulheres" in publico:
        tema_categoria = "Juventude Feminina"
    else:
        tema_categoria = random.choice(list(temas.keys()))

    tema = random.choice(temas[tema_categoria])

    # Palavras-chave (garantindo que seja uma string)
    palavras_amostra = temas[tema_categoria] + [publico, tema]
    keywords = ", ".join(random.sample(palavras_amostra, random.randint(2, min(4, len(palavras_amostra)))))

    # Engajamento
    likes = random.randint(10, 500)
    intervalo = round(random.uniform(0.5, 120), 2)

    sql_output += f"""INSERT INTO vk_posts VALUES (
        {i},
        '{data_post.date()}',
        '{data_post.time().strftime('%H:%M')}',
        '{data_post.strftime('%A')}',
        {likes},
        {intervalo},
        '{tipo}',
        '{publico}',
        '{tema}',
        '{keywords}'
    );
    """

# Gerar arquivo
with open('vk_posts_final.sql', 'w', encoding='utf-8') as f:
    f.write(sql_output)

print("✅ Arquivo 'vk_posts_final.sql' gerado com sucesso!")
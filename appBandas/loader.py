from appBandas.models import Banda, Album, Musica
import json

# Limpa os dados existentes do banco de dados
Banda.objects.all().delete()
Album.objects.all().delete()
Musica.objects.all().delete()

# Carrega e processa os dados das bandas
with open('appBandas/json/bandas.json') as f:
    bandas = json.load(f)

    for banda in bandas:
        nova_banda, criada = Banda.objects.get_or_create(
            nome=banda['nome'],
            defaults={'nMembros': banda.get('nMembros', 0)}  # Define um valor padrão de 0 para nMembros se não estiver presente
        )

# Carrega e processa os dados dos álbuns e músicas
with open('appBandas/json/albuns.json') as f:
    albuns = json.load(f)

    for entrada in albuns:
        banda_nome = entrada['banda']
        banda = Banda.objects.get(nome=banda_nome)

        for album_data in entrada.get('albums', []):
            if 'ano_lancamento' not in album_data:
                continue  # Pula esta entrada se 'ano_lancamento' não estiver presente

            # Calcula o número de músicas no álbum
            numero_musicas = len(album_data.get('musicas', []))

            # Cria o objeto Album com o número de músicas calculado
            album_obj = Album.objects.create(
                nome=album_data['nome'],
                ano_lancamento=album_data['ano_lancamento'],
                nMusicas=numero_musicas,  # Define o número de músicas no álbum
                banda=banda
            )

            for musica_data in album_data.get('musicas', []):
                titulo_musica = musica_data.get('titulo', 'Música Desconhecida')
                duracao_musica = musica_data.get('duracao', '0:00')

                # Crie a música apenas se o título da música estiver presente
                if titulo_musica:
                    Musica.objects.create(
                        nome=titulo_musica,  # Aqui substituímos 'titulo' por 'nome'
                        duracao=duracao_musica,
                        album=album_obj
                    )

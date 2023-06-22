from gnewsclient import gnewsclient

# Crea una lista de temas y consultas de búsqueda para probar
topics = ['science', 'technology', 'business']
queries = ['Miura 1', 'Lanzamiento del Miura 1']

# Prueba cada combinación de tema y consulta de búsqueda
for topic in topics:
    for query in queries:
        # Configura el cliente de noticias con el tema y la consulta de búsqueda actuales
        client = gnewsclient.NewsClient(language='spanish', 
                                        location='spain', 
                                        topic=topic, 
                                        query=query, 
                                        max_results=5)

        news_list = client.get_news()
        
        # Si se encontraron noticias, imprímelas
        if news_list:
            print(f"Resultados para el tema '{topic}' y la consulta de búsqueda '{query}':\n")
            for item in news_list:
                print("Título : ", item['title'])
                print("Enlace : ", item['link'])
                print("")
        else:
            print(f"No se encontraron resultados para el tema '{topic}' y la consulta de búsqueda '{query}'.\n")

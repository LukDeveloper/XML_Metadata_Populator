import xml.etree.ElementTree as ET
import os

# Definindo namespaces
namespaces = {
    'gmd': 'http://www.isotc211.org/2005/gmd',
    'gco': 'http://www.isotc211.org/2005/gco'
}

# Register namespaces
for prefix, uri in namespaces.items():
    ET.register_namespace(prefix, uri)

# Função para substituir placeholders com "exemplos de dados"
def update_xml_with_data(xml_template, data):
    tree = ET.ElementTree(ET.fromstring(xml_template))
    root = tree.getroot()

    # Adicionando valor para o "Título"
    title = root.find('.//gmd:title/gco:CharacterString', namespaces)
    if title is not None:
        title.text = data.get('title', '')

    # Adicionando valor para "Resumo"
    abstract = root.find('.//gmd:abstract/gco:CharacterString', namespaces)
    if abstract is not None:
        abstract.text = data.get('abstract', '')

    # Adicionando valor para "Overview (URL da imagem)"
    overview = root.find('.//gmd:MD_BrowseGraphic/gmd:fileName/gco:CharacterString', namespaces)
    if overview is not None:
        overview.text = data.get('overview_url', '')

    # Adicionando valor para "Palavras-chave"
    keywords = root.findall('.//gmd:keyword/gco:CharacterString', namespaces)
    for i, keyword in enumerate(keywords):
        key = f'keyword_{i+1}'
        keyword.text = data.get(key, '')

    # Adicionando valor para "Recursos Online" e "Descrição do resurso online"
    online_resources = root.findall('.//gmd:CI_OnlineResource/gmd:linkage/gmd:URL', namespaces)
    online_resources_desc = root.findall('.//gmd:CI_OnlineResource/gmd:description/gco:CharacterString', namespaces)
    for i, resource in enumerate(online_resources):
        key = f'online_resource_url_{i+1}'
        resource.text = data.get(key, '')
    for i, resource in enumerate(online_resources_desc):
        key = f'online_resource_url_desc_{i+1}'
        resource.text = data.get(key, '')

    return tree

# Dados do banco de dados (exemplo)
exemplo_dados = [
    {
        'title': 'Título 1',
        'abstract': 'Resumo 1',
        'overview_url': 'http://example.com/overview1.png',
        'keyword_1': 'Palavra-chave 1',
        'keyword_2': 'Palavra-chave 2',
        'online_resource_url_1': 'http://example.com/resource1',
        'online_resource_url_desc_1': 'Tenha acesso ao recurso através do link (Descrição para o recurso online)'
    },
    {
        'title': 'Título 2',
        'abstract': 'Resumo 2',
        'overview_url': 'http://example.com/overview2.png',
        'keyword_1': 'Palavra-chave 3',
        'keyword_2': 'Palavra-chave 4',
        'online_resource_url_1': 'http://example.com/resource2',
        'online_resource_url_desc_1': 'Tenha acesso ao recurso através do link (Descrição para o recurso online)'
    },
]

# Caminho para Template XML ISO19115/19139
with open('...', 'r', encoding='utf-8') as file:
    xml_template = file.read()

# Diretório para salvar os arquivos XML de saída
output_dir = 'output_xml_files'
os.makedirs(output_dir, exist_ok=True)

# Gera arquivos XML para cada registro
for i, record in enumerate(exemplo_dados, start=1):
    tree = update_xml_with_data(xml_template, record)
    output_file = os.path.join(output_dir, f'record_{i}.xml')
    tree.write(output_file, encoding='UTF-8', xml_declaration=True)

print(f'{len(exemplo_dados)} arquivos XML foram gerados em {output_dir}')

# XML_Metadata_Populator

Este repositório contém um script em Python para automação da criação de arquivos XML de metadados no padrão **ISO 19115/19139**. O objetivo principal é preencher templates XML com dados fornecidos de forma dinâmica, permitindo integração com sistemas de metadados como o GeoNetwork.

## 🚀 Funcionalidades

- **Leitura e Manipulação de XML**: Carrega templates XML e atualiza os campos com dados fornecidos.
- **Suporte a Múltiplos Registros**: Processa vários conjuntos de dados em uma única execução, gerando arquivos XML individuais.
- **Gerenciamento de Saída**: Cria um diretório para salvar os arquivos gerados, nomeados de forma única.
- **Flexibilidade nos Dados**: Adapta os campos de metadados como título, resumo, palavras-chave, e recursos online com base nos dados recebidos.

## 📂 Estrutura

- `input.xml`: Template XML que segue o padrão ISO 19115/19139.
- `output_xml_files/`: Diretório onde os arquivos XML gerados são salvos.
- `script.py`: O script principal que processa os dados e gera os XMLs.

## 🛠️ Como Funciona

1. **Carregamento do Template**: Lê um arquivo XML base para ser preenchido.
2. **Substituição de Dados**:
   - Título e Resumo.
   - Palavras-chave e URLs de recursos online.
   - Imagem de overview.
3. **Geração de Arquivos**:
   - Cada registro no banco de dados é transformado em um arquivo XML único.
   - Os arquivos são salvos no diretório especificado.

## 🧑‍💻 Exemplo de Execução

1. Prepare o arquivo `input.xml` com o template XML.
2. Configure os dados no formato de dicionários em Python, como no exemplo abaixo:

   ```python
   exemplo_dados = [
       {
           'title': 'Título 1',
           'abstract': 'Resumo 1',
           'overview_url': 'http://example.com/overview1.png',
           'keyword_1': 'Palavra-chave 1',
           'keyword_2': 'Palavra-chave 2',
           'online_resource_url_1': 'http://example.com/resource1',
           'online_resource_url_desc_1': 'Descrição do recurso online'
       }
   ]
3. Execute o script:

```bash
python script.py
```

4. Os arquivos gerados serão salvos no diretório output_xml_files.

## 🔧 Requisitos
   - Python 3.x
   - Biblioteca xml.etree.ElementTree (já incluída na biblioteca padrão do Python)

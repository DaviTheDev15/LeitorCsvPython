import csv
import json

arquivoCSV = 'microdados_ed_basica_2023.csv'

arquivoJSON = 'dados.json'

coluna = 'SG_UF'
estado = 'PB'

colunas = ['NO_ENTIDADE', 'NO_UF', 'NO_MUNICIPIO', 'NO_MESORREGIAO', 'NO_MICRORREGIAO','NO_REGIAO','QT_MAT_BAS','QT_MAT_PROF','QT_MAT_EJA', 'QT_MAT_ESP', 'QT_MAT_INF','QT_MAT_FUND','QT_MAT_MED']

dadosFiltrados = []

with open(arquivoCSV, mode='r', encoding='latin-1') as csvArquivo:
    csvLeitor = csv.DictReader(csvArquivo, delimiter=';')
    for linha in csvLeitor:
        if linha[coluna] == estado:
            dados_extraidos = {campo: linha[campo] for campo in colunas}
            dadosFiltrados.append(dados_extraidos)

jsonDados = json.dumps(dadosFiltrados, indent=4, ensure_ascii=False)
with open(arquivoJSON, mode='w', encoding='utf-8') as json_file:
    json_file.write(jsonDados)
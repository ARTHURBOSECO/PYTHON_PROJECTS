import os
import shutil

def copiar_arquivo_com_substituicao(origem, destino):
    """
    Copia um arquivo da origem para o destino, substituindo se já existir.
    
    Parâmetros:
        origem (str): Caminho completo do arquivo de origem
        destino (str): Caminho completo do arquivo de destino
    """
    try:
        # Verifica se o arquivo de origem existe
        if not os.path.exists(origem):
            print(f"Erro: O arquivo de origem '{origem}' não foi encontrado.")
            return False
        
        # Verifica se o diretório de destino existe, se não, cria
        diretorio_destino = os.path.dirname(destino)
        if not os.path.exists(diretorio_destino):
            os.makedirs(diretorio_destino)
        
        # Copia o arquivo, substituindo se já existir
        shutil.copy2(origem, destino)
        print(f"Arquivo copiado com sucesso de '{origem}' para '{destino}'")
        return True
    
    except Exception as e:
        print(f"Ocorreu um erro ao copiar o arquivo: {e}")
        return False

# Definindo os caminhos de origem e destino
origem = r"D:\ARTHUR\Documentos\PW.rar"
destino = r"C:\Users\Arthur\OneDrive\Documentos\PW.rar"

# Executando a cópia
copiar_arquivo_com_substituicao(origem, destino)
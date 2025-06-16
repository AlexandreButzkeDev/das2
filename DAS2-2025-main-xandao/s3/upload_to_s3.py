import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

def upload_file_to_s3(file_name, bucket_name, object_name=None):
    """
    Faz o upload de um arquivo para um bucket S3.

    :param file_name: Caminho do arquivo local a ser enviado.
    :param bucket_name: Nome do bucket S3.
    :param object_name: Nome do arquivo no bucket S3 (opcional).
    """
    # Se nenhum nome de objeto for fornecido, usa o nome do arquivo local
    if object_name is None:
        object_name = file_name

    # Cria o cliente S3
    s3_client = boto3.client('s3')

    try:
        # Faz o upload do arquivo
        s3_client.upload_file(file_name, bucket_name, object_name)
        print(f"Arquivo '{file_name}' enviado com sucesso para o bucket '{bucket_name}' como '{object_name}'.")
    except FileNotFoundError:
        print(f"Erro: O arquivo '{file_name}' não foi encontrado.")
    except NoCredentialsError:
        print("Erro: Credenciais da AWS não encontradas.")
    except PartialCredentialsError:
        print("Erro: Credenciais da AWS incompletas.")
    except Exception as e:
        print(f"Erro: {e}")

# Exemplo de uso
if __name__ == "__main__":
    file_name = "./s3/exemplo.txt"  # Substitua pelo caminho do arquivo que deseja enviar
    bucket_name = "rafael19032004"  # Substitua pelo nome do bucket
    object_name = "index.html"  # Nome do arquivo no bucket (opcional)

    upload_file_to_s3(file_name, bucket_name, object_name)
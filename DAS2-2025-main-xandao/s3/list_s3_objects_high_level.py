import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

def list_s3_objects_high_level(bucket_name):
    """
    Lista os objetos de um bucket S3 usando a API de alto nível com paginação.

    :param bucket_name: Nome do bucket S3.
    """
    # Cria o recurso S3
    s3 = boto3.resource('s3')

    try:
        # Obtém o bucket
        bucket = s3.Bucket(bucket_name)

        print(f"Objetos no bucket '{bucket_name}':")
        # Lista os objetos com paginação
        for obj in bucket.objects.all():
            print(f"- {obj.key} (Tamanho: {obj.size} bytes)")
    except NoCredentialsError:
        print("Erro: Credenciais da AWS não encontradas.")
    except PartialCredentialsError:
        print("Erro: Credenciais da AWS incompletas.")
    except Exception as e:
        print(f"Erro: {e}")

# Exemplo de uso
if __name__ == "__main__":
    bucket_name = "rafael19032004"  # Substitua pelo nome do bucket
    list_s3_objects_high_level(bucket_name)
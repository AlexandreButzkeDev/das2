import boto3
import time
#Low level API DynamoDB
dynamodb = boto3.client('dynamodb', region_name='us-east-1')

try:
    inicio = time.time()
    resposta = dynamodb.get_item(
        TableName= 'cliente',
        Key={
            'cpf': {'S': '1234567891'}
        }
    )
    diff = time.time() - inicio
    print(diff)
    if "Item" in resposta:
        print("Item encontrado")
        print(resposta['Item'])
    else:
        print("Item não encontrado")
except Exception as e:
    print(e)
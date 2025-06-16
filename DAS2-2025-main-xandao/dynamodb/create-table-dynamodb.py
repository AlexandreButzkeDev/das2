import boto3

#Low level API DynamoDB
dynamodb = boto3.client('dynamodb', region_name='us-east-1')

try:
    resposta = dynamodb.create_table(
        TableName='cliente',
        KeySchema=[
            {
                'AttributeName': 'cpf',
                'KeyType': 'HASH' ## CHAVE DE PARTICAO
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'cpf',
                'AttributeType': 'S' ##Tipo String
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
    )
    print("Tabela criada com sucesso")
    print(resposta)
except Exception as e:
    print(e)
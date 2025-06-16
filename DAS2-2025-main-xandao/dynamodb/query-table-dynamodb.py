import boto3

#Low level API DynamoDB
dynamodb = boto3.client('dynamodb', region_name='us-east-1')

try:
    resposta = dynamodb.query(
        TableName = 'cliente',
        KeyConditionExpression = 'cpf = :cpf',
        ExpressionAttributeValues = {
            ':cpf': {'S': '09876543211'}
        }
    )
    if 'Items' in resposta and resposta['Items']:
        print("Itens encontrados")
        for item in resposta["Items"]:
            print(item)

except Exception as e:
    print(e)
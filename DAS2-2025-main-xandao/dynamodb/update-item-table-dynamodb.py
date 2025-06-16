import boto3

#Low level API DynamoDB
dynamodb = boto3.client('dynamodb', region_name='us-east-1')

try:
    resposta = dynamodb.update_item(
        TableName = 'cliente',
        Key = {
            'cpf': {'S': '1234567891'}
        },
        UpdateExpression='SET clienteativo = :val',
        ExpressionAttributeValues={
            ':val': {'S': 'false'}
        },
        ReturnValues="UPDATED_NEW"
    )
    print(resposta)
except Exception as e:
    print(e)
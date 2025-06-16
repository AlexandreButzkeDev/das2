import boto3

#Low level API DynamoDB
dynamodb = boto3.client('dynamodb', region_name='us-east-1')

try:
    resposta = dynamodb.scan(
        TableName='cliente',
        FilterExpression='clienteativo = :val',
        ExpressionAttributeValues={
            ':val': {'S': 'false'}
        }
    )
    if 'Items' in resposta and resposta['Items']:
        for item in resposta['Items']:
            print(item)
except Exception as e:
    print(e)
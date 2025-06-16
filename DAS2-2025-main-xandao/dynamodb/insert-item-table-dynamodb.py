import boto3

#Low level API DynamoDB
dynamodb = boto3.client('dynamodb', region_name='us-east-1')

items = [
    { 
        'cpf': {'S': '1234567891'},
        'nome': {'S': 'João da Silva'},
        'clienteativo': {'S': 'true'}
    },
    { 
        'cpf': {'S': '09876543211'},
        'nome': {'S': 'Maria de Oliveira'},
        'clienteativo': {'S': 'false'}
    },
    { 
        'cpf': {'S': '45634634564'},
        'nome': {'S': 'Carlos Souza'},
        'clienteativo': {'S': 'true'},
        'telefone': {'S': '5555-1234'}
    }
]

for item in items:
    try:
        dynamodb.put_item(
            TableName='cliente',
            Item=item
        )
        print(f"Item inserido {item}")
    except Exception as e:
        print(e)
import json

def handler(event, context):
    print('requestL {}'.format(json.dumps(event)))
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'text/plain'
        },
        'body': 'Hello, World! {}\n'.format(event['path'])
    }
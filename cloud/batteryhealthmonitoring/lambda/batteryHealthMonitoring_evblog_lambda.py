def handler(event, context):
    response = "Lambda invocation"
    print(response)
    return {
        'statusCode': 200,
        'body': response
    }
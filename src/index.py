def handler(event, context):
    print(f"Received event: {event}")
    return "Hello from Lambda triggered by S3!"
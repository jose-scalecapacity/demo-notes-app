def handler(event, context):
  return {
    "statusCode": 200,
    "body": f"You're in UPLOAD! Your message was: {event['body']}"
  }
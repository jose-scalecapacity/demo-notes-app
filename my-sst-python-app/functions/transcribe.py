def handler(event, context):
  return {
    "statusCode": 200,
    "body": "You're in TRANSCRIBE! Your request was received at {}.".format(event['requestContext']['time'])
  }
import json
import twistlock.serverless
@twistlock.serverless.handler
def handler(event, context):
    return {
           'statusCode': 200,
           'body': json.dumps('Hello from Lambda!')
            }
    def lambda_handler(event, context):
          # TODO implement
        return {
           'statusCode': 200,
           'body': json.dumps('Hello from Lambda!')
            }
  

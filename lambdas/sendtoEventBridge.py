import json
import boto3
import datetime

client = boto3.client('events')

def lambda_handler(event, context):
    # Mudar o nome do eventbridge
    
    response = client.put_events(
        Entries=[
            {
            'Time': datetime.datetime.now(),
            'Source': 'Lambda Envio',
            'Resources': [
             ],
            'DetailType': 'EB Demo',
            'Detail': json.dumps(event),
            'EventBusName': 'arn:aws:events:us-west-2:123456789012:event-bus/SEU-EVNET-BUS',
            'TraceHeader': 'test'
             },
                ]
             )
        
    return response
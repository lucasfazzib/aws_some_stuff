import boto3
import json
import logging
import datetime

#Estamos levando em conta que voce tneha uma Fila SQS como trigger desse lambda.

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def process_message(message, event_bus_name):
    try:
        # body = json.loads(message['Body'])
        logger.info(f'Processando mensagem: {message}')
        print(message)
        # Envia a mensagem para o EventBridge
        eventbridge = boto3.client('events')
        event_bus_arn = f"arn:aws:events:us-west-2:123213123123321:event-bus/{event_bus_name}"
        response = eventbridge.put_events(
            Entries=[
                {
                    'Time': datetime.datetime.now(),
                    'Source': 'FromSourceTest',
                    'DetailType': 'NewMessage',
                    'Detail': json.dumps(message),
                    'EventBusName': event_bus_arn,
                    'TraceHeader': 'TestEventReadTrace'
                },
            ],
        )
        
        logger.info(f'Resposta do EventBridge: {response}')
    except Exception as e:
        logger.error(f'Erro ao processar mensagem: {e}')


def lambda_handler(event, context):
    try:
        for record in event["Records"]:
            payload = json.loads(record["body"])
            process_message(payload,event_bus_name='event-bus-name-that-you-defined')
    except Exception as e:
        logger.error(f'Erro ao processar mensagens: {e}')
        raise e
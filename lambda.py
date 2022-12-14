import boto3  
import json

def lambda_handler(event, context):

    sqs = boto3.resource('sqs')

    queue = sqs.get_queue_by_name(QueueName='cs5260-requests')

    response = queue.send_message(MessageBody=json.dumps(event))


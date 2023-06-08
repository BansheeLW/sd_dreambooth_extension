import string

import boto3
import json
import base64


class PostTrainHook:
    def __init__(self, message: str):
        self._message = message

    def to_sqs(self, quque_url: string = ""):
        """
        通过SQS发生task回执

        Args:
            quque_url: SQS 队列URL
        Returns:
        """
        if not quque_url:
            # todo 这里要指定aws region和aws account
            region = "us-west-2"
            account = "022637123599"
            # queue_url格式为：f"https://sqs.{region}.amazonaws.com/{account}/sagemaker-hook"
            queue_url = f"https://sqs.{region}.amazonaws.com/{account}/train_model_job_test"

        payload_bytes = self._message.encode('utf-8')
        payload_base64 = base64.b64encode(payload_bytes)
        real_message = {
            "biz_type": 0,
            "topic": "db_train_completed",
            "metadata": {},
            "payload": payload_base64.decode('utf-8'),
            "queue_tag": -1,
            "key": "",
        }
        real_message = json.dumps(real_message)

        client = boto3.client('sqs', region_name="us-west-2")
        response = client.send_message(QueueUrl=queue_url, MessageBody=real_message)
        return response

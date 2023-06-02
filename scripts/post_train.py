import string

import boto3


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
            region = "us-east-1"
            account = "843245141269"
            # quque_url格式为：f"https://sqs.{region}.amazonaws.com/{account}/sagemaker-hook"
            quque_url = f"https://sqs.{region}.amazonaws.com/{account}/sagemaker-hook"

        client = boto3.client('sqs',region_name="us-east-1")
        response = client.send_message(QueueUrl=quque_url, MessageBody=self._message)
        return response

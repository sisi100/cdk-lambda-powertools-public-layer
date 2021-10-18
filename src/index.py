from aws_lambda_powertools import Logger
from aws_lambda_powertools.utilities.typing import LambdaContext

logger = Logger(service="payment")


@logger.inject_lambda_context
def handler(event, context: LambdaContext):
    logger.info("Hello!!")
    return "hogehoge"

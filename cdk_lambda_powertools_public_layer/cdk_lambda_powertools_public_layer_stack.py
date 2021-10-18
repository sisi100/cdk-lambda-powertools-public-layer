from aws_cdk import core as cdk, aws_lambda, aws_lambda_python
import os


class CdkLambdaPowertoolsPublicLayerStack(cdk.Stack):
    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        powertools_layer = aws_lambda.LayerVersion.from_layer_version_arn(
            self,
            "lambda-powertools-layer",
            f"arn:aws:lambda:{os.getenv('CDK_DEFAULT_REGION')}:017000801446:layer:AWSLambdaPowertoolsPython:3",
        )

        aws_lambda_python.PythonFunction(
            self, f"HogeLambda", entry="src", runtime=aws_lambda.Runtime.PYTHON_3_9, layers=[powertools_layer],
        )

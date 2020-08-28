import json
from typing import Dict

from aws_cdk import aws_apigateway, core
from aws_cdk.aws_apigateway import IResource


class AgmiStack(core.Stack):
    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        api = aws_apigateway.RestApi(self, "example")

        create_noddy_endpoint(api.root, "GET", {"message": "hi from root!"})

        apples = aws_apigateway.Resource(
            self, id="apples", parent=api.root, path_part="apples"
        )

        create_noddy_endpoint(apples, "GET", {"message": "You have 3 apples"})


def create_noddy_endpoint(resource: IResource, method: str, response: Dict):
    resource.add_method(
        method,
        aws_apigateway.MockIntegration(
            request_templates={"application/json": json.dumps({"statusCode": 200})},
            integration_responses=[
                {
                    "statusCode": "200",
                    "responseTemplates": {"application/json": json.dumps(response)},
                }
            ],
        ),
        method_responses=[
            {
                "statusCode": "200",
                "responseModels": {
                    "application/json": aws_apigateway.Model.EMPTY_MODEL
                },
            }
        ],
    )

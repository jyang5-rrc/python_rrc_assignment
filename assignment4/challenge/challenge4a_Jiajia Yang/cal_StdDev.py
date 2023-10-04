import json
import boto3
import botocore.response as br

# connect to AWS lambda
lambda_client = boto3.client("lambda")

# dictionary containing function input data
p = {"nums": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]}

# invoke the function with input and fetch result
response = lambda_client.invoke(FunctionName="StdDev", Payload=json.dumps(p))

# convert result (StreamingBody) into a regular Python dictionary
payload = json.loads(response["Payload"].read())

# print original list of numbers and result, rounded to 3 decimal places
print(f"StdDev of nums {payload['nums']} is: {float(payload['standard deviation']):.3f}")

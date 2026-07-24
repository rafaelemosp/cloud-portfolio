# AWS visitor counter

The portfolio visitor counter uses AWS Lambda, DynamoDB and a Lambda Function URL.
The function URL accepts requests only from `https://rafaellemos.cloud`.

## Deploy

1. Open AWS CloudFormation in `ap-southeast-2`.
2. Create a stack using `infrastructure/visitor-counter.yml`.
3. Keep the default allowed origin and create the stack.
4. Copy `VisitorCounterEndpoint` from the stack Outputs tab.
5. Paste it into the `visitor-counter-endpoint` meta tag in `index.html`.
6. Commit and push. GitHub Actions will deploy the site and refresh CloudFront.

The DynamoDB table uses one provisioned read unit and one provisioned write unit,
with auto scaling disabled. The Lambda function uses 128 MB and has a five-second
timeout.

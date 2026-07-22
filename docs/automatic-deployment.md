# Automatic GitHub-to-S3 deployment

Every push to the `main` branch starts the workflow in
`.github/workflows/deploy-s3.yml`. GitHub receives a temporary AWS identity,
uploads the website to S3 and optionally refreshes CloudFront.

## 1. Add GitHub as an AWS identity provider

In AWS IAM, add an OpenID Connect identity provider with:

- Provider URL: `https://token.actions.githubusercontent.com`
- Audience: `sts.amazonaws.com`

This is an account-level setting and only needs to be created once.

## 2. Create the deployment role

Create an IAM role named `CloudPortfolioGitHubDeploy`. Use the following trust
policy, replacing `AWS_ACCOUNT_ID` with your 12-digit AWS account number:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Federated": "arn:aws:iam::AWS_ACCOUNT_ID:oidc-provider/token.actions.githubusercontent.com"
      },
      "Action": "sts:AssumeRoleWithWebIdentity",
      "Condition": {
        "StringEquals": {
          "token.actions.githubusercontent.com:aud": "sts.amazonaws.com",
          "token.actions.githubusercontent.com:sub": "repo:rafaelemosp/cloud-portfolio:ref:refs/heads/main"
        }
      }
    }
  ]
}
```

This trust policy restricts deployment access to the `main` branch of this
specific GitHub repository.

## 3. Give the role permission to deploy

Attach this inline policy to the role. Replace `YOUR_BUCKET_NAME` with the exact
S3 bucket name:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "ListPortfolioBucket",
      "Effect": "Allow",
      "Action": "s3:ListBucket",
      "Resource": "arn:aws:s3:::YOUR_BUCKET_NAME"
    },
    {
      "Sid": "DeployPortfolioFiles",
      "Effect": "Allow",
      "Action": [
        "s3:PutObject",
        "s3:DeleteObject",
        "s3:GetObject"
      ],
      "Resource": "arn:aws:s3:::YOUR_BUCKET_NAME/*"
    }
  ]
}
```

If CloudFront is added later, also allow `cloudfront:CreateInvalidation` for the
distribution used by this website.

## 4. Configure the GitHub repository

Open the repository on GitHub, then go to **Settings → Secrets and variables →
Actions**.

Add one repository secret:

- `AWS_ROLE_ARN`: the ARN of `CloudPortfolioGitHubDeploy`

Add two repository variables:

- `AWS_REGION`: `ap-southeast-2`
- `S3_BUCKET`: the exact S3 bucket name

Optional repository variable:

- `CLOUDFRONT_DISTRIBUTION_ID`: add this after CloudFront is configured

## 5. Deploy

Commit and push a change to `main`. Follow its progress under the repository's
**Actions** tab. The workflow can also be started manually with **Run workflow**.

Local file saves cannot reach GitHub by themselves. A commit and push are the
safe trigger that records the change and starts deployment.

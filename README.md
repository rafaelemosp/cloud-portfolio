# Rafael Lemos Cloud Portfolio

A responsive, terminal-inspired portfolio documenting my cloud computing,
infrastructure and technical support learning journey.

## Live website

[https://rafaellemos.cloud](https://rafaellemos.cloud)

## Project status

The website is hosted in Amazon S3 and delivered globally through Amazon
CloudFront with HTTPS and a custom Route 53 domain. Every push to the `main`
branch triggers an automatic deployment through GitHub Actions using secure
AWS OIDC, followed by a CloudFront cache invalidation.

## Technologies

- HTML5
- CSS3
- JavaScript
- Amazon S3
- Amazon CloudFront
- Amazon Route 53
- AWS Certificate Manager
- AWS IAM and GitHub OIDC
- GitHub Actions

## Run locally

No build tools or dependencies are required. Open `index.html` in a browser, or
serve the project with any local static web server.

## Project structure

- `index.html` — main portfolio page
- `style.css` — layout, responsive styling and animations
- `script.js` — typing effect and animated network background
- `projects/aws-portfolio.html` — AWS portfolio project details
- `site.webmanifest` and favicon files — browser and install metadata

## Deployment architecture

`GitHub -> GitHub Actions -> Amazon S3 -> Amazon CloudFront -> Route 53`

The deployment uses short-lived AWS credentials, HTTPS, CloudFront caching,
Route 53 DNS and automated cache invalidation. A serverless visitor counter
using Lambda and DynamoDB is planned as a future enhancement.

## Automatic deployment

Pushes to the `main` branch automatically deploy the website to Amazon S3 with
GitHub Actions. Authentication uses short-lived AWS credentials through OpenID
Connect rather than permanent access keys. Follow the
[automatic deployment setup guide](docs/automatic-deployment.md) to complete
the one-time AWS and GitHub configuration.

## Accessibility

The site uses semantic HTML and respects the system's reduced-motion
preference. Its primary content remains available when JavaScript is disabled.

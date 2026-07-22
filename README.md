# Rafael Lemos Cloud Portfolio

A responsive, terminal-inspired portfolio documenting my cloud computing,
infrastructure and technical support learning journey.

## Project status

The website is currently in development. An Amazon S3 bucket has been created,
but the website upload and static hosting configuration are still pending.

## Technologies

- HTML5
- CSS3
- JavaScript
- Amazon S3 (planned hosting)
- Git

## Run locally

No build tools or dependencies are required. Open `index.html` in a browser, or
serve the project with any local static web server.

## Project structure

- `index.html` — main portfolio page
- `style.css` — layout, responsive styling and animations
- `script.js` — typing effect and animated network background
- `projects/aws-portfolio.html` — AWS portfolio project details
- `site.webmanifest` and favicon files — browser and install metadata

## Deployment roadmap

1. Complete the one-time GitHub and AWS deployment configuration.
2. Enable and test Amazon S3 static website hosting.
3. Add CloudFront for CDN delivery and HTTPS.
4. Connect a custom domain with Route 53.
5. Add a visitor counter using Lambda and DynamoDB.

## Automatic deployment

Pushes to the `main` branch automatically deploy the website to Amazon S3 with
GitHub Actions. Authentication uses short-lived AWS credentials through OpenID
Connect rather than permanent access keys. Follow the
[automatic deployment setup guide](docs/automatic-deployment.md) to complete
the one-time AWS and GitHub configuration.

## Accessibility

The site uses semantic HTML and respects the system's reduced-motion
preference. Its primary content remains available when JavaScript is disabled.

<div align="center">

![VERIQTA Press](https://github.com/veriqta/veriqta/blob/main/veriqta-press-banner.svg)

# VERIQTA Press

**Free engineering PDFs and practical learning resources.**

[Browse topics](#browse-topics) · [Search every PDF](CATALOG.md) · [Start learning](#choose-a-learning-path) · [Contribute](#contribute)

</div>

Practical engineering knowledge for learning, building and operating real systems. Explore handbooks, reference guides, projects and learning resources covering Linux, programming, cloud infrastructure, DevOps, security and production engineering.

Browse by subject below, follow a suggested learning path, or use the [PDF catalog](CATALOG.md) to find a publication by title.

Published by [VERIQTA](https://veriqta.com/), covering engineering education, technical publishing and professional assessment.

## Find and download a PDF

1. Choose a topic below, or open the [complete catalog](CATALOG.md) and use **Ctrl+F** / **Command+F** to search titles.
2. Follow a PDF link to preview it on GitHub. If a preview is unavailable, use the file's download control.
3. Download the PDF to read locally. For an offline copy of the entire collection, use GitHub's **Code → Download ZIP**, or clone it:

```sh
git clone https://github.com/veriqta/VERIQTA-PRESS.git
cd VERIQTA-PRESS
```

The collection contains large binary files; cloning or downloading the whole repository takes more space and time than saving an individual PDF. No software installation or build step is needed to read the documents.

## Browse topics

Choose a subject to explore its publications and practical resources.

### Foundations

| Topic | What you will find |
| --- | --- |
| [Linux](linux/) | Administration, commands, permissions, internals and labs. |
| [Programming & development](programming-and-development/) | Python, Go, Git, APIs, YAML and developer tools. |
| [Networking](networking/) | Protocols, NGINX, traffic analysis and network operations. |
| [Shell scripting](shell-scripting/) | Bash fundamentals and practical automation. |

### Cloud, containers & delivery

| Topic | What you will find |
| --- | --- |
| [AWS](aws/) | AWS services, architecture, projects and operations. |
| [Azure & Google Cloud](azure-and-google-cloud/) | Azure, AKS, GCP and cloud fundamentals. |
| [Containers](containers/) | Docker, Compose, Podman and container internals. |
| [Kubernetes](kubernetes/) | Clusters, Helm, Argo CD, service mesh and certification practice. |
| [CI/CD](ci-cd/) | Jenkins, GitHub Actions, GitLab and deployment pipelines. |
| [Infrastructure as code](infrastructure-as-code/) | Infrastructure provisioning, configuration management and repeatable automation. |
| [DevOps](devops/) | General handbooks, daily operations, commands and FinOps. |

### Operate, secure & troubleshoot

| Topic | What you will find |
| --- | --- |
| [Incident response](incident-response/) | Incident playbooks, case studies and production failures. |
| [Site reliability engineering](site-reliability-engineering/) | SRE practices, on-call work, chaos engineering and reliability. |
| [Monitoring & observability](monitoring-and-observability/) | Prometheus, Grafana, ELK, Dynatrace and New Relic. |
| [Troubleshooting](troubleshooting/) | Diagnostic playbooks, log reading and common delivery failures. |
| [Production engineering](production-engineering/) | Production readiness, operational ownership and service continuity. |
| [Databases](databases/) | PostgreSQL, MySQL and Redis operations. |
| [DevSecOps & identity](devsecops-and-identity/) | Pipeline security, Trivy and DevSecOps practices. |
| [Cloud security](cloud-security/) | AWS security labs, controls and misconfigurations. |

### Specialist engineering

| Topic | What you will find |
| --- | --- |
| [Platform engineering](platform-engineering/) | Developer platforms, self-service infrastructure and shared engineering capabilities. |
| [Infrastructure engineering](infrastructure-engineering/) | Infrastructure operations, outages, Kafka and RabbitMQ. |
| [AI for DevOps](ai-for-devops/) | AI-assisted operations, agents and projects. |
| [AI & GPU infrastructure](ai-and-gpu-infrastructure/) | GPU platforms, AI infrastructure and MLOps. |
| [Engineering internals](engineering-internals/) | System internals, performance and deeper engineering mechanisms. |
| [Architecture & design](architecture-and-design/) | System design, production architecture and diagrams. |
| [Forward-deployed engineering](forward-deployed-engineering/) | Engineering delivery in customer environments. |
| [Staff & principal engineering](staff-and-principal-engineering/) | Staff-level engineering responsibilities and judgement. |

### Career & practical work

| Topic | What you will find |
| --- | --- |
| [Career & certifications](career-and-certifications/) | Roadmaps, interviews, resumes, certification and first-month guidance. |
| [Hands-on projects](hands-on-projects/) | DevOps, cloud, Kubernetes and infrastructure builds. |
| [Engineering portfolio](engineering-portfolio/) | Home labs, portfolio guidance and project ideas. |

## Choose a learning path

- **New to engineering:** [Linux](linux/) → [Networking](networking/) → [Programming](programming-and-development/) → [Shell scripting](shell-scripting/).
- **Build and deliver applications:** [Containers](containers/) → [CI/CD](ci-cd/) → [AWS](aws/) or [Azure & Google Cloud](azure-and-google-cloud/) → [Infrastructure as code](infrastructure-as-code/) → [Kubernetes](kubernetes/).
- **Operate production systems:** [Monitoring](monitoring-and-observability/) → [Troubleshooting](troubleshooting/) → [Incident response](incident-response/) → [SRE](site-reliability-engineering/).
- **Prepare for a role:** [Career & certifications](career-and-certifications/) → [Hands-on projects](hands-on-projects/) → [Engineering portfolio](engineering-portfolio/).

These are suggested routes; choose documents that fit your goals and experience. Practise commands in an isolated lab, check version-specific details against official documentation, and record what you tested and learned.

## How the library is organized

- Topic folders hold publications about a particular technology or practice. Tool-specific interview guides and projects stay with their technology, such as AWS or Kubernetes.
- General career preparation lives in `career-and-certifications/`; cross-topic builds live in `hands-on-projects/`; portfolio presentation and home-lab guidance live in `engineering-portfolio/`.
- Incident case studies and response playbooks live in `incident-response/`. General diagnostic guides live in `troubleshooting/`.
- Infrastructure-as-code publications are grouped into [Terraform & Terragrunt](infrastructure-as-code/terraform-and-terragrunt/), [Ansible](infrastructure-as-code/ansible/) and [Chef](infrastructure-as-code/chef/).

## Contribute

Found a broken link, outdated example or unclear explanation? [Open an issue](https://github.com/veriqta/VERIQTA-PRESS/issues) with the document name, affected section and suggested correction. Include a public technical source where relevant.

For a contribution, fork the repository, create a branch, place the document in the closest topic folder, and add links to that folder's README and the complete catalog. Check that relative links open correctly. Preserve existing PDFs when reorganizing; keep credentials, private data and generated artifacts out of contributions. Respect authorship and applicable licensing.

Star the repository to bookmark it. Use GitHub's Watch settings to choose update notifications; forks do not automatically receive upstream changes.

## About VERIQTA

VERIQTA Press brings VERIQTA's engineering publications and learning resources together. Explore more through the [official website](https://veriqta.com/), [VERIQTA WORLD repositories](https://github.com/VERIQTA-WORLD), [@veriqta](https://www.instagram.com/veriqta/) and [@veriqta_academy](https://www.instagram.com/veriqta_academy/).

## Licence and attribution

See [LICENSE](LICENSE) for repository licensing terms. Third-party materials may have separate conditions; check the document and source before reuse or redistribution. Inclusion does not imply affiliation with a technology vendor.

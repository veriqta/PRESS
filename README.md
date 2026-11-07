<div align="center">

![VERIQTA Press](https://github.com/veriqta/veriqta/blob/main/veriqta-press-banner.svg)

# VERIQTA Press

**Free engineering PDFs and practical learning resources.**

[Browse topics](#browse-topics) · [Search every PDF](CATALOG.md) · [Start learning](#choose-a-learning-path) · [Contribute](#contribute)

</div>

Explore **292 PDFs across 30 topics**, from Linux fundamentals to cloud infrastructure, DevOps, security and production engineering. Each topic folder has a README linking to its PDFs. The [complete catalog](CATALOG.md) lists every title in one searchable page.

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

Folders use descriptive lowercase names with hyphens. PDF publication filenames and volume numbers are preserved. Counts below refer to PDFs, including any distinct files with similar titles.

### Foundations

| Topic | PDFs | What you will find |
| --- | ---: | --- |
| [Linux](linux/) | 26 | Administration, commands, permissions, internals and labs. |
| [Programming & development](programming-and-development/) | 16 | Python, Go, Git, APIs, YAML and developer tools. |
| [Networking](networking/) | 14 | Protocols, NGINX, traffic analysis and network operations. |
| [Shell scripting](shell-scripting/) | 4 | Bash fundamentals and practical automation. |

### Cloud, containers & delivery

| Topic | PDFs | What you will find |
| --- | ---: | --- |
| [AWS](aws/) | 22 | AWS services, architecture, projects and operations. |
| [Azure & Google Cloud](azure-and-google-cloud/) | 9 | Azure, AKS, GCP and cloud fundamentals. |
| [Containers](containers/) | 11 | Docker, Compose, Podman and container internals. |
| [Kubernetes](kubernetes/) | 35 | Clusters, Helm, Argo CD, service mesh and certification practice. |
| [CI/CD](ci-cd/) | 24 | Jenkins, GitHub Actions, GitLab and deployment pipelines. |
| [Infrastructure as code](infrastructure-as-code/) | 17 | Separate Terraform/Terragrunt, Ansible and Chef folders. |
| [DevOps](devops/) | 13 | General handbooks, daily operations, commands and FinOps. |

### Operate, secure & troubleshoot

| Topic | PDFs | What you will find |
| --- | ---: | --- |
| [Incident response](incident-response/) | 15 | Incident playbooks, case studies and production failures. |
| [Site reliability engineering](site-reliability-engineering/) | 6 | SRE practices, on-call work, chaos engineering and reliability. |
| [Monitoring & observability](monitoring-and-observability/) | 9 | Prometheus, Grafana, ELK, Dynatrace and New Relic. |
| [Troubleshooting](troubleshooting/) | 5 | Diagnostic playbooks, log reading and common delivery failures. |
| [Production engineering](production-engineering/) | 2 | Environment takeovers and first on-call guidance. |
| [Databases](databases/) | 4 | PostgreSQL, MySQL and Redis operations. |
| [DevSecOps & identity](devsecops-and-identity/) | 3 | Pipeline security, Trivy and DevSecOps practices. |
| [Cloud security](cloud-security/) | 3 | AWS security labs, controls and misconfigurations. |

### Specialist engineering

| Topic | PDFs | What you will find |
| --- | ---: | --- |
| [Platform engineering](platform-engineering/) | 2 | Platform foundations and bootcamp material. |
| [Infrastructure engineering](infrastructure-engineering/) | 6 | Infrastructure operations, outages, Kafka and RabbitMQ. |
| [AI for DevOps](ai-for-devops/) | 4 | AI-assisted operations, agents and projects. |
| [AI & GPU infrastructure](ai-and-gpu-infrastructure/) | 4 | GPU platforms, AI infrastructure and MLOps. |
| [Engineering internals](engineering-internals/) | 1 | eBPF and deeper systems behaviour. |
| [Architecture & design](architecture-and-design/) | 4 | System design, production architecture and diagrams. |
| [Forward-deployed engineering](forward-deployed-engineering/) | 1 | Engineering delivery in customer environments. |
| [Staff & principal engineering](staff-and-principal-engineering/) | 1 | Staff-level engineering responsibilities and judgement. |

### Career & practical work

| Topic | PDFs | What you will find |
| --- | ---: | --- |
| [Career & certifications](career-and-certifications/) | 17 | Roadmaps, interviews, resumes, certification and first-month guidance. |
| [Hands-on projects](hands-on-projects/) | 9 | DevOps, cloud, Kubernetes and infrastructure builds. |
| [Engineering portfolio](engineering-portfolio/) | 5 | Home labs, portfolio guidance and project ideas. |

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

If you followed an older numbered-folder link, use the [catalog](CATALOG.md) to find the same PDF by its original filename.

## Contribute

Found a broken link, outdated example or unclear explanation? [Open an issue](https://github.com/veriqta/VERIQTA-PRESS/issues) with the document name, affected section and suggested correction. Include a public technical source where relevant.

For a contribution, fork the repository, create a branch, place the document in the closest topic folder, and update that folder's README, the complete catalog and root counts. Check that relative links open correctly. Preserve existing PDFs when reorganizing; keep credentials, private data and generated artifacts out of contributions. Respect authorship and applicable licensing.

Star the repository to bookmark it. Use GitHub's Watch settings to choose update notifications; forks do not automatically receive upstream changes.

## About VERIQTA

VERIQTA Press brings VERIQTA's engineering publications and learning resources together. Explore more through the [official website](https://veriqta.com/), [VERIQTA WORLD repositories](https://github.com/VERIQTA-WORLD), [@veriqta](https://www.instagram.com/veriqta/) and [@veriqta_academy](https://www.instagram.com/veriqta_academy/).

## Licence and attribution

See [LICENSE](LICENSE) for repository licensing terms. Third-party materials may have separate conditions; check the document and source before reuse or redistribution. Inclusion does not imply affiliation with a technology vendor.

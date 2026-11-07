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
| [Linux](00.%20Linux) | Administration, commands, permissions, internals and labs. |
| [Programming & development](01.%20Programming%20%26%20Development) | Python, Go, Git, APIs, YAML and developer tools. |
| [Networking](02.%20Networking) | Protocols, NGINX, traffic analysis and network operations. |
| [Shell scripting](03.%20Shell%20Scripting) | Bash fundamentals and practical automation. |

### Cloud, containers & delivery

| Topic | What you will find |
| --- | --- |
| [AWS](09.%20AWS) | AWS services, architecture, projects and operations. |
| [Azure & Google Cloud](10.%20Azure%20%26%20Google%20Cloud) | Azure, AKS, GCP and cloud fundamentals. |
| [Containers](05.%20Docker%20%26%20Containers) | Docker, Compose, Podman and container internals. |
| [Kubernetes](06.%20Kubernetes) | Clusters, Helm, Argo CD, service mesh and certification practice. |
| [CI/CD](07.%20CI-CD%20%26%20GitOps) | Jenkins, GitHub Actions, GitLab and deployment pipelines. |
| [Infrastructure as code](08.%20Infrastructure%20as%20Code) | Infrastructure provisioning, configuration management and repeatable automation. |
| [DevOps](04.%20DevOps) | General handbooks, daily operations, commands and FinOps. |

### Operate, secure & troubleshoot

| Topic | What you will find |
| --- | --- |
| [Incident response](15.%20Incident%20Response) | Incident playbooks, case studies and production failures. |
| [Site reliability engineering](14.%20SRE%20%26%20Reliability%20Engineering) | SRE practices, on-call work, chaos engineering and reliability. |
| [Monitoring & observability](13.%20Monitoring%20%26%20Observability) | Prometheus, Grafana, ELK, Dynatrace and New Relic. |
| [Troubleshooting](16.%20Troubleshooting) | Diagnostic playbooks, log reading and common delivery failures. |
| [Production engineering](17.%20Production%20Engineering) | Production readiness, operational ownership and service continuity. |
| [Databases](11.%20Databases) | PostgreSQL, MySQL and Redis operations. |
| [DevSecOps & identity](18.%20DevSecOps%20%26%20Identity) | Pipeline security, Trivy and DevSecOps practices. |
| [Cloud security](19.%20Cloud%20Security) | AWS security labs, controls and misconfigurations. |

### Specialist engineering

| Topic | What you will find |
| --- | --- |
| [Platform engineering](20.%20Platform%20Engineering) | Developer platforms, self-service infrastructure and shared engineering capabilities. |
| [Infrastructure engineering](12.%20Infrastructure%20Engineering) | Infrastructure operations, outages, Kafka and RabbitMQ. |
| [AI for DevOps](21.%20AI%20for%20DevOps) | AI-assisted operations, agents and projects. |
| [AI & GPU infrastructure](22.%20AI%20Infrastructure%20%26%20MLOps) | GPU platforms, AI infrastructure and MLOps. |
| [Engineering internals](24.%20Advanced%20Engineering%20Internals) | System internals, performance and deeper engineering mechanisms. |
| [Architecture & design](23.%20System%20Architecture%20%26%20Design) | System design, production architecture and diagrams. |
| [Forward-deployed engineering](25.%20Forward%20Deployed%20Engineering) | Engineering delivery in customer environments. |
| [Staff & principal engineering](26.%20Staff%20%26%20Principal%20Engineering) | Staff-level engineering responsibilities and judgement. |

### Career & practical work

| Topic | What you will find |
| --- | --- |
| [Career & certifications](27.%20Career%2C%20Interviews%20%26%20Certifications) | Roadmaps, interviews, resumes, certification and first-month guidance. |
| [Hands-on projects](28.%20Hands-On%20Projects) | DevOps, cloud, Kubernetes and infrastructure builds. |
| [Engineering portfolio](29.%20Engineering%20Portfolio%20%26%20Home%20Labs) | Home labs, portfolio guidance and project ideas. |

## Choose a learning path

- **New to engineering:** [Linux](00.%20Linux) → [Networking](02.%20Networking) → [Programming](01.%20Programming%20%26%20Development) → [Shell scripting](03.%20Shell%20Scripting).
- **Build and deliver applications:** [Containers](05.%20Docker%20%26%20Containers) → [CI/CD](07.%20CI-CD%20%26%20GitOps) → [AWS](09.%20AWS) or [Azure & Google Cloud](10.%20Azure%20%26%20Google%20Cloud) → [Infrastructure as code](08.%20Infrastructure%20as%20Code) → [Kubernetes](06.%20Kubernetes).
- **Operate production systems:** [Monitoring](13.%20Monitoring%20%26%20Observability) → [Troubleshooting](16.%20Troubleshooting) → [Incident response](15.%20Incident%20Response) → [SRE](14.%20SRE%20%26%20Reliability%20Engineering).
- **Prepare for a role:** [Career & certifications](27.%20Career%2C%20Interviews%20%26%20Certifications) → [Hands-on projects](28.%20Hands-On%20Projects) → [Engineering portfolio](29.%20Engineering%20Portfolio%20%26%20Home%20Labs).

These are suggested routes; choose documents that fit your goals and experience. Practise commands in an isolated lab, check version-specific details against official documentation, and record what you tested and learned.

## How the library is organized

- Topic folders hold publications about a particular technology or practice. Tool-specific interview guides and projects stay with their technology, such as AWS or Kubernetes.
- General career preparation lives in `27. Career, Interviews & Certifications/`; cross-topic builds live in `28. Hands-On Projects/`; portfolio presentation and home-lab guidance live in `29. Engineering Portfolio & Home Labs/`.
- Incident case studies and response playbooks live in `15. Incident Response/`. General diagnostic guides live in `16. Troubleshooting/`.
- Infrastructure-as-code publications cover Terraform, Terragrunt, Ansible and Chef in the [Infrastructure as Code](08.%20Infrastructure%20as%20Code/) folder.

## Contribute

Found a broken link, outdated example or unclear explanation? [Open an issue](https://github.com/veriqta/VERIQTA-PRESS/issues) with the document name, affected section and suggested correction. Include a public technical source where relevant.

For a contribution, fork the repository, create a branch, place the document in the closest topic folder, and add links to that folder's README and the complete catalog. Check that relative links open correctly. Preserve existing PDFs when reorganizing; keep credentials, private data and generated artifacts out of contributions. Respect authorship and applicable licensing.

Star the repository to bookmark it. Use GitHub's Watch settings to choose update notifications; forks do not automatically receive upstream changes.

## About VERIQTA

VERIQTA Press brings VERIQTA's engineering publications and learning resources together. Explore more through the [official website](https://veriqta.com/), [VERIQTA WORLD repositories](https://github.com/VERIQTA-WORLD), [@veriqta](https://www.instagram.com/veriqta/) and [@veriqta_academy](https://www.instagram.com/veriqta_academy/).

## Licence and attribution

See [LICENSE](LICENSE) for repository licensing terms. Third-party materials may have separate conditions; check the document and source before reuse or redistribution. Inclusion does not imply affiliation with a technology vendor.

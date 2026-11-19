# Role Fit — 2026

This page maps the repositories in this profile to four common engineering role families. Everything listed is a hands-on lab, coursework project, or reference implementation. It is evidence of practice — not a claim of employment history.

## DevOps / Platform Engineer

| Requirement | Where to look | Evidence |
| --- | --- | --- |
| CI/CD pipelines and automation | [devops-platform-2026](https://github.com/aryafatthurahman4-collab/devops-platform-2026) | GitHub Actions for test, Terraform validation, Kubernetes linting, Trivy scanning, image build, and a GHCR release workflow |
| Cloud infrastructure (AWS) | [devops-platform-2026](https://github.com/aryafatthurahman4-collab/devops-platform-2026), [aws-ec2-web-hosting-part-1](https://github.com/aryafatthurahman4-collab/aws-ec2-web-hosting-part-1) | VPC, subnets, NAT/IGW, security groups, IAM/IRSA, EKS, RDS, ECR, EC2 |
| Containers and Kubernetes | [devops-platform-2026](https://github.com/aryafatthurahman4-collab/devops-platform-2026), [k8s](https://github.com/aryafatthurahman4-collab/k8s) | Multi-stage Dockerfiles, non-root containers, Kustomize overlays, Helm chart, HPA, PDB, NetworkPolicy, probes |
| Infrastructure as Code | [devops-platform-2026](https://github.com/aryafatthurahman4-collab/devops-platform-2026), [terraform-databricks-sra-modernized](https://github.com/aryafatthurahman4-collab/terraform-databricks-sra-modernized) | Terraform modules, variables and validation, remote-state example, `fmt`/`validate` in CI |
| Monitoring and observability | [devops-platform-2026](https://github.com/aryafatthurahman4-collab/devops-platform-2026), [prometheus](https://github.com/aryafatthurahman4-collab/prometheus), [grafana](https://github.com/aryafatthurahman4-collab/grafana) | Prometheus scrape config and alert rules, Grafana dashboard JSON, health/readiness probes, SLO notes |
| DevSecOps | [devops-platform-2026](https://github.com/aryafatthurahman4-collab/devops-platform-2026) | Trivy config/image scans, least-privilege IAM, secret hygiene, Kubernetes security contexts, SBOM generation |
| Incident response and operations | [devops-platform-2026](https://github.com/aryafatthurahman4-collab/devops-platform-2026) | Runbook, incident-response guide, RCA template, rollback and restore procedures |
| Cost and scalability | [devops-platform-2026](https://github.com/aryafatthurahman4-collab/devops-platform-2026) | Right-sizing notes, spot-node option, NAT/RDS cost guidance, HPA and PDB configuration |

## Backend Engineer

| Requirement | Where to look | Evidence |
| --- | --- | --- |
| Java and Quarkus services | [backend-service-2026](https://github.com/aryafatthurahman4-collab/backend-service-2026) | Java 21, Quarkus REST, Panache, service layer, DTOs, validation, problem-detail errors |
| REST APIs and contracts | [backend-service-2026](https://github.com/aryafatthurahman4-collab/backend-service-2026) | Versioned REST endpoints, OpenAPI, pagination, status transitions, idempotency |
| PostgreSQL and SQL | [backend-service-2026](https://github.com/aryafatthurahman4-collab/backend-service-2026), [hris-itk-laravel](https://github.com/aryafatthurahman4-collab/hris-itk-laravel) | Flyway migrations, constraints, indexes, aggregate queries, transactional writes |
| Redis and caching | [backend-service-2026](https://github.com/aryafatthurahman4-collab/backend-service-2026) | Cache-aside configuration and local Compose service |
| Messaging concepts (Kafka/NATS) | [backend-service-2026](https://github.com/aryafatthurahman4-collab/backend-service-2026), [snowflake-databricks](https://github.com/aryafatthurahman4-collab/snowflake-databricks) | Integration notes and event-driven extension points |
| Testing | [backend-service-2026](https://github.com/aryafatthurahman4-collab/backend-service-2026) | Unit tests plus `@QuarkusTest` resource tests with H2, run in CI |
| Containers and deployment | [backend-service-2026](https://github.com/aryafatthurahman4-collab/backend-service-2026) | Multi-stage Dockerfile, non-root runtime, Kubernetes manifests, probes, HPA |
| Frontend integration | [nextjs-aws-production](https://github.com/aryafatthurahman4-collab/nextjs-aws-production), [ui-modernized](https://github.com/aryafatthurahman4-collab/ui-modernized) | TypeScript/React/Next.js clients and API integration patterns |

## Software Quality Assurance / Test Automation (Banking)

| Requirement | Where to look | Evidence |
| --- | --- | --- |
| Test strategy, plan, and cases | [qa-automation-2026](https://github.com/aryafatthurahman4-collab/qa-automation-2026) | Strategy, release plan, 25+ test cases, requirements traceability matrix, defect log and template |
| E2E and UI automation | [qa-automation-2026](https://github.com/aryafatthurahman4-collab/qa-automation-2026) | Playwright Chromium flows for transfers, balances, history, and negative cases |
| API and integration testing | [qa-automation-2026](https://github.com/aryafatthurahman4-collab/qa-automation-2026) | API tests for happy path, insufficient funds, idempotency, currency mismatch, unknown accounts |
| SQL and data integrity | [qa-automation-2026](https://github.com/aryafatthurahman4-collab/qa-automation-2026) | Ledger debit/credit netting, balance reconciliation, orphan checks, unique idempotency keys |
| Banking transaction flows | [qa-automation-2026](https://github.com/aryafatthurahman4-collab/qa-automation-2026) | Accounts, transfers, ledger entries, atomic debit/credit, idempotent replay |
| Performance testing | [qa-automation-2026](https://github.com/aryafatthurahman4-collab/qa-automation-2026) | k6 stages and thresholds with a documented interpretation guide |
| CI/CD continuous testing | [qa-automation-2026](https://github.com/aryafatthurahman4-collab/qa-automation-2026) | GitHub Actions runs DB, API, and E2E suites and publishes HTML/JUnit artifacts |
| Unit testing practice | [pengujian-unit-latihan-soal](https://github.com/aryafatthurahman4-collab/pengujian-unit-latihan-soal) | Node test-runner exercises with boundary and validation cases |
| Browser testing practice | [amazon-aws-kernellinux-ami](https://github.com/aryafatthurahman4-collab/amazon-aws-kernellinux-ami) | Playwright test suite with a CI browser install |

## AI-Assisted Software Engineering

| Requirement | Where to look | Evidence |
| --- | --- | --- |
| Applied machine learning | [machine-learning-dicoding](https://github.com/aryafatthurahman4-collab/machine-learning-dicoding), [credit-card-fraud](https://github.com/aryafatthurahman4-collab/credit-card-fraud) | Preprocessing, EDA, training, evaluation, imbalanced-data handling |
| Computer vision | [cnn](https://github.com/aryafatthurahman4-collab/cnn), [sensor-hewan](https://github.com/aryafatthurahman4-collab/sensor-hewan) | CNN training and camera-sensor integration with a telemetry database |
| Research experiments | [quantum-hybrid-diffusion-models](https://github.com/aryafatthurahman4-collab/quantum-hybrid-diffusion-models), [quantum-hybrid-resornizations-databricks-snowflake](https://github.com/aryafatthurahman4-collab/quantum-hybrid-resornizations-databricks-snowflake) | Quantum-classical hybrid experiments and Databricks/Snowflake integration |
| Data platforms | [snowflake-databricks](https://github.com/aryafatthurahman4-collab/snowflake-databricks), [data-preprocessing-eda-training-evaluation-deployment](https://github.com/aryafatthurahman4-collab/data-preprocessing-eda-training-evaluation-deployment) | Data engineering notes and an end-to-end ML pipeline |
| AI-assisted delivery | [devops-platform-2026](https://github.com/aryafatthurahman4-collab/devops-platform-2026), [backend-service-2026](https://github.com/aryafatthurahman4-collab/backend-service-2026) | AI-assisted scaffolding, tests, documentation, and review-ready commits |

## How to review a repository quickly

1. Open the README and read the architecture diagram.
2. Check the CI badge and the latest workflow run.
3. Run the documented test command locally.
4. Read the runbook or test plan to see how the project is operated and verified.

> Prefer evidence over claims: every project above is public, runnable, and documented.

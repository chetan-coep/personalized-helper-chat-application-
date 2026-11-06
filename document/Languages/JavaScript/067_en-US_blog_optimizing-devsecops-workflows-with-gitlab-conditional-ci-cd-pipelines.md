---
id: "javascript_067"
technology: "JavaScript"
category: "Languages"
title: "JavaScript"
doc_order: 67
source_url: "https://developer.mozilla.org/en-US/blog/optimizing-devsecops-workflows-with-gitlab-conditional-ci-cd-pipelines"
language: "en"
retrieved_at: "2026-11-01 21:53:32"
content_hash: "bca3e46975e189c5977f18e59050919ac0744023a3fac92ccc8d6cc60297f372"
---

# JavaScript

Source: https://developer.mozilla.org/en-US/blog/optimizing-devsecops-workflows-with-gitlab-conditional-ci-cd-pipelines

---

# Optimizing DevSecOps workflows with GitLab's conditional CI/CD pipelines

CI/CD pipelines can be simple or complex, but what makes them efficient are the rules that define when and how they run. By using rules, you can create smarter CI/CD pipelines that boost team productivity and allow organizations to iterate faster. In this guide, you will learn about the different types of CI/CD pipelines, their use cases, and how to create highly efficient DevSecOps workflows by leveraging rules.

## [Understanding GitLab pipelines](https://developer.mozilla.org#understanding_gitlab_pipelines)

A pipeline is the top-level component in GitLabs's [continuous integration](https://docs.gitlab.com/ee/ci/introduction/index.html#continuous-integration) and [continuous delivery/continuous deployment](https://docs.gitlab.com/ee/ci/introduction/index.html#continuous-delivery) framework. It consists of [jobs](https://docs.gitlab.com/ee/ci/jobs/index.html), which are lists of tasks to be executed. Jobs are organized into [stages](https://docs.gitlab.com/ee/ci/yaml/index.html#stages), which define the sequence in which the jobs run.

A pipeline can have a [basic configuration](https://docs.gitlab.com/ee/ci/pipelines/pipeline_architectures.html#basic-pipelines), where jobs run concurrently in each stage. Pipelines can also have complex setups, such as [parent-child pipelines](https://docs.gitlab.com/ee/ci/pipelines/downstream_pipelines.html#parent-child-pipelines), [merge trains](https://docs.gitlab.com/ee/ci/pipelines/merge_trains.html), [multi-project pipelines](https://docs.gitlab.com/ee/ci/pipelines/downstream_pipelines.html#multi-project-pipelines), or the more advanced [Directed Acyclic Graph (DAG) pipelines](https://docs.gitlab.com/ee/ci/directed_acyclic_graph/index.html). DAG pipelines are more advanced setups that are used for complex dependencies.

The image below is a representation of a [*gitlab-runner pipeline*](https://gitlab.com/gitlab-org/gitlab-runner/-/pipelines/798871212/) showing job dependencies.

The image below depicts a DAG pipeline.

The complexity of a GitLab pipeline is often determined by specific use cases. For example, a use case might require testing an application and packaging it into a container; in such cases, the GitLab pipeline can even be used to deploy the container to an orchestrator like Kubernetes or a container registry. Another use case might involve building applications that target different platforms with varying dependencies, which is where our DAG pipelines shine.

## [Exploring CI/CD rules](https://developer.mozilla.org#exploring_cicd_rules)

In GitLab, CI/CD rules are the key to managing the flow of jobs in a pipeline. One of the powerful features of GitLab CI/CD is the ability to control when a CI/CD job runs, which can depend on the context, the changes made, [workflow rules](https://docs.gitlab.com/ee/ci/yaml/workflow.html), values of CI/CD variables, or custom conditions. In addition to using `rules`, you can control the flow of CI/CD pipelines using the following keywords:

- `needs`: Establishes relationships between jobs and is commonly used in DAG pipelines
- `only`: Defines when a job should run
- `except`: Defines when a job should not run
- `workflow`: Controls when pipelines are created

**Note:** `only` and `except` should not be used with `rules` because this can lead to unexpected behavior. You will learn more about effectively using `rules` in the subsequent sections.


## [Introduction to the rules feature](https://developer.mozilla.org#introduction_to_the_rules_feature)

[`rules`](https://docs.gitlab.com/ee/ci/yaml/#rules) determine if and when a job runs in a pipeline. If multiple `rules` are defined, they are all evaluated in sequence until a matching `rule` is found, at which point, the job is executed according to the specified configuration.

`rules` can be defined using the keywords `if`, `changes`, `exists`, `allow_failure`, `needs` and `variables`.

### [rules:if](https://developer.mozilla.org#rulesif)

The `if` keyword evaluates if a job should be added to a pipeline. The evaluation is done based on the values of [CI/CD variables](https://docs.gitlab.com/ee/ci/variables/index.html) defined in the scope of the job or pipeline and [predefined CI/CD variables](https://docs.gitlab.com/ee/ci/variables/predefined_variables.html).

```
job:
  script:
    - echo $(date)
  rules:
    - if: $CI_MERGE_REQUEST_SOURCE_BRANCH_NAME == $CI_DEFAULT_BRANCH
```
In the CI/CD script above, the job prints the current date and time using the `echo` command. The job is executed only if the source branch of a merge request (`CI_MERGE_REQUEST_SOURCE_BRANCH_NAME`) is the same as the project's default branch (`CI_DEFAULT_BRANCH`) in a [merge request pipeline](https://docs.gitlab.com/ee/ci/pipelines/merge_request_pipelines.html). You can use `==` and `!=` operators for comparison, while `=~` and `!~` operators allow you to compare a variable to a regular expression. You can combine multiple expressions using the `&&` (AND) and `||` (OR) operators and parentheses for grouping expressions.

### [rules:changes](https://developer.mozilla.org#ruleschanges)

With the `changes` keyword, you can watch for changes to certain files or folders for a job to execute. GitLab uses the output from [git's diffstat](https://git-scm.com/docs/git-diff#Documentation/git-diff.txt---statltwidthgtltname-widthgtltcountgt) to determine files that have changed and match them against the array of files provided for the `changes` rule. A use case is an infrastructure project that houses resource files for different components of an infrastructure, and you want to execute a `terraform` plan when changes are made to the terraform files.

```
job:
  script:
    - terraform plan
  rules:
    - if: $CI_PIPELINE_SOURCE == "merge_request_event"
      changes:
        - terraform/**/*.tf
```
In this example, the `terraform` plan is executed only when files with the `.tf` extension are changed in the `terraform` folder and its subdirectories. An additional rule ensures the job is executed for [merge request pipelines](https://docs.gitlab.com/ee/ci/pipelines/merge_request_pipelines.html).

The `changes` rule, as shown below, can look for changes in specific files with `paths`:

```
job:
  script:
    - terraform plan
  rules:
    - if: $CI_PIPELINE_SOURCE == "merge_request_event"
      changes:
        paths:
          - terraform/main.tf
```
Changes to files in a source reference (branch, tag, commit) can also be compared against other references in the Git repository. The CI/CD job will only execute when the source reference differs from the specified reference value defined in [`rules:changes:compare_to`](https://docs.gitlab.com/ee/ci/yaml/#ruleschangescompare_to). This value can be a Git commit SHA, a tag, or a branch name. The following example compares the source reference to the current production branch, `refs/head/production`.

```
job:
  script:
    - terraform plan
  rules:
    - if: $CI_PIPELINE_SOURCE == "merge_request_event"
      changes:
        paths:
          - terraform/main.tf
        compare_to: "refs/head/production"
```
### [rules:exists](https://developer.mozilla.org#rulesexists)

Similar to changes, you can execute CI/CD jobs only when specific files exist by using the [`rules:exists`](https://docs.gitlab.com/ee/ci/yaml/#rulesexists) rules. For example, you can run a job that checks whether a `Gemfile.lock` file exists. The following example audits a Ruby project for vulnerable versions of gems or insecure gem sources using the [bundler-audit project](https://github.com/rubysec/bundler-audit).

```
job:
  script:
    - bundle-audit check --format json --output bundle-audit.json
  rules:
    - if: $CI_PIPELINE_SOURCE == "merge_request_event"
      changes:
        exists:
          - Gemfile.lock
```
### [rules:allow\_failure](https://developer.mozilla.org#rulesallow_failure)

There are scenarios where the failure of a job should not affect the subsequent jobs and stages in the pipeline. This can be useful in use cases where non-blocking tasks are required as part of a project but don't impact the project in any way. The [`rules:allow_failure`](https://docs.gitlab.com/ee/ci/yaml/#rulesallow_failure) rule can be set to `true` or `false`. It defaults to `false` when the rule is not specified.

```
job:
  script:
    - bundle-audit check --format json --output bundle-audit.json
  rules:
    - if: $CI_PIPELINE_SOURCE == "merge_request_event" && $CI_MERGE_REQUEST_TARGET_BRANCH_PROTECTED == "false"
      changes:
        exists:
          - Gemfile.lock
      allow_failure: true
```
In this example, the job can fail only if a merge request event triggers the pipeline and the target branch is not protected.

### [rules:needs](https://developer.mozilla.org#rulesneeds)

Disabled by default, `rules:needs` was introduced in [GitLab 16](https://about.gitlab.com/releases/2023/05/22/gitlab-16-0-released/) and can be enabled using the `introduce_rules_with_needs` [feature flag](https://docs.gitlab.com/ee/user/feature_flags.html). The `needs` rule is used to execute jobs out of sequence without waiting for other jobs in a stage to complete. When used with `rules`, it overrides the job's `needs` specification when the specified conditions are met.

```
stages:
  - build
  - qa
  - deploy
build-dev:
  stage: build
  rules:
    - if: $CI_COMMIT_BRANCH != $CI_DEFAULT_BRANCH
  script: echo "Building dev version..."
build-prod:
  stage: build
  rules:
    - if: $CI_COMMIT_BRANCH == $CI_DEFAULT_BRANCH
  script: echo "Building production version..."
qa-checks:
  stage: qa
  script:
    - echo "Running QA checks before publishing to Production...."
deploy:
  stage: deploy
  needs: ["build-dev"]
  rules:
    - if: $CI_COMMIT_REF_NAME == $CI_DEFAULT_BRANCH
      needs: ["build-prod", "qa-checks"]
    - when: on_success # Run the job in other cases
  script: echo "Deploying application."
```
In the example above, the `deploy` job has the `build-dev` job as a dependency before it runs; however, when the commit branch is the project's default branch, its dependency changes to `build-prod` and `qa-checks`. This can allow for extra checks to be implemented based on the context.

### [rules:variables](https://developer.mozilla.org#rulesvariables)

In some situations, you may need only certain variables in specific conditions, or their values may change based on content. The rules:variables rule allows you to define variables when specific conditions are met, enabling the creation of more dynamic CI/CD execution workflows.

```
job:
  variables:
    DEPLOY_VERSION: "dev"
  rules:
    - if: $CI_COMMIT_REF_NAME == $CI_DEFAULT_BRANCH
      variables:
        DEPLOY_VERSION: "stable"
  script:
    - echo "Deploying $DEPLOY_VERSION version"
```
### [workflow:rules](https://developer.mozilla.org#workflowrules)

So far, we have looked at controlling when jobs run in a pipeline using the `rules` keyword. Sometimes, you want to control how the entire pipeline behaves: That's where [`workflow:rules`](https://docs.gitlab.com/ee/ci/yaml/#workflowrules) provides a powerful option. `workflow:rules` are evaluated before jobs and take precedence over the job rules. For example, if a job has rules allowing it to run on a specific branch, but the `workflow:rules` set jobs running on the branch to `when: never`, those jobs will not run.

All the features of `rules` mentioned in the previous sections also apply to `workflow:rules`.

```
workflow:
  rules:
    - if: $CI_PIPELINE_SOURCE == "schedule"
      when: never
    - if: $CI_PIPELINE_SOURCE == "push"
      when: never
    - when: always
```
In the example above, the CI/CD pipeline runs except when a schedule or push event is triggered.

## [Practical applications of GitLab CI/CD rules](https://developer.mozilla.org#practical_applications_of_gitlab_cicd_rules)

In the previous section, we looked at different ways of using the rules feature of GitLab CI/CD. In this section, let's explore some practical use cases.

### [Developer experience](https://developer.mozilla.org#developer_experience)

One of the advantages of a DevSecOps platform is that it enables developers to focus on what they do best: writing code while minimizing operational tasks. A company's DevOps or Platform team can create CI/CD templates for various stages of their development lifecycle and use rules to add CI/CD jobs to handle specific tasks based on their technology stack. A developer only needs to include a default CI/CD script, and pipelines are automatically created based on the files detected, refs used, or defined variables, leading to increased productivity.

### [Security and quality assurance](https://developer.mozilla.org#security_and_quality_assurance)

A major function of CI/CD pipelines is to be able to catch bugs or vulnerabilities before they are deployed into production infrastructure. Using CI/CD rules, security and quality assurance teams can dynamically run additional checks based on specific triggers. For example, malware scans can be added when unapproved file extensions are detected, or more advanced performance tests are automatically added when substantial changes are made to the codebase. With GitLab's built-in security, including security in your pipelines can be done with just a few lines of code.

```
include:
  # Static
  - template: Jobs/Container-Scanning.gitlab-ci.yml
  - template: Jobs/Dependency-Scanning.gitlab-ci.yml
  - template: Jobs/SAST.gitlab-ci.yml
  - template: Jobs/Secret-Detection.gitlab-ci.yml
  - template: Jobs/SAST-IaC.gitlab-ci.yml
  - template: Jobs/Code-Quality.gitlab-ci.yml
  - template: Security/Coverage-Fuzzing.gitlab-ci.yml
  # Dynamic
  - template: Security/DAST.latest.gitlab-ci.yml
  - template: Security/BAS.latest.gitlab-ci.yml
  - template: Security/DAST-API.latest.gitlab-ci.yml
  - template: API-Fuzzing.latest.gitlab-ci.yml
```
### [Automation](https://developer.mozilla.org#automation)

The power of GitLab's CI/CD rules shines through in the (nearly) limitless possibilities of automating your CI/CD pipelines. GitLab [AutoDevOps](https://docs.gitlab.com/ee/topics/autodevops/) is an example. It uses an opinionated best-practice collection of [GitLab CI/CD templates](https://gitlab.com/gitlab-org/gitlab/-/tree/master/lib/gitlab/ci/templates) and rules to detect the technology stack used. AutoDevOps creates relevant jobs that take your application all the way to production from a push. You can review the [AutoDevOps template](https://gitlab.com/gitlab-org/gitlab/-/blob/master/lib/gitlab/ci/templates/Auto-DevOps.gitlab-ci.yml) to learn how it leverages CI/CD rules for greater efficiency. [GitLab Duo](https://about.gitlab.com/gitlab-duo/) offers AI-powered workflows that help to simplify tasks and build secure software faster.

### [CI/CD component utilization](https://developer.mozilla.org#cicd_component_utilization)

Growth comes with several iterations and establishing best practices. While building CI/CD pipelines, your DevOps team likely created several CI/CD scripts that they repurpose across pipelines using the include keyword. With [GitLab 16](https://about.gitlab.com/releases/2023/05/22/gitlab-16-0-released/), GitLab introduced [CI/CD components](https://about.gitlab.com/releases/2023/05/22/gitlab-16-0-released/#cicd-components), an experimental feature that allows your team to create reusable CI/CD components and publish them as a catalog that can be used to build smarter CI/CD pipelines rapidly. You can learn more about [using CI/CD components](https://docs.gitlab.com/ee/ci/components/) and the [component catalog direction](https://about.gitlab.com/direction/verify/component_catalog/).

## [Conclusion](https://developer.mozilla.org#conclusion)

In this guide, we explored the different types of GitLab CI/CD pipelines, from understanding their basic structure to advanced configurations that enhance DevSecOps workflows. GitLab CI/CD enables you to run smarter pipelines by leveraging rules. It does so together with [GitLab Duo](https://about.gitlab.com/gitlab-duo/)'s AI-powered workflows
to help you build secure software fast. We encourage you to leverage these powerful features to optimize your DevSecOps initiatives.

*This is a sponsored article by GitLab. GitLab is a comprehensive web-based DevSecOps platform providing Git-repository management, issue-tracking, continuous integration, and deployment pipeline features. Available in both open-source and proprietary versions, it's designed to cover the entire DevOps lifecycle, making it a popular choice for teams looking for a single platform to manage both code and operational data.*
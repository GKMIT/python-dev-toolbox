
# Contributing Guidelines

Welcome! We're excited to have you contribute to this project. Even though this is an internal repository, we follow best practices from open-source development to ensure maintainability, collaboration, and transparency.

Below are guidelines to help you get started with contributing effectively.

---

## 📋 Table of Contents

1. [Getting Started](#getting-started)
2. [Code of Conduct](#code-of-conduct)
3. [How to Contribute](#how-to-contribute)
4. [Branching Strategy](#branching-strategy)
5. [Commit Message Guidelines](#commit-message-guidelines)
6. [Pull Request Process](#pull-request-process)
7. [Coding Standards](#coding-standards)
8. [Issue Tracking](#issue-tracking)
9. [Documentation](#documentation)
10. [Review and Approval](#review-and-approval)
11. [FAQ](#faq)

---

## ✅ Getting Started

- Fork the repository (if external).
- Clone the repository locally:

  ````bash
  git clone https://github.com/GKMIT/python-dev-toolbox.git
  cd your-repo
  ````
* Set up the project locally following the instructions in the `README.md`.

---

## 🧠 Code of Conduct

We follow a respectful, inclusive, and harassment-free environment. All contributors are expected to adhere to our [Code of Conduct](CODE_OF_CONDUCT.md).

---

## 🤝 How to Contribute

There are multiple ways you can contribute:

* Reporting bugs
* Suggesting features or improvements
* Fixing issues
* Improving documentation
* Writing tests

Feel free to open a discussion or raise an issue before you start a major contribution.

---

## 🌱 Branching Strategy

We use the following branching model:

* `main`: Stable production-ready code.
* `dev`: Active development happens here.
* `feature/xyz`: New features.
* `bugfix/xyz`: Bug fixes.
* `docs/xyz`: Documentation updates.

Create your branch from `dev` unless advised otherwise.

---

## ✍️ Commit Message Guidelines

Use clear, concise commit messages. We follow a format similar to [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/):

````
<type>(<scope>): <subject>
````

**Types:**

* `feat`: New feature
* `fix`: Bug fix
* `docs`: Documentation change
* `refactor`: Code change that neither fixes a bug nor adds a feature
* `test`: Adding missing tests
* `chore`: Maintenance task

**Examples:**

````
feat(auth): add JWT support
fix(api): handle null payloads in response
````

---

## 🔃 Pull Request Process

1. Ensure your branch is up to date with `main`.
2. Create a pull request (PR) to merge into `main`.
3. Follow the PR template and clearly describe what’s being changed.
4. Link any related issue or ticket.
5. Assign reviewers from the team.

**PR Tips:**

* Keep your PR focused and small.
* Avoid mixing unrelated changes.
* Ensure tests pass and code lints correctly.

---

## 🎯 Coding Standards

* Follow the coding style of the project (PEP8 for Python).
* Use linters and formatters where configured.
* Write tests for new logic or features.
* Ensure backward compatibility unless otherwise planned.

---

## 🐛 Issue Tracking

* Use the [Issues](../../issues) tab to report bugs or suggest enhancements.
* Tag issues properly (`bug`, `enhancement`, `question`, etc.).
* Assign or self-assign issues to avoid duplication of work.

---

## 📚 Documentation

* Keep the `README.md` and other relevant docs updated.
* Document new features, APIs, or architectural decisions.
* If adding a new script or tool, include usage examples.

---

## ✅ Review and Approval

* At least 1–2 code reviews are required before merging.
* Discuss any large architectural changes in advance.
* Once approved, squash & merge your PRs unless otherwise instructed.

---

## ❓ FAQ

**Q: Can I work on more than one issue?**
A: Yes, but keep each change in its own branch and PR.

**Q: Who can approve PRs?**
A: Maintainers or team leads. See the `CODEOWNERS` file if applicable.

**Q: What if I’m stuck?**
A: Don’t hesitate to ask in the team channel or leave a comment in the issue or PR.

---

## 🙌 Thanks for contributing!

Let’s build something great together!

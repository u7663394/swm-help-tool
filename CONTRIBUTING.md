# Contributing to swm-help-tool

First off, thank you for considering contributing to **swm-help-tool**! Your help is greatly appreciated and will make this project better for everyone.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
  - [Reporting Bugs](#reporting-bugs)
  - [Suggesting Enhancements](#suggesting-enhancements)
  - [Submitting Pull Requests](#submitting-pull-requests)
- [Development Setup](#development-setup)
- [Coding Guidelines](#coding-guidelines)
- [Style Guide](#style-guide)
- [Acknowledgements](#acknowledgements)

## Code of Conduct

Please note that this project is released with a [Contributor Code of Conduct](CODE_OF_CONDUCT.md). By participating in this project you agree to abide by its terms.

## How Can I Contribute?

### Reporting Bugs

If you find a bug in **swm-help-tool**, please [open an issue](https://github.com/u7663394/swm-help-tool/issues) with detailed information about the problem. Include steps to reproduce the bug, expected behavior, and any relevant screenshots or logs.

### Suggesting Enhancements

Have an idea to improve **swm-help-tool**? We’d love to hear it! Please [open an issue](https://github.com/u7663394/swm-help-tool/issues) to discuss your suggestion. Be as detailed as possible to help us understand the value and implementation of your idea.

### Submitting Pull Requests

Pull requests are welcome! Here’s how to get started:

1. **Fork the Repository**: Click the fork button at the top right of the repository page.
2. **Clone Your Fork**:
    ```bash
    git clone https://github.com/your-username/swm-help-tool.git
    cd swm-help-tool
    ```
3. **Create a Branch**:
    ```bash
    git checkout -b feature/your-feature-name
    ```
4. **Make Your Changes**: Implement your feature or fix.
5. **Commit Your Changes**:
    ```bash
    git commit -m "Add feature: your feature description"
    ```
6. **Push to Your Fork**:
    ```bash
    git push origin feature/your-feature-name
    ```
7. **Open a Pull Request**: Navigate to the original repository and create a pull request from your fork.

Please ensure your pull request follows the [Coding Guidelines](#coding-guidelines) and includes relevant tests.

## Development Setup

To set up the development environment, follow these steps:

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/u7663394/swm-help-tool.git
    cd swm-help-tool
    ```
2. **Create a Virtual Environment** (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```
3. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
4. **Run Tests** (if applicable):
    ```bash
    pytest
    ```

## Coding Guidelines

- **Write Clean Code**: Follow Python best practices for writing clean and readable code.
- **Documentation**: Document your code where necessary. Update the README and other documentation if your changes affect them.
- **Testing**: Include tests for new features and ensure existing tests pass.

## Style Guide

This project adheres to the [PEP 8](https://pep8.org/) style guide. Please ensure your code follows these guidelines. You can use tools like `flake8` or `black` to help maintain consistency.

## Acknowledgements

- **Guochen Wang** for developing and maintaining the project.
- [PyAutoGUI](https://pyautogui.readthedocs.io/) and [Keyboard](https://keyboard.readthedocs.io/) for providing the necessary libraries to automate tasks.

Thank you for your interest in contributing to **swm-help-tool**! Together, we can make the Shawarma Legend gaming experience even better.


# Shawarma Legend Game Assistant

## Introduction

`swm-help-tool` is a game automation script specifically designed for **Shawarma Legend**. By automating tasks such as resource collection and material preparation, it enhances the gaming experience by increasing efficiency and reducing manual effort.

## Author

Developed and maintained by **Guochen Wang**.

## Features

- **Automated Resource Collection**: Automatically collects various in-game materials like cucumbers, salt, juice, and sweet potatoes.
- **Intelligent Inventory Management**: Monitors and updates inventory in real-time to ensure sufficient materials.
- **Automated Cutting Operations**: Simulates mouse actions to automatically cut potatoes and meat, improving efficiency.
- **Highly Customizable**: Users can adjust script parameters to suit different game requirements.
- **Pre-configured Hotkeys**: During the game, the following hotkeys can be used for various automated tasks:
  1. Press `1` to start pre-preparation tasks.
  2. Press `2` to automatically make a shawarma.
  3. Press `3` to automatically add meat.
  4. Press `4` to automatically add other ingredients.

## Usage

Once installed, simply run the script, and use the pre-configured hotkeys during gameplay to automate your tasks as described in the **Features** section.

## Installation

Ensure you have Python installed along with the necessary dependencies. Then, clone this repository and install the dependencies:

```bash
git clone https://github.com/u7663394/swm-help-tool.git
cd swm-help-tool
pip install pyautogui keyboard

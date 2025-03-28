# Proof-of-Concept - Expressing cybersecurity standards in OSCAL Format

This PoC demonstrates how to express cybersecurity-related information using the **OSCAL** format.

## Goals Checklist

- [ ] Convert a control of cybersecurity standard (e.g., CSA Safe App Standard) into an **OSCAL catalog model**.
- [ ] Express it as a **markdown document**.

## Setup Instructions

Follow these steps to set up and build the repository:

1. **Open PowerShell as Administrator**

    Run the following command to allow scripts to run:

    ```powershell
    Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
    ```

2. **Configure VS Code for Microsoft C++**
   - Open the **Visual Studio Installer**
   - Check the option **Desktop Development with C++** and install.

3. **Create and Activate a Virtual Environment**:
   - Open **Visual Studio Code** (VSC)
   - Create a new directory
   - Open a new terminal, navigate to the previously created directory 
   - Create a new virtual environment and activate

    ```bash
    python -m venv venv.trestle
    (venv.trestle) .\venv\Scripts\Activate
    ```

4. **Upgrade/Install dependencies**

     ```bash
     (venv.trestle) pip install --upgrade pip
     (venv.trestle) pip install compliance-trestle
     ```

7. **Initialise a OSCAL compatible project**

     ```bash
     (venv.trestle) trestle init
     ```

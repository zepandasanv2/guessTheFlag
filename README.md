# Project Setup Guide

## 📌 Virtual Environment Setup

To keep dependencies isolated, it's recommended to use a virtual environment. Follow these steps:

### **1. Create a Virtual Environment**
Run the following command in the project's root directory:

```bash
python -m venv venv
```

### **2. Activate the Virtual Environment**
- **Windows (CMD)**:
  ```bash
  venv\Scripts\activate.bat
  ```
- **Windows (PowerShell)**:
  ```powershell
  venv\Scripts\Activate
  ```
- **macOS/Linux**:
  ```bash
  source venv/bin/activate
  ```

If the virtual environment is activated, you should see `(venv)` at the beginning of the terminal prompt.

---

## 📌 Installing Dependencies

To install the required dependencies, run:

```bash
pip install -r requirements.txt
```

This will install all the packages listed in `requirements.txt`.

---

## 📌 Updating `requirements.txt`

If you install new dependencies, update the `requirements.txt` file by running:

```bash
pip freeze > requirements.txt
```

Commit the updated file to keep dependencies in sync:

```bash
git add requirements.txt
git commit -m "Updated dependencies"
```

---

## 📌 Deactivating the Virtual Environment

Once done, deactivate the virtual environment with:

```bash
deactivate
```

---

## 📌 Troubleshooting

- If `pip` is not recognized, ensure Python is installed and added to the system PATH.
- If activation fails in PowerShell, try running:

  ```powershell
  Set-ExecutionPolicy Unrestricted -Scope Process
  ```

---

### 🚀 Now you're ready to use this project!


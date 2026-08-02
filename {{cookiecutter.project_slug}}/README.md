# Speaker Backend

## Prerequisites

Before getting started, install the following:

- Python 3.12+
- Docker Desktop
- Git
- `just` (command runner)

---

# 1. Install `just`

`just` is used to simplify common development commands.

### Windows (Winget)

```powershell
winget install Casey.Just
```

Or with Chocolatey:

```powershell
choco install just
```

### macOS

```bash
brew install just
```

### Linux

#### Debian / Ubuntu

```bash
sudo apt update
sudo apt install just
```

If your distribution doesn't provide a recent version:

```bash
cargo install just
```

Verify the installation:

```bash
just --version
```

---

# 2. Clone the project

```bash
git clone -b <branch-name> <repository-url>
cd sbc_speaker
```

---

# 3. Create a Python virtual environment (Optional)

A virtual environment is recommended if you want to run Python tools locally.

### Using Python

```bash
python -m venv .venv
```

Activate it:

**Windows**

```powershell
.venv\Scripts\activate
```

**Linux / macOS**

```bash
source .venv/bin/activate
```

### Or using UV

```bash
uv init
uv venv
```

Activate it the same way as above.

> **Note:** The application itself runs inside Docker. The virtual environment is only needed for local tooling.

---

# 4. Build the Docker images (First time only)

```bash
just build
```

---

# 5. Start the development environment

```bash
just up
```

---

# 6. Initialize the database (First time only)

```bash
just migrate
just superuser
```

---

# 7. When you change models

Create new migrations:

```bash
just makemigrations
```

Apply them:

```bash
just migrate
```

---

# Common Commands

| Command | Description |
|---------|-------------|
| `just build` | Build Docker images |
| `just up` | Start all services |
| `just down` | Stop all services |
| `just clean` | Stop services and remove Docker volumes (deletes database data) |
| `just logs` | View application logs |
| `just makemigrations` | Generate Django migrations |
| `just migrate` | Apply database migrations |
| `just superuser` | Create a Django superuser |
| `just shell` | Open the Django shell |
| `just collectstatic` | Collect static files |

---

# Typical Development Workflow

Start the application:

```bash
just up
```

After modifying Django models:

```bash
just makemigrations
just migrate
```

Stop the application:

```bash
just down
```

Reset the local database completely:

```bash
just clean
just up
just migrate
```
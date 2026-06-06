# Edge AI Architecture

```text
                           +------------------+
                           |     FastAPI      |
                           +------------------+
                                     |
                +--------------------+--------------------+
                |                                         |
      +-------------------+                  +-------------------+
      |    Health API     |                  |    Analyze API    |
      +-------------------+                  +-------------------+
                |                                         |
                +--------------------+--------------------+
                                     |
                     +--------------------------------+
                     |        AI Orchestrator         |
                     +--------------------------------+
                                     |
      -----------------------------------------------------------------
      |                  |                  |               |           |
+-------------+   +-------------+   +-------------+  +-------------+  +-------------+
|   Camera    |   | Face Detect |   | Mask Detect |  | Helmet Det. |  |  Liveness   |
+-------------+   +-------------+   +-------------+  +-------------+  +-------------+
                                     |
                                     v
                     +--------------------------------+
                     |       Event Generator          |
                     +--------------------------------+
                                     |
                                     v
                     +--------------------------------+
                     |      Future ASP.NET API        |
                     +--------------------------------+
                                     |
                                     v
                     +--------------------------------+
                     |       React Dashboard          |
                     +--------------------------------+
```

---

## Component Flow

### 1. FastAPI

* Entry point for all requests.
* Hosts Health API and Analyze API.

### 2. Health API

* Service status monitoring.
* Returns application and AI module health.

### 3. Analyze API

* Accepts images/video frames.
* Sends requests to the AI Orchestrator.

### 4. AI Orchestrator

* Central controller for AI pipelines.
* Manages execution of multiple AI models.

### 5. AI Modules

* **Camera** – Frame acquisition.
* **Face Detection** – Detects human faces.
* **Mask Detection** – Checks mask compliance.
* **Helmet Detection** – Verifies helmet usage.
* **Liveness Detection** – Prevents spoofing using photos/videos.

### 6. Event Generator

* Consolidates AI results.
* Creates structured events with timestamps and confidence scores.

### 7. Future ASP.NET API

* Receives events from the AI service.
* Stores data in the database.
* Provides APIs for reporting and integrations.

### 8. React Dashboard

* Displays live events.
* Shows analytics and historical reports.
* Provides monitoring and administration interface.

---

## Overall Workflow

```text
Camera/Image
      │
      ▼
FastAPI Analyze API
      │
      ▼
AI Orchestrator
      │
      ├── Face Detection
      ├── Mask Detection
      ├── Helmet Detection
      └── Liveness Detection
      │
      ▼
Event Generator
      │
      ▼
ASP.NET API
      │
      ▼
Database
      │
      ▼
React Dashboard
```


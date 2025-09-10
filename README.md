# AI Learning Support Tool (Prototype)
**Purpose:** Prototype web tool to help teachers & parents identify learning difficulties and generate personalized recommendations (stories, games, exercises).

**Highlights**
- Lightweight FastAPI backend (Python)
- Simple static frontend (HTML + JS)
- Local SQLite DB for saving child progress (optional)
- Ready to run locally or in Docker

---

## Architecture (high-level)
mermaid
flowchart TD
  Parent/Teacher-->UI(Frontend(HTML/JS))
  UI-->API(Backend)
  API-->Database

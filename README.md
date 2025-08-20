# Cloud Security Compliance Dashboard & Automation Toolkit

A showcase project for Security Analyst job applications. This project demonstrates a cloud security compliance dashboard and automation toolkit using mock data (no real credentials or sensitive information).

## Features
- FastAPI backend with endpoints for compliance reports
- Mock data for AWS, Azure, and GCP services
- Ready for frontend integration (React, Vue, or plain HTML/JS)

## Backend Quickstart
1. Navigate to the backend directory:
   ```powershell
   cd "Personal Projects\Active Projects\Could Security Compliance Dashboard and Automation Toolkit\backend"
   ```
2. Install dependencies:
   ```powershell
   pip install -r requirements.txt
   ```
3. Run the FastAPI server:
   ```powershell
   uvicorn main:app --reload
   ```
4. Visit [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) for the interactive API docs.

## Frontend
- The `frontend` folder is ready for your dashboard UI code.
- Fetch data from `/api/compliance` and display it in a dashboard.

## Why Mock Data?
- This project is designed for job applications and portfolio use.
- No real cloud credentials or sensitive data are used.

## Example API Endpoints
- `GET /api/compliance` — List all compliance reports
- `GET /api/compliance/{report_id}` — Get details for a specific report

---

*Feel free to expand this project with more endpoints, automation scripts, or a frontend dashboard!*

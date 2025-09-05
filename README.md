# Cloud Security Compliance Dashboard and Automation Toolkit

## Overview
This project provides a dashboard and automation toolkit for monitoring and managing cloud security compliance. It includes a FastAPI backend and a simple JavaScript frontend.

## Structure
- `Backend/`: FastAPI backend API
- `Frontend/`: Dashboard web interface

## Backend Setup
1. Navigate to the `Backend` folder.
2. Install dependencies:
	```sh
	pip install -r requirements.txt
	```
3. Run the API server:
	```sh
	uvicorn main:app --reload
	```

## Frontend Setup
1. Navigate to the `Frontend` folder.
2. Open `index.html` in your web browser.
3. The dashboard will fetch and display compliance results from the backend.

## Usage
- View compliance checks and reports in the dashboard.
- Backend API endpoints can be extended for automation and integrations.

## Troubleshooting
- Ensure the backend is running and accessible at `http://localhost:8000`.
- Check browser console and backend logs for errors.

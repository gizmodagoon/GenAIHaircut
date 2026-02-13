# GenAI Haircut Tracker

GenAI Haircut Tracker is a web application that helps clients and barbers track haircut histories, share photos, and receive AI-generated feedback. Clients can upload photos of their haircuts, tag styles and barbers, see trends over time, and share with friends. Barbers can maintain portfolios, get insights on consistency and quality, and build a verified public profile. This project uses React and TypeScript for the web interface, with plans to integrate AI-driven image analysis and recommendations in future phases.

## Prerequisites

- [Node.js](https://nodejs.org/) (v20.19+ or v22.12+)
- npm (included with Node.js)

## Local Development Setup

1. **Install dependencies**

   ```bash
   cd frontend
   npm install
   ```

2. **Configure environment variables (optional)**

   Create a `.env` file in the `frontend/` directory to override defaults:

   ```env
   VITE_API_URL=http://localhost:8000
   ```

   If omitted, the app defaults to `http://localhost:8000`.

3. **Start the development server**

   ```bash
   npm run dev
   ```

   The app will be available at [http://localhost:5173](http://localhost:5173).

4. **Start the backend**

   The frontend expects the FastAPI backend to be running. From the `backend/` directory:

   ```bash
   pip install -r requirements.txt
   uvicorn api.main:app --reload
   ```

   The API will be available at [http://localhost:8000](http://localhost:8000).

## Available Scripts

| Command           | Description                        |
| ----------------- | ---------------------------------- |
| `npm run dev`     | Start the Vite development server  |
| `npm run build`   | Type-check and build for production|
| `npm run preview` | Preview the production build       |
| `npm run lint`    | Run ESLint                         |

# AGENTS.md

## Project overview

This repository contains a small web application for tracking home electricity meter readings, usage history, and monthly consumption forecasts.

The app is based on an existing Excel workbook that already contains the core formulas for:

- electricity usage calculation,
- daily average consumption,
- monthly/period forecast,
- estimated electricity bill,
- historical billing period analysis.

The goal is not to recreate Excel in the browser. The goal is to extract the useful business logic from the spreadsheet and move it into a clean, testable web application.

---

## Main product goal

The user should be able to:

1. View historical electricity usage.
2. Add a new electricity meter reading.
3. See current usage in the active billing period.
4. See a forecast for the end of the billing period.
5. See an estimated electricity bill.
6. Later: edit tariffs and compare historical periods.

---

## Preferred tech stack

Use this stack unless explicitly asked otherwise:

### Backend

- Python
- FastAPI
- Pydantic
- SQLAlchemy
- Alembic
- SQLite for MVP
- PostgreSQL later if needed
- Pytest for tests

### Frontend

- React
- TypeScript
- Vite
- Simple component-based architecture
- Prefer clean, minimal UI
- Charts can be added later with Recharts

### Deployment / local dev

- Docker Compose
- `.env` configuration
- Keep local development simple

---

## Project structure

Expected structure:

```text
electricity-usage-tracker/
  backend/
    app/
      main.py
      domain/
        forecast.py
        billing.py
      routers/
        readings.py
        forecast.py
        tariffs.py
      db/
        database.py
      models/
        reading.py
        billing_period.py
        tariff.py
      schemas/
        reading.py
        forecast.py
        tariff.py
    tests/
      test_forecast.py
      test_billing.py

  frontend/
    src/
      api/
        client.ts
      components/
        dashboard/
          DashboardCards.tsx
          ForecastChart.tsx
        readings/
          ReadingForm.tsx
          ReadingsTable.tsx
      pages/
      types/
        forecast.ts
        reading.ts

  docs/
    excel-mapping.md
    mvp-plan.md

  scripts/
    import_excel_data.py
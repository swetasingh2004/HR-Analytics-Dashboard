# HR Analytics Dashboard

A portfolio-ready HR analytics project that turns employee-level data into practical insights about workforce composition, performance, attendance, attrition, and compensation.

## What is included

- Interactive, browser-based dashboard (no paid BI license required)
- Reproducible sample dataset with 60 employee records
- SQL schema, inserts, KPI queries, and analysis views
- HR Analytics Report (PDF)
- GitHub Pages deployment instructions

## Dashboard preview

Open `dashboard/index.html` in a browser, or publish the repository with GitHub Pages. Use the department, location, and employment-status filters to recalculate all KPIs and charts.

### KPIs

| KPI | Definition |
| --- | --- |
| Headcount | Employees matching the selected filters |
| Attrition rate | Terminated employees / all employees |
| Average performance | Mean rating on a 1-5 scale |
| Average attendance | Mean attendance percentage |
| Average salary | Mean annual salary |

## Quick start

1. Fork or upload this folder to a new GitHub repository.
2. Open `dashboard/index.html` locally, or enable **Settings -> Pages -> Deploy from a branch**, then select your default branch and `/ (root)`.
3. Import `data/hr_employee_data.csv` into Power BI/Tableau if a native BI submission is also required. The included SQL scripts create the same model in PostgreSQL.

## Repository structure

```
dashboard/       Interactive dashboard source (HTML, CSS, JavaScript)
data/            Sample HR employee dataset and data dictionary
sql/             PostgreSQL schema, seed data, and analytics queries
reports/         Submission-ready HR Analytics Report PDF
docs/            Dashboard screenshots and implementation notes
```

## Tech stack

HTML5, CSS3, JavaScript, Chart.js, PostgreSQL-compatible SQL, and ReportLab.

## Data notes

The included employee records are synthetic and exist only for demonstration. Do not treat the metrics as facts about a real organization. For real HR data, restrict access, remove direct identifiers, define metric ownership, and validate join dates, termination dates, and leave rules before publishing.

## SQL setup

Run the scripts in this order:

```sql
\i sql/01_schema.sql
\i sql/02_seed_data.sql
\i sql/03_analytics_queries.sql
```

The `03_analytics_queries.sql` file includes reusable views for workforce KPIs, attrition, attendance risk, salary benchmarking, and employee detail.

## Suggested screenshots for your submission

1. Dashboard overview with all filters set to All.
2. Attrition and attendance charts.
3. Salary versus performance scatter chart.
4. Employee insight table after selecting a department.

## Author
Name:Sweta Singh
Kinetrexa Software Privale Limited
Data Ananlytics Intern


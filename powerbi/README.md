# Power BI / Tableau Build Guide

The runnable dashboard in `dashboard/` is the project’s interactive dashboard deliverable. If your internship reviewer specifically asks for a Power BI or Tableau file, use this guide to reproduce the same design in under 20 minutes.

## Power BI Desktop

1. Select **Get Data -> Text/CSV** and choose `../data/hr_employee_data.csv`.
2. Ensure `monthly_salary`, `attendance_pct`, `performance_rating`, `engagement_score`, `overtime_hours`, and `training_hours` are numeric. Ensure `hire_date` is a date.
3. Create these measures:

```DAX
Headcount = COUNTROWS('hr_employee_data')
Active Headcount = CALCULATE([Headcount], 'hr_employee_data'[employment_status] = "Active")
Attrition Count = CALCULATE([Headcount], 'hr_employee_data'[attrition] = "Yes")
Attrition Rate = DIVIDE([Attrition Count], [Headcount], 0)
Average Performance = AVERAGE('hr_employee_data'[performance_rating])
Average Attendance = AVERAGE('hr_employee_data'[attendance_pct])
Average Monthly Salary = AVERAGE('hr_employee_data'[monthly_salary])
```

4. Add slicers for `department`, `location`, and `employment_status`.
5. Add cards for the six measures above. Use a clustered column chart for attrition rate by department, donut chart for headcount by department, column chart for attendance bands, scatter chart for monthly salary vs performance, and a detailed table.
6. Apply a navy (`#102A43`), blue (`#1976D2`), teal (`#00A6A6`), and coral (`#E65B64`) palette. Save as `HR_Analytics_Dashboard.pbix` and add it to the repository if your file size permits.

## Tableau Public

1. Connect to `../data/hr_employee_data.csv`.
2. Create calculated fields for Attrition Rate, Attendance Risk, and Average Salary with the same definitions as the SQL layer.
3. Assemble the five KPI cards and four charts described above on a 1366 x 768 dashboard.
4. Publish to Tableau Public and add the public URL to the main README.

## Important submission note

The data is synthetic. Label the dashboard as a portfolio prototype and never upload actual employee-level information to a public repository or Tableau Public.

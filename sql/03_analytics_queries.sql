-- Workforce KPI view
CREATE OR REPLACE VIEW vw_workforce_kpis AS
SELECT
    COUNT(*) AS total_headcount,
    COUNT(*) FILTER (WHERE employment_status = 'Active') AS active_headcount,
    ROUND(100.0 * COUNT(*) FILTER (WHERE attrition = 'Yes') / NULLIF(COUNT(*), 0), 2) AS attrition_rate_pct,
    ROUND(AVG(performance_rating), 2) AS avg_performance_rating,
    ROUND(AVG(attendance_pct), 2) AS avg_attendance_pct,
    ROUND(AVG(monthly_salary), 2) AS avg_monthly_salary
FROM employees;

-- Attrition by department and location
SELECT department, location, COUNT(*) AS employees,
       COUNT(*) FILTER (WHERE attrition = 'Yes') AS exits,
       ROUND(100.0 * COUNT(*) FILTER (WHERE attrition = 'Yes') / COUNT(*), 2) AS attrition_rate_pct
FROM employees GROUP BY department, location ORDER BY attrition_rate_pct DESC;

-- Attendance risk list for HR intervention
SELECT employee_id, department, job_role, attendance_pct, overtime_hours, engagement_score
FROM employees
WHERE employment_status = 'Active' AND attendance_pct < 92
ORDER BY attendance_pct ASC, overtime_hours DESC;

-- Salary benchmark by department
SELECT department, COUNT(*) AS headcount, ROUND(AVG(monthly_salary), 0) AS avg_monthly_salary,
       ROUND(MIN(monthly_salary), 0) AS min_salary, ROUND(MAX(monthly_salary), 0) AS max_salary,
       ROUND(AVG(performance_rating), 2) AS avg_performance
FROM employees GROUP BY department ORDER BY avg_monthly_salary DESC;

-- Employee-level semantic layer for Power BI/Tableau
CREATE OR REPLACE VIEW vw_employee_analytics AS
SELECT *,
       CASE WHEN attendance_pct < 92 THEN 'High Risk'
            WHEN attendance_pct < 95 THEN 'Watch' ELSE 'Healthy' END AS attendance_risk,
       CASE WHEN engagement_score < 6.5 THEN 'Low'
            WHEN engagement_score < 8 THEN 'Medium' ELSE 'High' END AS engagement_band,
       EXTRACT(YEAR FROM AGE(CURRENT_DATE, hire_date)) AS tenure_years
FROM employees;

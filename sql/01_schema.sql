DROP TABLE IF EXISTS employees;

CREATE TABLE employees (
    employee_id VARCHAR(12) PRIMARY KEY,
    department VARCHAR(50) NOT NULL,
    job_role VARCHAR(80) NOT NULL,
    location VARCHAR(50) NOT NULL,
    gender VARCHAR(20) NOT NULL,
    age INTEGER CHECK (age BETWEEN 18 AND 70),
    hire_date DATE NOT NULL,
    employment_status VARCHAR(20) NOT NULL CHECK (employment_status IN ('Active', 'Terminated')),
    attrition VARCHAR(3) NOT NULL CHECK (attrition IN ('Yes', 'No')),
    performance_rating NUMERIC(2,1) CHECK (performance_rating BETWEEN 1 AND 5),
    attendance_pct NUMERIC(5,2) CHECK (attendance_pct BETWEEN 0 AND 100),
    monthly_salary NUMERIC(12,2) CHECK (monthly_salary >= 0),
    overtime_hours NUMERIC(6,1) CHECK (overtime_hours >= 0),
    training_hours NUMERIC(6,1) CHECK (training_hours >= 0),
    engagement_score NUMERIC(3,1) CHECK (engagement_score BETWEEN 1 AND 10)
);

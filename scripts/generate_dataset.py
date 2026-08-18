"""Generate reproducible synthetic employee records for the HR dashboard."""
import csv, os

headers = ['employee_id','department','job_role','location','gender','age','hire_date','employment_status','attrition','performance_rating','attendance_pct','monthly_salary','overtime_hours','training_hours','engagement_score']
base = [
['EMP-1001','Technology','Data Analyst','Bengaluru','Female',29,'2021-06-14','Active','No',4.4,96.4,78000,12,28,8.2],['EMP-1002','Sales','Sales Executive','Mumbai','Male',34,'2019-03-22','Active','No',3.8,94.1,65000,22,18,7.1],['EMP-1003','Human Resources','HR Specialist','Delhi','Female',31,'2020-08-08','Active','No',4.1,97.3,72000,6,34,8.6],['EMP-1004','Finance','Financial Analyst','Bengaluru','Male',27,'2022-01-17','Terminated','Yes',3.2,89.6,69000,18,12,5.8],['EMP-1005','Operations','Operations Manager','Pune','Female',39,'2017-09-04','Active','No',4.5,97.8,98000,14,42,8.8],['EMP-1006','Technology','Software Engineer','Hyderabad','Male',26,'2022-06-11','Active','No',4.0,95.5,85000,16,31,7.9],['EMP-1007','Sales','Account Manager','Delhi','Female',30,'2020-04-15','Terminated','Yes',3.1,90.2,71000,25,16,5.9],['EMP-1008','Marketing','Content Strategist','Mumbai','Female',28,'2021-11-09','Active','No',4.2,96.8,68000,9,26,8.3],['EMP-1009','Operations','Supply Chain Analyst','Pune','Male',32,'2018-07-19','Active','No',3.9,93.7,74000,19,22,7.0],['EMP-1010','Finance','Accountant','Delhi','Female',36,'2016-02-27','Active','No',4.3,98.1,82000,5,38,8.7],['EMP-1011','Technology','Product Manager','Bengaluru','Female',35,'2018-10-12','Active','No',4.6,97.0,125000,11,45,9.0],['EMP-1012','Sales','Sales Executive','Hyderabad','Male',24,'2023-02-01','Terminated','Yes',2.9,88.9,54000,28,10,5.2],['EMP-1013','Human Resources','Recruiter','Pune','Male',29,'2021-05-23','Active','No',3.7,95.9,61000,8,29,7.6],['EMP-1014','Marketing','Marketing Manager','Bengaluru','Female',38,'2017-04-30','Active','No',4.4,96.7,110000,10,40,8.9],['EMP-1015','Operations','Quality Analyst','Mumbai','Male',27,'2022-08-18','Active','No',3.6,92.8,58000,21,20,6.8],['EMP-1016','Technology','UX Designer','Delhi','Female',30,'2020-01-09','Active','No',4.1,95.2,88000,13,33,8.1],['EMP-1017','Finance','Financial Analyst','Hyderabad','Male',33,'2019-11-26','Terminated','Yes',3.0,91.1,76000,20,15,5.7],['EMP-1018','Sales','Account Manager','Mumbai','Female',31,'2019-06-17','Active','No',4.0,94.9,79000,17,24,7.5],['EMP-1019','Human Resources','HR Manager','Bengaluru','Female',42,'2015-03-08','Active','No',4.5,98.4,118000,4,48,9.1],['EMP-1020','Marketing','SEO Analyst','Pune','Male',25,'2022-04-02','Active','No',3.8,93.5,56000,15,19,7.2]]
rows = list(base)
for n in range(40):
    r = list(base[n % len(base)]); r[0] = f'EMP-{1021+n}'; r[5] = max(22, r[5] + n % 5 - 2); r[9] = round(min(5,max(2.5,r[9]+(n%4-1.5)*.15)),1); r[10] = round(min(99.5,max(86,r[10]+(n%6-2.5)*.8)),1); r[11] += (n%7)*2500; r[8] = 'Yes' if n%11==0 else 'No'; r[7] = 'Terminated' if n%11==0 else 'Active'; r[14] = round(min(9.8,max(4.5,r[14]+(n%5-2)*.2)),1); rows.append(r)
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
with open(os.path.join(root,'data','hr_employee_data.csv'),'w',newline='',encoding='utf-8') as f:
    writer=csv.writer(f); writer.writerow(headers); writer.writerows(rows)
with open(os.path.join(root,'sql','02_seed_data.sql'),'w',encoding='utf-8') as f:
    f.write('-- Generated from data/hr_employee_data.csv; synthetic data only.\nINSERT INTO employees ('+','.join(headers)+') VALUES\n')
    values=[]
    for r in rows:
        values.append('('+','.join("'"+str(v).replace("'","''")+"'" if isinstance(v,str) else str(v) for v in r)+')')
    f.write(',\n'.join(values)+';\n')
print(f'Generated {len(rows)} records.')

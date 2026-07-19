USE adherence;

-- Total Patients
SELECT COUNT(DISTINCT patient_id) AS Total_Patients
FROM dim_patients;

-- Patients by Insurance Type
SELECT insurance_type,
COUNT(*) AS Total_Patients
FROM dim_patients
GROUP BY insurance_type
ORDER BY Total_Patients DESC;

-- Prescriptions by Drug Class
SELECT drug_class,
COUNT(*) AS Total_Prescriptions
FROM fact_prescriptions
GROUP BY drug_class
ORDER BY Total_Prescriptions DESC;

-- Average Days Supply
SELECT AVG(days_supply) AS Average_Days_Supply
FROM fact_prescriptions;

-- Total Refills by Prescription
SELECT prescription_id,
COUNT(*) AS Total_Refills
FROM fact_refills
GROUP BY prescription_id
ORDER BY Total_Refills DESC;

-- Doctor Performance
SELECT
doctor_specialty,
COUNT(*) AS Prescriptions
FROM fact_prescriptions fp
JOIN dim_doctors dd
ON fp.doctor_id = dd.doctor_id
GROUP BY doctor_specialty
ORDER BY Prescriptions DESC;

-- Flattened Dataset for Machine Learning
SELECT
p.patient_id,
p.age,
p.gender,
p.region,
p.insurance_type,
d.doctor_specialty,
d.prescribing_channel,
pr.drug_class,
pr.days_supply,
COUNT(r.refill_id) AS total_fills,
AVG(r.days_supply_per_fill) AS days_supply_per_fill
FROM dim_patients p
JOIN fact_prescriptions pr
ON p.patient_id = pr.patient_id
JOIN dim_doctors d
ON pr.doctor_id = d.doctor_id
LEFT JOIN fact_refills r
ON pr.prescription_id = r.prescription_id
GROUP BY
p.patient_id,
p.age,
p.gender,
p.region,
p.insurance_type,
d.doctor_specialty,
d.prescribing_channel,
pr.drug_class,
pr.days_supply;

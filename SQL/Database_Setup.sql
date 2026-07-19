CREATE DATABASE adherence;

USE adherence;

CREATE TABLE dim_patients (
    patient_id INT PRIMARY KEY,
    age INT,
    gender VARCHAR(10),
    region VARCHAR(50),
    insurance_type VARCHAR(50)
);

CREATE TABLE dim_doctors (
    doctor_id INT PRIMARY KEY,
    doctor_specialty VARCHAR(100),
    prescribing_channel VARCHAR(50)
);

CREATE TABLE fact_prescriptions (
    prescription_id INT PRIMARY KEY,
    patient_id INT,
    doctor_id INT,
    drug_class VARCHAR(100),
    prescription_date DATE,
    days_supply INT,
    FOREIGN KEY (patient_id) REFERENCES dim_patients(patient_id),
    FOREIGN KEY (doctor_id) REFERENCES dim_doctors(doctor_id)
);

CREATE TABLE fact_refills (
    refill_id INT PRIMARY KEY,
    prescription_id INT,
    refill_number INT,
    refill_date DATE,
    days_supply_per_fill INT,
    FOREIGN KEY (prescription_id) REFERENCES fact_prescriptions(prescription_id)
);

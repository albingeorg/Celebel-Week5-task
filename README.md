# AWS Data Engineering Pipeline

This project demonstrates key AWS data engineering tasks:

## 1. Export Data to CSV, Parquet, and Avro (Glue Jobs)
Scripts in `glue_jobs/` extract data from a relational database and save it in:
- `CSV`: For compatibility
- `Parquet`: For analytics efficiency
- `Avro`: For schema evolution and compact serialization

### Files:
- `extract_to_csv.py`
- `extract_to_parquet.py`
- `extract_to_avro.py`

## 2. Schedule and Event-Based Automation
- **Schedule-based**: Configured using CloudFormation (see `cloudformation/glue_job_trigger.yaml`)
- **Event-based**: A Lambda function (`lambda_triggers/s3_event_trigger.py`) triggers a Glue job on S3 file uploads.

## 3. Full Database Replication (DMS)
- Configuration for replicating all tables using AWS DMS is provided in:
  - `dms_full_replication/dms_full_replication.json`

## 4. Selective Table/Column Replication (DMS)
- Configuration for replicating only specific tables and columns using AWS DMS is provided in:
  - `dms_selective_replication/dms_selective_replication.json`

---

## Prerequisites
- AWS Account with appropriate permissions
- AWS CLI configured
- Glue, DMS, Lambda, and S3 setup

## Folder Structure
```
aws_data_pipeline/
├── glue_jobs/
├── dms_full_replication/
├── dms_selective_replication/
├── lambda_triggers/
├── cloudformation/
└── README.md
```

## Author
Generated with ❤️ by ChatGPT

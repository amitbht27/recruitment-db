# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "bd52b192-f37c-4aa3-8c2e-4bb8ec624371",
# META       "default_lakehouse_name": "esm_configuration_lh",
# META       "default_lakehouse_workspace_id": "4c1fea8a-8342-4c52-b018-8a7a5cc2f075",
# META       "known_lakehouses": [
# META         {
# META           "id": "bd52b192-f37c-4aa3-8c2e-4bb8ec624371"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

# Welcome to your new notebook
# Type here in the cell editor to add code!


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC ALTER TABLE myservices_dbo_all_requests DROP COLUMNS (
# MAGIC     completed_date ,
# MAGIC     created_date ,
# MAGIC     updated_date ,
# MAGIC     ingestion_date );
# MAGIC 


# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC ALTER TABLE myservices_dbo_all_requests ADD COLUMNS (
# MAGIC     is_valid BOOLEAN,
# MAGIC     dw_load_date DATE,
# MAGIC     dw_load_datetime TIMESTAMP,
# MAGIC     dw_batch_id STRING
# MAGIC );

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC UPDATE myservices_dbo_all_requests
# MAGIC SET
# MAGIC     dw_load_date = CURRENT_DATE(),
# MAGIC     dw_load_datetime = CURRENT_TIMESTAMP(),
# MAGIC     dw_batch_id = date_format(current_timestamp(), 'yyyyMMddHHmmss');

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC UPDATE myservices_dbo_all_requests
# MAGIC SET 
# MAGIC     is_valid =1,
# MAGIC     completed_at = TO_DATE(completed_at),
# MAGIC     created_at = TO_DATE(created_at),
# MAGIC     updated_at = TO_DATE(updated_at),
# MAGIC      _ingest_ts = TO_DATE(_ingest_ts);
# MAGIC 


# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC UPDATE myservices_dbo_all_requests
# MAGIC SET 
# MAGIC     is_valid =0
# MAGIC     where subject='Employee Contract Management - Issuing a Contract of Employment'
# MAGIC     or team ='HR Recruitment Admin Team' or _fivetran_deleted=1;

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC ALTER TABLE myservices_dbo_all_requests 
# MAGIC SET TBLPROPERTIES (
# MAGIC   'delta.columnMapping.mode' = 'name',
# MAGIC   'delta.minReaderVersion' = '2',
# MAGIC   'delta.minWriterVersion' = '5'
# MAGIC );

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC /*ALTER TABLE myservices_dbo_all_requests 
# MAGIC RENAME COLUMN id TO request_id;
# MAGIC 
# MAGIC ALTER TABLE myservices_dbo_all_requests 
# MAGIC RENAME COLUMN resolution_duration TO resolution_duration_mins;*/

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC 
# MAGIC SELECT * FROM esm_configuration_lh.myservices_dbo_all_requests where is_valid=1 limit 100

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC --DESCRIBE myservices_dbo_all_requests;
# MAGIC 
# MAGIC ALTER TABLE myservices_dbo_all_requests
# MAGIC ALTER COLUMN completed_at TYPE DATE;

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

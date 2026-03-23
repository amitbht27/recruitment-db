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
# META         },
# META         {
# META           "id": "8cfcbf6f-b116-4d91-9009-aa997769f2e1"
# META         },
# META         {
# META           "id": "d86ee5d7-287a-4471-b6af-17d61201ef2f"
# META         }
# META       ]
# META     },
# META     "warehouse": {
# META       "known_warehouses": [
# META         {
# META           "id": "bb6422cb-7fa0-4071-a1ba-dceac5c55c34",
# META           "type": "Lakewarehouse"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

from com.microsoft.spark.fabric.Constants import Constants
from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

# SOURCE PARAMETERS
source_ws = "MYSERVICES_SILVER_STAGING_WS_UAT"
source_lakehouse = "myservices_silver_staging_lh"
# source_schema_name = "dbo"
# table_name = "all_requests"

# TARGET PARAMETERS
target_ws= "IT_RECRUITMENT_PMI_SILVER_CURATED_WS_UAT"
target_lakehouse = "esm_configuration_lh"

# # READ
# path = f"abfss://{source_ws}@onelake.dfs.fabric.microsoft.com/{source_lakehouse}.Lakehouse/Tables/{table_name}"
# df = spark.read.format("delta").load(path)


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

target_table_name = table_name  

target_table_path = (
    f"abfss://{target_ws}@onelake.dfs.fabric.microsoft.com/"
    f"{target_lakehouse}.Lakehouse/Files/delta/{target_table_name}"
)

# WRITE TO TARGET LAKEHOUSE
(
    df.write
      .format("delta")
      .mode("overwrite")
      .option("overwriteSchema", "true")
      .save(target_table_path)
)

spark.sql(f"""
        CREATE TABLE IF NOT EXISTS {target_lakehouse}.{target_table_name}
        USING DELTA
        LOCATION '{target_table_path}'
    """)


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# TABLE_CONFIG = [
#     {"source_table": "all_requests" },
#     {"source_table": "all_requests_normalized" },
#     # {"source_table": "all_effort_classes" },
#     {"source_table": "all_organizations_contact_details" },
#     {"source_table": "all_organizations" },
#     # {"source_table": "all_organizations_time_allocations" },
#     {"source_table": "all_people" },
#     {"source_table": "all_people_contact_details" },
#     {"source_table": "all_people_roles" }
#     # ,
#     # {"source_table": "all_sites" },
#     # {"source_table": "all_time_entries" },
#     # {"source_table": "all_timesheet_settings" }
# ]

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

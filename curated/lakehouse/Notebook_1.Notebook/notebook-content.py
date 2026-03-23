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
# META     },
# META     "warehouse": {
# META       "default_warehouse": "49c5ba53-8b05-445e-b24c-d7c49e68e45c",
# META       "known_warehouses": [
# META         {
# META           "id": "49c5ba53-8b05-445e-b24c-d7c49e68e45c",
# META           "type": "Lakewarehouse"
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
# MAGIC SELECT * FROM esm_configuration_lh.myservices_dbo_all_requests where is_valid=1

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

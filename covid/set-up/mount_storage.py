# Databricks notebook source
# MAGIC %md
# MAGIC ## Mount the following data lake storage gen2 containers github
# MAGIC 1. raw
# MAGIC 2. processed
# MAGIC 3. lookup

# COMMAND ----------

# MAGIC %md
# MAGIC ### Set-up the configs
# MAGIC #### Please update the following 
# MAGIC - application-id
# MAGIC - service-credential
# MAGIC - directory-id

# COMMAND ----------

configs = {"fs.azure.account.auth.type": "OAuth",
           "fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
           "fs.azure.account.oauth2.client.id": "acf73a51-eaca-46cc-bed4-c969cbb861b2",
           "fs.azure.account.oauth2.client.secret": "-x~zC6EhTBSzPg~F5~dyJ_N96yv4.hYE~0",
           "fs.azure.account.oauth2.client.endpoint": "https://login.microsoftonline.com/4084161a-f315-49bc-ad31-72bdcc28e2f5/oauth2/token"}

# COMMAND ----------

# MAGIC %md
# MAGIC ### Mount the raw container
# MAGIC #### Update the storage account name before executing

# COMMAND ----------

dbutils.fs.mount(
  source = "abfss://raw@covidreportingdlsg2.dfs.core.windows.net/",
  mount_point = "/mnt/covidreportingdlsg2/raw",
  extra_configs = configs)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Mount the processed container
# MAGIC #### Update the storage account name before executing

# COMMAND ----------

dbutils.fs.mount(
  source = "abfss://processed@covidreportingdlsg2.dfs.core.windows.net/",
  mount_point = "/mnt/covidreportingdlsg2/processed",
  extra_configs = configs)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Mount the lookup container
# MAGIC #### Update the storage account name before executing

# COMMAND ----------

dbutils.fs.mount(
  source = "abfss://lookup@covidreportingdlsg2.dfs.core.windows.net/",
  mount_point = "/mnt/covidreportingdlsg2/lookup",
  extra_configs = configs)

# COMMAND ----------

dbutils.fs.ls("/mnt/covidreportingdlsg2/processed")

# COMMAND ----------



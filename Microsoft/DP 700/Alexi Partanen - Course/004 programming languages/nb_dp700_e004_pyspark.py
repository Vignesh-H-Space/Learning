#!/usr/bin/env python
# coding: utf-8

# ## nb_dp700_e004_pyspark
# 
# New notebook

# In[1]:


assignments = spark.sql("SELECT * FROM lh_dp700.dp700_e004.assignments")
departments = spark.sql("SELECT * FROM lh_dp700.dp700_e004.departments")
employees = spark.sql("SELECT * FROM lh_dp700.dp700_e004.employees")
projects = spark.sql("SELECT * FROM lh_dp700.dp700_e004.projects")


# In[2]:


display(assignments)
display(departments)
display(employees)
display(projects)


# In[3]:


import pyspark.sql.functions as F

display( \
    employees \
    .filter(F.col("salary") >= 75000) \
    .select(
        F.col("name"),
        F.col("salary"),
        F.concat(F.lit("$ "), F.col("salary")).alias("salary_string")
    )
)


# In[4]:


display( \
    employees \
    .filter("salary >= 75000") \
    .selectExpr(
        "name",
        "salary",
        "'$ ' || salary AS salary_string"
    ) \
)


# In[5]:


display( \
    employees \
    .join(departments, employees["department_id"] == departments["department_id"], "left") \
    .select(
        employees["name"],
        employees["department_id"],
        departments["department_name"]
    ) \
)


# In[6]:


import pyspark.sql.functions as F

e = employees.alias("e")
d = departments.alias("d")

display( \
    e.join(d, F.col("e.department_id") == F.col("d.department_id"), "left") \
    .select(
        F.col("e.name").alias("employee_name"),
        F.col("e.department_id"),
        F.col("d.department_name")
 ) \
)


# In[7]:


display( \
    employees \
    .join(departments, employees["department_id"] == departments["department_id"], "left") \
    .groupBy("department_name") \
    .count() \
    .withColumnRenamed("count", "number_of_employees") \
)


# In[9]:


import pyspark.sql.functions as F

e = employees.alias("e")
d = departments.alias("d")

display( \
    e.join(d, F.col("e.department_id") == F.col("d.department_id"), "left") \
    .groupBy(F.col("d.department_name")) \
    .count() \
    .withColumnRenamed("count", "number_of_employees") \
)


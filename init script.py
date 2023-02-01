# Databricks notebook source
dbutils.fs.put("/databricks/scripts/arana_python_install.sh","""
#!/bin/bash
echo 1
rm -rf /var/lib/apt/lists/*
echo 2
sudo apt-get update -y
echo 3
sudo apt-get install -y python3-dev graphviz libgraphviz-dev pkg-config
echo 5""", True)

# COMMAND ----------



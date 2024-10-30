# Databricks notebook source
import pandas as pd
import math

# file path
wsPath = '/Workspace/Users/praserth@ais.co.th'
inputPath = f"{wsPath}/track_small.csv"
outputPath = f"{wsPath}/output_small.csv"

# Extract
tracks = pd.read_csv(inputPath)
# tracks.display()

# Transform
tracks["UnitPrice"] = tracks["UnitPrice"].apply(lambda x: math.ceil(x))
# tracks.display()
                             
# Load
tracks.to_csv(outputPath, index=False)

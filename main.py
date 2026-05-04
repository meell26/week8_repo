from features.feature_engineering import *
import subprocess

# Step 1: features
print("Generating features...")
subprocess.run(["python", "features/feature_engineering.py"])

# Step 2: model
print("Training model...")
subprocess.run(["python", "model/train_model.py"])

print("Done")
import papermill as pm
import os

# Ensure output directory exists
os.makedirs("notebooks/runs", exist_ok=True)
KERNEL = "KhaiPhaDuLieu"

print("Starting execution of Question.ipynb...")
try:
    pm.execute_notebook(
        "notebooks/Question.ipynb",
        "notebooks/runs/Question_out.ipynb",
        kernel_name=KERNEL
    )
    print("Question.ipynb finished successfully.")
except Exception as e:
    print(f"Failed to run Question.ipynb: {e}")

print("Starting execution of Topic.ipynb...")
try:
    pm.execute_notebook(
        "notebooks/Topic.ipynb",
        "notebooks/runs/Topic_out.ipynb",
        kernel_name=KERNEL
    )
    print("Topic.ipynb finished successfully.")
except Exception as e:
    print(f"Failed to run Topic.ipynb: {e}")

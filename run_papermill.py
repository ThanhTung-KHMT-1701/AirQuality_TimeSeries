import os
import papermill as pm

# Run notebooks end-to-end (classification + regression + ARIMA)
os.makedirs("notebooks/runs", exist_ok=True)

KERNEL = "KhaiPhaDuLieu"

pm.execute_notebook(
    "notebooks/01_preprocessing_and_eda.ipynb",
    "notebooks/runs/01_preprocessing_and_eda.ipynb",
    parameters=dict(
        USE_UCIMLREPO=False,
        RAW_ZIP_PATH="data/raw/PRSA2017_Data_20130301-20170228.zip",
        OUTPUT_CLEANED_PATH="data/processed/01_cleaned.csv",
        LAG_HOURS=[1, 3, 24],
    ),
    language="python",
    kernel_name=KERNEL
)

pm.execute_notebook(
    "notebooks/02_feature_preparation.ipynb",
    "notebooks/runs/02_feature_preparation.ipynb",
    parameters=dict(
        CLEANED_PATH="data/processed/01_cleaned.csv",
        OUTPUT_DATASET_PATH="data/processed/02_dataset_for_clf.parquet",
        DROP_ROWS_WITHOUT_TARGET=True,
    ),
    language="python",
    kernel_name=KERNEL
)

pm.execute_notebook(
    "notebooks/03_classification_modelling.ipynb",
    "notebooks/runs/03_classification_modelling.ipynb",
    parameters=dict(
        DATASET_PATH="data/processed/02_dataset_for_clf.parquet",
        CUTOFF="2017-01-01",
        METRICS_PATH="data/processed/03_metrics.json",
        PRED_SAMPLE_PATH="data/processed/03_predictions_sample.csv",
    ),
    language="python",
    kernel_name=KERNEL
)

# --- NEW: Regression (supervised, lag-based) ---
pm.execute_notebook(
    "notebooks/04_regression_modelling.ipynb",
    "notebooks/runs/04_regression_modelling.ipynb",
    parameters=dict(
        USE_UCIMLREPO=False,
        RAW_ZIP_PATH="data/raw/PRSA2017_Data_20130301-20170228.zip",
        LAG_HOURS=[1, 3, 24],
        HORIZON=1,
        TARGET_COL="PM2.5",
        OUTPUT_REG_DATASET_PATH="data/processed/04_dataset_for_regression.parquet",
        CUTOFF="2017-01-01",
        MODEL_OUT="04_regressor.joblib",
        METRICS_OUT="04_regression_metrics.json",
        PRED_SAMPLE_OUT="04_regression_predictions_sample.csv",
    ),
    language="python",
    kernel_name=KERNEL
)

# --- NEW: Time-series forecasting with ARIMA only ---
pm.execute_notebook(
    "notebooks/05_arima_forecasting.ipynb",
    "notebooks/runs/05_arima_forecasting_run.ipynb",
    parameters=dict(
        RAW_ZIP_PATH="data/raw/PRSA2017_Data_20130301-20170228.zip",
        STATION="Aotizhongxin",
        VALUE_COL="PM2.5",
        CUTOFF="2017-01-01",
        P_MAX=3,
        Q_MAX=3,
        D_MAX=2,
        IC="aic",
        ARTIFACTS_PREFIX="05_arima_pm25",
    ),
    language="python",
    kernel_name=KERNEL
)

print("Đã chạy xong pipeline (classification + regression + ARIMA)")

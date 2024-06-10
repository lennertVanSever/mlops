import mlflow
import mlflow.sklearn
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load Dataset
X, y = datasets.load_iris(return_X_y=True)

# Split Data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Set Hyperparameters
solver = 'liblinear'
max_iter = 100
random_state = 42

# Train Model
model = LogisticRegression(solver=solver, max_iter=max_iter, random_state=random_state)
model.fit(X_train, y_train)

# Predict and Evaluate
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

# Initialize MLflow and start tracking
mlflow.set_tracking_uri(uri="http://localhost:5000")
mlflow.set_experiment("MLflow Test")

with mlflow.start_run():
    # Log parameters
    mlflow.log_param("solver", solver)
    mlflow.log_param("max_iter", max_iter)
    mlflow.log_param("random_state", random_state)
    
    # Log metrics
    mlflow.log_metric("accuracy", accuracy)
    
    # Log model
    mlflow.sklearn.log_model(model, "model")
    
    # Register model
    mlflow.register_model("runs:/{}/model".format(mlflow.active_run().info.run_id), "LogisticRegressionModel")

print("Model training and logging complete.")

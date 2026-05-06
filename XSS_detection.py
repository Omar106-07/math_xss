import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

# Load Excel file
data = pd.read_excel(r"C:\Users\omar\Desktop\XSS Attack Dataset with 461 entries.xlsx")

# Show structure
print(data.head())
print(data.columns)

# IMPORTANT: check column name for label
# change 'Label' if your file uses different name
label_column = "Label"   # <-- change if needed

# Convert text to numbers
data = data.apply(lambda x: pd.factorize(x)[0])

# Split features and target
X = data.drop(label_column, axis=1)
y = data[label_column]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Results
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))

# Save results to HTML

accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)

html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <title>XSS Detection Report</title>
    <style>
        body {{
            font-family: Arial;
            margin: 40px;
            background-color: #f4f4f4;
        }}
        h1, h2 {{
            color: #333;
        }}
        .box {{
            background: white;
            padding: 20px;
            margin-bottom: 20px;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }}
        pre {{
            background: #eee;
            padding: 10px;
            border-radius: 5px;
        }}
    </style>
</head>
<body>

<h1>XSS Attack Detection Report</h1>

<div class="box">
    <h2>📌 Project Description</h2>
    <p>This project detects Cross-Site Scripting (XSS) attacks using a Random Forest Machine Learning model.</p>
</div>

<div class="box">
    <h2>📊 Accuracy</h2>
    <p><strong>{accuracy:.4f}</strong></p>
</div>

<div class="box">
    <h2>📈 Classification Report</h2>
    <pre>{report}</pre>
</div>

<div class="box">
    <h2>📉 Confusion Matrix</h2>
    <pre>{cm}</pre>
</div>

<div class="box">
    <h2>⚙️ Model Used</h2>
    <p>Random Forest Classifier with 100 trees</p>
</div>

</body>
</html>
"""

# Save file
with open("report.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("✅ HTML report generated as report.html")
#!/usr/local/bin/python3



# model metrics
precision_metric = precision_score(y_test, predictions, average = "macro")

recall_metric = recall_score(y_test, predictions, average = "macro")

accuracy_metric = accuracy_score(y_test, predictions)

f1_metric = f1_score(y_test, predictions, average = "macro")

print('Accuracy: ', accuracy_metric)
print('Precision: ', precision_metric)
print('Recall: ', recall_metric)
print('F1 Score: ', f1_metric)

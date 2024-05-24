import matplotlib.pyplot as plt
from sklearn import metrics


# True binary labels
y = [0, 0,1,1,0,1,0]
# Predicted probabilities for class 1
y_preda = [-0.55,-0.05,0.25,0.55,0.6,0.75,0.8]
#y_predb = [0.59, 0.65, 0.85, 0.9, 0.45, 0.55, 0.7, 0.72]
#y_predc = [0.45, 0.65, 0.7, 0.9, 0.5, 0.57, 0.72, 0.85]
#y_predd = [0.55, 0.68, 0.73, 0.9, 0.45, 0.55, 0.7, 0.85]


fpr, tpr, thresholds = metrics.roc_curve(y, y_preda)
auc = metrics.auc(fpr, tpr)

# Print the TPR, FPR, and AUC values
for i in range(len(fpr)):
    print(f"FPR: {fpr[i]}, TPR: {tpr[i]}, Threshold: {thresholds[i]}")
print(f"AUC: {auc}")

# Plot the ROC curve
plt.figure()
plt.plot(fpr, tpr, label=f'ROC curve (AUC = {auc:.2f})')
plt.plot([0, 1], [0, 1], 'k--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic for Predictor A')
plt.legend(loc="lower right")
plt.show()
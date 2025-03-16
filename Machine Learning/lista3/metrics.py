import numpy as np

def confusion_matrix(y_true, y_pred):
    """
    [[TN, FP],
     [FN, TP]]
    """

    # True Negatives (TN)
    tn = np.sum((y_true == 0) & (y_pred == 0))
    # False Positives (FP)
    fp = np.sum((y_true == 0) & (y_pred == 1))
    # False Negatives (FN)
    fn = np.sum((y_true == 1) & (y_pred == 0))
    # True Positives (TP)
    tp = np.sum((y_true == 1) & (y_pred == 1))
    
    return np.array([[tn, fp],
                     [fn, tp]])


def accuracy_score(y_true, y_pred):
    """
    accuracy = correct / all
    """

    return np.sum(y_true == y_pred) / len(y_true)

def precision_score(y_true, y_pred):
    """
    precision = TP / (TP + FP)
    """

    cm = confusion_matrix(y_true, y_pred)
    tp = cm[1, 1]
    fp = cm[0, 1]
    
    denominator = tp + fp
    if denominator == 0:
        return 0.0
    return tp / denominator

def recall_score(y_true, y_pred):
    """
    recall = TP / (TP + FN)
    """

    cm = confusion_matrix(y_true, y_pred)
    tp = cm[1, 1]
    fn = cm[1, 0]
    
    denominator = tp + fn
    if denominator == 0:
        return 0.0
    return tp / denominator

def f1_score(y_true, y_pred):
    """
    F1 = 2 * (precision * recall) / (precision + recall)
    """

    p = precision_score(y_true, y_pred)
    r = recall_score(y_true, y_pred)
    
    denominator = p + r
    if denominator == 0:
        return 0.0
    return 2 * p * r / denominator

def roc_curve(y_true, y_score):
    """
    Returns (fpr, tpr, thresholds) for every threshold.
    """

    thresholds = np.sort(np.unique(y_score))[::-1]
    
    fpr_list = []
    tpr_list = []
    
    for t in thresholds:
        y_pred = (y_score >= t).astype(int)
        
        cm = confusion_matrix(y_true, y_pred)
        tn, fp, fn, tp = cm.ravel()
        
        # True Positive Rate
        if (tp + fn) == 0:
            tpr = 0.0
        else:
            tpr = tp / (tp + fn)
        
        # False Positive Rate 
        if (fp + tn) == 0:
            fpr = 0.0
        else:
            fpr = fp / (fp + tn)
        
        fpr_list.append(fpr)
        tpr_list.append(tpr)
    
    return np.array(fpr_list), np.array(tpr_list), thresholds

def roc_auc_score(y_true, y_score):
    """
    Field under the ROC curve
    """

    fpr, tpr, thresholds = roc_curve(y_true, y_score)
    
    # complete the curve
    if fpr[0] != 0 or tpr[0] != 0:
        fpr = np.insert(fpr, 0, 0)
        tpr = np.insert(tpr, 0, 0)
    if fpr[-1] != 1 or tpr[-1] != 1:
        fpr = np.append(fpr, 1)
        tpr = np.append(tpr, 1)
    
    # trapezoidal method
    auc = 0.0
    for i in range(1, len(fpr)):
        auc += 0.5 * (tpr[i] + tpr[i-1]) * (fpr[i] - fpr[i-1])

    return auc

if __name__ == "__main__":
    y_true = np.array([0, 0, 1, 1, 1, 0, 1, 0])
    y_pred = np.array([0, 0, 1, 1, 0, 0, 1, 1])
    y_score = np.array([0.1, 0.2, 0.8, 0.7, 0.3, 0.05, 0.9, 0.6])
    
    print("confusion_matrix:\n", confusion_matrix(y_true, y_pred))
    print("accuracy_score:", accuracy_score(y_true, y_pred))
    print("precision_scor:", precision_score(y_true, y_pred))
    print("recall_score:", recall_score(y_true, y_pred))
    print("f1_score:", f1_score(y_true, y_pred))
    
    fpr, tpr, thresholds = roc_curve(y_true, y_score)
    print("fpr:", fpr)
    print("tpr:", tpr)
    print("thresholds:", thresholds)
    
    auc_value = roc_auc_score(y_true, y_score)
    print("auc_value:", auc_value)

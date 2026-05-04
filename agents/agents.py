def detector(prediction):
   return "Anomaly" if prediction == -1 else "Normal"

def analyzer(prediction):
   if prediction == -1:
       return "Suspicious behavior detected (multiple failed logins or high activity)"
   return "No suspicious activity"

def reporter(analysis):
   if "Suspicious" in analysis:
       return " ALERT: Potential cyber attack detected! Immediate investigation recommended."
   return "System is operating normally"
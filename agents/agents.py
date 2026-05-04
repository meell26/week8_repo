def detector(data):
   if data['failed_logins'] > 3:
       return "Anomaly"
   return "Normal"

def analyzer(result):
   if result == "Anomaly":
       return "Multiple failed login attempts"
   return "No threat"

def reporter(analysis):
   return f"ALERT: {analysis}"
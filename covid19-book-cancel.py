# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 11:32:44 2021

@author: Admin
"""

from flask import Flask, jsonify



app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/criticalnumber/<int:n>')
def criticalnumber(n):
    n=int(input("enter the number\n"))
    s1=n
    
    
    if(s1==1):
        print(f"(s1) patient is normal checkup")
        result ={
            "patient_critical level":"patient is normal checkup",
            "pin_code":431601,
            "hospital":"goverment",
            "time_slot":"10.am"
            }
    
    elif(s1==2):
        print(f"(s1) patient is serious critical")
        result ={
            "patient_critical level":"patient is serious critical",
            "pin_code":431602,
            "hospital":"ayurvdic-hospital",
            "time_slot":"11.am"
            }
    
    elif(s1==3):
        print(f"(s1) patient is very much critical")
        result ={
            "patient_critical level": "patient is very much critical",
            "pin_code":431603,
            "hospital":"shri-guru-govind-hospital",
            "time_slot":"any-time"
            }
    
   
    elif(s1==0):
        total=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
        for i in range(0, len(total)):
            if total[i]==0:
                total.pop(i)
            else:
                print(f"(i) bed is full")
        print(f"(total) patient booking slot\n:")
        print(f"(s1) patient is total bed count")
        result ={
            "patient_critical level":"total bed is",
            "remaing-bed-available":i
            
            }
    
    elif(s1==-1):
        print(f"(s1) patient is very critical resudual booking")
        result ={
            "patient_critical level":"patient is very critical resudual booking",
            "pin_code":431604,
            "hospital":"private-sector",
            "time_slot":"10.am-10.pm"
            }
        
    else:
        print(f"(s1) patient is fine so no go hospital")
        result ={
            "patient_critical level":"patient is fine so no go hospital",
        
            }
        
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=False)
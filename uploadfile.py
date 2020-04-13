# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 10:45:42 2020

@author: OPEN NOW
"""

from flask import Flask, request, jsonify
from werkzeug import secure_filename
import csv
from hashlib import sha256
from time import time
import json
import os.path


class bc(object):
    def __init__(self,student_id):
        self.chain=[]
        self.student_id = student_id
    
    def verify(self):

        currentB=self.chain[-1]
        valid=True
        index = len(self.chain)-2
        print(index)
    
        while (index >= 0 and valid == True):
            
                prev_B=self.chain[index]
                
                if(currentB['header']['prev_hash']==self.data_hash(prev_B)):
                    currentB = prev_B
                    valid = True
                
                else:
                    valid=False
                    
                index -= 1
        
        return valid
  
    def load_data(self):
        
        filename = str(self.student_id + ".json")
       
        if os.path.exists(filename) == True:
            
            # load json to self.chain
            with open(filename, "r") as f:
               reader = json.load(f)
               for row in reader:
                   self.chain.append(row)
            return True
        else:
            return False
    
    def save_json(self):
        
        filename = str(self.student_id + ".json")
        with open(filename,'w') as f:
            json.dump(self.chain,f)

    def generic_lastBlock(self):
        data = {
            'stid': None,
            'code': None,
            'grade': None,
            'time':None,
            'year':None,
            'seme':None,
            'creater':None,
        }

        header = {
            'index':len(self.chain)+1,
            'timestamp':time(),
            'prev_hash':self.data_hash(self.chain[-1]),
            'hashData': self.data_hash(data),
        }

        block = {'header':header,'data': data}     
        self.chain.append(block)
                          
    def generic_block(self):
        data = {
            'stid': self.student_id,
            'code': None,
            'grade': None,
            'time':time(),
            'year':None,
            'seme':None,
            'creater':None,
        }

        header = {
            'index':1,
            'timestamp':time(),
            'prev_hash':None,
            'hashData': self.data_hash(data),
        }

        block = {'header':header,'data': data}     
        self.chain.append(block)
        
        self.generic_lastBlock()
        

    def data_hash(self,data):
        return sha256(str(data).encode('utf8')).hexdigest()
        

    def input_data(self,stdid,code,grade,year,seme,creator):
        
        print(self.chain[-1]['header']['prev_hash'])

        tmpBlock = self.chain[-1]
        
        tmpBlock['data']['stid'] = stdid
        tmpBlock['data']['code'] = code
        tmpBlock['data']['grade'] = grade
        tmpBlock['data']['time'] = time()
        tmpBlock['data']['year'] = year
        tmpBlock['data']['seme'] = seme
        tmpBlock['data']['creater'] = creator
        
        tmpBlock['header']['index'] = len(self.chain)
        tmpBlock['header']['timestamp'] = time()
        tmpBlock['header']['hashData'] = self.data_hash(tmpBlock['data'])
    
        self.generic_lastBlock()  
app = Flask(__name__)

	
@app.route('/uploader', methods = ['GET', 'POST'])
def uploader_file():
   try: 
       if request.method == 'POST':
          f = request.files['file']
          f.save(secure_filename(f.filename))
          with open(f.filename) as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                stid=row[0]
                code=row[1]
                year=row[2]
                seme=row[3]
                grade=row[4]
                creator=row[5]
                print (stid,code,year,seme,grade,creator)   
                
                if(code=="Null") or (creator=="Null") or (grade=="Null") or (seme=="Null") or (stid =="Null")or(year=="Null"):
                     
                        response = {'response': "Plese input data"}
                else:        
                
                    blockchain = bc(stid)
                    
                    if blockchain.load_data() == True:
                        blockchain.input_data(stid,code,grade,year,seme,creator)
                        blockchain.save_json()
                    else:
                        blockchain.generic_block()
                        blockchain.input_data(stid,code,grade,year,seme,creator)
                        blockchain.save_json()
                    
                    response = {
                    # 0 success
                    'response': 0
                    }
   except:
        response = {
            # 1 fail
            'response': 1
        }

   return jsonify(response)

@app.route('/cp', methods=['POST'])
def compareG():
    
    req_data = request.get_json()
    
    stid = req_data['stid']
    grade = req_data['grade']
    code = req_data['code']
    year = req_data['year']
    seme = req_data['seme']

    
    if code != "Null" : 
        flg_code = True 
    else: 
        flg_code = False
    if grade != "Null": 
        flg_grade = True 
    else: 
       flg_grade = False
    if year != "Null" :
        flg_year =True
    else:
        flg_year = False
    
    if seme != "Null":
        flg_seme =True
    else:
        flg_seme =False
  

    blockchain = bc(stid)
    i=len(blockchain.chain)
   
   
    if (flg_code==True) and (flg_grade==True) and (flg_year==True)and(flg_seme==True):
        if blockchain.load_data() == True:
                if blockchain.verify() == True:
                   for block in blockchain.chain:
                       if block["data"]['stid'] == stid:
                          
                                 if  block['data']['year']==year:  
                                       if  block['data']['seme']==seme: 
                                           if block['data']['code']==code:
                                              i="code right"
                                              if block['data']['grade']==grade:
                                                  i="code and grade"
                                                  response=0
                                              else:
                                                  i="code right and grade false"
                                                  response=1
                                           else:
                                              i="code false"
                                              response=2
                                       else:
                                           i="Don't have seme"
                                           response=3
                                     
                                 if block['data']['year']!=year:
                                      i="Don't Year"
                                      response=4
                if blockchain.verify() == False:
                   response=5
        if blockchain.load_data() == False:
                i="No chain"
                response=6
    if (flg_code==False) and (flg_grade==False) and (flg_year==False)and(flg_seme==False):
        response="input data"
            
    return jsonify(i,response)    

@app.route('/qr', methods=['POST'])
def queryblock():
    
    req_data = request.get_json()
    
    stid = req_data['stid']
    grade = req_data['grade']
    code = req_data['code']
    year = req_data['year']
    seme = req_data['seme']
    
    if code != "Null" : 
        flg_code = True 
    else: 
        flg_code = False
    if grade != "Null": 
        flg_grade = True 
    else: 
       flg_grade = False
    if year != "Null" :
        flg_year =True
    else:
        flg_year = False
    
    if seme != "Null":
        flg_seme =True
    else:
        flg_seme =False
    

    blockchain = bc(stid)
    
    if blockchain.load_data() == True:
        
        if blockchain.verify() == True:
            
            data = []
            for block in blockchain.chain:
                
             if block['header']['index']>1:
                if block["data"]['stid'] == stid:
                    
                    if flg_grade:
                        if block['data']['grade'] != grade: continue
                    
                    if flg_code:
                        if block['data']['code'] != code: continue
                    
                    if (flg_year==True) and (flg_seme==False):
                        if block['data']['year'] != year: continue
                        
                    
                    if (flg_year==True) and (flg_seme==True):
                        if block['data']['year']!= year and block['data']['seme'] != seme : continue
                    
                    
                        
                        
                    data.append(block)
            
            response = {"response": data}
            
            if len(data)==0:
                response={"response":"not found data"}
            
        else:
            response = {"response": "chain not valid"}
            
    else:
        response = {"response": "not found chain"}
        
    return jsonify(response) 

@app.route('/verify', methods=['POST'])
def verify_chain():
    req_data = request.get_json()
    
    try:
        
        blockchain = bc(req_data['stid'])
        
        if blockchain.load_data() == True:    
            if blockchain.verify() == True: 
                response = {'response': 0 }
            else:
                 response = {'response': 1 }
        else:
            response = {'response': 2 }
            
    except:
        response = {'response': 3 }

    return jsonify(response)

@app.route('/<uid>', methods=['GET'])
def show(uid):
    blockchain = bc(uid)
    blockchain.load_data()
    
    response = {
            'chain': blockchain.chain
        }

    return jsonify(response), 200 

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=2000)
from flask import Flask,render_template,request
import os
import pandas as pd
from ex.some import multiword_tokenize
import nltk
import csv
import glob
import zipfile
from os.path import basename
from flask import jsonify 
app = Flask(__name__,template_folder='Templates')

app.config["UPLOAD_PATH"] = "E:/"
a = pd.read_excel('C:/Users/sandeep.mandula/Downloads/Standard streets.xlsx')
a['Unnamed: 0']=a['Unnamed: 0'].str.lower()
a['Unnamed: 1']=a['Unnamed: 1'].str.lower()
dict(zip(a['Unnamed: 0'], a['Unnamed: 1']))
dict1 = a.set_index('Unnamed: 0').to_dict()['Unnamed: 1']

@app.route("/upload_file",methods=["GET","POST"])
def upload_file():
    if request.method == 'POST':
        for f in request.files.getlist('file_name'):
        #f=request.files['file_name']
            f.save(os.path.join(app.config['UPLOAD_PATH'],f.filename))
            mwe = ['new york','new hampshire','new jersey','new mexico','north carolina','north dakota','south carolina','south dakota','rhode island','west virginia','post office box']

            folpath = r'E:'
            s = []

            for fpath in glob.glob("{0}/*".format(folpath),recursive=True):
                
                #print(fpath)
                s.append(fpath)
            for i in s:
                #print(i)
                hj= i.split("/")[1]
                #print(hj)
                hj1 = hj.split(".")[0]
                #print(hj1)
                
                if i[-3:] == "csv":
                    dg = []
                    data = pd.read_csv(i,index_col=None)
                    #print(data.head())
                    data = data.rename(columns={data.columns[0]: 'Standard Streets'})
                    conv1 = data['Standard Streets'].tolist()
                    c = []

                    for i in conv1:
                        
                        #print(i)
                        a = i.lower()
                        a = multiword_tokenize(a, mwe)

                        #a = []
                        for i in a:

                            for k,v in dict1.items():
                                if k == i:
                                    y=a.index(i)
                                    a[y]=v
                        #print(a)

                        result = "" 

                        for elements in a: 
                            result += str(elements) + " " 

                        result = result.title()

                        cap = nltk.word_tokenize(result)
                        y = len(cap)
                        x=[]
                        for i in range(0,y):
                            if i in range(y-3,y):
                                z=cap[i].upper()
                                x.append(z)
                            else:
                                k=cap[i]
                                x.append(k)


                        finalresult = "" 

                        for elements in x: 

                            finalresult += str(elements) + " " 



                        #c.append(finalresult)
                        dg.append(finalresult)
                    df = pd.DataFrame(dg)
                    
                    df.to_csv('D:/Storing Files/'+hj1+"_finalresult.csv",index=False,header=False)
                        
                    #print((dg))
                        #dg.append(finalresult)

                    #print(data['Standard Streets'])
                    #data1 = (data.head())
                    #print(data1)
                    
                elif i[-4:]=="json":
                    cg = []
                    data = pd.read_json(i)
                    #print(data)
                    
                    data = data.rename(columns={data.columns[0]: 'Standard Streets'})
                    conv1 = data['Standard Streets'].tolist()
                    c= []
                    for i in conv1:
                        #print(i)
                        a = i.lower()
                        a = multiword_tokenize(a, mwe)

                        #a = []
                        for i in a:

                            for k,v in dict1.items():
                                if k == i:
                                    y=a.index(i)
                                    a[y]=v
                        #print(a)

                        result = "" 

                        for elements in a: 
                            result += str(elements) + " " 

                        result = result.title()

                        cap = nltk.word_tokenize(result)
                        y = len(cap)
                        x=[]
                        for i in range(0,y):
                            if i in range(y-3,y):
                                z=cap[i].upper()
                                x.append(z)
                            else:
                                k=cap[i]
                                x.append(k)


                        finalresult = "" 

                        for elements in x: 

                            finalresult += str(elements) + " " 


                        cg.append(finalresult)
                    df = pd.DataFrame(cg)
                    
                    df.to_json('D:/Storing Files/'+hj1+"_finalresultjson.json",orient='records',lines=True)
                    #df.to_json('temp.json', orient='records', lines=True)
                        
                    #print((cg))
                        

                    #print(data.head())
                elif i[-3:] == "xml":
                    eg = []
                    data = pd.read_xml(i)
                    data = data.rename(columns={data.columns[0]: 'Standard Streets'})
                    conv1 = data['Standard Streets'].tolist()
                    c = []
                    
                    for i in conv1:
                        #print(i)
                        a = i.lower()
                        a = multiword_tokenize(a, mwe)

                        #a = []
                        for i in a:

                            for k,v in dict1.items():
                                if k == i:
                                    y=a.index(i)
                                    a[y]=v
                        #print(a)

                        result = "" 

                        for elements in a: 
                            result += str(elements) + " " 

                        result = result.title()

                        cap = nltk.word_tokenize(result)
                        y = len(cap)
                        x=[]
                        for i in range(0,y):
                            if i in range(y-3,y):
                                z=cap[i].upper()
                                x.append(z)
                            else:
                                k=cap[i]
                                x.append(k)


                        finalresult = "" 

                        for elements in x: 

                            finalresult += str(elements) + " " 



                        eg.append(finalresult)
                    df = pd.DataFrame(eg,columns=['x'])
                    
                    
                    df.to_xml('D:/Storing Files/'+hj1+"_finalresultxml.xml")

                folspath = r'D:/Storing Files/'
                sss=  []

                for fspath in glob.glob("{0}/*".format(folspath),recursive=True):
    
                    print(fspath,'hai')
                    sss.append(fspath)
                print(sss,'hai')

                with zipfile.ZipFile('final.zip', 'w') as zipF:
                    for file in sss:
                        zipF.write(file,compress_type=zipfile.ZIP_DEFLATED)
                print(zipF,'hai')

                        
                    #print((eg))



    # write the header
    # writer.writerow(header)

    # write multiple rows
                #writer.writerow(finalresult)

        #return render_template("upload-files.html",msg="Files has been uploaded sucessfully",ll='C:/Users/sandeep.mandula/Downloads/flask/flask/final.zip')
    #return render_template("upload-files.html",msg="Please Choose a files")
    return jsonify({"msg":"Files has been uploaded sucessfully","ll":'C:/Users/sandeep.mandula/Downloads/flask/flask/final.zip'})



if __name__== '__main__':
    app.run(debug=True)


# a = pd.read_excel('/home/metagogy/Downloads/send/Standard streets.xlsx')
# a['Unnamed: 0']=a['Unnamed: 0'].str.lower()
# a['Unnamed: 1']=a['Unnamed: 1'].str.lower()
# dict(zip(a['Unnamed: 0'], a['Unnamed: 1']))
# dict1 = a.set_index('Unnamed: 0').to_dict()['Unnamed: 1']
# import nltk
# from nltk import word_tokenize
# from nltk.tokenize import MWETokenizer
# def multiword_tokenize(text, mwe):
#     # Initialize the MWETokenizer
#     protected_tuples = [word_tokenize(word) for word in mwe]
#     protected_tuples_underscore = ['_'.join(word) for word in protected_tuples]
#     tokenizer = MWETokenizer(protected_tuples)
#     # Tokenize the text.
#     tokenized_text = tokenizer.tokenize(word_tokenize(text))
#     # Replace the underscored protected words with the original MWE
#     for i, token in enumerate(tokenized_text):
#         if token in protected_tuples_underscore:
#             tokenized_text[i] = mwe[protected_tuples_underscore.index(token)]
#     return tokenized_text
# mwe = ['new york','new hampshire','new jersey','new mexico','north carolina','north dakota','south carolina','south dakota','rhode island','west virginia','post office box']

#s = 'E:/csvjson.json'

# if s[-3:] == "csv":
#     data = pd.read_csv(s)
# elif s[-4:]=="json":
#     data = pd.read_json(s)
# elif s[-3:] == "xml":
#     data = pd.read_xml(s)

# conv1 = data['Standard Streets'].tolist()
# for i in conv1:
#     #print(i)
#     a = i.lower()
#     a = multiword_tokenize(a, mwe)

#     #a = []
#     for i in a:

#         for k,v in dict1.items():
#             if k == i:
#                 y=a.index(i)
#                 a[y]=v
#     #print(a)

#     result = "" 

#     for elements in a: 
#         result += str(elements) + " " 

#     result = result.title()

#     cap = nltk.word_tokenize(result)
#     y = len(cap)
#     x=[]
#     for i in range(0,y):
#         if i in range(y-3,y):
#             z=cap[i].upper()
#             x.append(z)
#         else:
#             k=cap[i]
#             x.append(k)

#     finalresult = "" 

#     for elements in x: 
        
#         finalresult += str(elements) + " " 
        

#     print(finalresult)

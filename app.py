from flask import Flask, render_template,request
import string
import random
import datetime

app = Flask(__name__)

@app.route('/')

def jbm():
    return render_template('jbm.html')
    


@app.route('/result',methods=['POST','GET'])

def result():
   if request.method=='POST':
        
        reading = request.form.get('reading')


# working with user datas
        inputs = reading.split(":")
        inputs_01 = reading.split(":")
       
        print(inputs)
        print(type(inputs))

        if " CMM CNC \r\nPART NAME " in inputs:
            reading=reading[978:]
            reads="p name"
        else:
            
            reading=reading[878:]
            reads="no p name"
            

        inputs = reading.split("                   ")
        inputs.remove(inputs[-1])

       # GENERATING MULTIPLE VARIABLES
        strg = string.ascii_lowercase + string.ascii_uppercase
        num_all = []

        for i in range(len(strg)):
            num_all.append(i)

        str_all = []

        for j in num_all:
            for i in strg:
                a = i+"_"+f'{j}'
                str_all.append(a)


        

        lsst = []
        lst1={}
        lst2={}
        # lst3={}
            
        for name, value in zip(str_all, inputs):
                # print(name)
                # print(value)
                exec(f"{name}=value")
                new = {name:value}
                if value=="":
                    continue
                # elif "          " in value:
                #   lst3.update(new)    
                    
                
                    
                if "\n\n" in value or "\n \n" in value:    
                    lst2.update(new)
                elif "I" in value or "p" in value or "S" in value :    
                    lst2.update(new)
                elif "Diam" in value:
                    continue
                elif "Length" in value:
                    continue
                elif "Width" in value:
                    continue
                else:
                    lst1.update(new)
                
            # print(len(lst1)
            # print(lst1) 
            # print(len(lst2))
            # print(lst2)  

            # print(len(lst3))
            # print(lst3)          


        # SPLITING KEYS FORM THE DATA FOR READINGS
        keys_list = list(lst1.values())
        # SPLITING KEYS FORM THE DATA FOR HEADINGS

        keys_list_value = list(lst2.values())


        #REMOVE BLANK SPACES FROM THE READINGS
        blank = ["          ", "          \n\n" , "          \n"]

        if keys_list_value[-1] in blank[0]:
                keys_list_value.remove(keys_list_value[-1])

        elif keys_list_value[-1] in blank[1]:
            
            keys_list_value.remove(keys_list_value[-1])

        elif keys_list_value[-1] in blank[2]:
                keys_list_value.remove(keys_list_value[-1])

            
            
        else:
            pass


        #FUNCTION FOR SPLITING THE VALUES FROM THE READINGS
        def split(a1):

            delimiters = ["          \n\n","          \n \n"]
            value1 = a1
            for delimiter in delimiters:
                value1 = " ".join(value1.split(delimiter))
                new_value1 = value1.split(" ")
                for i in new_value1[:]:
                    if i == "":
                        new_value1.remove(i)
                
            # print(new_value1)        
                        
            # new_result = []
            # for i in new_value1:
            #     new_result.extend(i)
                
            return new_value1




        # REMOVING NEW LINE FORM THE READNIGS
        var_stage=[]
        var_stage_readdings=[]

        delimiters = ["\n","\n\n","\n\n\n","\n\n\n\n",'\r','\r\n',':']
        def rnew(x):
            value1= x
            for delimiter in delimiters:
                value1 = " ".join(value1.split(delimiter))
                new_value1 = value1.split(" ")
                for i in new_value1[:]:
                    if i == "":
                        new_value1.remove(i)
            return new_value1

        for i in keys_list_value:
            var_stage.append(rnew(i))

        for i in keys_list:
            var_stage_readdings.append(rnew(i))
            
        # print(var_stage)
        # print(len(var_stage))


        # REMOVEING UNWANTED VALUES FROM THE READINGS
        def split(a1):

            delimiters = ["       ",":","    ", "   ","\n",'\r\n','\r',"                             "]
            value1 = a1
            for delimiter in delimiters:
                value1 = " ".join(value1.split(delimiter))
                new_value1 = value1.split(" ")
                for i in new_value1[:]:
                    if i == "":
                        new_value1.remove(i)
                
            # print(new_value1)        
                        
            # new_result = []
            # for i in new_value1:
            #     new_result.extend(i)
                
                return new_value1
        
        
        # COMPLETE REMOVED SPACES
        removed_final=[]

        for i in range(0,len(keys_list)):
            x = split(keys_list[i])
            removed_final.append(x)
            # print(removed_final[i])
            
        # print(removed_final)
        # print(len(removed_final))

    # FUNCTION FOR READING HEADING 
        def name(val,val_2):
            tit=val
            number = val_2

            if number == 3:
                title = var_stage[tit][0]+" "+var_stage[tit][1]+" "+(var_stage[tit][2])+"                                                            "
            elif number == 4:
                title = var_stage[tit][0]+" "+var_stage[tit][1]+" "+(var_stage[tit][2])+" "+(var_stage[tit][3])+"                                                            "
            elif number == 6:
                title = var_stage[tit][0]+" "+var_stage[tit][1]+" "+(var_stage[tit][2])+" "+(var_stage[tit][3])+" "+(var_stage[tit][4])+"  "+(var_stage[tit][5])+"                                                            "
        
            else:   
                title = var_stage[tit][0]+" "+var_stage[tit][1]+" "+(var_stage[tit][2])+" "+(var_stage[tit][3])+"  "+(var_stage[tit][4])+"                                                            "
            
            return title
    
       


        # correction of hole positons


        def OK_report(arguments):
        
            value_x=arguments
            print(value_x)
            nominal_1 = arguments
                
                
            poss = [0.007,0.011,0.016,0.023,0.032]
            neg = [-0.005,-0.010,-0.015,-0.025,-0.030]
            
            
            
            
            
            if value_x[5] == "0.001" or value_x[5] == "0.002":
                if value_x[5] == "0.001" :
                    value_x[5] = "0.000"
                    value_x[1] = value_x[1]
                    value_x[2]  = value_x[1]
                    
                if value_x[5] == "0.002" :
                    value_x[5] = "0.000"
                    value_x[1] = value_x[1]
                    value_x[2]  = value_x[1]
                
            elif value_x[5] == "-0.001" or value_x[5] == "-0.002":
                if value_x[5] == "-0.001" :
                    value_x[5] = "0.000"
                    value_x[1] = value_x[1]
                    value_x[2]  = value_x[1]
                    
                if value_x[5] == "-0.002" :
                    value_x[5] = "0.000"
                    value_x[1] = value_x[1]
                    value_x[2]  = value_x[1]
                
            nom= float(value_x[1])
            act= float(value_x[2])
            low_tol = value_x[3]
            upr_tol= value_x[4]
            x_front = f"  {value_x[0]}   :  "
            tol ="   "+ low_tol+"    "+upr_tol+"   "
            new_act_x = value_x[2]   
                    
            if value_x[5] == "0.000" :
                if "-" in str(nom):
                    if (nom > -1000.000) and (nom < -100.000):
                            return x_front + " "+str( "%.3f" % nom) + "   " +" "+str(new_act_x)+tol+" "+str(value_x[5])+"                             "
                
                    if (nom > -100.000) and (nom < -10.000):
                            return x_front + "  "+str( "%.3f" % nom) + "   " +"  "+str(new_act_x)+tol+" "+str(value_x[5])+"                             "
                    if (nom > -10.000) and (nom < -1.000):
                            return x_front + "   "+str( "%.3f" % nom) + "   " +"   "+str(new_act_x)+tol+" "+str(value_x[5])+"                             "

                        
                if (nom < 5000.000) and (nom >1000.000):
                    return x_front + " "+str("%.3f" % nom) + "   " +" "+str("%.3f" % act)+tol+" "+str(value_x[5])+"                             "      
                elif (nom < 1000.000) and (nom >100.000):
                    return x_front + "  "+str("%.3f" % nom) + "   " +"  "+str("%.3f" % act)+tol+" "+str(value_x[5])+"                             "
                elif (nom < 100.000) and (nom >10.000):
                    return x_front + "   "+str("%.3f" % nom) + "   " +"   "+str("%.3f" % act)+tol+" "+str(value_x[5])+"                             "
                elif (nom < 10.000) and (nom >1.000):
                    return x_front + "    "+str("%.3f" % nom) + "   " +"    "+str("%.3f" % act)+tol+" "+str(value_x[5])+"                             " 
                
                else:
                    return x_front + str("%.3f" % nom) + "   " +str("%.3f" % act)+tol+" "+str(value_x[5])+"                             "

            else:    
                    #print("new nom: ",value_x[1])
                    s_poss=random.choice(poss)
                    new_act_x = float(act) - float(s_poss)
                    # print(s_poss)
                    # print(type(new_act_x))
                    
                    new_act_x ="%.3f" % new_act_x
                    #print("new act: ",new_act_x)
                    new_dev_x=float(new_act_x)-float(nom)
                    new_dev_x= "%.3f" % new_dev_x
                    #print("new dev: ",new_dev_x)
                    
                    if float(new_dev_x) <= float(low_tol) or float(new_dev_x) >= float(upr_tol) or float(new_dev_x) <= 0.000:
                        
                            poss = [0.031,0.035,0.041,0.045]
                            neg = [-0.005,-0.011,-0.012,-0.015]
                            s_poss=random.choice(neg)
                            # print("rand",s_poss)
                            new_act_x = float(act) - float(s_poss)
                            new_act_x ="%.3f" % new_act_x
                            #print("new act",new_act_x)
                            new_dev_x=float(new_act_x)-float(nom)
                            new_dev_x= "%.3f" % new_dev_x
                            #print("new dev",new_dev_x)
                    else:
                    #     print("ok")
                            pass

                    if "-" in str(new_dev_x):
                        if "-" in str(nom):
                            if (nom > -1000.000) and (nom < -100.000):
                                return x_front+" "+str( "%.3f" % nom) + "   "+" "+str(new_act_x)+tol+str(new_dev_x)+"                             "
                            elif (nom > -100.000) and (nom < -10.000):
                                return x_front + "  "+str( "%.3f" % nom) + "   " +"  "+str(new_act_x)+tol+str(new_dev_x)+"                             "
                            elif (nom > -10.000) and (nom < -1.000):
                                return x_front + "   "+str( "%.3f" % nom) + "   " +"   "+str(new_act_x)+tol+str(new_dev_x)+"                             "
                            elif (nom > -1.000) and (nom < 0.000):
                                return x_front + "   "+str( "%.3f" % nom) + "   " +"   "+str(new_act_x)+tol+str(new_dev_x)+"                             "
                            
                        
                        else:
                            if (nom < 5000.000) and (nom >1000.000):
                                return x_front +" "+str( "%.3f" % nom) + "   " +" "+str(new_act_x)+tol+str(new_dev_x)+"                             "
                            elif (nom < 1000.000) and (nom >100.000):
                                return x_front + "  "+str( "%.3f" % nom) + "   " +"  "+str(new_act_x)+tol+str(new_dev_x)+"                             "
                            elif (nom < 100.000) and (nom >10.000):
                                return x_front + "   "+str( "%.3f" % nom) + "   " +"   "+str(new_act_x)+tol+str(new_dev_x)+"                             "
                            elif (nom < 10.000) and (nom >1.000):
                                return x_front + "    "+str( "%.3f" % nom) + "   " +"    "+str(new_act_x)+tol+str(new_dev_x)+"                             "
                            elif (nom <= 0.000) and (nom >-1.000):
                                return x_front + "    "+str( "%.3f" % nom) + "   " +"   "+str(new_act_x)+tol+str(new_dev_x)+"                             "
        
                    
                    else:
                            new_dev_x = new_dev_x 
                        
                    if "-" not in str(new_dev_x):
                        if (nom < 5000.000) and (nom >1000.000):
                            return x_front +" "+str( "%.3f" % nom) + "   " +" "+str(new_act_x)+tol+" "+str(new_dev_x)+"                             "
                        if (nom > 1000.000) and (nom >900.000):
                            return x_front + "  "+str( "%.3f" % nom) + "   " +"  "+str(new_act_x)+tol+" "+str(new_dev_x)+"                             "
                        
                        if (nom < 1000.000) and (nom >100.000):
                            return x_front + "  "+str( "%.3f" % nom) + "   " +"  "+str(new_act_x)+tol+" "+str(new_dev_x)+"                             "
                        
                        elif (nom < 100.000) and (nom >10.000):
                            return x_front + "   "+str( "%.3f" % nom) + "   " +"   "+str(new_act_x)+tol+" "+str(new_dev_x)+"                             "
                        elif (nom < 10.000) and (nom >1.000):
                            return x_front + "    "+str( "%.3f" % nom) + "   " +"    "+str(new_act_x)+tol+" "+str(new_dev_x)+"                             "
                        
                        elif "-" in str(nom):
                            if (nom > -5000.000) and (nom < -1000.000):
                                return x_front +str( "%.3f" % nom) + "   " +str(new_act_x)+tol+" "+str(new_dev_x)+"                             "
                            if (nom > -1000.000) and (nom < -100.000):
                                return x_front +" "+str( "%.3f" % nom) + "   " +" "+str(new_act_x)+tol+" "+str(new_dev_x)+"                             "
                            if (nom > -100.000) and (nom < -10.000):
                                return x_front + "  "+str( "%.3f" % nom) + "   " +"  "+str(new_act_x)+tol+" "+str(new_dev_x)+"                             "
                            if (nom > -10.000) and (nom < -1.000):
                                return x_front + "   "+str( "%.3f" % nom) + "   " +"   "+str(new_act_x)+tol+" "+str(new_dev_x)+"                             "
                            if (nom > -1.000) and (nom < 0.000):
                                return x_front + "  "+str( "%.3f" % nom) + "   " +"  "+str(new_act_x)+tol+" "+str(new_dev_x)+"                             "                    
                            
                            
                    if "-" in str(nom):
                        if (nom > -5000.000) and (nom < -1000.000):
                            return x_front +str( "%.3f" % nom) + "   " +str(new_act_x)+tol+str(new_dev_x)+"                             "
                        elif (nom > -1000.000) and (nom < -100.000):
                            return x_front + "  "+str( "%.3f" % nom) + "   " +"  "+str(new_act_x)+tol+str(new_dev_x)+"                             "
                        
                        
                            
                            
                    

            # print(x_front)
            # print(len(x_front))
            
            # print(inputs_x)
            # print(len(inputs_x))

            return x_front + str(nom) + "   " +(new_act_x)+tol+(new_dev_x)+"                             "
            # print(slice_x)
                


        # # print(removed_final[2])
        x1=OK_report(var_stage_readdings[3])
        # y1=OK_report(removed_final[4])
        # z1=OK_report(removed_final[5])


        #print(len(x1))
        #print(len(y1))

        # print(x1)
        # print(y1)
        # print(z1)




        # correction of surface and trim points

        def OK_report_points(arguments):
                
            value_x=arguments
            print(value_x)
            nominal_1 = arguments
                
                
            poss = [0.012,0.013]
            neg = [-0.005,-0.010,-0.015,-0.025,-0.030]
            
            
            
            
            
            if value_x[5] == "0.001" or value_x[5] == "0.002":
                if value_x[5] == "0.001" :
                    value_x[5] = "0.000"
                    value_x[1] = value_x[1]
                    value_x[2]  = value_x[1]
                    
                if value_x[5] == "0.002" :
                    value_x[5] = "0.000"
                    value_x[1] = value_x[1]
                    value_x[2]  = value_x[1]
                
            elif value_x[5] == "-0.001" or value_x[5] == "-0.002":
                if value_x[5] == "-0.001" :
                    value_x[5] = "0.000"
                    value_x[1] = value_x[1]
                    value_x[2]  = value_x[1]
                    
                if value_x[5] == "-0.002" :
                    value_x[5] = "0.000"
                    value_x[1] = value_x[1]
                    value_x[2]  = value_x[1]
                
            nom= float(value_x[1])
            act= float(value_x[2])
            low_tol = value_x[3]
            upr_tol= value_x[4]
            x_front = f"  {value_x[0]}   :  "
            tol ="   "+ low_tol+"    "+upr_tol+"   "
            new_act_x = value_x[2]   
                    
            if value_x[5] == "0.000" :
                if "-" in str(nom):
                    if (nom > -5000.000) and (nom < -1000.000):
                            return x_front +str( "%.3f" % nom) + "   " +str(new_act_x)+tol+" "+str(value_x[5])+"                             "
                    elif (nom > -1000.000) and (nom < -100.000):
                            return x_front + " "+str( "%.3f" % nom) + "   " +" "+str(new_act_x)+tol+" "+str(value_x[5])+"                             "
                
                    if (nom > -100.000) and (nom < -10.000):
                            return x_front + "  "+str( "%.3f" % nom) + "   " +"  "+str(new_act_x)+tol+" "+str(value_x[5])+"                             "
                    elif (nom > -10.000) and (nom < -1.000):
                            return x_front + "   "+str( "%.3f" % nom) + "   " +"   "+str(new_act_x)+tol+" "+str(value_x[5])+"                             "
                    elif (nom > -1.000) and (nom < -0.0000):
                            return x_front + "   "+str( "%.3f" % nom) + "   " +"   "+str(new_act_x)+tol+" "+str(value_x[5])+"                             "
                        
                if (nom < 5000.000) and (nom >1000.000):
                    return x_front + " "+str("%.3f" % nom) + "   " +" "+str("%.3f" % act)+tol+" "+str(value_x[5])+"                             "
                elif (nom < 1000.000) and (nom >100.000):
                    return x_front + "  "+str("%.3f" % nom) + "   " +"  "+str("%.3f" % act)+tol+" "+str(value_x[5])+"                             "
                elif (nom < 100.000) and (nom >10.000):
                    return x_front + "   "+str("%.3f" % nom) + "   " +"   "+str("%.3f" % act)+tol+" "+str(value_x[5])+"                             "
                elif (nom < 10.000) and (nom >1.000):
                    return x_front + "    "+str("%.3f" % nom) + "   " +"    "+str("%.3f" % act)+tol+" "+str(value_x[5])+"                             " 
                
                else:
                    return x_front + str("%.3f" % nom) + "   " +str("%.3f" % act)+tol+" "+str(value_x[5])+"                             "

            else:    
                    #print("new nom: ",value_x[1])
                    
                poss=[0.005,0.006,0.007]
                neg=[-0.005,-0.006,-0.007]
                
                s_poss=random.choice(neg)
                s_neg=random.choice(poss)
                
                # print(type(value_x[5]))
                # print(s_poss)


                if "-" in str(value_x[5]):
                    
                    new_act_x = float(act) - float(s_poss)
                    # print("act: ",new_act_x)
                    new_dev_x = float(new_act_x) - float(nom)
                    # print("dev: ","%.3f" % new_dev_x)
                    if "-" not in str(new_dev_x):
                        new_act_x = float(act) - 0.001
                        new_dev_x = float(new_act_x) - float(nom)
                        
                    
                elif "-" not in str(value_x[5]):
                    
                    new_act_x = float(act) + float(s_neg)
                    # print("act: ",new_act_x)
                    new_dev_x = float(new_act_x) - float(nom)
                    # print("dev: ","%.3f" % new_dev_x)
                    if "-" in str(new_dev_x):
                        new_act_x = float(act) + 0.001
                        new_dev_x = float(new_act_x) + float(nom)

                    
                else:
                    pass
                    
                # print(type(new_dev_x))   
                    
                if (new_dev_x) >= float(upr_tol) or (new_dev_x) <= float(low_tol) or new_dev_x == 0.000:
                    poss=-0.004
                    new_act_x = float(act) - float(poss)
                    # print("act: ",new_act_x)
                    new_dev_x = float(new_act_x) - float(nom)
                    # print("dev: ","%.3f" % new_dev_x)
                        
                    
                new_act_x =  "%.3f" %  new_act_x  
                new_dev_x =  "%.3f" % new_dev_x          



                if "-" in str(new_dev_x):
                    if "-" in str(nom):
                        if (nom > -1000.000) and (nom < -100.000):
                            return x_front+" "+str( "%.3f" % nom) + "   "+" "+str(new_act_x)+tol+str(new_dev_x)+"                             "
                        elif (nom > -100.000) and (nom < -10.000):
                            return x_front + "  "+str( "%.3f" % nom) + "   " +"  "+str(new_act_x)+tol+str(new_dev_x)+"                             "
                        elif (nom > -10.000) and (nom < -1.000):
                            return x_front + "   "+str( "%.3f" % nom) + "   " +"   "+str(new_act_x)+tol+str(new_dev_x)+"                             "

                    
                    else:
                        if (nom < 5000.000) and (nom >1000.000):
                            return x_front +" "+str( "%.3f" % nom) + "   " +" "+str(new_act_x)+tol+str(new_dev_x)+"                             "
                        elif (nom < 1000.000) and (nom >100.000):
                            return x_front + "  "+str( "%.3f" % nom) + "   " +"  "+str(new_act_x)+tol+str(new_dev_x)+"                             "
                        elif (nom < 100.000) and (nom >10.000):
                            return x_front + "   "+str( "%.3f" % nom) + "   " +"   "+str(new_act_x)+tol+str(new_dev_x)+"                             "
                        elif (nom < 10.000) and (nom >1.000):
                            return x_front + "    "+str( "%.3f" % nom) + "   " +"    "+str(new_act_x)+tol+str(new_dev_x)+"                             "
                
                else:
                        new_dev_x = new_dev_x 
                    
                if "-" not in str(new_dev_x):
                    if (nom < 5000.000) and (nom >1000.000):
                        return x_front +" "+str( "%.3f" % nom) + "   " +" "+str(new_act_x)+tol+" "+str(new_dev_x)+"                             "
                    if (nom < 1000.000) and (nom >100.000):
                        return x_front + "  "+str( "%.3f" % nom) + "   " +"  "+str(new_act_x)+tol+" "+str(new_dev_x)+"                             "
                    elif (nom < 100.000) and (nom >10.000):
                        return x_front + "   "+str( "%.3f" % nom) + "   " +"   "+str(new_act_x)+tol+" "+str(new_dev_x)+"                             "
                    elif (nom < 10.000) and (nom >1.000):
                        return x_front + "    "+str( "%.3f" % nom) + "   " +"    "+str(new_act_x)+tol+" "+str(new_dev_x)+"                             "
                    
                    elif "-" in str(nom):
                        if (nom > -5000.000) and (nom < -1000.000):
                            return x_front +str( "%.3f" % nom) + "   " +str(new_act_x)+tol+" "+str(new_dev_x)+"                             "
                        if (nom > -1000.000) and (nom < -100.000):
                            return x_front +" "+str( "%.3f" % nom) + "   " +" "+str(new_act_x)+tol+" "+str(new_dev_x)+"                             "
                        if (nom > -100.000) and (nom < -10.000):
                            return x_front + "  "+str( "%.3f" % nom) + "   " +"  "+str(new_act_x)+tol+" "+str(new_dev_x)+"                             "
                        if (nom > -10.000) and (nom < -1.000):
                            return x_front + "   "+str( "%.3f" % nom) + "    " +"  "+str(new_act_x)+tol+" "+str(new_dev_x)+"                             "
                        
                            
                        
                if "-" in str(nom):
                    if (nom > -5000.000) and (nom < -1000.000):
                        return x_front +str( "%.3f" % nom) + "   " +str(new_act_x)+tol+str(new_dev_x)+"                             "
                    elif (nom > -1000.000) and (nom < -100.000):
                        return x_front + "  "+str( "%.3f" % nom) + "   " +"  "+str(new_act_x)+tol+str(new_dev_x)+"                             "
                    
                            
                                
                                
                        

                # print(x_front)
                # print(len(x_front))
                
                # print(inputs_x)
                # print(len(inputs_x))

                return x_front + str(nom) + "   " +(new_act_x)+tol+(new_dev_x)+"                             "
                # print(slice_x)
                    



        # x1=OK_report_points(removed_final[21])
        # y1=OK_report_points(removed_final[22])
        # z1=OK_report_points(removed_final[23])


        # #print(len(x1))
        # #print(len(y1))

        # print(x1)
        # print(y1)
        # print(z1)





        keys_list_2 = list(lst1.values())



        blank = ["          ", "          \n\n" , "          \n"]

        if keys_list_2[-1] in blank[0]:
                keys_list_2.remove(keys_list_2[-1])

        elif keys_list_2[-1] in blank[1]:
            
            keys_list_2.remove(keys_list_2[-1])

        elif keys_list_2[-1] in blank[2]:
                keys_list_2.remove(keys_list_2[-1])

            
            
        else:
            pass



        counter=0
        counter_2=0
        remover = []
        # remover_2 = []
        newline = "\n"
        for j in range(0,len(keys_list_value)):
            counter_2 = counter_2+1   
            if "POINT" in keys_list_value[j]:
                break
                
            
            else:    
                title = name(j,len(var_stage[j]))
                remover.append((title))
                for i in range(0,3):
                    x =OK_report(var_stage_readdings[counter])
                    remover.append(x)
                    
                    if i == 2:
                        remover.append(" ")
                    counter=counter+1


        for k1 in range(counter_2-1,(len(keys_list_value))):
            title = name(k1,len(var_stage[k1]))
            remover.append((title))
            
            for l1 in range(0,3):
                if counter == len(removed_final):
                        break 
                else:
                    x =OK_report_points(var_stage_readdings[counter])
                    remover.append(x)
                    
                    if l1 == 2:
                        remover.append(" ")
                        
                    counter=counter+1


                    # if i != 3:
                #     x =OK_report(removed_final[counter])+newline
                #     remover.append(x)

                # else:
                #     x = newline+OK_report(removed_final[counter])+newline
                #     print(newline)
                #     remover.append(x)
                
            
            # print(remover)



        final_stage=[]
        deli=["\n","\n\n","\n\n\n"]
        for i in remover:
                
                final_stage.append(i)
                
        print(final_stage)


        report_details = open('JBM_OK_REPORTS/CIMTRIX_WORD_FILE.txt', encoding='utf8')
        report_data = report_details.read()
        report_details.close()
        report_data

        
        TODAYSDATE=request.form.get('PRG_DATE')
        Operater_name=request.form.get('OPERATOR')
        Gauge_name=request.form.get('PART_NAME')
        PRG_NUMBER=request.form.get('PART_NUMBER')
        Gauge_number=request.form.get('Gauge_Number')













        if Gauge_name == "":
                style=f"""
DATE           : {TODAYSDATE}                                                           
COMPANY        : JBMA                                                                 
OPERATOR       : {Operater_name}                                                                
CMM NAME       : CMM CNC                                                                                                           
REPORT NO      : JBMAS/QAC/F-26B                                                      
PART NUMBER    : {PRG_NUMBER}                                                
COMMENT        : PANEL CHECKER VALIDATION-(KJ/QA/PC/{Gauge_number})                              
------------------------------------------------------------------------------------- 
ELEM#      NOMINAL     ACTUAL    LOW_TOL  UPP_TOL    DEV  OUT_OF_TOL   CONTROL        
------------------------------------------------------------------------------------- """.format()

        else:
                style=f"""
DATE           : {TODAYSDATE}                                                           
COMPANY        : JBMA                                                                 
OPERATOR       : {Operater_name}                                                                
CMM NAME       : CMM CNC                                                              
PART NAME      : {Gauge_name}                                             
REPORT NO      : JBMAS/QAC/F-26B                                                      
PART NUMBER    : {PRG_NUMBER}                                                
COMMENT        : PANEL CHECKER VALIDATION-(KJ/QA/PC/{Gauge_number})                              
------------------------------------------------------------------------------------- 
ELEM#      NOMINAL     ACTUAL    LOW_TOL  UPP_TOL    DEV  OUT_OF_TOL   CONTROL        
------------------------------------------------------------------------------------ """.format()                                                       
            

        
        
        
        file_final = open((f'JBM_OK_REPORTS/BINFILES/{PRG_NUMBER}.txt').format(PRG_NUMBER),'w')



        for ITEM in style:
                file_final.write(ITEM)
        file_final.write("\n")       
                        
        # file.writelines(final_stage)
        for items in remover:
                file_final.write('%s\n' %items)
                

        file_final.close()



        file_01 = open((f'JBM_OK_REPORTS/BINFILES/{PRG_NUMBER}.txt').format(PRG_NUMBER), encoding='utf8')
        file_1 = file_01.read()
        file_01.close()

        # remove trashfiels
        
        import os 

        rep=PRG_NUMBER
        removethefile = open((f'JBM_OK_REPORTS/BINFILES/{rep}.txt').format(), encoding='utf8')
        file_11 = removethefile.read()
        removethefile.close()
        print(removethefile)
        if os.path.exists(f'JBM_OK_REPORTS/BINFILES/{rep}.txt'): 
            os.remove(f'JBM_OK_REPORTS/BINFILES/{rep}.txt')


        return render_template('result.html',reading1=file_1,read=inputs_01)



if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)
    






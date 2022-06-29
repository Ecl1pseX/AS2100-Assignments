#!/usr/local/bin/python3.9

# Pranit Zope
# AE20B046
# Task 2 : Linear Regression of a given Data

import numpy as np
from matplotlib import pyplot as plt

class matrixoperations(): #this class contains all functions that involve matrix operations

    def determinant(m):
        det=m[0][0]*m[1][1]-m[0][1]*m[1][0]
        return det

    def inverse(m):
        inv=np.zeros((2,2))
        inv[0][0]=m[1][1]/matrixoperations.determinant(m)
        inv[0][1]=-1*(m[0][1]/matrixoperations.determinant(m))
        inv[1][0]=-1*(m[1][0]/matrixoperations.determinant(m))
        inv[1][1]=(m[0][0]/matrixoperations.determinant(m))

        return inv

class linearregression():  #this class contains all functions which we will need for doing the liniear reggression of a data

    def solution(start,end,file):  #with the help of this funciton we find the solution, i.e m and c for the line that will be the best fitting line
        a1=np.ones(end-start)
        a2=np.loadtxt(file,usecols=(0,),skiprows=start,max_rows=end-start)
        
        A=np.stack([a1,a2],axis=1)

        AT=np.matrix.transpose(A)
        B=np.loadtxt(file,usecols=(1,),skiprows=start,max_rows=end-start)


        AT_B=np.zeros(2)
        for i in range(0,2):
            for j in range(0,1):
                tempsum=0
                for k in range(0,end-start):
                    tempsum=tempsum+AT[i][k]*B[k]
            
                AT_B[i]=tempsum


        AT_A=np.zeros((2,2))
        for i in range(0,2):
            for j in range(0,2):
                tempsum=0
                for k in range(0,end-start):
                    tempsum=tempsum+AT[i][k]*A[k][j]
                AT_A[i][j]=tempsum

        AT_Ainv=matrixoperations.inverse(AT_A)

        ATAinv_ATB=np.zeros(2)
        for i in range(2):
            for j in range(1):
                tempsum=0
                for k in range(2):
                    tempsum=tempsum+AT_Ainv[i][k]*AT_B[k]
                ATAinv_ATB[i]=tempsum
        
        return ATAinv_ATB


    def graph(start,end,file,dataset_no,fig_no):    #with the help of this function, we can plot the given data as well as the line we got in the sloution function.
        xy=np.loadtxt(file,usecols=(0,1),skiprows=start,max_rows=end-start)

        sol=linearregression.solution(start,end,file)
        m=sol[1]
        c=sol[0]

        x=np.linspace(start,end,100)
        y=m*x+c

        plt.plot(xy[:,0],xy[:,1],label='Given Dataset',marker=".",markersize="5")
        plt.plot(x,y,label='Best fitting line: y='+str(round(m,3))+'x+('+str(round(c,3))+')')
        filename=file[0]+file[1]+file[2]+file[3]+file[4]

        plt.xlabel('X')
        plt.ylabel('Y')

        plt.title(filename+ " : Row "+str(start+1)+" to "+str(end))
        
        plt.legend(loc="lower right")

        plt.grid(linestyle='--')
        plt.savefig("plot."+str(dataset_no)+"."+str(fig_no)+".png")
        
        plt.clf()


    def error(start,end,file):  #with the help of this funciton, we can find the errors in respectve datasets

        x=np.loadtxt(file,usecols=(0,),skiprows=start,max_rows=end-start)
        y1=np.loadtxt(file,usecols=(1,),skiprows=start,max_rows=end-start)
        sol=linearregression.solution(start,end,file)
        m=sol[1]
        c=sol[0]

        final_err=0
        for i in range(end-start):
            y2=m*x[i]+c
            final_err=final_err+(y1[i]-y2)*(y1[i]-y2)
    
        return np.sqrt(final_err)



#Here we will define what our "files" are going to be
data1="data1.txt"
data2="data2.txt"
data3="data3.txt"


#Here, we will calculate the errors in respective dataset and print it
error_value=[]
error_value.append(linearregression.error(0,50,data1))
error_value.append(linearregression.error(50,100,data1))
error_value.append(linearregression.error(100,200,data1))
error_value.append(linearregression.error(0,200,data1))

error_value.append(linearregression.error(0,50,data2))
error_value.append(linearregression.error(50,100,data2))
error_value.append(linearregression.error(100,200,data2))
error_value.append(linearregression.error(0,200,data2))

error_value.append(linearregression.error(0,50,data3))
error_value.append(linearregression.error(50,100,data3))
error_value.append(linearregression.error(100,200,data3))
error_value.append(linearregression.error(0,200,data3))

print("Errors for each Part (Dataset,Figure) : "+str(error_value))


#Lastly, here, we will plot the actual dataset in points and the line that we found by using the matrix method
linearregression.graph(0,50,data1,1,1)
linearregression.graph(50,100,data1,1,2)
linearregression.graph(100,200,data1,1,3)
linearregression.graph(0,200,data1,1,4)

linearregression.graph(0,50,data2,2,1)
linearregression.graph(50,100,data2,2,2)
linearregression.graph(100,200,data2,2,3)
linearregression.graph(0,200,data2,2,4)

linearregression.graph(0,50,data3,3,1)
linearregression.graph(50,100,data3,3,2)
linearregression.graph(100,200,data3,3,3)
linearregression.graph(0,200,data3,3,4)



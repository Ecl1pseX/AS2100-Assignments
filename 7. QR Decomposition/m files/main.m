# Pranit Zope
# AE20B046 
# AS2101 Task 07


#importing data
data=importdata("data2.txt");

#Making it in the form AX=B for solving
#initially A in the form of [x1 1; x2 1;....]
A=columnvec(data,1);
A=[A,ones(size(data)(1),1)];

#finding initial B [y1; y2; y3....]
B=columnvec(data,2);

#For converting it into square matrix, we multiply by A Transpose
B=transpose(A)*B;
A=transpose(A)*A;

#AX=B
[Q1,R1]=manual(A);
[Q2,R2]=qr(A);

#solution
x1=backsub(A,B,Q1,R1)

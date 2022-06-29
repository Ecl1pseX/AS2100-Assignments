# Pranit Zope
# AE20B046 
# AS2101 Task 07

function [Q,R] = manual (A)
[m,n]=size(A); #size of matrix
Q=[];
R=zeros(m);#initialising a zero matrix
for i=1:m
  q_temp=columnvec(A,i);
  for j=1:i-1
    q_temp-=dotprod(columnvec(Q,j),columnvec(A,i)).*columnvec(Q,j);
  endfor
    q_temp/=sqrt(dotprod(q_temp,q_temp));
    Q=[Q, q_temp];
endfor

for i=1:m

for j=i:m
    R(i,j)=(dotprod(columnvec(A,j),columnvec(Q,i)));
endfor
endfor
endfunction #end
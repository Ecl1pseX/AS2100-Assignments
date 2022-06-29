# Pranit Zope
# AE20B046 
# AS2101 Task 07

function x = backsub(A,B,Q,R)

m=size(A)(1,1);
RX=transpose(Q)*B;
x=zeros(m,1);
for i=m:-1:1
  x(i,1)+=RX(i,1);
  for j=i+1:m
    x(i,1)-=R(i,j)*x(j,1);
endfor
  x(i,1)/=R(i,i);
endfor

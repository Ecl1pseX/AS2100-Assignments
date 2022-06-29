# Pranit Zope
# AE20B046 
# AS2101 Task 07



function a = columnvec(A, i)
[p,q]=size(A);
a=[];

for j=1:p
  a=[a;A(j,i)];
endfor
endfunction

# Pranit Zope
# AE20B046 
# AS2101 Task 07

function A = randommatrix (n)
V=rand(n,1);
A= eye(n)-V*transpose(V);
endfunction

//2020BTEIT00061 ABHISHEK DEOKAR

Observation:
1) We are taking the values of votes as input in thousands, and using the amount to be spent for advertisement of policies  
   and using this 2 matrix calculating the amount to be spent on each policy 


2)  For LU decomposition , AB = X  
    We are taking the values of A as Build Roads   : -2, 5, 3, 6
				     Infrastructure: 8, 2, -5, -2
       				     Farm subsidies: 1, 3, 10, 4
                                     Fuel price    : 10, 6, -2, 5

   X, number of votes is taken as input
   We need to calculate B, amount to be spent on advertisment of different policies to win the election.

2) Terms of U matrix are given by:

   For all j
            	i=0 
		U_{ij} = A_{ij}
		
		i>0 
		U_{ij} = A_{ij} - Σ {i-1} {k=0}  L_{ik}U_{kj}             

And the terms for L matrix:

 For all i
		 j=0 
		 L_{ij} = A_{ij}/U_{jj}
		 j>0 
		 L_{ij} = A_{ij} - Σ {k=0}^{j-1}L_{ik}U_{kj}} / {U_{jj}}  

3) We can make the code parallel by assigning 2 processors , task to compute each Lower and Upper matrix . Both of the matrix are independently
   solvable and can be computed by each of the processor .


4 ) Time complexity for this LU decomposition is O(n^3) 

To install mpi
sudo apt install mpich

To run using mpi
mpicc file.c -o file
mpirun -np 4 ./file

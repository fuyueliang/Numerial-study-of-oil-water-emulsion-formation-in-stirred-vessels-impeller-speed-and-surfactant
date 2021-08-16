#!/bin/bash
#PBS -N CONVERT
#PBS -o CONVERT.out
#PBS -j oe
#PBS -lselect=1:ncpus=48:mem=100gb
#PBS -lwalltime=12:00:00
set -vx
cd $PBS_O_WORKDIR
module purge
module load anaconda3/personal
source activate vtkenv
python Multithread_pool.py && mv *.vtk VTK_SAVE
echo "... Run finished @ $(date) with error code $OK ..."

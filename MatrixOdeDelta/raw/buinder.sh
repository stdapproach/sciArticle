#!/bin/bash
# This is a comment
whoami
#copy /b Abstract.md + 0_Introduction.md solveLinearOdeDeltaFunction.md
cat Abstract.md \
	2_LinearAlgebra_intro.md \
	2_1_LinearEquations.md \
	2_2_Matrix_Algebra.md \
	2_3_Determinants.md \
	2_4_Eigen.md \
	2_5_Decomposition.md \
	2_6_Exponent.md \
	Appendix_A_Series_and_parallel_springs.md \
	References.md >| matrixOdeDelta.md


#haroopad -f solveLinearOdeDeltaFunction.md
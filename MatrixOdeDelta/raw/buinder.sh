#!/bin/bash
# This is a comment
whoami
#copy /b Abstract.md + 0_Introduction.md solveLinearOdeDeltaFunction.md
cat Abstract.md \
	2_LinearAlgebra_intro.md \
	2_1_LinearEquations.md \
	Appendix_A_Series_and_parallel_springs.md \
	References.md >| matrixOdeDelta.md


#haroopad -f solveLinearOdeDeltaFunction.md
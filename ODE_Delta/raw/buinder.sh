#!/bin/bash
# This is a comment
whoami
#copy /b Abstract.md + 0_Introduction.md solveLinearOdeDeltaFunction.md
cat Abstract.md \
	0_Introduction.md \
	1_Definition.md \
	2_FirstGlimpse.md \
	3_ProblemType0.md \
	4_VerificationType0.md \
	AppendixA.md \
	AppendixB.md \
	References.md >| solveLinearOdeDeltaFunction.md


#haroopad -f solveLinearOdeDeltaFunction.md
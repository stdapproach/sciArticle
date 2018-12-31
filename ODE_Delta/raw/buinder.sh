#!/bin/bash
# This is a comment
whoami
#copy /b Abstract.md + 0_Introduction.md solveLinearOdeDeltaFunction.md
cat Abstract.md \
	0_Introduction.md \
	1_Definition.md \
	2_FirstGlimpse.md \
	AppendixA.md \
	AppendixB.md >| solveLinearOdeDeltaFunction.md


#haroopad -f solveLinearOdeDeltaFunction.md
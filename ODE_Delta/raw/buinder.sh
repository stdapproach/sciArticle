#!/bin/bash
cat _Abstract.md \
	0_Introduction.md \
	1_Definition.md \
	2_FirstGlimpse.md \
	2prim_bookReview.md \
	3_ProblemType0.md \
	4_VerificationType0.md \
	5_ProblemType1.md \
	6_VerificationType1.md \
	AppendixA.md \
	AppendixB.md \
	AppendixC.md \
	References.md >| solveLinearOdeDeltaFunction.md

#haroopad -f solveLinearOdeDeltaFunction.md

#pandoc Abstract.md -o output.pdf -V fontsize=12pt
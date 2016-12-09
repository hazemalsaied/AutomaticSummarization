Using the CRFs approaches , we prove that it outperformed the character- based method using the CRF approaches . 
This approach is effective for performing desired segmentation based on user requirements to R-oov and R-iv . 
We also successfully employed the confidence measure to make a confidence-dependent word segmentation . 
Under the scheme , each character of a word is labeled as âBâ if it is the first character of a multiple-character word , or âOâ if the character functions as an independent word , or âIâ otherwise For example , â ( whole ) ( Beijing city ) â is labeled as â ( whole ) /O ( north ) /B ( capital ) /I ( city ) /Iâ . 
In this work , we proposed a subword-based IOB tagging method for Chinese word segmentation . 
Even with the use of confidence measure , the word- based IOB tagging still outperformed the character-based IOB tagging . 
Each sub Word is given a prior IOB tags , tw . C Miob ( t|w ) , a ï£« M ï£«ï£¶ï£¶ confidence probability derived in the process of IOB tags exp ï£¬ ) ' ï£¬ ) ' Î»k fk ( tiâ1 ti , W ) + ) ' Âµk gk ( ti , W ) ï£·ï£· , ï£¬ï£­ ï£¬ï£­ k ï£·ï£¸ ( 1 ) gin is defined as Z = ) ' T =t0 t1 Â·Â·Â·tM 
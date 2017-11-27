# SkillsData

getData.py: Query Jive API to download every SEI person's resume

Argument[1]: Jive user name
Argument[2]: Jive password

Not in code: convert resumes to .txt. 
 - docx: for f in *.docx; do textutil -convert txt "$f"; done
 - pdf: for f in *.pdf; do pdftotext "$f" "$f".txt; done
 - doc: Open in word and convert to docx. Very few resumes are doc. 

For pdf files (very few are pdf), it is necessary to go into file and remove new lines within paragraphs / spacing. During the conversion, to keep the formatting, the conversion tool adds new lines to maintain the spacing of the document for long lines. For the parsing to work, the spacing should not include these. 

There are few PDFs, and most are docx. Going forward, it would be best if all resumes were docx. 

Another enhancement that needs to be made - some resumes include sub-sections within the skills to designate "sub-categories" or "level of skill". These need to be added into the logic so they are parsed correctly. 

getAttributes.py: Parse through the resumes and build either a JSON or flattened CSV of all the skills to person. 

Enhancement needs: 
1. Add user name column generated from the name
2. Add sub-sections above
3. Designate JSON or CSV by python argument vs. commenting out lines of code
4. Update Education parsing (different than other skills) 

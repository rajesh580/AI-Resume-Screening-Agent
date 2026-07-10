from parser import extract_text_from_pdf

resume = extract_text_from_pdf("resumes/res.pdf")

print(resume)
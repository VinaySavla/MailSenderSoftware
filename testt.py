
# import pandas as pd

# val=[]
# data = pd.read_excel("Book1.xlsx")
# email=""
# for name in data:
#     val.append(str(name))
    

#     print(name)

# print(val)
# for i in val:
#     if i=='Email' or i=='email' or i=='EMAIL':
#         email=i
#         print(email+"#######")



# zz=[]
# for sel in val:
    

#     # a=(data[sel].astype(str))
#     zz.append((data[sel].astype(str)))
    

    
    

# # print(zz)

# print(len(val))
# print(len(zz[0]))

# data.iloc[[1]]
# print(data.iloc[[0]])


# # for i in range(len(val)):
# #     for j in zz[i]:
# #         if 'nan' in j or 'NaN' in j:
# #                     j = "unknown"
# #         print(j)
    

# df = pd.read_excel('Book1.xlsx')

# l1 = []

# for index, row in df.iterrows():
#     l1.append(row.to_list())

# print(l1[0])
# print(len(l1[0]))


# for i in l1[2]:
#     i=str(i)
#     if 'nan' in i or 'NaN' in i:
#         i = "unknown"
#     print(i)






# from docx import Document

# document = Document("tempalate.docx")
# paragraph = document
# # print(paragraph)

# # paragraph.text = "Willem Hendrik"
# document.save("resume_edited.docx")

# # z.save("tempalate1111.docx")


# document = Document('mail_resume_body.docx')

# for paragraph in document.paragraphs:
#     for run in paragraph.runs:
#         # print(run.text)
#         if run.bold:
#             print(run.text)

with open("html_file.html",'r') as pdf:
    data = pdf.readlines()
    print(data)
    all_text = ""
    for line in data:
        # line = line.replace("\n","")
        all_text = all_text+line
    print(all_text)
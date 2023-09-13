from PyPDF2 import PdfReader

# def acc_cxldate_puller(str):

if __name__ == '__main__':
    reader = PdfReader("report_1P.pdf")

    #These two lists will be storing account number and cancellation date
    account=list()
    cxl_date=list()
    for page in reader.pages:
    # page = reader.pages[0]
        textt=page.extract_text()

        # print(type(textt))
        textt = textt.replace("\n", " ")
        print(textt)
        
        flag=0

        #Extracting account numbers
        for idx in range(0, len(textt)):
            next_nine_char_str=textt[idx : idx+9]
            if(next_nine_char_str.isnumeric()):
                account.append(next_nine_char_str)
                idx+=9

        #Extracting cancellation dates
        for idx in range(0, len(textt)-5):
            if((textt[idx]=='/' and textt[idx+2]=='/')):
                if(flag==1 ):
                    if(textt[idx-2].isnumeric()):
                        cxl_date.append(textt[idx-2:idx+5])
                    else:
                        cxl_date.append(textt[idx-1:idx+5])
                flag=flag^1
                # print(flag)
            elif((textt[idx]=='/' and textt[idx+3]=='/')):
                if(flag==1 ):
                    if(textt[idx-2].isnumeric()):
                        cxl_date.append(textt[idx-2:idx+6])
                    else:
                        cxl_date.append(textt[idx-1:idx+6])
                flag=flag^1
                # print(flag)
        #To remove the extra one date coming through footer/description of EVERY page        
        cxl_date.pop()
    
    if(len(account)!=len(cxl_date)):
        print("Data is mismatched")
            
    print("Total number of cancellation", len(account))

    for idx in range(0, len(cxl_date)):
        print(account[idx], cxl_date[idx])
    
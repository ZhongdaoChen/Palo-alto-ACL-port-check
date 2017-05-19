
import xlrd
#fname = "ACLcheck.xlsx"
bk = xlrd.open_workbook("ExportedACL.xlsx")
filerange = range(bk.nsheets)
try:
    sh = bk.sheet_by_name("sheet1")
except:
    print("File name or sheet name error")
nrows = sh.nrows
ncols = sh.ncols

#cell_value = sh.cell_value(7,17)
#print(type(cell_value))

service_wont_check = ["www", "https", "ssh", "smtp", "application-default", "domain", "tcp-53", "ntp", "http-all",
                      "UDP-ANY", "ldaps", "ftp", "service-http", "tcp-80", "TCP-ANY"]
#if you wanna skip any port, add it here
fp = open('port_to_check.txt', 'w')
addr_port_pair = []
for i in range (28,nrows):
    service_info = sh.cell_value(i,17)
    service_list = service_info.split("\n")
    for j in service_list:
        if j != "" and j not in service_wont_check and [sh.cell_value(i,14),service_info] \
                not in addr_port_pair and "udp" not in j and sh.cell_value(i, 11) != "disabled" and sh.cell_value(i, 14) \
                != "Any":
            #print(service_info)
            addr_port_pair.append([sh.cell_value(i, 14), j])

for i in range(0, len(addr_port_pair)):
    print(addr_port_pair[i])
    fp.write(str(addr_port_pair[i]) + "\n")

print(len(addr_port_pair))

fp.close()
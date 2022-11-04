import sys
# Arguments passed
print("\nName of Python script:", sys.argv[0])

# total arguments
n = len(sys.argv)
print("Total arguments passed:", n)

if n > 2 or n == 1:
    print("Please pass Correct Arg")
    exit(1)

path = sys.argv[1]
try:
    loadFile = open(path)
except:
    print("unable to load file")
    exit(1)
    
firstLine = loadFile.readline()
tableName = firstLine.split()
print(tableName)
if tableName == "":
    print("First List is empty")
    exit(1)
schemaName = ""
schemaType = ""
for i in tableName:
    if "Schema" in i or "schema" in i or "SCHEMA" in i:
        schemaName = i
    if "table" in i or "Table" in i or "TABLE" in i:
        schemaType = "Tables"
    elif "view" in i or "View" in i or "VIEW" in i:
        schemaType = "Views"
    elif "PROCEDURE" in i or "Proedure" in i or "proedure" in i:
        schemaType = "Stored Procedures"
    else:
        continue
if schemaName == "" or schemaType == "":
    print(" please place the files in correct location ")
    exit(1)
splitSchemaName = schemaName.split('.')
checkPath = splitSchemaName[0]+"/"+schemaType
if checkPath in path and checkPath != "/":
    print(" files locations are correct ")
else:
    print(" please place the files in correct location ")

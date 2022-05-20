class Contact:
    def __init__(self, infos):
        self.infos = {"TEL": set()}
        
        for info in infos:
            info = info.replace("\n", "")

            if info.split(":")[0] == "TEL":
                self.infos["TEL"].add( info.split(":")[1] )

            else:
                self.infos[info.split(":")[0]] = info.split(":")[1]

    def merge(self, obj):
        #print("Fusion (%s): %s && %s\n"%(self.infos["FN"], self.infos["TEL"], obj.infos["TEL"]))
        self.infos["TEL"] = self.infos["TEL"].union(obj.infos["TEL"])

    def save(self, file):
        file.write("BEGIN:VCARD\n")
        file.write("VERSION:3.0\n")
        file.write("PRODID:ez-vcard 0.10.3\n")
        file.write("FN:" + self.infos["FN"]+"\n")

        for num in self.infos["TEL"]:
            file.write("TEL:" + num +"\n")

        for key in self.infos:
            if key not in "BEGIN, VERSION, PRODID, FN, TEL, END":
                file.write("%s:%s\n"%(key, self.infos[key]))

        file.write("END:VCARD\n")

    def __str__(self):
        return self.infos["FN"] + " : " + ", ".join(self.infos["TEL"])

    def __eq__(self, obj):
        return (type(obj) is type(self)) and (self.infos["FN"] == obj.infos["FN"])

    def __gt__(self, obj): # For sorting Contact objects
        return (type(obj) is type(self)) and (self.infos["FN"] > obj.infos["FN"])

def main():
    fileName = "contacts.vcf"
    file = open(fileName, "r", encoding="utf-8")

    lines = file.readlines()
    infos = []
    contacts = []
    
    for line in lines:
        if line.split(":")[0] == "BEGIN":
            infos = [line]

        elif line.split(":")[0] == "END":
            infos.append(line)
            contact = Contact(infos)
            contacts.append(contact)

        else:
            infos.append(line)

    contacts.sort()
    print("contacts : " + str(len(contacts)))

    finalContacts = []
    for contact in contacts:
        if len(finalContacts) > 0:
            if contact == finalContacts[-1]:
                finalContacts[-1].merge(contact)
            else :
                finalContacts.append(contact)
        else :
            finalContacts.append(contact)

    print("finalContacts : " + str(len(finalContacts)))

    #file_ = open("formatted-contacts.vcf", "w", encoding="utf8")
    #for c in finalContacts:
        #c.save(file_)
    #file_.close()

    file.close()

if __name__ == "__main__":
    main()

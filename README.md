# CSV_Offer_Cleaner

A CSV-Template (see example file) will be filled with values by a supplier. It happens, that the format of the CSV-file will be changed. It also happens that the values inserted by the supplier are incorrect (format errors).
The filled CSV-file will be uploaded in an ERP-System. It cannot be uploaded, if there are format errors or not allowed values.

Goals:
1. Clear issues, like format errors in a given CSV. 
- unwanted carriage return
- special chars
- additional columns / rows
- doubble rows in the head part
2. GUI APP to show differences between the received and the cleaned file
- table

The CSV-File has a specific structure. It contains an upper part and a lower part, that are different from each other.
Upper part untill row 39:
- First column until has keyvalues, that are not allowed to change. The order of the keayvalues must stay the same.
- The second column untill row 39 must be empty (no values)
- The third column is filled with information by the supplier
- The fourth column contains a designation for column three
row 40 is empty

Lowwer part:
Starts at row 41 (Head) and has ten columns
The amount of rows is variable (can be 1 or 500 for example).
First and second column contain special keyvalueas that can occur multiple times in the same column and are considered container. The Keyvalues in the first and second column need to be the same.
The third column contains the supplier code, that can occur only once per container.
The fourth column contains the description of what the code in column three means.
The fifth column Contains a price. The price has to be filled. If there is no value, it is considered for free = 0.
The sixth column has to be filled and contains a special code (LF1, LF2, ... ,LF10)
The seventh column can be filled (no must have). Natural number.
The eights column can be filled (no must have) with a code from the supplier.
The nineth column can be filled (no must have) with an capital "F".

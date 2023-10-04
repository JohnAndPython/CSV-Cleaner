# CSV-Cleaner

A CSV-Template (see example file) will be filled with values by a supplier. It happens, that the format of the CSV-file will be changed. It also happens that the values inserted by the supplier are incorrect (format errors).
The filled CSV-file will be uploaded in an ERP-System. It cannot be uploaded, if there are format errors or not allowed values.

The Goal is to:
Clear issues, like format errors in a given CSV. 
- unwanted carriage return
- special chars
- additional columns / rows
- doubble rows in the head part

The CSV-File has a specific structure. It contains an upper part and a lower part, that are different from each other.
Upper part untill row 39:
- First column until has keyvalues, that are not allowed to change. The order of the keayvalues must stay the same.
- The second column untill row 39 must be empty (no values)
- The third column is filled with information by the supplier
- The fourth column contains a designation for column three
row 40 is empty
Lowwer part:

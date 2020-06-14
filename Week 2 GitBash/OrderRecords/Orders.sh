#Note that order_records.csv.aa Combined 2 entries into one line of data, So I seperated Stephine Clark from First Name Last Name. 
#create a directory called AllRecords
mkdir AllRecords
#Copy all rercords from 2011-2017 into the AllRecords Directory
find . -iname '*.csv*' -exec cp {} AllRecords \;
#Create a subdirectory in AllRecords called VIPCustomerOrders
mkdir AllRecords/VIPCustomerOrders
#Combine all the records into one file to make it easier to pull info from
cat AllRecords/order_records.csv.a* > fullrecords.csv.ag
#Find all orders from Michael Davis and display the info
grep -r 'Michael,Davis'*
#Find all orders from Michael Campbell and display the info
grep -r 'Michael,Campbell'*
#Find Qualifer columns to make it easier to idetify what the info means
grep 'first,last' fullrecords.csv.ag > 1qualifer.output
#Find all orders from Michael Davis and move the info to michael_davis_orders.output
grep 'Michael,Davis' fullrecords.csv.ag > michael_davis_orders.output
#Find all orders from Michael Campbell and move the info to michael_campbell.output
grep 'Michael,Campbell' fullrecords.csv.ag > michael_campbell_orders.output
# Move qualifer.output, michael_davis_orders.output & michael_davis_orders.output into VIPCustomerOrders
mv 1qualifer.output michael_davis_orders.output michael_campbell_orders.output AllRecords/VIPCustomerOrders/
#Create a file called VIPCustomerDetails.md
touch VIPCustomerOrders.md
#Move Michael Davis's & Michael Campbell's order info to VIPCustomerDetails.md
cat AllRecords/VIPCustomerOrders/* > VIPCustomerOrders.md
#End Script
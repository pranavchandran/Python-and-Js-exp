function frappe1(frmdate,todate) {
    var from_date = Date.parse(frmdate);
    var to_date = Date.parse(todate);
    
    var date1 = new Date(from_date)
    var date2 = new Date(to_date)

    const diffTime = Math.abs(date2 - date1);
    const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24)); 
    console.log(from_date)
    console.log(to_date)
    console.log(date1)
    console.log(date2)

    console.log(diffDays + " days");



};
            
frappe1("10-04-2019", "10-02-2019");
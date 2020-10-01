function isItGreaterThan(date1, date2, days) {
    var firstDate = new Date(date1);
    var secondDate = new Date(date2);
    var time = days * 60 * 60 * 24 * 1000
    if ((secondDate.getTime() - firstDate.getTime()) < time) {
      console.log({dateCheck: `Not greater than ${days} days`});
    } else {
      console.log({dateCheck: `Greater than ${days} days`});
    }
  }
  
  isItGreaterThan('10/01/2019', '10/02/2019', 3);
  isItGreaterThan('10/01/2019', '10/03/2019', 3);
  isItGreaterThan('10/01/2019', '10/04/2019', 3);
  
  isItGreaterThan('10/01/2019', '10/02/2019', 10);
  isItGreaterThan('10/01/2019', '10/03/2019', 10);
  isItGreaterThan('10/01/2019', '10/14/2019', 10);
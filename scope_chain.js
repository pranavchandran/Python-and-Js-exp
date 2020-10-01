var name = 'Pranav';
console.log("line no:3",name)

function sayName(){
    var name = 'Ice cream'
    console.log("line no:6",name)
    sayNameTwo();
    function sayNameTwo(){
        var name = 'ice3'
        console.log('line num 10',name)
    }

}

sayName();
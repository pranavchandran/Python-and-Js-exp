// function greet(){
//     console.log('hello')
// }

// function greet(){
//     return ('hello')
// }


// function greet(firstName,lastName){
//     return ('hello ' + firstName + ' ' + lastName)
// }

// console.log(greet('pranav','C'))

// function greet(firstName,lastName){
//     // if(typeof firstName=== 'undefined'){firstName='pranav'}
//     // if(typeof lastName=== 'undefined'){lastName='Chandran'}

//     return ('hello ' + firstName + ' ' + lastName)
// }
// console.log(greet())

function greet(firstName='pranav',lastName='chandran'){
    // if(typeof firstName=== 'undefined'){firstName='pranav'}
    // if(typeof lastName=== 'undefined'){lastName='Chandran'}

    return ('hello ' + firstName + ' ' + lastName)
}
// console.log(greet())

// Function expressions

// const square = function(x){
//     return x * x;
// }

const square = function(x=3){
    return x * x;
}

// console.log(square(2));
// console.log(typeof square());
// console.log(square(3))

// immediately invokable function expressions - IIFE,s
// not working
// (function(name){
//     console.log('IIFE ran...' + name);
// })('jack');

// Property methods

const todo = {
    add : function(){
        console.log('add todo ..')
    },
    edit : function(id){
        console.log(`Edit todo ${id}`)
    }
}

todo.delete = function(){
    console.log('Delete todo...')
}

todo.add()
todo.edit(10234)
todo.delete()
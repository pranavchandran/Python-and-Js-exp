const names = ['youtube','facebook','insta','netflix','amazon']

// for(const n of names){
//     console.log(n);
// }

const symbols = {
    yt:'youtube',
    ig:'Instagram',
    fb:'facebook',
    sc:'selfcoder'

}
// it bring back keys
// for (const n in symbols){
//     console.log(n)
// }

// bringing values back
// for (const n in symbols){
//     console.log(symbols[n])
// }

for (const n in symbols){
    console.log(`Key is: ${n} and value is: ${symbols[n]}`)
    
}
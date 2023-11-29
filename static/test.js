let checker=false
const queryString = window.location.search;
const urlParams = new URLSearchParams(queryString);
const id = urlParams.get('id')
console.log(Number(id));
function test(){
    $.get(`/test/${id}`).then(response=>{
        if(response['status']==true){
            document.querySelector('#ti').textContent='True'
            clearInterval(inter);
            console.log('ok')
        }
    })
}

let inter=setInterval(()=>{
    test()
},5000)

// while (checker==false){
//     setTimeout(()=>{
//         test()
//     },1000)
// }
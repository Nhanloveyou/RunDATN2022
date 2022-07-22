function inra(){
    var answers = document.getElementById("out-all-types");
    var answer = answers.innerText
    let i;
    let end = '<h5 className="bar">'
    if(check_string(answer) === true){
        for(i in answer) {
            if(answer[i] === "|"){
                end += '</h5> <h5 className = "bar">'
            }
            if(answer[i] !== "|"){
                end += answer[i] 
            }
        }
        end= end.slice(0, -4)
        answers.innerHTML = end
    }
}

function check_string(a){
    if(a.split("|").length - 1 > 0){
        return true
    }
    if(a.split("|").length - 1 === 0){
        return false
    }
}

setInterval(inra, 200)


// document.getElementById("input_").addEventListener("submit", function(e){
//     var refreshId = setInterval(function() {
//         var properID = check_string(document.getElementById("out-all-types").innerText);
//         if (properID) {
//             inra();
//             clearInterval(refreshId);
//         }
//       }, 3000);
//   	//do whatever an submit the form
// });

// var refreshId = setInterval(function() {
//     var properID = check_string(document.getElementById("out-all-types").innerText);
//     if (properID) {
//         inra();
//         clearInterval(refreshId);
//     }
//   }, 3000);


// document.getElementById("output").innerHTML = x
//     console.log("Test");
//     console.log(answers);
// }
// inra()
// setTimeout(inra, 60000)
// var answers = document.getElementById("output").innerHTML

// console.log(answers)
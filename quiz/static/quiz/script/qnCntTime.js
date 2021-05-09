var hiddenCount = 0;
var hiddenInterval;
var hiddenChange = 0;
var submit = document.getElementById("submit");
var answer = document.getElementById("answer");

// Check if the tab is hidden
document.addEventListener('visibilitychange', () => {
    if (document.hidden) {
        hiddenChange++;
        console.log(hiddenChange);
        hiddenInterval = window.setInterval(()=>{
            hiddenCount++;
        }, 1000);
    }
    else {
        window.clearInterval(hiddenInterval);
    }
});

function sendrequest(){
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "", true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.send(JSON.stringify({
        "windowChange": hiddenChange,
        "windowTime": hiddenCount,
        "answer": answer.value,
    }));
}

submit.onclick = () => sendrequest();
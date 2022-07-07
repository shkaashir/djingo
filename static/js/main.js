let gateway = `ws://${window.location.hostname}:${location.port}/ws/bingo/`;
let websocket;

window.addEventListener('load', onLoad);
function onLoad() {
    initWebSocket();
}
 

function initWebSocket() {
    console.log('Trying to open a WebSocket connection...');
    websocket = new WebSocket(gateway);
    websocket.onopen    = onOpen;
    websocket.onclose   = onClose;
    websocket.onmessage = onMessage;
}

function onOpen(event) {
    console.log('Connection opened');
}

function onClose(event) {
    console.log('Connection closed');
    setTimeout(initWebSocket, 2000);
}

function onMessage(event) {
   const data = JSON.parse(event.data)
   console.log(data)
   if(Array.isArray(data)){
    addDataToTable(data)
   }else{
    addRandomGeneratedNumberToElement(data.roulette_number)
   }
}

function addRandomGeneratedNumberToElement(number){
    document.getElementById('random-number').innerText=number
}

function addDataToTable(data){
    let  i = 0
    const color = ['#B30E50','#FF3300','#FC4B54','#FD882D','#43C2C1']
    document.getElementById('bingo-table-body').innerHTML=''
    while (i<data.length){
        let tr = document.createElement("tr")
        for (let j=0;j<data.length;j++){
            let res = data[j][i]
            if (i===2 && i===j){
                res = 'free'
            }
            tr.innerHTML+=`
                <td>
                    <div class="bingo-circ position-relative" style="background-color:${color[j]}">
                        <p class="position-absolute top-50 translate-middle">${res}</p>
                    </div>
                </td>
            `
        }
        document.getElementById('bingo-table-body').appendChild(tr);
        i+=1
    }
}
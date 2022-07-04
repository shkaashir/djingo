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
   addDataToTable(data)
}

function addDataToTable(data){
    document.getElementById('bingo-table-body').innerHTML=''
    for (let i=0;i<data.length;i++){
        let tr = document.createElement("tr")
        // document.getElementById('bingo-table-body').innerHTML+=tr
        for(let j=0;j<data.length;j++){
            tr.innerHTML+=`
                <td>
                    <div class="bingo-circ position-relative">
                        <p class="position-absolute top-50 translate-middle">${data[i][j]}</p>
                    </div>
                </td>
            `
        }
        document.getElementById('bingo-table-body').appendChild(tr);
    }
}
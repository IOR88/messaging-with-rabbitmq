import io from 'socket.io-client';

const MWR_BASE_URL = 'http://localhost:8000/';

function createSocket(channel){
    return io.connect(`${MWR_BASE_URL}${channel}`)
}

export {createSocket}